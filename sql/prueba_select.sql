SELECT * from usuario;
SELECT * from producto;
SELECT * from corte;
SELECT * from coste;
SELECT * from venta;

-- Prueba de filtro por día 
SELECT * from venta WHERE date LIKE "%-06 %";
-- Prueba de filtro por mes
SELECT * from venta WHERE date LIKE "%-06-%";