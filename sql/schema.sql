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
            cut_name VARCHAR(15) NOT NULL,
            cut_price INT NOT NULL
		);

CREATE TABLE Venta(
			id INT PRIMARY KEY AUTO_INCREMENT,
            name_cli VARCHAR(15) NOT NULL,
            l_name_cli VARCHAR(15) NOT NULL,
            id_cut_type INT NOT NULL,
            id_user INT NOT NULL,
            date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(id_cut_type) REFERENCES Corte(id),
            FOREIGN KEY(id_user) REFERENCES Usuario(id)
        );
        
CREATE TABLE Producto(
			id INT PRIMARY KEY AUTO_INCREMENT,
            prod_name VARCHAR(15) NOT NULL,
            prod_price INT NOT NULL
		);

CREATE TABLE Coste(
			id INT PRIMARY KEY AUTO_INCREMENT,
            name_cost VARCHAR(15) NOT NULL,
            id_pro_type INT NOT NULL,
            id_user INT NOT NULL,
            date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(id_pro_type) REFERENCES Producto(id),
            FOREIGN KEY(id_user) REFERENCES Usuario(id)
        );