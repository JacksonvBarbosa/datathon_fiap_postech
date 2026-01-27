# MLOps Portfolio Skeleton

Estrutura mínima pensada para portfólio júnior, usando Poetry e preparada para CI/CD no GitHub Actions. Organize seus experimentos, dados, código de modelo, testes e automações em pastas claras para recrutadores.

## Como usar
- Instale Python via pyenv (ex.: `pyenv install 3.11.9`).
- Crie e ative o ambiente: `poetry env use $(pyenv which python)` e `poetry install`.
- Ajuste `pyproject.toml` com seu nome, email e dependências.
- Rode qualidade e testes: `poetry run ruff check .` e `poetry run pytest`.
- Crie notebooks de exploração em `notebooks/` e scripts reprodutíveis em `src/`.

## Docker (opcional)
- Build: `docker build -t mlops-portfolio .`
- Subir com compose (monta o código local): `docker compose up -d`
- Entrar no container: `docker compose exec mlops bash`
- Dentro do container, rode `poetry run ruff check .` ou `poetry run pytest`.
- Altere o comando/entrypoint no `docker-compose.yml` conforme o que quiser executar (ex.: API, treino, batch).

## Organização das pastas
- `configs/` — YAMLs ou TOMLs de configuração (ex.: paths, hiperparâmetros).
- `data/` — referência de camadas de dados (`raw/`, `processed/`, `features/`). Git-ignore protege dados locais.
- `notebooks/` — análises exploratórias rápidas; exporte resultados para `reports/` se quiser.
- `reports/` — gráficos, tabelas ou artefatos gerados por notebooks/pipelines.
- `scripts/` — CLIs utilitários (ex.: baixar dados, treinar, servir local).
- `src/mlops_portfolio/` — código versionado de produção/pipeline:
  - `data_ingestion/`, `data_processing/`, `features/`, `models/`, `evaluation/`, `pipelines/`, `serving/`, `utils/`.
- `tests/` — `unit/` e `integration/`; mantenha fixtures em `tests/conftest.py`.
- `.github/workflows/ci.yml` — pipeline de lint + testes com Poetry.

## Próximos passos sugeridos
- Definir dependências principais (por exemplo, `pandas`, `scikit-learn`, `mlflow`).
- Adicionar um pipeline simples em `src/mlops_portfolio/pipelines/` e um notebook demonstrando a mesma lógica em `notebooks/`.
- Subir para o GitHub e habilitar Secrets se precisar de credenciais (ex.: buckets ou registries).
- Documentar comandos úteis no `README` ou `Makefile` conforme evoluir.

