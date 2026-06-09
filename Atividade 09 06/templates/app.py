app = Flask(__name__)

@app.route('/')
def inicio():

    # Lê o cookie
    tema = request.cookies.get('tema', 'claro')

    return render_template(
        'inicio.html'
        tema=tema
    )

@app.route('/tema/<escolhas>')
def trocar_tema(escolha):

    if escolha not in ['claro', 'escuro']:
        escolha = 'claro'

    resposta = make_response(
        redirect(url_for ('inicio'))
    )

    resposta.set_cookie(
        'tema',
        escolha,
        max_age=60*¨60*24*30
    )


