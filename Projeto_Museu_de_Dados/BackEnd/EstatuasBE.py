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


def Criar_estátua():
    estátua = input("Digite o nome de usuário: ")
    preço = input("Digite a preço: ")

    cur.execute(
        "INSERT INTO Estátuas (estátua_nome, preço) VALUES (%s, %s)",
        (estátua, preço)
    )

    conn.commit()

def Update_estátua():
    estátua = input("Digite o nome do usuário que deseja atualizar: ")
    novo_estátua = input("Digite o novo estátua: ")
    nova_preço = input("Digite a nova preço")

    cur.execute( 
        "UPDATE Estátuas SET preço = %s, estátua_nome = %s WHERE estátua_nome = %s",
        (novo_estátua,nova_preço,estátua)
    )

    conn.commit()
    print("Usuário atualizada com sucesso")

def Ler_Estátuas():
    cur.execute(
        "SELECT * FROM Estátuas"
    )
    
    resultados = cur.fetchall()
    print("Resultados da consulta:")
    for linha in resultados:
    
        print(f"- {linha}")


def Deletar_estátua():
    estátua = input("Digite o Usuário que deseja deletar: ")

    cur.execute(
        "DELETE FROM Estátuas WHERE estátua_nome = %s",
        (estátua,)
    )

    conn.commit()

    print("Usuário Deletado com sucesso!")


cur.close()