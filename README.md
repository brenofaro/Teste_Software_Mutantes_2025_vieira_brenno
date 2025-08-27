

### Clonar repositorio da urllib3

```bash
git clone https://github.com/urllib3/urllib3.git
```

### Criar ambiente virtual

```bash
python -m venv .venv
```

### Ativar ambiente virtual

Linux:

```bash
source .venv/bin/activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Comandos pytest

```bash

# Executar todos os testes
pytest -vv 

# Executar testes com cobertura
pytest -vv --cov=com/automationpanda/example

# Executar testes com report
pytest -vv --cov=com/automationpanda/example --cov-report html

mutmut run
```