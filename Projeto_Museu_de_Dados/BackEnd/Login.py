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

def Criar_Tabela():
    cur.execute('''CREATE TABLE Usuarios(
        usuario_nome VARCHAR(50) UNIQUE NOT NULL,
        senha VARCHAR (256) NOT NULL,
        CONSTRAINT Usuarios_pk PRIMARY KEY (usuario_nome)
    )''')


def Criar_Usuario():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    cur.execute(
        "INSERT INTO Usuarios (usuario_nome, senha) VALUES (%s, %s)",
        (usuario, senha)
    )

    conn.commit()

def Update_Usuario():
    usuario = input("Digite o nome do usuário que deseja atualizar: ")
    novo_usuario = input("Digite o novo Usuario: ")
    nova_senha = input("Digite a nova senha")

    cur.execute( 
        "UPDATE Usuarios SET senha = %s, usuario_nome = %s WHERE usuario_nome = %s",
        (novo_usuario,nova_senha,usuario)
    )

    conn.commit()
    print("Usuário atualizada com sucesso")

def Ler_Usuarios():
    cur.execute(
        "SELECT * FROM Usuarios"
    )
    
    resultados = cur.fetchall()
    print("Resultados da consulta:")
    for linha in resultados:
    
        print(f"- {linha}")


def Deletar_Usuario():
    usuario = input("Digite o Usuário que deseja deletar: ")

    cur.execute(
        "DELETE FROM Usuarios WHERE usuario_nome = %s",
        (usuario,)
    )

    conn.commit()

    print("Usuário Deletado com sucesso!")


cur.close()