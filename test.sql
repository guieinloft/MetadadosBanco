create table Funcionario(
    idFunc int not null auto_increment,
    nome varchar(255) not null,
    cpf varchar(20) not null,
    nasc date null,
    salario decimal(8,2) null,
    primary key(idFunc)
);
