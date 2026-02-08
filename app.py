from flask import Flask, render_template, request, redirect
import banco

app = Flask(__name__)

# Garante que a tabela existe
banco.criar_tabela()

@app.route('/')
def index():
    # Pega os sócios do banco
    lista_socios = banco.listar_socios()
    # Mostra o arquivo HTML enviando a lista para ele
    return render_template('index.html', socios=lista_socios)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/criar', methods=['POST'])
def criar():
    # Pega os dados digitados no formulário do navegador
    nome = request.form['nome']
    cpf = request.form['cpf']
    plano = request.form['plano']
    
    banco.adicionar_socio(nome, cpf, plano)
    return redirect('/')

@app.route('/deletar/<int:id>')
def deletar(id):
    banco.deletar_socio(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)