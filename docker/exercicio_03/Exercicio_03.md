# ⚙️ Exercício 3 — Boas Práticas + Múltiplos Ambientes

## Objetivo:
Aplicar boas práticas de build e configuração de ambientes (dev/prod).

## Descrição:
Usando o projeto do exercício anterior, os campistas devem:
1. Criar dois Dockerfiles ou estágios no mesmo arquivo:
   - dev: com volume montado e live reload (ex: nodemon, flask --reload).
   - prod: build otimizado, sem volumes, com imagem final leve (ex: FROM node:alpine + npm ci --only=production).

2. Criar dois arquivos Compose:
   - docker-compose.dev.yml — monta volume local, expõe portas, usa Dockerfile de dev.
   - docker-compose.prod.yml — usa imagem final otimizada, sem montar volumes.

1. Testar ambos os ambientes:
    - docker compose -f docker-compose.dev.yml up
    - docker compose -f docker-compose.prod.yml up

## Critérios de sucesso:
- Ambientes dev/prod funcionam de forma independente.
- O build final segue boas práticas (camadas otimizadas, .dockerignore, imagem leve).
- Estrutura organizada e reutilizável.