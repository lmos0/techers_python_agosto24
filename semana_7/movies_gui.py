import requests, tkinter

window = tkinter.Tk()

window.title('Consulta sobre Filmes')
window.geometry('400x300')


def getting_info_from_api(filme_consultado):
    url = f'https://www.omdbapi.com/?t={filme_consultado}&apikey=35d90404'
    resposta = requests.get(url)
    info_movie = resposta.json()

    texto_da_resposta = (
    f"Título:\t {info_movie['Title']}\n"
    f"Ano de Lançamento:\t {info_movie['Year']}\n"
    f"Nota IMDB:\t {info_movie['imdbRating']}\n"
    f"Direção:\t {info_movie['Director']}\n"
    f"Elenco:\t {info_movie['Actors']}\n"
    f"País de Origem:\t {info_movie['Country']}\n"
    )

    return texto_da_resposta


def update_gui():
    filme_escolhido = entry.get()
    texto = getting_info_from_api(filme_escolhido)
    label.config(text=texto)

#Criar Widgets

frame = tkinter.Frame() #Widget invisível que tem a função de criar um sub-divisão dentro da janela/ou de outro widget
button = tkinter.Button(frame, text='Consultar Filme', font=('Arial', 12), command=update_gui)
entry = tkinter.Entry(frame, width=30, font=('Arial', 12))
label = tkinter.Label(frame, font=('Arial', 10), justify='left', wraplength=250)


#Posicionar
frame.pack(pady=20)

entry.pack(pady=10)
label.pack(pady=10)
button.pack(pady=10)

window.mainloop()