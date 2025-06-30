# 💰 Sistema de Controle de Contas Bancárias (CLI)

Este projeto é um sistema simples de controle de contas bancárias pessoais, desenvolvido em Python, com persistência via SQLite e visualização gráfica com matplotlib. Ele simula funcionalidades típicas de um aplicativo financeiro, executado em ambiente de linha de comando (CLI).

## 🧩 Funcionalidades principais

- Criar contas associadas a bancos reais
- Realizar transferências entre contas
- Registrar movimentações (entrada/saída)
- Desativar contas com saldo zerado
- Listar e somar o total de saldo entre contas
- Filtrar histórico por data
- Gerar gráfico de saldo por banco

## 🛠️ Tecnologias utilizadas

- **Python 3.13**
- **SQLModel** (modelagem e ORM)
- **SQLite** (banco de dados local)
- **Enum** (representação clara de tipos e status)
- **datetime** (manipulação de datas)
- **matplotlib** (visualização gráfica)
- **Programação orientada a objetos**
- Arquitetura em camadas: `models.py`, `views.py`, `templates.py`

## 🧠 Conhecimentos demonstrados

- Modelagem de dados relacionais com `SQLModel`
- Criação de enums para tipagem segura de valores fixos
- Manipulação de banco de dados relacional com sessões e consultas SQL
- Uso de `Relationship()` para associar tabelas
- Validação de saldo antes de operações
- Conversão entre tipos como `str`, `float` e `date`
- Parsing de datas com `strptime` e filtragem entre períodos
- Exibição de gráficos usando `matplotlib`
- Separação de responsabilidades entre lógica de negócio e interface

## ▶️ Como executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repo.git
    cd nome-do-repo

2. Crie um ambiente virtual e ative:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate.bat  # Windows

3. Instale as dependências:
    pip install -r requirements.txt

4. Execute o projeto:
    python templates.py

## 📌 Possíveis melhorias
    - Adicionar persistência de histórico de transferências
    - Implementar autenticação de usuário
    - Adicionar testes com pytest
    - Criar uma interface web com FastAPI + Vue

## 👨‍💻 Autor
    Desenvolvido por Alan com foco em aprendizado de desenvolvimento fullstack com Python 🐍.