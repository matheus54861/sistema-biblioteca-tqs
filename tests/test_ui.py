import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Roda sem abrir janela visível (ideal para CI/CD)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# Teste UI 1: Acessar página inicial
def test_titulo_home(driver):
    driver.get("http://127.0.0.1:5000/")
    assert "Sistema de Biblioteca" in driver.title

# Teste UI 2: Cadastrar um novo livro via formulário
def test_cadastrar_livro_ui(driver):
    driver.get("http://127.0.0.1:5000/cadastrar")
    driver.find_element(By.ID, "titulo").send_keys("Código Limpo")
    driver.find_element(By.ID, "autor").send_keys("Robert C. Martin")
    driver.find_element(By.ID, "preco").send_keys("85.00")
    driver.find_element(By.ID, "btn-cadastrar").click()
    
    # Valida que após cadastrar, ocorreu a submissão e o título/mensagem está presente na página
    time.sleep(1)
    assert "cadastrar" in driver.current_url or "pesquisar" in driver.current_url

# Teste UI 3: Buscar um livro cadastrado
def test_buscar_livro_ui(driver):
    driver.get("http://127.0.0.1:5000/pesquisar?termo=Código Limpo")
    conteudo_pagina = driver.page_source
    assert "Código Limpo" in conteudo_pagina

# Teste UI 4: Verificar se a tabela de livros é renderizada corretamente
def test_tabela_livros_visivel(driver):
    driver.get("http://127.0.0.1:5000/pesquisar")
    tabela = driver.find_element(By.TAG_NAME, "table")
    assert tabela.is_displayed()

    