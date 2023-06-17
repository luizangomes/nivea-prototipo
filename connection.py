import psycopg2
conn = psycopg2.connect(database = "niveaprototipo", user = "niveaproject", host= 'localhost', password = "nivea", port = 5432)
cur = conn.cursor()
# Para inicilizar o banco de dados pela primeira vez rode os comentários abaixo:
# cur.execute("""CREATE TABLE aluno(
#             idAluno INT UNIQUE NOT NULL,
#             anoEscolar VARCHAR (45) NOT NULL,
#             turma VARCHAR (100) NOT NULL,
#             nomeCompleto VARCHAR (100) NOT NULL,
#             PRIMARY KEY(idAluno));
#             """)
# cur.execute("""CREATE TABLE rav(
#             idRav INT UNIQUE PRIMARY KEY,
#             dataDeCriacao TIMESTAMP NOT NULL,
#             bimestre INT NOT NULL,
#             idAluno INT UNIQUE NOT NULL,
#             CONSTRAINT fk_aluno FOREIGN KEY (idAluno) REFERENCES aluno(idAluno));
#             """)
# cur.execute("""CREATE TABLE pergunta(
#             idPergunta INT UNIQUE PRIMARY KEY NOT NULL, 
#             conteudoPergunta VARCHAR(100) NOT NULL)""")
# cur.execute("""CREATE TABLE resposta(
#             idResposta INT UNIQUE PRIMARY KEY NOT NULL,
#             conteudoResposta VARCHAR(100) NOT NULL)""")
# cur.execute("""CREATE TABLE textoGerado(
#             idTextoGerado INT UNIQUE PRIMARY KEY,
#             dataDeCriacao TIMESTAMP NOT NULL,
#             bimestre INT,
#             idPergunta INT UNIQUE NOT NULL,
#             idResposta INT UNIQUE NOT NULL,
#             idRav INT UNIQUE NOT NULL,
#             CONSTRAINT fk_pergunta FOREIGN KEY (idPergunta) REFERENCES pergunta(idPergunta),
#             CONSTRAINT fk_resposta FOREIGN KEY (idResposta) REFERENCES resposta(idResposta),
#             CONSTRAINT fk_rav FOREIGN KEY (idRav) REFERENCES rav(idRav));
#             """)
# conn.commit()
cur.close()
conn.close()