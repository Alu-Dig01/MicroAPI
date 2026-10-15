# Micro API de Gestão de Tarefas

API RESTful para criação e gerenciamento de tarefas internas. O projeto implementa um MVP organizado em camadas, com persistência inicial em memória.

## Objetivo

Disponibilizar operações para criar, consultar, atualizar e remover tarefas, aplicando validação de dados e separação de responsabilidades entre API, serviço, repositório e modelos.

## Stack

- Python 3.12
- FastAPI
- Pydantic v2
- Uvicorn

## Estrutura do projeto

```text
app/
├── api/
│   └── task_routes.py          # Rotas HTTP de tarefas
├── models/
│   └── task.py                 # Contratos Pydantic
├── repositories/
│   └── task_repository.py      # Persistência em memória
├── services/
│   ├── priority_advisor.py     # Sugestão de prioridade
│   └── task_service.py         # Regras de negócio
└── main.py                     # Aplicação FastAPI e health check
```

## Funcionalidades implementadas

- `GET /health`: verifica a disponibilidade da aplicação.
- Modelos `TaskCreate`, `TaskUpdate` e `TaskOut` com validações Pydantic.
- `TaskRepository` em memória com operações de criação, consulta, atualização e remoção.
- `TaskService` para orquestrar regras de negócio e sugestões de prioridade.
- `PriorityAdvisor` com heurística local e integração opcional com LLM por `OPENAI_API_KEY`.
- Router CRUD de tarefas registrado em `app/api/task_routes.py`.
- Validação global e respostas JSON consistentes para erros `404`, `422` e `500`.

## Endpoints

- `GET /health`
- `POST /tasks`
- `GET /tasks`
- `GET /tasks/{task_id}`
- `PUT /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

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

3. Instale as dependências:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Inicie o servidor:

   ```powershell
   python -m uvicorn app.main:app --reload
   ```

5. Acesse:

   - Health check: `http://127.0.0.1:8000/health`
   - Documentação interativa: `http://127.0.0.1:8000/docs`

## Observações

- O repositório é em memória; os dados são perdidos quando a aplicação é reiniciada.
- Sem `OPENAI_API_KEY`, a sugestão de prioridade usa somente a heurística local e não gera custo de API.
- Para habilitar a integração opcional com LLM, instale o pacote `openai` e defina `OPENAI_API_KEY` no ambiente.

## Roadmap de releases

### v0.1 — Estrutura inicial

- [x] Inicialização do repositório Git
- [x] Organização das camadas da aplicação
- [x] Modelos Pydantic para tarefas
- [x] Configuração inicial do `.gitignore`

### v0.2 — API básica

- [x] Criar aplicação FastAPI e health check
- [x] Implementar repository e service de tarefas
- [x] Implementar router CRUD de tarefas
- [x] Registrar o router de tarefas na aplicação
- [x] Adicionar validação e tratamento global de erros

### v0.3 — Persistência e qualidade

- [ ] Substituir persistência em memória por armazenamento durável
- [ ] Adicionar testes automatizados
- [ ] Documentar contratos e exemplos de uso

### v1.0 — MVP publicado

- [ ] Consolidar regras de negócio
- [ ] Configurar ambiente de produção
- [ ] Publicar a primeira versão estável
