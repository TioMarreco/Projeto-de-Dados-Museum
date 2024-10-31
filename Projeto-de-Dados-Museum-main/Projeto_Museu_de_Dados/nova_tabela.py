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
    port=port,
    host=host,
)


conn.autocommit = True
cur = conn.cursor()


cur.execute('''CREATE TABLE fosseis(
     fosseis_nome VARCHAR(50) UNIQUE NOT NULL,
        CONSTRAINT fosseis_pk PRIMARY KEY (fosseis_nome)
    )''')
