from pypdf import PdfReader
import tkinter
from tkinter import filedialog


def openfile():
    
    filename = filedialog.askopenfilename(title='Seleciona arquivo PDF', initialdir=r"C:\Users\luis.santos\Documents\pyad3\semana_8\pdf_gui.py")
    leitor = PdfReader(filename)
    pagina = leitor.pages[4]
    print(pagina.extract_text())



window = tkinter.Tk()

label = tkinter.Label(window, text='Nenhum arquivo selecionado')
text = tkinter.Text(window)
button = tkinter.Button(window, text='Selecionar arquivo', command=openfile)

label.pack()
text.pack()
button.pack()


window.mainloop()

