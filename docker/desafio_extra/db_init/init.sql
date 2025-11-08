CREATE TABLE IF NOT EXISTS comidas (
  id serial PRIMARY KEY,
  nome text NOT NULL,
  descricao text UNIQUE NOT NULL,
  created_at timestamptz DEFAULT now()
);

INSERT INTO comidas (nome, descricao)
VALUES ('Paçoca','Esse é um doce de amendoim'),
       ('Bolo de Cenoura','Esse é um bolo feito com cenouras'),
       ('Brigadeiro','Esse é um doce de chocolate')