
create table clientes(
	id INT PRIMARY KEY IDENTITY(1,1),
	id_usuario int not null,
	empresa varchar(255) NOT NULL,
)


create table clientes(
	id INT PRIMARY KEY IDENTITY(1,1),
	empresa varchar(255) NOT NULL,
	id_usuarios varchar(255) NOT NULL UNIQUE,
	password varchar(255) NOT NULL,
	
)

CREATE TABLE tomadores (
    id INT PRIMARY KEY IDENTITY(1,1),
    id_usuario INT,
    id_nota VARCHAR(36),
    cnpj_tomador VARCHAR(255),
    razao_tomador VARCHAR(255),
    insc_mun_tomador VARCHAR(255),
    endereco_tomador VARCHAR(255)
);



CREATE TABLE prestadores (
    id INT PRIMARY KEY IDENTITY(1,1),
    id_usuario INT,
    id_nota VARCHAR(36),
    cnpj_prestador VARCHAR(255),
    razao_prestador VARCHAR(255),
    insc_mun_prestador VARCHAR(255),
    endereco_prestador VARCHAR(255)
);


CREATE TABLE notas_fiscais (
    id INT PRIMARY KEY IDENTITY(1,1),
    id_usuario INT,
    id_nota VARCHAR(36),
    local_incidencia_imposto VARCHAR(255),
    descricao_atividades VARCHAR(MAX),
    porcentagem VARCHAR(255),
    servicos VARCHAR(255),
    deducoes VARCHAR(255),
    base_de_calculo VARCHAR(255),
    inss VARCHAR(255),
    iss_retido VARCHAR(255),
    endereco_obra VARCHAR(255),
    cno VARCHAR(255),
    codigo_servico VARCHAR(MAX),
    valor_total_deducoes VARCHAR(255),
    aliquota VARCHAR(255),
    valor_total_nota VARCHAR(255),
    valor_iss VARCHAR(255),
    ir VARCHAR(255)
);




