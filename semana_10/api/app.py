from flask import Flask, jsonify, request 

app = Flask(__name__)

#banco de dados em memória

livros = {}

emprestimos = {}

@app.route('/livros')
def listar_livros():
    return jsonify(livros)


@app.route('/livros', methods=['POST'])
def adicionar_livros():
    dados = request.json
    titulo = dados.get("titulo")
    autor = dados.get("autor")

    if not titulo or not autor:
        return jsonify({"erro": "Campo título e o campo autor são obrigatórios" }), 400
    
    livros[titulo] = {
        "autor": autor,
        "disponivel": True
    }

    print(livros)
    return jsonify({"mensagem": "Livro adicionado com sucesso!"}), 200

@app.route('/emprestimos', methods=['POST'] )
def registrar_emprestimo():
    dados = request.json
    titulo = dados.get('titulo')
    usuario = dados.get('usuario')

    if titulo not in livros:
        return jsonify({"erro": "Livro não encontrado"}), 404
    
    if not livros[titulo]["disponivel"]:
        return jsonify({"erro": "Livro não disponível"}), 400
    
    livros[titulo]["disponivel"] = False
    emprestimos[usuario] = titulo
    return jsonify({"mensagem": "Empréstimo registrado com sucesso"}), 200

@app.route('/devolver', methods=['POST'])
def devolver_livro():
    dados = request.json
    usuario = dados.get('usuario')

    if usuario not in emprestimos:
        return jsonify({"erro": "Empréstimo não encontrado para este usuário"}), 404
    
    titulo = emprestimos[usuario]
    livros[titulo]['disponivel'] = True
    del emprestimos[usuario]

    return jsonify({"mensagem": "Livro devolvido com sucesso"}), 200
if __name__ == '__main__':
    app.run(debug=True)