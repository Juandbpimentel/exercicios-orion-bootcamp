SELECT 
    a.nome AS nome_aluno,
    c.nome AS nome_curso
FROM alunos a
INNER JOIN cursos c ON a.curso_id = c.id;

SELECT 
    a.nome AS nome_aluno,
    c.nome AS nome_curso
FROM alunos a
INNER JOIN cursos c ON a.curso_id = c.id
WHERE c.nome = 'Engenharia de Software';

UPDATE alunos a
SET curso_id = 5
FROM cursos c
WHERE a.nome = 'João Silva' AND c.nome = 'Redes de Computadores';

SELECT 
    c.nome AS nome_curso
FROM cursos c
LEFT JOIN alunos a ON c.id = a.curso_id
GROUP BY c.id, c.nome
HAVING COUNT(a.id) = 0;