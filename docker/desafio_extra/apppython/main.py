from typing import List, Annotated
from fastapi import FastAPI, HTTPException, status, Request, Depends
from database import get_database_connection
from classes import Comida, ComidaCreate
from contextlib import asynccontextmanager
import os
import psycopg2

PYTHON_ENV = os.getenv("PYTHON_ENV", "development")
IS_DEV = PYTHON_ENV == "development"

# Lifespan manager para gerenciar conexão do banco (compatível com múltiplos workers)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: criar conexão ao banco
    print("Iniciando aplicação e conectando ao banco...")
    app.state.db = get_database_connection()
    print("✓ Aplicação iniciada e banco conectado.")
    
    yield
    
    # Shutdown: fechar conexão
    print("Finalizando aplicação...")
    db = getattr(app.state, "db", None)
    if db:
        try:
            db.close()
            print("✓ Conexão ao banco fechada.")
        except Exception as e:
            print(f"✗ Erro ao fechar conexão: {e}")
    print("✓ Aplicação finalizada.")

app = FastAPI(title="Comidas API", debug=IS_DEV, lifespan=lifespan)

# Dependency: fornece a conexão ao banco de dados
def get_db(request: Request) -> psycopg2.extensions.connection:
    """Dependency que retorna a conexão do banco do app state"""
    return request.app.state.db

# Type alias para simplificar anotações
DbDep = Annotated[psycopg2.extensions.connection, Depends(get_db)]

@app.get("/")
def read_root():
    return {"Hello": "World", "env": PYTHON_ENV}

@app.get("/health")
def health_check(db: DbDep):
    """Endpoint de health check para verificar status da aplicação e conexão com DB"""
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT 1;")
            cursor.fetchone()
        return {
            "status": "ok",
            "environment": PYTHON_ENV,
            "database": "connected"
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database connection failed: {str(e)}"
        )

@app.get("/comidas/", response_model=List[Comida])
def list_comidas(db: DbDep):
    with db.cursor() as cursor:
        cursor.execute("SELECT id, nome, descricao, created_at FROM comidas;")
        rows = cursor.fetchall()
        items = [Comida(id=row[0], nome=row[1], descricao=row[2], created_at=row[3]) for row in rows]
    return items

@app.post("/comidas/", response_model=Comida)
def create_comida(comida: ComidaCreate, db: DbDep):
    with db.cursor() as cursor:
        cursor.execute(
            "INSERT INTO comidas (nome, descricao) VALUES (%s, %s) RETURNING id, created_at;",
            (comida.nome, comida.descricao)
        )
        row = cursor.fetchone()  # tupla: (id, created_at)
        db.commit()
        new_comida = Comida(id=row[0], nome=comida.nome, descricao=comida.descricao, created_at=row[1])
    return new_comida

@app.get("/comidas/{comida_id}", response_model=Comida)
def get_comida(comida_id: int, db: DbDep):
    with db.cursor() as cursor:
        cursor.execute(
            "SELECT id, nome, descricao, created_at FROM comidas WHERE id = %s;",
            (comida_id,)
        )
        row = cursor.fetchone()
        if row is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comida not found")
        comida = Comida(id=row[0], nome=row[1], descricao=row[2], created_at=row[3])
    return comida