# ⚙️ Exercício 3 — Não relacional (CRUD Básico)

## Objetivo:

Aprender a estrutura básica de um banco NoSQL (MongoDB) e entender o conceito de "Schema Flexível".

## Ferramenta Sugerida:
MongoDB Atlas (nuvem gratuita) ou MongoDB (via Docker).

## Descrição:

Crie uma coleção (equivalente a uma "tabela") para os posts de um blog. Você irá inserir documentos (equivalente a "linhas") com estruturas diferentes para provar a flexibilidade.
1. Criar uma coleção:
   - Nomeie a coleção como posts.
2. Inserir (Create):
   - Insira um documento com: titulo, autor e conteudo.
3. Testar Schema Flexível:
   - Insira um segundo documento com: titulo, autor, conteudo e um campo novo:
     - tags (um array de strings, ex: ["nosql", "flexivel"]).

4. Consultar (Read):
   - Use o comando find() para listar todos os documentos da coleção posts.

Critérios de sucesso:
- find() retorna os dois documentos.
- O segundo documento possui o campo tags e o primeiro não, provando que o banco aceitou estruturas diferentes na mesma coleção.