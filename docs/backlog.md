# Backlog do MVP

## Release 1 — Core

- [ ] **RF01 — Health check**
  - Critérios de aceite:
    - [ ] `GET /health` retorna `200 OK`.
    - [ ] A resposta contém `status: "ok"`.
    - [ ] A resposta contém `timestamp` em UTC e formato ISO 8601.

- [ ] **RF02 — Criar tarefa**
  - Critérios de aceite:
    - [ ] `POST /tasks` cria uma tarefa com UUID.
    - [ ] `title` é obrigatório e aceita entre 3 e 100 caracteres.
    - [ ] `description` é opcional.
    - [ ] `status` assume `false` quando não informado.
    - [ ] `created_at` é gerado em UTC.

- [ ] **RF03 — Listar tarefas**
  - Critérios de aceite:
    - [ ] `GET /tasks` retorna `200 OK`.
    - [ ] A resposta retorna uma lista de tarefas.

- [ ] **RF04 — Consultar tarefa por ID**
  - Critérios de aceite:
    - [ ] `GET /tasks/{task_id}` retorna a tarefa existente.
    - [ ] Retorna `404 Not Found` para UUID inexistente.

- [ ] **RF05 — Atualizar tarefa**
  - Critérios de aceite:
    - [ ] `PUT /tasks/{task_id}` atualiza título, descrição e status.
    - [ ] Retorna a tarefa atualizada.
    - [ ] Retorna `404 Not Found` para UUID inexistente.

- [ ] **RF06 — Remover tarefa**
  - Critérios de aceite:
    - [ ] `DELETE /tasks/{task_id}` remove uma tarefa existente.
    - [ ] Retorna `204 No Content`.
    - [ ] Retorna `404 Not Found` para UUID inexistente.

- [ ] **RT01 — Repositório em memória**
  - Critérios de aceite:
    - [ ] Operações de persistência ficam isoladas na camada `repositories`.
    - [ ] A camada de API não acessa a estrutura de dados diretamente.

## Release 2 — Qualidade

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

## Release 3 — Entrega final

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
