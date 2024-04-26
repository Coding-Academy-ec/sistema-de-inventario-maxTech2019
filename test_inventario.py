import unittest
import sqlite3
import logica

class TestInventario(unittest.TestCase):

    # Método para configurar el entorno de pruebas
    def setUp(self):
        # Conectar a la base de datos de prueba
        self.conn = sqlite3.connect(':memory:')
        # Crear la tabla de productos
        self.conn.execute('''CREATE TABLE productos (
                            id INTEGER PRIMARY KEY,
                            nombre TEXT NOT NULL,
                            precio REAL NOT NULL,
                            existencias INTEGER NOT NULL
                            )''')
        self.conn.commit()

    # Método para limpiar el entorno de pruebas
    def tearDown(self):
        # Cerrar la conexión a la base de datos
        self.conn.close()

    # Prueba para agregar un producto
    def test_agregar_producto(self):
        logica.agregar_producto("Producto1", 10.99, 100)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        self.assertEqual(len(productos), 1)
        self.assertEqual(productos[0][1], "Producto1")
        self.assertEqual(productos[0][2], 10.99)
        self.assertEqual(productos[0][3], 100)

    # Prueba para actualizar existencias
    def test_actualizar_existencias(self):
        logica.agregar_producto("Producto1", 10.99, 100)
        logica.actualizar_existencias(1, 50)
        cursor = self.conn.cursor()
        cursor.execute("SELECT existencias FROM productos WHERE id = 1")
        existencias = cursor.fetchone()
        self.assertIsNotNone(existencias)
        self.assertEqual(existencias[0], 50)

    # Prueba para registrar una venta
    def test_registrar_venta(self):
        logica.agregar_producto("Producto1", 10.99, 100)
        logica.registrar_venta(1, 20)
        cursor = self.conn.cursor()
        cursor.execute("SELECT existencias FROM productos WHERE id = 1")
        existencias = cursor.fetchone()
        self.assertIsNotNone(existencias)
        self.assertEqual(existencias[0], 80)

    # Prueba para generar un informe
    def test_generar_informe(self):
        logica.agregar_producto("Producto1", 10.99, 100)
        logica.agregar_producto("Producto2", 5.99, 50)
        informe = logica.generar_informe()
        self.assertEqual(len(informe), 2)
        self.assertIn(("Producto1", 10.99, 100), informe)
        self.assertIn(("Producto2", 5.99, 50), informe)

if __name__ == '__main__':
    unittest.main()
