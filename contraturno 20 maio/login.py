from flask import flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')
     
@app.route('/autenticar', methods=['GET'])
def autenticar():
    username = request.args.get('username')
    curso = request.args.get('curso')
    return f'Bem-vindo, {username}! Você está matriculado no curso de {curso}.'
    cidade = request.args.get('cidade')
    return f'Bem-vindo, {username}! Você está matriculado no curso de {curso} e mora em {cidade}.'
    



if __name__ == '__main__':
    app.run(debug=True)