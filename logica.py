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
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET existencias = ? WHERE id = ?", (nuevas_existencias, id_producto))
    conn.commit()
    conn.close()

def registrar_venta(id_producto, cantidad_vendida):
    # Función para registrar una venta y actualizar las existencias en la base de datos
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT existencias FROM productos WHERE id = ?", (id_producto,))
    existencias_actuales = cursor.fetchone()[0]
    nuevas_existencias = existencias_actuales - cantidad_vendida
    actualizar_existencias(id_producto, nuevas_existencias)
    conn.close()

def generar_informe():
    # Función para generar un informe de inventario
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos
