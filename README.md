# 📚 Sistema de Biblioteca Virtual — Projeto Integrado P2 (TQS)

Projeto desenvolvido para a disciplina de **Testes e Qualidade de Software (TQS)** do curso de **Ciência da Computação — UNISAGRADO (2026)**, ministrada pelo **Prof. Dr. Elvio Gilberto da Silva**.

O objetivo deste projeto é demonstrar a aplicação prática de um processo completo de planejamento, especificação, execução, automação de testes, TDD, integração contínua (CI/CD) e análise de métricas de qualidade sobre uma aplicação web funcional.

---

## 👥 Identificação dos Integrantes
* **Integrante 1:** [Inserir Nome Completo - RA]
* **Integrante 2:** [Inserir Nome Completo - RA]
* **Integrante 3:** [Inserir Nome Completo - RA] *(remover se for dupla)*
* **Contato do Grupo:** [Inserir e-mail institucional ou pessoal do responsável]

---

## 📌 Nome e Versão do Sistema
* **Nome do Sistema:** Sistema de Biblioteca Virtual (`sistema-biblioteca-tqs`)
* **Versão Testada:** `v1.0.0`
* **Link do Repositório GitHub:** [Inserir URL do seu repositório no GitHub]

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.11+
* **Framework Web:** Flask 3.0.2
* **Banco de Dados:** SQLite 3 (persistência local em arquivo)
* **Frontend / Estilização:** HTML5, Jinja2 e Bootstrap 5.3 (via CDN)
* **Testes Unitários e de API:** Pytest 8.1.1 e Requests 2.31.0
* **Testes de Interface (E2E):** Selenium WebDriver 4.18.1 (Google Chrome)
* **Ferramenta de Apoio API:** Postman (Coleção JSON exportada)
* **CI/CD:** GitHub Actions

---

## ⚙️ Pré-requisitos
Antes de iniciar, certifique-se de ter instalado em sua máquina:
1. **Python 3.10 ou superior** (com `pip` habilitado).
2. **Git** para clonagem e controle de versão.
3. **Google Chrome** atualizado (necessário para a execução dos testes automatizados de interface com Selenium).
4. **Editor/IDE** recomendado: Visual Studio Code (VS Code).

---

## 🚀 Instalação e Configuração do Ambiente

1. **Clone o repositório:**
   ```bash
   git clone [INSIRA_A_URL_DO_SEU_REPOSITORIO_AQUI]
   cd sistema-biblioteca-tqs
   ```

2. **Crie e ative um ambiente virtual (`venv`):**
   * **No Windows (Git Bash / Linux / Mac):**
     ```bash
     python -m venv venv
     source venv/Scripts/activate  # No Linux/Mac use: source venv/bin/activate
     ```
   * **No Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate
     ```

3. **Instale as dependências do projeto:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🗄️ Banco de Dados e Massa de Dados
* O sistema utiliza um banco de dados relacional **SQLite** gerado automaticamente na raiz do projeto com o nome `database.db` na primeira inicialização (`init_db()`).
* **Restauração do Ambiente:** Para resetar os dados entre baterias de teste, basta encerrar a aplicação, excluir o arquivo `database.db` e iniciar o servidor novamente. Um banco limpo será recriado automaticamente.
* **Credenciais Fictícias:** O sistema atual opera em ambiente local sem autenticação de login/senha, utilizando exclusivamente dados fictícios de livros (títulos, autores e valores ilustrativos) para garantir conformidade com as regras de segurança e privacidade da disciplina.

---

## ▶️ Como Executar o Sistema
1. Com o ambiente virtual ativado, execute o servidor Flask:
   ```bash
   python app.py
   ```
2. Abra o navegador e acesse:
   ```text
   http://127.0.0.1:5000/
   ```
3. Utilize o menu inicial para navegar entre os fluxos de **Cadastrar Novo Livro**, **Pesquisar Catálogo**, **Alugar**, **Comprar** e **Remover**.

---

## 🧪 Como Executar os Testes Automatizados

### 1. Testes Unitários (Pytest)
Validam regras de negócio isoladas, cálculos de desconto, validações de preço e a evolução implementada via TDD (cálculo de multa por atraso):
```bash
pytest tests/test_unit.py -v -o pythonpath=.
```

### 2. Testes de Integração e API (Requests & Postman)
Com o servidor Flask rodando (`python app.py` em um terminal), execute em outro terminal:
```bash
pytest tests/test_api.py -v -o pythonpath=.
```
*(Opcional: Importe o arquivo `postman/postman_collection.json` no Postman para execução visual).*

### 3. Testes de Sistema / Interface Ponta a Ponta (Selenium)
Com o servidor Flask rodando em segundo plano, execute:
```bash
pytest tests/test_ui.py -v -o pythonpath=.
```

### 4. Executar Toda a Suíte de Testes de Uma Vez
```bash
pytest -v -o pythonpath=.
```

---

## 🔄 Acesso ao Pipeline CI/CD
* O pipeline de integração contínua está configurado em `.github/workflows/pipeline.yml` utilizando **GitHub Actions**.
* **Gatilho:** Executado automaticamente a cada `push` ou `pull_request` nas branches `main` ou `master`.
* **Visualização:** Acesse a aba **Actions** no repositório oficial do GitHub para acompanhar o histórico de builds, logs de instalação e resultados dos testes unitários.

---

## 📂 Localização dos Documentos (Estrutura Google Drive)
Toda a documentação gerencial e evidências técnicas estão organizadas na pasta oficial do Google Drive (`P2_TQS_2026_TURMA_GRUPOXX_SISTEMA-BIBLIOTECA`) seguindo o padrão exigido:
* `00_IDENTIFICACAO_E_README` — Este arquivo e ficha de identificação.
* `01_SISTEMA_ALVO` — Código-fonte completo.
* `02_REQUISITOS_ESCOPO_RISCOS` — Catálogo de requisitos (RF/RNF) e matriz de riscos.
* `03_PLANO_DE_TESTES` — Estratégia, cronograma e critérios de entrada/saída.
* `04_CASOS_E_RASTREABILIDADE` — Catálogo dos 24 casos de teste e matriz de rastreabilidade.
* `05_EXECUCAO_MANUAL` & `06_DEFEITOS` — Evidências de execução e relatório de issues.
* `07` a `10` — Scripts de automação (Unitário, API/Postman, Selenium) e testes não funcionais.
* `11_METRICAS_E_QUALIDADE` — Planilha de indicadores e análise de qualidade.
* `12_TDD_CICD_MELHORIA` — Evidências do ciclo Red-Green-Refactor e logs do pipeline.
* `13_RELATORIO_FINAL` & `14_APRESENTACAO_E_VIDEO_CONTINGENCIA` — Relatório em DOCX/PDF, slides e vídeo de demonstração.
* `15_DIARIO_DE_PARTICIPACAO` & `16_BACKUP_ENTREGA` — Registro de atividades do grupo e cópia de segurança.

---

## ⚠️ Problemas Conhecidos e Limitações
* **Concorrência de Escrita:** Por utilizar SQLite local em arquivo único, múltiplas requisições simultâneas de escrita podem sofrer bloqueio temporário (*database is locked*), comportamento esperado para o escopo acadêmico.
* **Testes Selenium em Ambiente Sem Interface Gráfica:** Os testes de UI estão configurados por padrão em modo `--headless` para compatibilidade com execuções automatizadas.