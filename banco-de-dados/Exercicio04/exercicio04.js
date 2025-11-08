use orion_db

db.posts.updateOne(
    {titulo: "Introdução ao NoSQL"},{
        $set:{
            comentarios:[
                {
                    usuario: "Carlos Silva",
                    mensagem: "Ótimo artigo! Muito esclarecedor.",
                    data: new Date()
                },
                {
                    usuario: "Maria Santos",
                    mensagem: "Adorei a explicação sobre NoSQL.",
                    data: new Date()
                }
            ]
        }
    }
)

db.posts.updateOne({
    titulo: "Vantagens do NoSQL"
},{
    $set:{
        comentarios:[
            {
                usuario: "Pedro Oliveira",
                mensagem: "Excelente visão sobre as vantagens do NoSQL.",
                data: new Date()
            }
        ]
    }
})

db.posts.find({tags:"nosql"});

db.posts.find({autor:"Juan Pimentel"});