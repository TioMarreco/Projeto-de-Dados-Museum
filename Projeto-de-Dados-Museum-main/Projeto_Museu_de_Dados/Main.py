import customtkinter as ctk
import psycopg2
from tkinter import messagebox

conn = psycopg2.connect(
    dbname="20221214010013",
     user="postgres",
     password="pabd",
     host="localhost"
)
cursor = conn.cursor()

# Função de login
def login():
    usuario_nome = entry_usuario_nome.get()
    senha = entry_password.get()

    try:

        cursor.execute("SELECT * FROM usuarios WHERE usuario_nome=%s AND senha=%s", (usuario_nome, senha))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Login", "Login bem-sucedido!")
            abrir_tela_escolha()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro de conexão: {e}")

# Função para abrir a tela de escolha entre Estátuas e quadros
def abrir_tela_escolha():
    root.withdraw()  # Oculta a janela de login
    tela_escolha = ctk.CTkToplevel(root)
    tela_escolha.title("Escolha um Tipo")
    
    def abrir_tela_quadros():
        tela_escolha.withdraw()
        tela_quadros = ctk.CTkToplevel(tela_escolha)
        tela_quadros.title("Gerenciar quadros")

        def adicionar_quadro():
            def salvar_quadro():
                quadro_nome = entry_quadro_nome.get()
                preço = entry_preço.get()
                try:
                    cursor.execute("INSERT INTO quadros (quadro_nome, preço) VALUES (%s, %s)", (quadro_nome, preço))
                    conn.commit()
                    messagebox.showinfo("Sucesso", "Quadro adicionado com sucesso!")
                    entry_quadro_nome.delete(0, ctk.END)
                    entry_preço.delete(0, ctk.END)
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao adicionar quadro: {e}")

            label_quadro_nome = ctk.CTkLabel(tela_quadros, text="Nome do Quadro:")
            label_quadro_nome.pack(pady=5)

            entry_quadro_nome = ctk.CTkEntry(tela_quadros)
            entry_quadro_nome.pack(pady=5)

            label_preço = ctk.CTkLabel(tela_quadros, text="Preço:")
            label_preço.pack(pady=5)

            entry_preço = ctk.CTkEntry(tela_quadros)
            entry_preço.pack(pady=5)

            buttoon_salvar_quadro = ctk.CTkButton(tela_quadros, text="Salvar quadro", command=salvar_quadro)
            buttoon_salvar_quadro.pack(pady=10)

        button_adicionar_quadro = ctk.CTkButton(tela_quadros, text="Adicionar Quadro", command=adicionar_quadro)
        button_adicionar_quadro.pack(pady=10)

        def ver_quadros():
            try:
                cursor.execute("SELECT quadro_nome, preço FROM quadros;")
                quadros = cursor.fetchall()
                quadros_lista = "\n".join([f"{q[0]} - R${q[1]}" for q in quadros])
                messagebox.showinfo("quadros", f"quadros:\n{quadros_lista}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao ler quadros: {e}")

        button_ver_quadros = ctk.CTkButton(tela_quadros, text="Ver quadros", command=ver_quadros)
        button_ver_quadros.pack(pady=10)

        def remover_quadro():
            def excluir_quadro():
                quadro_nome = entry_quadro_remover.get()
                try:
                    cursor.execute("DELETE FROM quadros WHERE quadro_nome=%s", (quadro_nome,))
                    conn.commit()
                    messagebox.showinfo("Sucesso", "Quadro removido com sucesso!")
                    entry_quadro_remover.delete(0, ctk.END)
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao remover quadro: {e}")

            label_quadro_remover = ctk.CTkLabel(tela_quadros, text="Nome do Quadro a Remover:")
            label_quadro_remover.pack(pady=5)

            entry_quadro_remover = ctk.CTkEntry(tela_quadros)
            entry_quadro_remover.pack(pady=5)

            button_excluir_quadro = ctk.CTkButton(tela_quadros, text="Remover Quadro", command=excluir_quadro)
            button_excluir_quadro.pack(pady=10)

        button_remover_quadro = ctk.CTkButton(tela_quadros, text="Remover Quadro", command=remover_quadro)
        button_remover_quadro.pack(pady=10)

    def abrir_tela_estátuas():
        tela_escolha.withdraw()
        tela_estátuas = ctk.CTkToplevel(tela_escolha)
        tela_estátuas.title("Gerenciar Estátuas")

        def adicionar_estátua():
            def salvar_estátua():
                estátua_nome = entry_estátua_nome.get()
                preço = entry_preço_estátua.get()
                try:
                    cursor.execute("INSERT INTO estátuas (estátua_nome, preço) VALUES (%s, %s)", (estátua_nome, preço))
                    conn.commit()
                    messagebox.showinfo("Sucesso", "Estátua adicionada com sucesso!")
                    entry_estátua_nome.delete(0, ctk.END)
                    entry_preço_estátua.delete(0, ctk.END)
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao adicionar estátua: {e}")

            label_estátua_nome = ctk.CTkLabel(tela_estátuas, text="Nome da Estátua:")
            label_estátua_nome.pack(pady=5)

            entry_estátua_nome = ctk.CTkEntry(tela_estátuas)
            entry_estátua_nome.pack(pady=5)

            label_preço_estátua = ctk.CTkLabel(tela_estátuas, text="Preço:")
            label_preço_estátua.pack(pady=5)

            entry_preço_estátua = ctk.CTkEntry(tela_estátuas)
            entry_preço_estátua.pack(pady=5)

            buttoon_salvar_estátua = ctk.CTkButton(tela_estátuas, text="Salvar estátua", command=salvar_estátua)
            buttoon_salvar_estátua.pack(pady=10)


        button_salvar_estátua = ctk.CTkButton(tela_estátuas, text="Adicionar Estátua", command=adicionar_estátua)
        button_salvar_estátua.pack(pady=10)

        def ver_estátuas():
            try:
                cursor.execute("SELECT estátua_nome, preço FROM estátuas;")
                estátuas = cursor.fetchall()
                estátuas_lista = "\n".join([f"{e[0]} - R${e[1]}" for e in estátuas])
                messagebox.showinfo("Estátuas", f"Estátuas:\n{estátuas_lista}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao ler estátuas: {e}")

        button_ver_estátuas = ctk.CTkButton(tela_estátuas, text="Ver Estátuas", command=ver_estátuas)
        button_ver_estátuas.pack(pady=10)

        def remover_estátua():
            def excluir_estátua():
                estátua_nome = entry_estátua_remover.get()
                try:
                    cursor.execute("DELETE FROM estátuas WHERE estátua_nome=%s", (estátua_nome,))
                    conn.commit()
                    messagebox.showinfo("Sucesso", "Estátua removida com sucesso!")
                    entry_estátua_remover.delete(0, ctk.END)
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao remover estátua: {e}")

            label_estátua_remover = ctk.CTkLabel(tela_estátuas, text="Nome da Estátua a Remover:")
            label_estátua_remover.pack(pady=5)

            entry_estátua_remover = ctk.CTkEntry(tela_estátuas)
            entry_estátua_remover.pack(pady=5)

            button_excluir_estátua = ctk.CTkButton(tela_estátuas, text="Remover Estátua", command=excluir_estátua)
            button_excluir_estátua.pack(pady=10)

        button_remover_estátua = ctk.CTkButton(tela_estátuas, text="Remover Estátua", command=remover_estátua)
        button_remover_estátua.pack(pady=10)

    # Botões para escolher entre Estátuas e quadros
    button_quadros = ctk.CTkButton(tela_escolha, text="Gerenciar quadros", command=abrir_tela_quadros)
    button_quadros.pack(pady=10)

    button_estátuas = ctk.CTkButton(tela_escolha, text="Gerenciar Estátuas", command=abrir_tela_estátuas)
    button_estátuas.pack(pady=10)


# Configurações da janela
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

root = ctk.CTk()  # Criação da janela
root.title("Tela de Login")
root.geometry('300x300')

# Widgets da tela de login
label_usuario_nome = ctk.CTkLabel(root, text="Usuário")
label_usuario_nome.pack(pady=10)

entry_usuario_nome = ctk.CTkEntry(root)
entry_usuario_nome.pack(pady=10)

label_password = ctk.CTkLabel(root, text="Senha")
label_password.pack(pady=10)

entry_password = ctk.CTkEntry(root, show="*")
entry_password.pack(pady=10)

button_login = ctk.CTkButton(root, text="Login", command=login)
button_login.pack(pady=20)

def abrir_tela_principal():
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
                cursor.execute("INSERT INTO usuarios (usuario_nome, senha) VALUES (%s, %s)", (novo_usuario, nova_senha))
                conn.commit()
                messagebox.showinfo("Sucesso", "Usuário criado com sucesso!")
                entry_novo_usuario.delete(0, ctk.END)
                entry_nova_senha.delete(0, ctk.END)

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

        tela_criar_usuario.deiconify()

    def ler_usuarios():
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT usuario_nome FROM usuarios;")
            usuarios = cursor.fetchall()
            usuarios_lista = "\n".join([user[0] for user in usuarios])
            messagebox.showinfo("Usuários", f"Usuários:\n{usuarios_lista}")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler usuários: {e}")

    def deletar_usuario():
        def excluir_usuario():
            usuario_a_deletar = entry_usuario_deletar.get()
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM usuarios WHERE usuario_nome=%s", (usuario_a_deletar,))
                conn.commit()
                messagebox.showinfo("Sucesso", "Usuário deletado com sucesso!")
                entry_usuario_deletar.delete(0, ctk.END)
  
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao deletar usuário: {e}")
        
        label_usuario_deletar = ctk.CTkLabel(tela_deletar_usuario, text="Usuário a Deletar:")
        label_usuario_deletar.pack(pady=5)

        entry_usuario_deletar = ctk.CTkEntry(tela_deletar_usuario)
        entry_usuario_deletar.pack(pady=5)

        button_excluir = ctk.CTkButton(tela_deletar_usuario, text="Deletar Usuário", command=excluir_usuario)
        button_excluir.pack(pady=10)

        tela_deletar_usuario.deiconify()

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


button_editar = ctk.CTkButton(root, text='Editar usuarios', command=abrir_tela_principal)
button_editar.pack(pady=15)


# Iniciar o loop principal
root.mainloop()