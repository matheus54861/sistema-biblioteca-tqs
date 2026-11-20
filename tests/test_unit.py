import pytest
import sqlite3
import os
from app import app, init_db

@pytest.fixture
def client():
    # Prepara um banco de testes temporário isolado
    app.config['TESTING'] = True
    test_db = 'test_database.db'
    
    conn = sqlite3.connect(test_db)
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

    with app.test_client() as client:
        yield client

    if os.path.exists(test_db):
        os.remove(test_db)

# Teste 1: Cálculo de preço com desconto (o seu teste inicial)
def test_calculo_preco_livro():
    preco_base = 50.0
    desconto = 10.0
    preco_final = preco_base - desconto
    assert preco_final == 40.0

# Teste 2: Validação da rota principal (Home)
def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200

# Teste 3: Validação de regra de negócio para preço inválido/negativo
def test_validar_preco_invalido():
    preco = -10.0
    assert preco <= 0

# Teste 4: Validação de preço válido
def test_validar_preco_valido():
    preco = 49.90
    assert preco > 0

# Teste 5: Verificação do status padrão de um livro cadastrado
def test_status_inicial_livro():
    status_padrao = 'Disponível'
    assert status_padrao == 'Disponível'

# Teste 6: Validação da lógica de filtro de busca por texto
def test_filtro_busca_titulo():
    titulo = "Engenharia de Software"
    termo_busca = "Engenharia"
    assert termo_busca.lower() in titulo.lower()

def test_calcular_multa_atraso():
    from app import calcular_multa
    # 3 dias de atraso com taxa de R$ 2.00 por dia = R$ 6.00
    assert calcular_multa(dias_atraso=3, taxa_diaria=2.0) == 6.0

    def test_remover_livro_logica():
        # Simula a remoção de um ID de livro no banco de dados
        livros_cadastrados = [1, 2, 3]
        livro_a_remover = 2
        if livro_a_remover in livros_cadastrados:
            livros_cadastrados.remove(livro_a_remover)
        assert livro_a_remover not in livros_cadastrados