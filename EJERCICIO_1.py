while True:
    contrasena = input("Ingrese la contraseña: ")
    
    # Verificar longitud mínima de 8 caracteres
    if len(contrasena) < 8:
        print("Error: La contraseña debe tener al menos 8 caracteres.")
        continue
    
    # Verificar al menos una letra mayúscula
    tiene_mayuscula = False
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
            break
    
    if not tiene_mayuscula:
        print("Error: La contraseña debe contener al menos una letra mayúscula.")
        continue
    
    # Verificar al menos un número
    tiene_numero = False
    for caracter in contrasena:
        if caracter.isdigit():
            tiene_numero = True
            break
    
    if not tiene_numero:
        print("Error: La contraseña debe contener al menos un número.")
        continue
    
    # Si pasa todas las validaciones
    print("¡Contraseña válida!")
    break