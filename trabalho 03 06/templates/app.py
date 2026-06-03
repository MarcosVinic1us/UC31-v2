from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cadrastro', methods =['GET','POST'])
def cadrastro():

    mnesagem = ""

    if request.method == 'POST':
        if not nome:
            mensagem = "O campo nome é obrigatório"
    elif:
        mensagem = f"Cadrastrom realizado com sucesso! Bem-vindo, {nome}"
        
    return render_template('cadrastro.html', mensagem= mensagem)

@app.route('/validacao', methods = ['POST'])
def cadrastro():

    name = request.form.get('nome', '').strip().tittle()
    email = request.form.get('email', '').strip().lower()
    cidade = request.form.get('cidade', '').strip().tittle()
    CPF = request.form.get('CPF','').strip().tittle()
    estado = request.form.get('estado','').strip().tittle()
    curso = request.form.get('curso','').strip().tittle()
    idade = request.form.get('idade','').strip().tittle()
    senha = request.form.get('senha','').strip().tittle()
    
    return f"""
    Nome: {nome}<br>
    Email: {email}<br>
    Cidade: {cidade}
    CPF: {CPF}<br>
    estado: {estado}<br>
    curso: {curso}
    idade: {idade}<br>
    senha: {senha}

    """
if__name__ == '__main__':
    app.run(debug =True)

