CREATE DATABASE negocio;

USE negocio;

-- TABELA EMPRESA
CREATE TABLE empresa
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    saldo DECIMAL(10,2) NOT NULL
);

-- TABELA PRODUTOS
CREATE TABLE produtos
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL
);

-- =========================
-- TABELA VENDAS
-- =========================
CREATE TABLE vendas
(
    id INT PRIMARY KEY AUTO_INCREMENT,

    produto_id INT NOT NULL,

    quantidade INT NOT NULL,

    valor_total DECIMAL(10,2) NOT NULL,

    data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (produto_id)
        REFERENCES produtos(id)
);

-- =========================
-- INSERINDO EMPRESA
-- =========================
INSERT INTO empresa(saldo)
VALUES(10000);

-- =========================
-- INSERINDO PRODUTOS
-- =========================
INSERT INTO produtos(nome, preco, estoque)
VALUES
('Machine1', 7400, 5),
('Machine2', 5000, 10),
('Machine3', 9000, 2),
('Headset', 500, 15),
('Mouse', 150, 20);


CREATE USER 'victor'@'localhost'
IDENTIFIED BY '1234';