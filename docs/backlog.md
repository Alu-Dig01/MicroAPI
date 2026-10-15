# Backlog do MVP

## v0.1 — Estrutura inicial

- [x] **RT00 — Preparação do projeto**
  - Critérios de aceite:
    - [x] Repositório Git inicializado.
    - [x] Camadas `api`, `services`, `repositories` e `models` criadas.
    - [x] Modelos Pydantic iniciais e `.gitignore` configurados.

## v0.2 — API básica

- [x] **RF01 — Health check**
  - Critérios de aceite:
    - [x] `GET /health` retorna `200 OK`.
    - [x] A resposta contém `status: "ok"`.
    - [x] A resposta contém `timestamp` em UTC e formato ISO 8601.

- [x] **RF02 — Criar tarefa**
  - Critérios de aceite:
    - [x] `POST /tasks` cria uma tarefa com UUID.
    - [x] `title` é obrigatório e aceita entre 3 e 100 caracteres.
    - [x] `description` é opcional.
    - [x] `status` assume `false` quando não informado.
    - [x] `created_at` é gerado em UTC.

- [x] **RF03 — Listar tarefas**
  - Critérios de aceite:
    - [x] `GET /tasks` retorna `200 OK`.
    - [x] A resposta retorna uma lista de tarefas.

- [x] **RF04 — Consultar tarefa por ID**
  - Critérios de aceite:
    - [x] `GET /tasks/{task_id}` retorna a tarefa existente.
    - [x] Retorna `404 Not Found` para UUID inexistente.

- [x] **RF05 — Atualizar tarefa**
  - Critérios de aceite:
    - [x] `PUT /tasks/{task_id}` atualiza título, descrição e status.
    - [x] Retorna a tarefa atualizada.
    - [x] Retorna `404 Not Found` para UUID inexistente.

- [x] **RF06 — Remover tarefa**
  - Critérios de aceite:
    - [x] `DELETE /tasks/{task_id}` remove uma tarefa existente.
    - [x] Retorna `204 No Content`.
    - [x] Retorna `404 Not Found` para UUID inexistente.

- [x] **RT01 — Repositório em memória**
  - Critérios de aceite:
    - [x] Operações de persistência ficam isoladas na camada `repositories`.
    - [x] A camada de API não acessa a estrutura de dados diretamente.

## v0.3 — Persistência e qualidade

- [ ] **RT02 — Validação e tratamento de erros**
  - Critérios de aceite:
    - [ ] Dados inválidos retornam `422 Unprocessable Entity`.
    - [ ] Recursos inexistentes retornam `404 Not Found`.
    - [ ] Respostas de erro seguem formato JSON consistente.

- [ ] **RT03 — Testes automatizados**
  - Critérios de aceite:
    - [ ] Existe teste para `GET /health`.
    - [ ] Existem testes para criar, listar, consultar, atualizar e remover tarefas.
    - [ ] Existem testes para validação de título e recurso inexistente.
    - [ ] Todos os testes passam localmente.

- [ ] **RT04 — Tipagem e organização**
  - Critérios de aceite:
    - [ ] Funções públicas possuem tipagem estática.
    - [ ] Regras de negócio ficam na camada `services`.
    - [ ] Rotas ficam na camada `api`.
    - [ ] Modelos Pydantic ficam na camada `models`.

- [ ] **RT05 — Observabilidade básica**
  - Critérios de aceite:
    - [ ] A aplicação registra eventos de inicialização.
    - [ ] Erros inesperados são registrados em log.

## v1.0 — MVP publicado

- [ ] **RT06 — Documentação da API**
  - Critérios de aceite:
    - [ ] Documentação OpenAPI está disponível em `/docs`.
    - [ ] Rotas possuem resumo e descrição adequados.
    - [ ] README contém instruções atualizadas para execução local.

- [ ] **RT07 — Revisão de escopo**
  - Critérios de aceite:
    - [ ] Todos os itens planejados das releases anteriores estão concluídos.
    - [ ] Itens fora de escopo não foram incorporados sem aprovação.
    - [ ] O documento `docs/escopo-mvp.md` está atualizado.

- [ ] **RT08 — Publicação da versão MVP**
  - Critérios de aceite:
    - [ ] Código está versionado no repositório remoto.
    - [ ] Dependências estão registradas em `requirements.txt`.
    - [ ] A aplicação inicia com `python -m uvicorn app.main:app --reload`.
