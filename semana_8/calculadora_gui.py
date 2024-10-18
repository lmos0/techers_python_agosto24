import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_resut.delete(1.0, "end")
    text_resut.insert(1.0, calculation)


def clear_field():
    global calculation
    calculation = ""
    text_resut.delete(1.0, "end")

def eval_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_resut.delete(1.0,"end")
        text_resut.insert(1.0,calculation)
    except ZeroDivisionError:
        clear_field()
        text_resut.insert(1.0, 'Não é possível dividir por zero')
    except SyntaxError:
        clear_field()
        text_resut.insert( 1.0, 'Insira apenas números')

root = tk.Tk()
root.geometry('320x310')
root.title('Calculadora TECHERS')

btn_params = {'padx':10, 'pady': 10, 'fg':'white', 'bg':'#333333', 'font':('Arial', 12), 'width':5}

text_resut = tk.Text(root, height=2, width=16, font=('Arial', 20), bg='#eee')
text_resut.grid(columnspan=4, padx=10, pady=10)


btn_1 = tk.Button(root, text='1', **btn_params, command=lambda:add_to_calculation(1) )
btn_1.grid(row=2, column=0)

btn_2 = tk.Button(root, text='2', **btn_params, command=lambda:add_to_calculation(2))
btn_2.grid(row=2, column=1)

btn_3 = tk.Button(root,text='3', **btn_params, command=lambda:add_to_calculation(3) )
btn_3.grid(row=2, column=2)

btn_4 = tk.Button(root, text='4', **btn_params, command=lambda:add_to_calculation(4))
btn_4.grid(row=3, column=0)

btn_5 = tk.Button(root, text='5', **btn_params, command=lambda:add_to_calculation(5))
btn_5.grid(row=3, column=1)

btn_6 = tk.Button(root, text='6', **btn_params, command=lambda:add_to_calculation(6))
btn_6.grid(row=3, column=2)


btn_7 = tk.Button(root, text='7', **btn_params, command=lambda:add_to_calculation(7))
btn_7.grid(row=4, column=0)

btn_8 = tk.Button(root, text='8', **btn_params, command=lambda:add_to_calculation(8))
btn_8.grid(row=4, column=1)

btn_9 = tk.Button(root, text='9', **btn_params, command=lambda:add_to_calculation(9))
btn_9.grid(row=4, column=2)

btn_0 = tk.Button(root, text='0', **btn_params, command=lambda:add_to_calculation(0))
btn_0.grid(row=5, column=1)


btn_plus = tk.Button(root, text='+', **btn_params, command=lambda:add_to_calculation('+'))
btn_plus.grid(row=2, column=3)

btn_minus = tk.Button(root, text='-', **btn_params, command=lambda:add_to_calculation('-'))
btn_minus.grid(row=3, column=3)

btn_multi = tk.Button(root, text='x', **btn_params, command=lambda:add_to_calculation('*'))
btn_multi.grid(row=4, column=3)

btn_div = tk.Button(root, text='÷', **btn_params, command=lambda:add_to_calculation('/'))
btn_div.grid(row=5, column=3)

btn_erase = tk.Button(root, text='C', **btn_params, command=clear_field)
btn_erase.grid(row=5, column=0)

btn_equal = tk.Button(root,text='=', **btn_params, command=eval_calculation)
btn_equal.grid(row=5, column=2)

root.mainloop()

