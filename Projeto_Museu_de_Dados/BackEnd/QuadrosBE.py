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
    

def Criar_quadro():
    quadro = input("Digite o nome de usuário: ")
    preço = input("Digite a preço: ")

    cur.execute(
        "INSERT INTO Quadros (quadro_nome, preço) VALUES (%s, %s)",
        (quadro, preço)
    )

    conn.commit()

def Update_quadro():
    quadro = input("Digite o nome do usuário que deseja atualizar: ")
    novo_quadro = input("Digite o novo quadro: ")
    nova_preço = input("Digite a nova preço")

    cur.execute( 
        "UPDATE Quadros SET preço = %s, quadro_nome = %s WHERE quadro_nome = %s",
        (novo_quadro,nova_preço,quadro)
    )

    conn.commit()
    print("Usuário atualizada com sucesso")

def Ler_Quadros():
    cur.execute(
        "SELECT * FROM Quadros"
    )
    
    resultados = cur.fetchall()
    print("Resultados da consulta:")
    for linha in resultados:
    
        print(f"- {linha}")


def Deletar_quadro():
    quadro = input("Digite o Usuário que deseja deletar: ")

    cur.execute(
        "DELETE FROM Quadros WHERE quadro_nome = %s",
        (quadro,)
    )

    conn.commit()

    print("Usuário Deletado com sucesso!")


cur.close()