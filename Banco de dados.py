import psycopg2

# Dados de conexão
dbname = '20221214010013'
user = 'postgres'
password = 'pabd'
host = 'localhost'  # ou o endereço do servidor de banco de dados
port = '5432'  # padrão para PostgreSQL

# Estabelecendo a conexão
try:
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        port=port
    )
    
    # Criar um cursor
    cur = conn.cursor()
except psycopg2.Error as e:
    print(f"Erro ao executar o comando SQL: {e}")


    print("Conexão estabelecida com sucesso!")
except psycopg2.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")


cur.execute('''CREATE TABLE Usuarios(
    username VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR (256) NOT NULL,
    CONSTRAINT username_pk PRIMARY KEY (username)
)''')

conn.commit()
conn.close()


