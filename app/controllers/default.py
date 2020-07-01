from app import app


@app.route('/') #Cria uma rota
def main():
    return 'Meu e-commerce em Flask :D'

