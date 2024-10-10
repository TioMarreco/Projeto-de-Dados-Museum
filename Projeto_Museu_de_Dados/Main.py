import customtkinter as ctk
import psycopg2
from tkinter import messagebox

# Função de login
def login():
    usuario_nome = entry_username.get()
    senha = entry_password.get()

    try:
        conn = psycopg2.connect(
            dbname="20221214010013",
            user="postgres",
            password="pabd",
            host="localhost"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE usuario_nome=%s AND senha=%s", (usuario_nome, senha))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

        cursor.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro de conexão: {e}")

def abrir_tela_principal(conn):
    root.withdraw()  # Oculta a janela de login
    root.geometry('300x300')
    tela_principal = ctk.CTkToplevel(root)
    tela_principal.title("Tela Principal")

    def criar_usuario():
        def salvar_usuario():
            novo_usuario = entry_novo_usuario.get()
            nova_senha = entry_nova_senha.get()
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO usuarios (username, password) VALUES (%s, %s)", (novo_usuario, nova_senha))
                conn.commit()
                messagebox.showinfo("Sucesso", "Usuário criado com sucesso!")
                entry_novo_usuario.delete(0, ctk.END)
                entry_nova_senha.delete(0, ctk.END)
                cursor.close()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao criar usuário: {e}")

        label_novo_usuario = ctk.CTkLabel(tela_criar_usuario, text="Novo Usuário:")
        label_novo_usuario.pack(pady=5)

        entry_novo_usuario = ctk.CTkEntry(tela_criar_usuario)
        entry_novo_usuario.pack(pady=5)

        label_nova_senha = ctk.CTkLabel(tela_criar_usuario, text="Nova Senha:")
        label_nova_senha.pack(pady=5)

        entry_nova_senha = ctk.CTkEntry(tela_criar_usuario, show="*")
        entry_nova_senha.pack(pady=5)

        button_salvar = ctk.CTkButton(tela_criar_usuario, text="Criar Usuário", command=salvar_usuario)
        button_salvar.pack(pady=10)

    def ler_usuarios():
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM usuarios;")
            usuarios = cursor.fetchall()
            usuarios_lista = "\n".join([user[0] for user in usuarios])
            messagebox.showinfo("Usuários", f"Usuários:\n{usuarios_lista}")
            cursor.close()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler usuários: {e}")

    def deletar_usuario():
        def excluir_usuario():
            usuario_a_deletar = entry_usuario_deletar.get()
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM usuarios WHERE username=%s", (usuario_a_deletar,))
                conn.commit()
                messagebox.showinfo("Sucesso", "Usuário deletado com sucesso!")
                entry_usuario_deletar.delete(0, ctk.END)
                cursor.close()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao deletar usuário: {e}")

        label_usuario_deletar = ctk.CTkLabel(tela_deletar_usuario, text="Usuário a Deletar:")
        label_usuario_deletar.pack(pady=5)

        entry_usuario_deletar = ctk.CTkEntry(tela_deletar_usuario)
        entry_usuario_deletar.pack(pady=5)

        button_excluir = ctk.CTkButton(tela_deletar_usuario, text="Deletar Usuário", command=excluir_usuario)
        button_excluir.pack(pady=10)

    # Layout da tela principal
    button_criar = ctk.CTkButton(tela_principal, text="Criar Usuário", command=criar_usuario)
    button_criar.pack(pady=10)

    button_ler = ctk.CTkButton(tela_principal, text="Ler Todos os Usuários", command=ler_usuarios)
    button_ler.pack(pady=10)

    button_deletar = ctk.CTkButton(tela_principal, text="Deletar Usuário", command=deletar_usuario)
    button_deletar.pack(pady=10)

    # Criando sub-telas para criar e deletar usuários
    tela_criar_usuario = ctk.CTkToplevel(tela_principal)
    tela_criar_usuario.title("Criar Usuário")
    tela_criar_usuario.withdraw()  # Inicialmente oculta

    tela_deletar_usuario = ctk.CTkToplevel(tela_principal)
    tela_deletar_usuario.title("Deletar Usuário")
    tela_deletar_usuario.withdraw()  # Inicialmente oculta

    # Mostra as telas apropriadas
    button_criar.configure(command=lambda: (tela_criar_usuario.deiconify(), tela_deletar_usuario.withdraw()))
    button_deletar.configure(command=lambda: (tela_deletar_usuario.deiconify(), tela_criar_usuario.withdraw()))

# Configurações da janela
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

root = ctk.CTk()  # Criação da janela
root.title("Tela de Login")

# Widgets da tela de login
label_username = ctk.CTkLabel(root, text="Usuário")
label_username.pack(pady=10)

entry_username = ctk.CTkEntry(root)
entry_username.pack(pady=10)

label_password = ctk.CTkLabel(root, text="Senha")
label_password.pack(pady=10)

entry_password = ctk.CTkEntry(root, show="*")
entry_password.pack(pady=10)

button_login = ctk.CTkButton(root, text="Login", command=login)
button_login.pack(pady=20)

# Iniciar o loop principal
root.mainloop()