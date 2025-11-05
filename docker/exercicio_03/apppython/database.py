from dotenv import load_dotenv
import os
import psycopg2

def load_database_config():
    # Usando variáveis de ambiente, com fallback para .env se não estiverem definidas
    db_host = os.environ.get('DB_HOST')
    if db_host is None:
        print("DB_HOST não foi encontrado nas variáveis de ambiente, carregando de .env")
        load_dotenv(dotenv_path='.pythonapp.env')
        db_host = os.environ.get('DB_HOST')

    db_port = os.environ.get('DB_PORT')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_name = os.environ.get('DB_NAME', 'postgrtes')

    if db_host is None:
        raise ValueError("DB_HOST não está definido nas variáveis de ambiente ou no arquivo .env")

    

    db_config = {
        'host': db_host if db_host else 'localhost',
        'port': int(db_port) if db_port else 5432,
        'user': db_user if db_user else 'postgres',
        'password': db_password if db_password else 'postgres',
        'database': db_name if db_name else 'postgres',
    }

    return db_config

def get_database_connection():
    config = load_database_config()
    try:
        conn = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            password=config['password'],
            database=config['database']
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None