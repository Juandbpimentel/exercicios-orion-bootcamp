import uvicorn
from typing import List
from fastapi import FastAPI, HTTPException, status, Request
from database import get_database_connection
from classes import Comida, ComidaCreate
import os

PYTHON_ENV = os.getenv("PYTHON_ENV", "development")
IS_DEV = PYTHON_ENV == "development"

app = FastAPI(debug=IS_DEV)

# criar conexão no startup (cada worker/proc executa isso)
@app.on_event("startup")
def startup_event():
    app.state.db = get_database_connection()

@app.get("/")
def read_root():
    return {"Hello": "World", "env": PYTHON_ENV}

@app.get("/comidas/", response_model=List[Comida])
def list_comidas(request: Request):
    db_conn = request.app.state.db
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, nome, descricao, created_at FROM comidas;")
        rows = cursor.fetchall()
        items = [Comida(id=row[0], nome=row[1], descricao=row[2], created_at=row[3]) for row in rows]
    return items

@app.post("/comidas/", response_model=Comida)
def create_comida(comida: ComidaCreate):
    with app.state.db.cursor() as cursor:
        cursor.execute(
            "INSERT INTO comidas (nome, descricao) VALUES (%s, %s) RETURNING id, created_at;",
            (comida.nome, comida.descricao)
        )
        row = cursor.fetchone()  # tupla: (id, created_at)
        app.state.db.commit()
        new_comida = Comida(id=row[0], nome=comida.nome, descricao=comida.descricao, created_at=row[1])
    return new_comida

@app.get("/comidas/{comida_id}", response_model=Comida)
def get_comida(comida_id: int):
    with app.state.db.cursor() as cursor:
        cursor.execute(
            "SELECT id, nome, descricao, created_at FROM comidas WHERE id = %s;",
            (comida_id,)
        )
        row = cursor.fetchone()
        if row is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comida not found")
        comida = Comida(id=row[0], nome=row[1], descricao=row[2], created_at=row[3])
    return comida