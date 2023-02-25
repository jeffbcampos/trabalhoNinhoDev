exercicios aula 6 codigos sql

CREATE TABLE Alunos (
  NroMatricula INT PRIMARY KEY,
  cpf VARCHAR(11),
  nome VARCHAR(100),
  endereco VARCHAR(200),
  telefone VARCHAR(20),
  ano_nascimento INT
);

CREATE TABLE disciplina (
    CodDisciplina INT PRIMARY KEY,
    nome VARCHAR(50),
    codigo_curso INT,
    FOREIGN KEY (codigo_curso) REFERENCES matricula(codigo_curso)
);

CREATE TABLE matricula (
    NroMatricula INT PRIMARY KEY,
    codigo_curso INT,
    semestre INT,
    ano INT,
    nota FLOAT,
    nrofaltas INT
);
