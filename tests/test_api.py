import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

# Teste API 1: Validar se a página inicial responde com sucesso (Status 200)
def test_api_home_status():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200

# Teste API 2: Validar a rota de pesquisa (GET /pesquisar)
def test_api_pesquisa_status():
    response = requests.get(f"{BASE_URL}/pesquisar")
    assert response.status_code == 200

# Teste API 3: Validar cadastro de um livro via requisição POST (Fluxo Positivo)
def test_api_cadastrar_livro_post():
    dados_livro = {
        "titulo": "Arquitetura Limpa",
        "autor": "Robert C. Martin",
        "preco": "79.90"
    }
    # Envia os dados simulando o formulário
    response = requests.post(f"{BASE_URL}/cadastrar", data=dados_livro, allow_redirects=True)
    assert response.status_code == 200
    # Verifica se o livro recém cadastrado aparece na página de pesquisa
    assert "Arquitetura Limpa" in response.text

# Teste API 4: Validar busca de livro específico com parâmetro de consulta (Query Param)
def test_api_busca_com_filtro():
    params = {"termo": "Arquitetura Limpa"}
    response = requests.get(f"{BASE_URL}/pesquisar", params=params)
    assert response.status_code == 200
    assert "Arquitetura Limpa" in response.text

# Teste API 5: Validar resposta de rota inexistente (Fluxo Negativo / Erro 404)
def test_api_rota_nao_encontrada():
    response = requests.get(f"{BASE_URL}/rota-inexistente-12345")
    assert response.status_code == 404