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
