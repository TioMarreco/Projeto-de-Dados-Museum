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

def login():
    
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    cur.execute ("SELECT * FROM Usuarios WHERE usuario_nome = %s AND senha = %s;" (usuario,senha))

    resultado = cursor.fetchone()

    if resultado:
        print("Login bem-sucedido! Bem-vindo,", usuario)
    else:
        print("Usuário ou senha incorretos.")


cur.close
    

