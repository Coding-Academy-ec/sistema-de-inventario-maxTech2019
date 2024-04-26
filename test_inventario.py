import unittest
import logica
import sqlite3

class TestInventario(unittest.TestCase):
    def setUp(self):
        self.conn = logica.conectar()
        cursor = self.conn.cursor()
        # Verificar si la tabla ya existe antes de crearla
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='productos'")
        if not cursor.fetchone():
            cursor.execute("CREATE TABLE productos (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, precio REAL NOT NULL, existencias INTEGER NOT NULL)")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()


    def test_actualizar_existencias(self):
        logica.agregar_producto("Producto1", 10.99, 100)
        logica.actualizar_existencias(1, 50)
        cursor = self.conn.cursor()
        cursor.execute("SELECT existencias FROM productos WHERE id = 1")
        existencias = cursor.fetchone()[0]
        self.assertEqual(existencias, 50)

if __name__ == '__main__':
    unittest.main()
