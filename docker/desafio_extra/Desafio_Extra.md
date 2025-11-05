# 🚀 Desafio Extra — Aplicação Completa com Docker Compose
## Objetivo
Desenvolver e orquestrar uma aplicação __completa__ utilizando __Dockerfile__ e __Docker Compose__,
aplicando boas práticas e estrutura profissional de containers.

## Descrição do Desafio
Você deve montar uma stack composta por __três serviços principais__:
1. __API (backend)__ – construída a partir de um `Dockerfile`
2. __Banco de dados__ – utilizando imagem oficial (`PostgreSQL` ou `MySQL`)
3. __Interface de administração__ – utilizando `Adminer` ou `pgAdmin`

A aplicação deve permitir que o usuário acesse a API e visualize/interaja com os dados do
banco via interface web.

## 📦 Requisitos Técnicos
1️⃣ API
- Deve ser construída via __Dockerfile customizado__.
- Deve se conectar ao banco de dados através do __hostname do serviço__ (`db`).
- Deve expor uma rota `/health` que retorne status da aplicação (ex: `{"status": "ok"}`).
- Variáveis de ambiente como `DB_HOST`, `DB_USER`, `DB_PASS`, `DB_NAME` devem ser
configuradas no Compose.
- Use uma imagem base leve (`node:alpine`, `python:3.11-alpine`, etc.).
- O código-fonte deve ser montado via volume em ambiente de desenvolvimento.

2️⃣ Banco de Dados
- Utilize imagem oficial (`postgres` ou `mysql`).
- Configure __volume nomeado__ para persistência.
- Configure variáveis de ambiente (usuário, senha e nome do banco).
- Adicione um __healthcheck__ no Compose para garantir que o banco está disponível antes da API iniciar.
Exemplo:
```yaml
healthcheck:
    test: ["CMD", "pg_isready", "-U", "postgres"]
    interval: 10s
    timeout: 5s
    retries: 5
```

3️⃣ Interface de Administração
- Utilize o `adminer` (para MySQL) ou `pgadmin` (para PostgreSQL).
- Configure o serviço para se conectar ao banco via hostname `db`.
- Exponha a porta (ex: `8080:80`).
```
project/
│
├── api/
│ ├── Dockerfile
│ ├── package.json
│ └── src/
│     └── index.js
│
├── docker-compose.yml
└── .env
```

## O que será avaliado
- Organização e estrutura do projeto
- Uso correto de variáveis de ambiente e `.env`
- Uso de volumes e networks nomeadas
- Configuração de dependências (`depends_on`, `healthcheck`)
- Imagem leve e Dockerfile otimizado
- Funcionamento geral da stack (`docker compose up -d`)