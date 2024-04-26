import unittest
import logica

class TestInventario(unittest.TestCase):
    def setUp(self):
        self.conn = logica.conectar()
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE productos (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, precio REAL NOT NULL, existencias INTEGER NOT NULL)")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_agregar_producto(self):
        logica.agregar_producto("Producto1", 10.99, 100)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        self.assertEqual(len(productos), 1)

    def test_actualizar_existencias(self):
        logica.agregar_producto("Producto1", 10.99, 100)
        logica.actualizar_existencias(1, 50)
        cursor = self.conn.cursor()
        cursor.execute("SELECT existencias FROM productos WHERE id = 1")
        existencias = cursor.fetchone()[0]
        self.assertEqual(existencias, 50)

    def test_registrar_venta(self):
        logica.agregar_producto("Producto1", 10.99, 100)
        logica.registrar_venta(1, 20)
        cursor = self.conn.cursor()
        cursor.execute("SELECT existencias FROM productos WHERE id = 1")
        existencias = cursor.fetchone()[0]
        self.assertEqual(existencias, 80)

    def test_generar_informe(self):
        logica.agregar_producto("Producto1", 10.99, 100)
        logica.agregar_producto("Producto2", 5.99, 50)
        informe = logica.generar_informe()
        self.assertEqual(len(informe), 2)

if __name__ == '__main__':
    unittest.main()
