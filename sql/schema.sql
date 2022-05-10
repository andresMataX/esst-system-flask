SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS Usuario;
DROP TABLE IF EXISTS Corte;
DROP TABLE IF EXISTS Venta;
DROP TABLE IF EXISTS Coste;
DROP TABLE IF EXISTS Producto;
SET FOREIGN_KEY_CHECKS=1;
CREATE TABLE Usuario(
            id INT PRIMARY KEY AUTO_INCREMENT,
            user VARCHAR(50) UNIQUE NOT NULL,
            pass VARCHAR(255) NOT NULL
        );

CREATE TABLE Corte(
			id INT PRIMARY KEY AUTO_INCREMENT,
            cut_name VARCHAR(40) NOT NULL,
            cut_price INT NOT NULL
		);

CREATE TABLE Venta(
			id INT PRIMARY KEY AUTO_INCREMENT,
            name_cli VARCHAR(30) NOT NULL,
            l_name_cli VARCHAR(30) NOT NULL,
            id_cut_type INT NOT NULL,
            date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(id_cut_type) REFERENCES Corte(id)
        );
        
CREATE TABLE Producto(
			id INT PRIMARY KEY AUTO_INCREMENT,
            prod_name VARCHAR(40) NOT NULL,
            prod_price INT NOT NULL
		);

CREATE TABLE Coste(
			id INT PRIMARY KEY AUTO_INCREMENT,
            name_cost VARCHAR(40) NOT NULL,
            id_pro_type INT NOT NULL,
            date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(id_pro_type) REFERENCES Producto(id)
        );

CREATE TABLE Transaccion(
			id INT PRIMARY KEY AUTO_INCREMENT,
            tran_price INT,
            tran_type INT
		);

-- Datos necesarios por default
-- Tipo de producto
INSERT INTO Producto(prod_name, prod_price) VALUES ("Tinte", 48);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Gorros de procesamiento", 320);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Delantal", 230);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Sillón reclinable hidráulico", 3899);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Máquinas de corte", 365);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Tijeras", 314);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Gel", 25);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Talco", 56);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Capa", 89);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Plancha", 494);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Horquillas", 290);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Cepillos", 550);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Tazones", 101);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Secador de cabello", 330);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Plancha para rizado", 371);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Plancha para alisado", 494);
INSERT INTO Producto(prod_name, prod_price) VALUES ("Toallas para mano", 217);

-- Tipo de corte
INSERT INTO Corte(cut_name, cut_price) VALUES ("Caballero", 70);
INSERT INTO Corte(cut_name, cut_price) VALUES ("Infantil", 60);
INSERT INTO Corte(cut_name, cut_price) VALUES ("Dama", 90);
INSERT INTO Corte(cut_name, cut_price) VALUES ("Peinado", 700);
INSERT INTO Corte(cut_name, cut_price) VALUES ("Tinte", 500);
INSERT INTO Corte(cut_name, cut_price) VALUES ("Alaciado", 1000);
INSERT INTO Corte(cut_name, cut_price) VALUES ("Baño de color", 600);