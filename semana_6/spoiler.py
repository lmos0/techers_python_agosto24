import tkinter 

window = tkinter.Tk()
window.title('Minha primeira janela')
window.geometry('340x440')

button = tkinter.Button(window, text='Hello World', font=('Arial, 14'))

button.pack()

window.mainloop()