from tkinter import ttk
import tkinter

janela = tkinter.Tk() #Classe TK é a classe que cria a janela principal do nosso programa

janela.title('Minha primeira janela')
janela.geometry('340x440') #330 pixeis de largura e 440pixeis de altura
janela.resizable(True, True) # Ativa/Desativa a possibilidade de redimenssionar o tamanho da tela LxA


#widgets => São componentes visuais que colocamos na janela/tela
 #botão, caixa de texto, rótulo(label), container, frame


def hello_world():
    print('hello world')

### Criação dos Widgets

label = tkinter.Label(janela, text='Tela de Login', font=('Georgia', 20))
button = tkinter.Button(janela, text='Fazer Login', font=('Times New Roman', 15), background='blue', foreground='white', command=hello_world)
entry = tkinter.Entry(janela, show='*')
checkbox = tkinter.Checkbutton(janela)
label2 = tkinter.Label(janela,text='Concordo com os termos de uso' )
radio = tkinter.Radiobutton(janela, text='Português')
radio2 = tkinter.Radiobutton(janela, text='Inglês')
radio3 = tkinter.Radiobutton(janela, text='Francês')



#### Posicionamento dos widgets
# label.pack()
# button.pack()
# entry.pack()
checkbox.grid(row=0, column=0)
label2.grid(row=0, column=1)

radio.grid(row=1, column=0)
radio2.grid(row=2, column=0 )
radio3.grid(row=3, column=0)



janela.mainloop() #Garantir que minha janela fique aberta durante toda a execução do código
