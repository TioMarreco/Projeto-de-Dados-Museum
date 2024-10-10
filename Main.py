import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BackEnd.EstatuasBE import *
from BackEnd.UsuárioBE import *
from BackEnd.QuadrosBE import *
from BackEnd.Login import *
import customtkinter as ctk
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
        
        cursor = conn.cursor()
        
        # Consulta SQL
        query = sql.SQL("SELECT * FROM usuarios WHERE usuario = %s AND senha = %s")
        cursor.execute(query, (usuario, senha))
        
        # Verifica se um resultado foi encontrado
        resultado = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        return resultado is not None
            
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return False
    

def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    if verificar_usuario_senha(usuario, senha):
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

def abrir_crud():
    # Implementar a lógica para abrir a tela do CRUD
    pass

app = ctk.CTk()

app.title("Tela de Login")
app.geometry("300x200")

# Campos de entrada
label_usuario = ctk.CTkLabel(app, text="Usuário")
label_usuario.pack(pady=10)

entry_usuario = ctk.CTkEntry(app)
entry_usuario.pack(pady=5)

label_senha = ctk.CTkLabel(app, text="Senha")
label_senha.pack(pady=10)

entry_senha = ctk.CTkEntry(app, show="*")
entry_senha.pack(pady=5)

# Botão de login
btn_login = ctk.CTkButton(app, text="Login", command=verificar_login)
btn_login.pack(pady=10)

# Botão para abrir CRUD
btn_crud = ctk.CTkButton(app, text="Abrir CRUD", command=abrir_crud)
btn_crud.pack(pady=10)

app.mainloop()

