SELECT * from usuario;
SELECT * from producto;
SELECT * from corte;
SELECT * from coste;
SELECT * from venta;
SELECT * from transaccion;

-- Prueba de filtro por día 
SELECT * from venta WHERE date LIKE "%-10 %";
-- Prueba de filtro por mes
SELECT * from venta WHERE date LIKE "%-06-%";
-- Prueba de filtro por año
SELECT * from venta WHERE date LIKE "%5-%";

SELECT cut_price FROM Corte WHERE id = 1;

-- Obtención del último id registrado en una tabla
SELECT @@identity AS id FROM transaccion;
SELECT MAX(id) AS id FROM transaccion;