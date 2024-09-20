import psycopg2 as p2


dbname = '20221214010013'
user = 'postgres'
password = 'pabd'
host = 'localhost'  # ou o endereço do servidor de banco de dados
port = '5432'  # padrão para PostgreSQL


conn = p2.connect(
    dbname=dbname,        
    user=user,
    password=password,
    port=port
)

conn.autocommit = True
    
cur = conn.cursor()

def Criar_Tabela():
    cur.execute('''CREATE TABLE Usuarios(
        usuario_nome VARCHAR(50) UNIQUE NOT NULL,
        senha VARCHAR (256) NOT NULL,
        CONSTRAINT Usuarios_pk PRIMARY KEY (usuario_nome)
    )''')

    
    

def Criar_usuario():
    cur.execute('''INSERT INTO Usuarios
                )


conn.close()
cur.close()