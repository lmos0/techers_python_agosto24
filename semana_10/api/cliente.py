import tkinter as tk 
from tkinter import messagebox
from tkinter import ttk

import requests 

API_URL_LIVROS = "http://127.0.0.1:5000/livros" 
API_URL_EMPRESTIMOS = 'http://127.0.0.1:5000/emprestimos'
API_URL_DEVOLVER = "http://127.0.0.1:5000/devolver"

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

# style = ttk.Style()
# style.config('TButton', font=('Arial', 10))



root.mainloop()