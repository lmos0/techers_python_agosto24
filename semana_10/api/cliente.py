import tkinter as tk 
from tkinter import messagebox
from tkinter import ttk

import requests 

API_URL_LIVROS = "http://127.0.0.1:5000/livros" 
API_URL_EMPRESTIMOS = 'http://127.0.0.1:5000/emprestimos'
API_URL_DEVOLVER = "http://127.0.0.1:5000/devolver"


def adicionar_livros():
    titulo = entry_title.get()
    autor = entry_author.get()

    if not titulo or not autor:
        messagebox.showerror("Erro", "Os campos 'Título' e 'Autor' são obrigatórios")
        return
    
    dados = {"titulo": titulo, "autor": autor}
    response = requests.post(API_URL_LIVROS, json=dados)

    if response.status_code == 200:
        messagebox.showinfo('Sucesso', 'Livro adicionado com sucesso!')
    
    else:
        messagebox.showerror('Erro', 'Erro ao adicionar o livro')

def listar_livros():
    response = requests.get(API_URL_LIVROS)

    if response.status_code == 200:
        livros = response.json()
        lista_livros.delete(0, tk.END)
        for titulo, dados in livros.items():
            status = "Disponível" if dados['disponivel'] else "Emprestado"
            lista_livros.insert(tk.END, f'{titulo} - {dados['autor']} ({status})' )
    
    else:
        messagebox.showerror('Erro', 'Não foi possível listar os livros')

def registrar_emprestimo():
    titulo = entry_title.get()
    usuario = entry_user.get()

    if not titulo or not usuario:
        messagebox.showerror('Erro', 'Título e usuário são obrigatórios')
        return
    
    dados = {"titulo": titulo, "usuario": usuario}
    response = requests.post(API_URL_DEVOLVER, json=dados)

    if response.status_code == 200:
        messagebox.showinfo('Sucesso', 'Empréstimo registrado com sucesso')
        lista_livros()
    else:
        messagebox.showerror('Erro', 'Erro ao registrar empréstimo')


root = tk.Tk()
root.title("Sistema de Gestão de Biblioteca")
root.geometry('500x400')
root.configure(bg='#f4f4f4')

title_label = tk.Label(root, text='Sistema de Gestão de Biblioteca', font=('Arial', 16, 'bold'), bg='#f4f4f4')
title_label.pack(pady=10)

#Frame para os Inputs
input_frame = tk.Frame(root, bg='#f4f4f4')
input_frame.pack(padx=10, pady=10)

tk.Label(input_frame, text='Título do Livro', bg='#f4f4f4').grid(row=0, column=0, padx=5, pady=5)
entry_title = tk.Entry(input_frame, width=30)
entry_title.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Autor', bg='#f4f4f4').grid(row=1, column=0, padx=5, pady=5)
entry_author = tk.Entry(input_frame, width=30)
entry_author.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Usuário', bg='#f4f4f4').grid(row=2, column=0, padx=5, pady=5)
entry_user = tk.Entry(input_frame, width=30)
entry_user.grid(row=2, column=1, padx=5, pady=5)

### Frame para os Botões

button_frame = tk.Frame(root, bg='#f4f4f4')
button_frame.pack(pady=10)

style = ttk.Style()
style.configure("TButton", font=('Arial', 10), padding=5)

btn_add = ttk.Button(button_frame, text='Adicionar Livro', command=adicionar_livros)
btn_add.grid(row=0, column=0, padx=5)

btn_loan = ttk.Button(button_frame, text='Registrar Empréstimo')
btn_loan.grid(row=0, column=1, padx=5)

btn_return = ttk.Button(button_frame, text='Devolver Livro')
btn_return.grid(row=0, column=2, padx=5)

btn_list = ttk.Button(button_frame, text='Listar Livros', command=listar_livros)
btn_list.grid(row=0, column=3, padx=5)

#Frame Listbox

list_frame = tk.Frame(root, bg='#f4f4f4')
list_frame.pack(padx=10, pady=10, fill='both', expand=True)

#Listbox para mostar os livros
lista_livros = tk.Listbox(list_frame, width=50, height=10, font=('Arial', 10))
lista_livros.pack(expand=True, fill='both', side='left')

#Scrollbar

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')

lista_livros.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=lista_livros.yview)


listar_livros()
root.mainloop()