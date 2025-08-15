# Lista de comandos úteis para o projeto `learning-fastAPI`

## Banco de dados

### Acessar o banco de dados SQLite pelo terminal

```bash
pipx run harlequin database.db
```

### Criar uma nova migração

```bash
alembic revision --autogenerate -m "nome_da_migração"
```

### Aplicar migrações pendentes

```bash
alembic upgrade head
```

### Reverter a última migração

```bash
alembic downgrade -1
```

### Debug no FastAPI
Caso você queira debugar o FastAPI, você pode colocar o seguinte trecho de código no ponto onde você quer debugar:

```python
breakpoint()
```
E então, ao rodar basta bater na rota que você colocou o `breakpoint()`, e o terminal irá parar naquele ponto, permitindo que você veja as variáveis e o estado do programa.

Para sair do modo de depuração do `breakpoint()`, basta digitar o comando `exit` ou pressionar `Ctrl+D` no terminal onde o depurador está ativo. Ou você pode digitar `c` para continuar a execução do programa.
