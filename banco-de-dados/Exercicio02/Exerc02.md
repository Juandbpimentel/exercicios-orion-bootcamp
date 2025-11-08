️# Exercício 2 — Banco relacional (JOINs e Filtros)

## Objetivo:

Aprender a consultar dados de múltiplas tabelas usando JOIN e a filtrar resultados com WHERE

## Descrição:

Usando o esquema e os dados do Exercício 1, você agora vai responder perguntas
complexas que exigem a combinação de dados das tabelas alunos e cursos.

1. Escrever um SELECT que:
   - Use INNER JOIN para mostrar o nome do aluno e o nome do curso que ele está fazendo, em uma única consulta.

2. Escrever um SELECT que:
   - Use WHERE e JOIN para mostrar apenas os alunos que estão no curso de,
por exemplo, "Desenvolvimento Web".

1. Executar um UPDATE que:
    - Altere o curso_id de um aluno específico (ex: "Mover Maria para o curso de Ciência de Dados").

## Critérios de sucesso:
- A consulta JOIN retorna os nomes corretos (ex: "João Silva", "Desenvolvimento Web").
- A consulta com WHERE filtra corretamente os alunos.
- O UPDATE é bem sucedido e um novo SELECT com JOIN reflete a mudança.

## Extras (avançado):
- Escreva um SELECT com LEFT JOIN e WHERE para descobrir quais cursos não
possuem nenhum aluno matriculado.