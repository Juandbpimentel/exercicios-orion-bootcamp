# 🧱 Exercício 1 — Dockerfile + Compose: “Hello Container”
## Objetivo:
Aprender a criar uma imagem customizada a partir de um Dockerfile e orquestrar com o
docker-compose.

## Descrição:
Crie uma aplicação simples (ex: Node.js, Python ou PHP) que exiba “Hello from Docker!”.
Os campistas devem:
1. Criar um __Dockerfile__ que:
   - Use uma imagem base leve (ex: `node:alpine`, `python:3.11-alpine` ou `php:8.2-apache`).
   - Configure o `WORKDIR`.
   - Copie o código da aplicação.
   - Instale dependências.
   - Defina o comando de execução (`CMD`).
2. Criar um __docker-compose.yml__ que:
   - Faça o __build__ da imagem a partir do Dockerfile.
   - Exponha a porta (ex: `3000:3000`).
   - Monte um __volume local__ para permitir edição em tempo real (opcional).

## Critérios de sucesso:
- docker compose up sobe a aplicação corretamente.
- Acessar http://localhost:3000 retorna a mensagem.
- Estrutura segue boas práticas (.dockerignore, imagem leve, etc).