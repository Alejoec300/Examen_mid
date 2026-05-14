import os
from dotenv import load_dotenv
from typing import Optional
from fastapi import FastAPI, HTTPException
from sqlmodel import Field, SQLModel, Session, create_engine, select
from pydantic import BaseModel
import bcrypt

load_dotenv()
PEPPER = os.getenv("PEPPER")

engine = create_engine("sqlite:///usuarios.db")

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    hashed_password: str

class Credenciales(BaseModel):
    username: str
    password: str

SQLModel.metadata.create_all(engine)
app = FastAPI()

@app.post("/register")
def register(credenciales: Credenciales):
    if not PEPPER:
        raise HTTPException(status_code=500, detail="Error de configuración: PEPPER no encontrado")
        
    password_con_pepper = (credenciales.password + PEPPER)[:72]
    hashed = bcrypt.hashpw(password_con_pepper.encode(), bcrypt.gensalt())
    
    usuario = User(username=credenciales.username, hashed_password=hashed.decode())
    with Session(engine) as session:
        try:
            session.add(usuario)
            session.commit()
            return {"mensaje": "Usuario registrado"}
        except:
            raise HTTPException(status_code=400, detail="El usuario ya existe")

@app.post("/login")
def login(credenciales: Credenciales):
    with Session(engine) as session:
        usuario = session.exec(select(User).where(User.username == credenciales.username)).first()
    
    if not usuario:
        raise HTTPException(status_code=404, detail="No encontrado")
    
    password_con_pepper = (credenciales.password + PEPPER)[:72]
    if bcrypt.checkpw(password_con_pepper.encode(), usuario.hashed_password.encode()):
        return {"mensaje": "Login exitoso"}
    
    raise HTTPException(status_code=401, detail="Error")