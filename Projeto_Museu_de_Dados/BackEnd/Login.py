import psycopg2 as p2
from psycopg2 import sql

def verificar_usuario_senha(usuario, senha):
    try:
        # Conexão com o banco de dados
        conn = p2.connect(
            dbname = '20221214010013'
            user = 'postgres'
            password = 'pabd'
            host = 'localhost'  # ou o endereço do servidor de banco de dados
            port = '5432'
        )
        cur = conn.cursor()
        
        # Consulta SQL
        query = sql.SQL("SELECT * FROM usuarios WHERE usuario = %s AND senha = %s")
        cur.execute(query, (usuario, senha))
        
        # Verifica se um resultado foi encontrado
        resultado = cur.fetchone()
        
        cur.close()
        conn.close()
        
        if resultado:
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return False

