from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF

def obter_produtos():
    with open ("produtos.csv", "r") as file:
        lista_produtos = []
        for linha in file:
            nome,descricao,preco,imagem = linha.strip().split(",")
            produto = {
                "nome": nome,
                "descricao": descricao,
                "preco": float (preco),
                "imagem": imagem
            }
            lista_produtos.append(produto)
        return lista_produtos

def adicionar_produto(p):
    linha = f"\n{p['nome']},{p['descricao']},{p['preco']},{p['imagem']}"
    with open("produtos.csv", "a") as file:
        file.write(linha)
    

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return render_template('produtos.html', produtos=obter_produtos())

#GET
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro-produto.html")

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in obter_produtos():
        if produto["nome"].lower() == nome.lower():
            return render_template("produto.html", produto=produto)
    return "produto não encontrado"

@app.route("/gerarcpf")
def gerador_cpf():
    cpf = CPF()
    return render_template("gerarCPF.html", cpf = cpf.generate(mask=True))

@app.route("/validarcpf")
def validar_cpf():
    cpf = CPF()
    cpf.validate("012.345.678-90")
    cpf.validate("012.345.678-91")
    if cpf.validate == True:
        return render_template("validarCPF.html", cpf = "cpf valido")
    else:
        return render_template("validarCPF.html", cpf = "cpf invalido")

@app.route("/produtos", methods=['POST'])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']
    imagem = request.form['imagem']
    produto = { "nome": nome, "descricao": descricao, "preco": preco, "imagem": imagem}
    adicionar_produto(produto)

    return redirect(url_for("produtos"))

app.run(port=5001)
