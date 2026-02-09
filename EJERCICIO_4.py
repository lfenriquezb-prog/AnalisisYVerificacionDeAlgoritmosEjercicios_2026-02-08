# Sistema de inventario usando diccionarios

def agregar_producto(inventario):
    """Función para agregar un nuevo producto al inventario"""
    nombre = input("Ingrese el nombre del producto: ").strip()
    
    # Validar si el producto ya existe
    if nombre in inventario:
        print("Error: El producto ya existe en el inventario.")
        return
    
    try:
        # Validar precio
        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("Error: El precio debe ser mayor a cero.")
            return
        
        # Validar cantidad
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
            return
        
        # Agregar al inventario
        inventario[nombre] = {
            "precio": precio,
            "cantidad": cantidad
        }
        print(f"¡Producto '{nombre}' agregado exitosamente!")
    
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para precio y cantidad.")

def mostrar_inventario(inventario):
    """Función para mostrar todos los productos en el inventario"""
    if not inventario:
        print("\nEl inventario está vacío.")
        return
    
    print("\n===== INVENTARIO ACTUAL =====")
    for nombre, datos in inventario.items():
        print(f"Nombre: {nombre}")
        print(f"  Precio: ${datos['precio']:.2f}")
        print(f"  Cantidad: {datos['cantidad']}")
        print("-" * 30)

def actualizar_cantidad(inventario):
    """Función para actualizar la cantidad de un producto"""
    nombre = input("Ingrese el nombre del producto: ").strip()
    
    # Validar si el producto existe
    if nombre not in inventario:
        print("Error: El producto no existe en el inventario.")
        return
    
    try:
        # Validar nueva cantidad
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        if nueva_cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
            return
        
        # Actualizar cantidad
        inventario[nombre]["cantidad"] = nueva_cantidad
        print(f"¡Cantidad del producto '{nombre}' actualizada a {nueva_cantidad}!")
    
    except ValueError:
        print("Error: Ingrese un número válido para la cantidad.")

def main():
    """Función principal que maneja el menú del sistema"""
    inventario = {}  # Diccionario para almacenar los productos
    
    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Actualizar cantidad")
        print("4. Salir")
        print("=================================")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            actualizar_cantidad(inventario)
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema de inventario!")
            break
        else:
            print("Error: Opción no válida. Por favor seleccione 1, 2, 3 o 4.")

# Iniciar el programa
if __name__ == "__main__":
    main()