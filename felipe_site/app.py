from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF

lista_produtos = [
    { "nome": "Coca-cola", "descricao": "Bom", "preco": "34", "imagem": "https://s2-autoesporte.glbimg.com/60nN_HcELu8vZR5cU4zPwFhjOoU=/0x0:1079x743/888x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_cf9d035bf26b4646b105bd958f32089d/internal_photos/bs/2023/4/X/KBUANHSba3nEgm2x3FDQ/ferrari-sf90-stradale-max-verstappen.jpg" },
    { "nome": "Doritos", "descricao": "Suja mão", "preco": "67", "imagem": "https://s2-autoesporte.glbimg.com/60nN_HcELu8vZR5cU4zPwFhjOoU=/0x0:1079x743/888x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_cf9d035bf26b4646b105bd958f32089d/internal_photos/bs/2023/4/X/KBUANHSba3nEgm2x3FDQ/ferrari-sf90-stradale-max-verstappen.jpg" },
    { "nome": "Chocolate", "descricao": "Bom!", "preco": "21", "imagem": "https://s2-autoesporte.glbimg.com/60nN_HcELu8vZR5cU4zPwFhjOoU=/0x0:1079x743/888x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_cf9d035bf26b4646b105bd958f32089d/internal_photos/bs/2023/4/X/KBUANHSba3nEgm2x3FDQ/ferrari-sf90-stradale-max-verstappen.jpg"}
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

#GET
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro-produto.html")

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
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
        return render_tempalte("validarCPF.html", cpf = "cpf valido")
    else:
        return render_template("validarCPF.html", cpf = "cpf invalido")

@app.route("/produtos", methods=['POST'])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']
    imagem = request.form['imagem']
    produto = { "nome": nome, "descricao": descricao, "preco": preco, "imagem": imagem}
    lista_produtos.append(produto)

    return redirect(url_for("produtos"))

app.run(port=5001)
