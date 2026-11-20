from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'chave_secreta_ficticia'

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            preco REAL NOT NULL,
            status TEXT DEFAULT 'Disponível'
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        preco = float(request.form['preco'])
        
        if not titulo or not autor or preco <= 0:
            flash('Preencha todos os campos corretamente!', 'danger')
            return redirect(url_for('cadastrar'))
            
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO livros (titulo, autor, preco, status) VALUES (?, ?, ?, ?)',
                       (titulo, autor, preco, 'Disponível'))
        conn.commit()
        conn.close()
        flash('Livro cadastrado com sucesso!', 'success')
        return redirect(url_for('pesquisar'))
    return render_template('cadastrar.html')

@app.route('/pesquisar', methods=['GET'])
def pesquisar():
    termo = request.args.get('termo', '')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    if termo:
        cursor.execute("SELECT * FROM livros WHERE titulo LIKE ?", ('%' + termo + '%',))
    else:
        cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    conn.close()
    return render_template('pesquisar.html', livros=livros, termo=termo)

@app.route('/alugar/<int:id>', methods=['GET', 'POST'])
def alugar(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("UPDATE livros SET status = 'Alugado' WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return render_template('alugar.html')
    conn.close()
    return redirect(url_for('pesquisar'))

@app.route('/comprar/<int:id>', methods=['GET', 'POST'])
def comprar(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("UPDATE livros SET status = 'Vendido' WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return render_template('comprar.html')
    conn.close()
    return redirect(url_for('pesquisar'))

@app.route('/remover/<int:id>', methods=['POST'])
def remover(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livros WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    flash('Livro removido com sucesso!', 'success')
    return redirect(url_for('pesquisar'))

def calcular_multa(dias_atraso, taxa_diaria=2.0):
    if dias_atraso <= 0:
        return 0.0
    return dias_atraso * taxa_diaria

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)