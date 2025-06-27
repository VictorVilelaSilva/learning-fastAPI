# Fast Zero API

## Índice

1. [Pré-requisitos](#-pré-requisitos)
2. [Rodando o Projeto pela Primeira Vez](#-rodando-o-projeto-pela-primeira-vez)
3. [Para Quem Já Fez a Instalação Inicial](#-para-quem-já-fez-a-instalação-inicial)
4. [Colocando o Interpretador do Poetry no VSCode](#colocando-o-interpretador-do-poetry-no-vscode)
5. [Estrutura do Projeto](#-estrutura-do-projeto)
6. [Tecnologias Utilizadas](#-tecnologias-utilizadas)
7. [Licença](#-licença)

---

Este projeto utiliza FastAPI para criar uma API robusta e moderna, seguindo boas práticas de desenvolvimento.

## 📋 Pré-requisitos

- Python 3.13 ou superior
- pipx (para instalação isolada de ferramentas Python)
- Poetry (para gerenciamento de dependências)

## 🚀 Rodando o Projeto pela Primeira Vez

### 1. Gerenciamento de Versões Python com pipx

pipx é essencial para instalar ferramentas Python globalmente, mas de forma isolada:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

> ⚠️ Reinicie seu terminal após a instalação para que as mudanças de PATH sejam aplicadas.

### 2. Instalação do Poetry

Usamos Poetry para gerenciar as dependências do projeto:

```bash
pipx install poetry
```

### 3. Configuração Inicial do Projeto

Navegue até a pasta raiz do projeto e instale as dependências:

```bash
poetry install
```
Este comando criará um ambiente virtual isolado com todas as dependências necessárias.

### 4. Ativando o Ambiente Virtual

Para trabalhar dentro do ambiente virtual do Poetry:

```bash
poetry shell
```

Você verá o nome do ambiente virtual no prompt do seu terminal, indicando que ele está ativo.

### 5. Executando o Projeto

Uma vez no ambiente virtual, você pode iniciar a aplicação FastAPI:

```bash
fastapi dev fast_zero/app.py
```

> 💡 A aplicação estará disponível em http://localhost:8000
>
> 📚 A documentação da API estará em http://localhost:8000/docs

## 🔄 Para Quem Já Fez a Instalação Inicial

Se você já configurou o ambiente anteriormente:

1. **Navegue até a pasta do projeto**:
   ```bash
   cd /caminho/para/learning-fastAPI
   ```

2. **Ative o ambiente virtual do Poetry**:
   ```bash
   poetry shell
   ```

3. **Atualize dependências** (se necessário):
   ```bash
   poetry update
   ```
4. **Execute o projeto**:
   ```bash
   fastapi dev fast_zero/app.py
   ```

## Colocando o Interpretador do Poetry no VSCode
Para configurar o Visual Studio Code para usar o interpretador do Poetry, siga estes passos:
1. dentro do terminal do vscode, ative o ambiente virtual do Poetry:
   ```bash
   poetry shell
   ```
2. Digite o comando abaixo para saber o path do interpretador do Poetry:
   ```bash
   poetry env info --path
   ```
3. Copie o caminho retornado e abra o Visual Studio Code.
4. Pressione `Ctrl + Shift + P` e digite "Python: Select Interpreter".
5. Cole o caminho do interpretador do Poetry na barra de pesquisa e selecione-o.

## 📝 Estrutura do Projeto

```
fast_zero/
  ├── __init__.py
  └── app.py           # Aplicação principal FastAPI
tests/
  └── __init__.py      # Testes automatizados
poetry.lock            # Versões exatas das dependências
pyproject.toml         # Configuração do projeto
README.md
```

## 🛠️ Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e de alto desempenho
- **Poetry**: Gerenciamento de dependências e empacotamento
- **Uvicorn**: Servidor ASGI para aplicações Python

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.
