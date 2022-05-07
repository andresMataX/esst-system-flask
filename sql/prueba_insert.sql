-- -------------- Necesarias
-- Usuario
INSERT INTO Usuario(user, pass) VALUES ("andre", "qwe");
-- Corte
INSERT INTO Corte(cut_name, cut_price) VALUES ("Caballero", 60);
-- Producto
INSERT INTO Producto(prod_name, prod_price) VALUES ("Tinte", 50);
-- Reinicio de IDs
ALTER TABLE producto AUTO_INCREMENT = 1;

-------------- Pruebas
-- Venta
INSERT INTO Venta(name_cli, l_name_cli, id_cut_type, id_user) VALUES ("Jesús", "Mata", 1, 1);
-- prueba para filtro
INSERT INTO Venta(name_cli, l_name_cli, id_cut_type, id_user, date) VALUES ("Jesús", "Mata", 1, 1, "2022-06-06 15:43:29");

-- Coste
INSERT INTO Coste(name_cost, id_pro_type, id_user) VALUES ("Tinte Azul", 1, 1);

-- Tipo de corte
INSERT INTO Corte(cut_name, cut_price) VALUES ("Tinte Azul", 1);