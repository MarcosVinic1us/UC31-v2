from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cadrastro', methods =['GET','POST'])
def cadrastro():

    nome = ""

    if request.method == 'POST':
        if not nome:
                mensagem = "O campo nome é obrigatório"
        else:
            mensagem = f"Cadrastro realizado com sucesso! Bem-vindo, {nome}"
        
    return render_template('cadastro.html', nome= nome)

@app.route('/validacao', methods = ['POST'])
def validacao():

    nome = request.form.get('nome', '').strip().tittle()
    email = request.form.get('email', '').strip().lower()
    telefone = request.form.get('telefone', '').strip().tittle()
    cargo = request.form.get('cargo','').strip().tittle()
    
    return f"""
    Nome: {nome}<br>
    Email: {email}<br>
    Telefone: {telefone}
    Cargo: {cargo}<br>
    

    """
    if__name__ == '__main__'
    app.run(debug =True)
