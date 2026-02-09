while True:
    # Lista para guardar las notas del estudiante actual
    notas = []
    contador = 1  # Contador para numerar las notas
    
    print("\nIngrese las notas del estudiante (escriba -1 para terminar):")
    
    # Paso 1: Ingresar notas hasta que se escriba -1
    while True:
        entrada = input(f"Nota {contador}: ")
        
        # Verificar si es -1 (terminar ingreso de notas)
        if entrada == "-1":
            break
        
        # Paso 2: Validar que sea un número
        try:
            nota = float(entrada)
        except ValueError:
            print("Error: Ingrese un número válido (ej: 3.5, 4).")
            continue
        
        # Paso 3: Validar que esté entre 0 y 5
        if 0 <= nota <= 5:
            notas.append(nota)
            contador += 1  # Incrementar el contador solo si la nota es válida
        else:
            print("Error: La nota debe estar entre 0 y 5.")
    
    # Paso 4: Mostrar las notas ingresadas y calcular el promedio
    if notas:  # Si hay al menos una nota válida
        print("\nNotas ingresadas:")
        for i, nota in enumerate(notas, 1):
            print(f"  Nota {i}: {nota}")
        
        promedio = sum(notas) / len(notas)
        print(f"\nPromedio del estudiante: {promedio:.2f}")
    else:
        print("\nNo se ingresaron notas válidas para este estudiante.")
    
    # Paso 5: Preguntar si quiere ingresar otro estudiante
    otro_estudiante = input("\n¿Desea ingresar otro estudiante? (s/n): ").strip().lower()
    if otro_estudiante != "s":
        print("\n¡Programa finalizado!")
        break