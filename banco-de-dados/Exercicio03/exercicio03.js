db.createCollection("posts");

db.posts.insertOne({
    titulo: "Introdução ao NoSQL",
    conteudo: "NoSQL é um tipo de banco de dados que oferece um mecanismo de armazenamento e recuperação de dados que é diferente do modelo relacional tradicional.",
    autor: "Juan Pimentel"
});

db.posts.insertOne({
    titulo: "Vantagens do NoSQL",
    conteudo: "Os bancos de dados NoSQL são conhecidos por sua flexibilidade, escalabilidade e desempenho em grandes volumes de dados.",
    autor: "Ana Souza",
    tags: ["nosql", "flexivel"]
});

db.posts.find();