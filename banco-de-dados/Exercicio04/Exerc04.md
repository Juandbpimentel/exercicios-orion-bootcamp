# ⚙️ Exercício 4 — Não relacional (Consultas Avançadas)

## Objetivo:

Aprender a consultar (filtrar) dados com base em campos específicos, arrays e documentos
aninhados.

## Descrição:

Usando a coleção posts do Exercício 3, você vai adicionar dados mais complexos (comentários) e aprender a filtrar os posts com base nesses novos dados.

1. Atualizar (Update):
   - Use updateOne() para adicionar um campo comentarios em um dos seus posts.
   - comentarios deve ser um array de documentos.

2. Criar dois arquivos Compose:
   - docker-compose.dev.yml — monta volume local, expõe portas, usa Dockerfile de dev.
   - docker-compose.prod.yml — usa imagem final otimizada, sem montar volumes.

1. Testar ambos os ambientes:
   - Escreva uma consulta find() que retorne apenas posts com a tag "nosql" (consultando dentro de um array).
   - Escreva uma consulta find() que retorne apenas posts onde o autor seja um nome específico.
   - docker compose -f docker-compose.prod.yml up

Critérios de sucesso:
- Ambientes dev/prod funcionam de forma independente.
- O build final segue boas práticas (camadas otimizadas, .dockerignore, imagem leve).
- Estrutura organizada e reutilizável.