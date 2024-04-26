import sqlite3

def conectar():
    # Función para establecer conexión a la base de datos
    conn = sqlite3.connect('inventario.db')
    return conn

def agregar_producto(nombre, precio, existencias):
    # Función para agregar un nuevo producto a la base de datos
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio, existencias) VALUES (?, ?, ?)", (nombre, precio, existencias))
    conn.commit()
    conn.close()

def actualizar_existencias(id_producto, nuevas_existencias):
    # Función para actualizar las existencias de un producto en la base de datos
    conn = conectar()
    # Crear un cursor para ejecutar consultas
    cursor.execute("UPDATE productos SET existencias = ? WHERE id = ?", (nuevas_existencias, id_producto))
    # Confirmar los cambios
    conn.close()

def registrar_venta(id_producto, cantidad_vendida):
    # Función para registrar una venta y actualizar las existencias en la base de datos
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET existencias = existencias - ? WHERE id = ?", (cantidad_vendida, id_producto))
    conn.commit()
    conn.close()

def generar_informe():
    # Función para generar un informe de inventario
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos
