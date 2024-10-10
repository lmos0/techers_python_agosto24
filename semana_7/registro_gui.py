import tkinter
from tkinter import ttk
from tkinter import messagebox



def buscar_dados():

    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    cpf = cpf_entry.get()

    if variavel_de_verificacao.get() != 'sim':
        messagebox.showerror('Erro', 'Você deve declarar que as informações são verdadeiras')
        return
    
    file = open('dados_de_usuario.txt', 'a')
    file.write(f'\nNome: {firstname}\n Sobrenome: {lastname}\n Título: {title}\n Idade:, {age}\n, CPF: {cpf}\n' )

    # print('Nome:', firstname)
    # print('Sobrenome:', lastname),
    # print('Título:', title),
    # print('Idade:', age)
    # print('CPF:', cpf)




window = tkinter.Tk()
window.title('Decleração IRPF da Shopee')
window.geometry('500x400')
window.resizable(False,False)

#btn_params = {'padx': 10, 'pady':10, 'fg': 'white', 'bg': '#333', 'font': ('Arial, 26')}

font_params = {'font':('Arial', 8, 'bold')}

#Criar Widgets
frame = tkinter.Frame()
user_info_frame = tkinter.LabelFrame(frame, text='Dados Pessoais', **font_params)
tax_info_frame = tkinter.LabelFrame(frame, text='Informações Fiscais', **font_params)

first_name_label = tkinter.Label(user_info_frame, text='Nome', **font_params)
first_name_entry = tkinter.Entry(user_info_frame)



last_name_label = tkinter.Label(user_info_frame,text='Sobrenome', **font_params)
last_name_entry = tkinter.Entry(user_info_frame)

title_label = tkinter.Label(user_info_frame, text='Pronome de tratamento',**font_params)
title_combobox = ttk.Combobox(user_info_frame, values=['', 'Sr.', 'Sra', "Msc", 'Dr', 'Dr(a)'])

age_label = tkinter.Label(user_info_frame, text='Idade', **font_params)
age_spinbox = tkinter.Spinbox(user_info_frame, from_= 16, to=110)

cpf_label = tkinter.Label(user_info_frame, text='CPF', **font_params)
cpf_entry = tkinter.Entry(user_info_frame)

income_label = tkinter.Label(tax_info_frame, text='Renda Declarada', **font_params)
income_entry = tkinter.Entry (tax_info_frame)

terms_frame = tkinter.LabelFrame(frame, text='Declaro que as informações fornecidas são verdadeiras', **font_params)
variavel_de_verificacao = tkinter.StringVar(value='sim')
terms_check = tkinter.Checkbutton(terms_frame, text='Sim', variable=variavel_de_verificacao, onvalue='sim', offvalue='não')


submit_button = tkinter.Button(window, text='Enviar', **font_params, command=buscar_dados)


#Posicionar Widgets
frame.pack()
user_info_frame.grid(row=0, column=0, padx=20, pady=20)
tax_info_frame.grid(row=1, column=0, padx=20, pady=20)
terms_frame.grid(row=2, column=0, padx=20, pady=20)



first_name_label.grid(row=0, column=1)
first_name_entry.grid(row=1, column=1)

last_name_label.grid(row=0, column=2)
last_name_entry.grid(row=1, column=2)

title_label.grid(row=0, column=0)
title_combobox.grid(row=1, column=0)

age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

cpf_label.grid(row=2, column=1)
cpf_entry.grid(row=3, column=1)

income_label.grid(row=0, column=0)
income_entry.grid(row=0, column=1)

terms_check.pack()

submit_button.pack()


window.mainloop()