import argparse
import logica

def agregar_producto(args):
    logica.agregar_producto(args.nombre, args.precio, args.existencias)
    print("Producto agregado con éxito.")

def actualizar_existencias(args):
    logica.actualizar_existencias(args.id, args.existencias)
    print("Existencias actualizadas.")

def registrar_venta(args):
    logica.registrar_venta(args.id, args.cantidad)
    print("Venta registrada.")

def generar_informe(args):
    productos = logica.generar_informe()
    print("Informe de inventario:")
    for producto in productos:
        print(producto)

def main():
    parser = argparse.ArgumentParser(description='Sistema de Gestión de Inventarios')
    subparsers = parser.add_subparsers(title='Acciones', dest='accion')

    # Comando para agregar un producto
    parser_agregar = subparsers.add_parser('agregar', help='Agregar un nuevo producto')
    parser_agregar.add_argument('nombre', type=str, help='Nombre del producto')
    parser_agregar.add_argument('precio', type=float, help='Precio del producto')
    parser_agregar.add_argument('existencias', type=int, help='Existencias iniciales del producto')
    parser_agregar.set_defaults(func=agregar_producto)

    # Comando para actualizar existencias
    parser_actualizar = subparsers.add_parser('actualizar', help='Actualizar existencias de un producto')
    parser_actualizar.add_argument('id', type=int, help='ID del producto a actualizar')
    parser_actualizar.add_argument('existencias', type=int, help='Nuevas existencias del producto')
    parser_actualizar.set_defaults(func=actualizar_existencias)

    # Comando para registrar una venta
    parser_venta = subparsers.add_parser('venta', help='Registrar una venta')
    parser_venta.add_argument('id', type=int, help='ID del producto vendido')
    parser_venta.add_argument('cantidad', type=int, help='Cantidad vendida del producto')
    parser_venta.set_defaults(func=registrar_venta)

    # Comando para generar un informe
    parser_informe = subparsers.add_parser('informe', help='Generar un informe de inventario')
    parser_informe.set_defaults(func=generar_informe)

    args = parser.parse_args()
    if 'func' in args:
        args.func(args)

if __name__ == '__main__':
    main()
