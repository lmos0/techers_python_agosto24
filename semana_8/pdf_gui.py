from pypdf import PdfReader
import tkinter
from tkinter import filedialog




def extract_text():
    global filename

    try:
        if filename is None:
            filename = filedialog.askopenfilename(title='Seleciona arquivo PDF', initialdir=r"C:\Users\luis.santos\Documents\pyad3\semana_8\pdf_gui.py")

    
        leitor = PdfReader(filename)
        pagina = leitor.pages[int(spinbox.get())]
        texto_do_pdf = pagina.extract_text()
        text.delete(1.0, tkinter.END)
        text.insert(tkinter.END, texto_do_pdf)
    except FileNotFoundError:
        label.config(text='Arquivo não encontrado', fg='red')
    except IndexError:
        label.config(text='Não há o número da página que você deseja acessar no arquivo', fg='red')
        text.delete(1.0, tkinter.END)
    except NameError:
        label.config(text='Você não selecionou nenhum arquivo', fg='red')



def openfile():
    
    global filename
    filename = filedialog.askopenfilename(title='Seleciona arquivo PDF', initialdir=r"C:\Users\luis.santos\Documents\pyad3\semana_8\pdf_gui.py")
    leitor = PdfReader(filename)
    label.config(text=filename)
    pagina = leitor.pages[int(spinbox.get())]
    texto_do_pdf = pagina.extract_text()
    text.delete(1.0, tkinter.END)
    text.insert(tkinter.END, texto_do_pdf)




window = tkinter.Tk()

window.title('Leitor de PDF')

label = tkinter.Label(window, text='Nenhum arquivo selecionado')
text = tkinter.Text(window)
button = tkinter.Button(window, text='Selecionar arquivo', command=openfile)
button_extract = tkinter.Button(window, text='Extrair texto', command=extract_text)
spinbox = tkinter.Spinbox(window, from_=1, to=1000)

label.pack()
spinbox.pack()
text.pack()
button.pack()
button_extract.pack()


window.mainloop()
