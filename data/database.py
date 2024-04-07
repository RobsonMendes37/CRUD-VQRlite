import psycopg2

def conectar_postgres():
    try:
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            port=5432,
            password="147258369",
            database="ProjetoFDB"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None
