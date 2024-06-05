from flask import Flask, render_template

lista_produtos = [
        { "nome": "Coca-cola", "descricao": "Bom" },
        { "nome": "Doritos", "descricao": "Suja mão" },
        { "nome": "Chocolate", "descricao": "Bom!" },
    ]

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home</h1>"


@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return render_template('produtos.html', produtos=lista_produtos)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto["nome"].lower() == nome.lower():
            return f"{produto['nome']}, {produto['descricao']}"
    return "produto nao encontrado"