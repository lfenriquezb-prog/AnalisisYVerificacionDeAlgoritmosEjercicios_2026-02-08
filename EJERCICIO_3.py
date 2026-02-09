# Saldo inicial del cajero
saldo = 500000.0

# Bucle principal del programa
while True:
    # Mostrar menú
    print("\n===== CAJERO AUTOMÁTICO =====")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    print("=============================")
    
    # Pedir al usuario que seleccione una opción
    opcion = input("Seleccione una opción (1-4): ")
    
    # Validar que la entrada sea un número
    if not opcion.isdigit():
        print("Error: Ingrese un número válido (1-4).")
        continue
    
    # Convertir a número
    opcion = int(opcion)
    
    # Procesar la opción seleccionada
    if opcion == 1:
        # Consultar saldo
        print(f"\nSu saldo actual es: ${saldo:,.2f}")
    
    elif opcion == 2:
        # Depositar dinero
        try:
            monto = float(input("Ingrese el monto a depositar: "))
            
            # Validar monto positivo
            if monto <= 0:
                print("Error: El monto debe ser mayor a cero.")
                continue
                
            # Actualizar saldo
            saldo += monto
            print(f"\nDepósito exitoso. Nuevo saldo: ${saldo:,.2f}")
            
        except ValueError:
            print("Error: Ingrese un número válido (ej: 1000.50).")
    
    elif opcion == 3:
        # Retirar dinero
        try:
            monto = float(input("Ingrese el monto a retirar: "))
            
            # Validar monto positivo
            if monto <= 0:
                print("Error: El monto debe ser mayor a cero.")
                continue
                
            # Validar suficiente saldo
            if monto > saldo:
                print(f"Error: Saldo insuficiente. Su saldo es: ${saldo:,.2f}")
                continue
                
            # Actualizar saldo
            saldo -= monto
            print(f"\nRetiro exitoso. Nuevo saldo: ${saldo:,.2f}")
            
        except ValueError:
            print("Error: Ingrese un número válido (ej: 1000.50).")
    
    elif opcion == 4:
        # Salir del programa
        print("\n¡Gracias por usar nuestro cajero automático!")
        print(f"Saldo final: ${saldo:,.2f}")
        break
    
    else:
        # Opción inválida
        print("Error: Opción no válida. Por favor seleccione 1, 2, 3 o 4.")