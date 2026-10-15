# Micro API de Gestão de Tarefas

API RESTful para criação e gerenciamento de tarefas. O projeto está em fase inicial de desenvolvimento e será construído como um MVP com camadas bem definidas.

## Objetivo

Disponibilizar uma API simples para criar, consultar, atualizar e remover tarefas, aplicando validação de dados e separação de responsabilidades entre API, serviço, repositório e modelos.

## Stack

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn

## Estrutura inicial

```text
app/
├── api/           # Rotas HTTP
├── models/        # Modelos de entrada e saída
├── repositories/  # Persistência de dados
└── services/      # Regras de negócio
```

## Como rodar localmente

1. Clone o repositório e entre na pasta do projeto:

   ```powershell
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   cd SEU_REPOSITORIO
   ```

2. Crie e ative o ambiente virtual:

   ```powershell
   python -m venv .venv
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\.venv\Scripts\Activate.ps1
   ```

3. Instale as dependências iniciais:

   ```powershell
   python -m pip install fastapi "uvicorn[standard]"
   ```

4. Quando o ponto de entrada da API estiver disponível, inicie o servidor:

   ```powershell
   python -m uvicorn app.main:app --reload
   ```

5. Acesse a documentação interativa em `http://127.0.0.1:8000/docs`.

> No estado atual, o modelo `Task` e as camadas iniciais já existem, mas o arquivo `app/main.py` e as rotas ainda serão implementados.

## Roadmap de releases

### v0.1 — Estrutura inicial

- [x] Inicialização do repositório Git
- [x] Organização das camadas da aplicação
- [x] Modelo Pydantic para tarefas
- [x] Configuração inicial do `.gitignore`

### v0.2 — API básica

- [ ] Criar aplicação FastAPI e ponto de entrada
- [ ] Implementar rotas CRUD de tarefas
- [ ] Adicionar validação e tratamento básico de erros

### v0.3 — Persistência e qualidade

- [ ] Implementar repositório para persistência de tarefas
- [ ] Adicionar testes automatizados
- [ ] Documentar contratos e exemplos de uso

### v1.0 — MVP publicado

- [ ] Consolidar regras de negócio
- [ ] Configurar ambiente de produção
- [ ] Publicar a primeira versão estável
