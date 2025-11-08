CREATE TABLE IF NOT EXISTS cursos (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL 
);

CREATE TABLE IF NOT EXISTS alunos(
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL,
	curso_id INT,
	FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

INSERT INTO cursos(nome) VALUES
	('Engenharia de Software'),
	('Sistemas de Informação'),
	('Design Digital'),
	('Ciências da Computação'),
    ('Redes de Computadores');
	
INSERT INTO alunos(nome, email, curso_id) VALUES
	('João Silva', 'joao.silva@email.com', 1),
    ('Maria Santos', 'maria.santos@email.com', 2),
    ('Pedro Oliveira', 'pedro.oliveira@email.com', 1),
    ('Ana Costa', 'ana.costa@email.com', 4),
	('Carlos Mendes', 'carlos.mendes@email.com', 1),
    ('Juliana Lima', 'juliana.lima@email.com', 2),
    ('Roberto Ferreira', 'roberto.ferreira@email.com', 1),
    ('Fernanda Alves', 'fernanda.alves@email.com', 4),
    ('Lucas Rodrigues', 'lucas.rodrigues@email.com', 1),
    ('Beatriz Souza', 'beatriz.souza@email.com', 2),
    ('Rafael Costa', 'rafael.costa@email.com', 1),
    ('Camila Martins', 'camila.martins@email.com', 1);

-- Consultar todos os alunos
SELECT * FROM alunos;

-- Consultar alunos com seus cursos
SELECT 
    a.id,
    a.nome,
    a.email,
    c.nome as nome_curso
FROM alunos a
INNER JOIN cursos c ON a.curso_id = c.id;

