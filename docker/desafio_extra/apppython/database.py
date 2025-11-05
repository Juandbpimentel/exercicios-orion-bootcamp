from dotenv import load_dotenv
import os
import psycopg2
import time

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
    db_name = os.environ.get('DB_NAME', 'postgres')

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

def get_database_connection(retries=5, delay=2):
    """
    Tenta conectar ao banco de dados com retry (útil para aguardar o banco inicializar)
    """
    config = load_database_config()
    last_exception = None
    
    for attempt in range(1, retries + 1):
        try:
            print(f"Tentativa {attempt}/{retries} de conexão ao banco de dados em {config['host']}:{config['port']}...")
            conn = psycopg2.connect(
                host=config['host'],
                port=config['port'],
                user=config['user'],
                password=config['password'],
                database=config['database']
            )
            conn.autocommit = False
            print(f"✓ Conectado com sucesso ao banco de dados!")
            return conn
        except Exception as e:
            last_exception = e
            print(f"✗ Erro ao conectar (tentativa {attempt}/{retries}): {e}")
            if attempt < retries:
                print(f"Aguardando {delay}s antes de tentar novamente...")
                time.sleep(delay)
    
    # Se todas as tentativas falharem, lançar a última exceção
    print(f"Falha ao conectar ao banco de dados após {retries} tentativas.")
    raise last_exception