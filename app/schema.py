instructions = [
    # Validación de relaciones y llaves foráneas para eliminar tablas
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS Usuario;',
    'DROP TABLE IF EXISTS Corte;',
    'DROP TABLE IF EXISTS Venta;',
    'DROP TABLE IF EXISTS Coste;',
    'DROP TABLE IF EXISTS Producto;',
    'SET FOREIGN_KEY_CHECKS=1;',
]