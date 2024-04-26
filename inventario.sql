-- Crear la tabla 'productos' para almacenar la información de los productos
CREATE TABLE productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    existencias INTEGER NOT NULL
);
