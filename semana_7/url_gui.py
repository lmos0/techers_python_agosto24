import tkinter, pyshorteners 

window = tkinter.Tk()
window.title('Encurtador de URL')
window.geometry('300x150')

def encurtar_link():
    encurtador = pyshorteners.Shortener()
    url_encurtada = encurtador.tinyurl.short(urllonga_entry.get())
    urlcurta_entry.insert(0, url_encurtada)


    
#Criar os widgets

urllonga_label = tkinter.Label(window, text='Coloque a URL a ser encurtada:')
urllonga_entry = tkinter.Entry(window)

urlcurta_label = tkinter.Label(window, text='Aqui está seu link encurtado:')
urlcurta_entry = tkinter.Entry(window)

botao_encurtador = tkinter.Button(window, text='Enviar', command=encurtar_link)



#Posicionar elementos

urllonga_label.pack()
urllonga_entry.pack()

urlcurta_label.pack()
urlcurta_entry.pack()

botao_encurtador.pack()





window.mainloop()