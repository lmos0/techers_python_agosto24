import tkinter
from tkinter import messagebox

main_window = tkinter.Tk()
main_window.title('Tela de Login')
main_window.geometry('340x440')
main_window.resizable(False, False)
main_window.configure(bg='gray')


def login():
    username = 'techers'
    password = 'coxinha_123'

    if username_entry.get() == username and password_entry.get() == password:
        #output_label.config(text='Login efetuado com sucesso')
        messagebox.showinfo('Sucesso', 'Login efetuado com sucesso')    
    else:
        #output_label.config(text='Usuário ou senha incorretos, tente novamente.')
        messagebox.showerror('Erro', 'Credenciais inválidas')
        


#Criar os elementos/widgets 

login_label = tkinter.Label(main_window, text='Tela de login', bg='gray', fg='white', font=("Arial", 20))

username_label = tkinter.Label(main_window,text='Usuário', bg='gray', fg='white', font=('Arial', 16))
username_entry = tkinter.Entry(main_window, font=('Arial', 14))

password_label = tkinter.Label(main_window, text='Senha', bg='gray', fg='white', font=('Arial', 16))
password_entry = tkinter.Entry(main_window, font=('Arial', 14), show='*' )

login_button = tkinter.Button(main_window, text='Logar', font=('Arial', 14), command=login)

output_label = tkinter.Label(main_window, text='', bg='gray', fg='white', font=('Arial', 10) )

#Posicionar os elementos

login_label.grid(row=0, column=0, columnspan=2)

username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)

password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)

login_button.grid(row=3, column=0, columnspan=2)

output_label.grid(row=4, column=0, columnspan=2)

main_window.mainloop()

