# Lista para almacenar los números ingresados
numeros = []

print("Ingrese números enteros. Escriba -1 para terminar.")

# Paso 1: Solicitar números al usuario hasta que ingrese -1
while True:
    try:
        entrada = input("Número: ")
        
        # Verificar si es -1 (terminar ingreso)
        if entrada == "-1":
            break
            
        # Convertir a entero
        numero = int(entrada)
        numeros.append(numero)
        
    except ValueError:
        print("Error: Ingrese un número entero válido (ej: 5, -3, 10).")

# Paso 2: Verificar si se ingresaron números
if not numeros:
    print("\nNo se ingresaron números. El programa terminará.")
else:
    # Paso 3: Calcular el número mayor
    numero_mayor = max(numeros)
    
    # Paso 4: Calcular el número menor
    numero_menor = min(numeros)
    
    # Paso 5: Calcular el promedio
    promedio = sum(numeros) / len(numeros)
    
    # Paso 6: Contar números pares e impares
    pares = 0
    impares = 0
    
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    # Paso 7: Mostrar resultados
    print("\n===== RESULTADOS =====")
    print(f"Número mayor: {numero_mayor}")
    print(f"Número menor: {numero_menor}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Cantidad de números pares: {pares}")
    print(f"Cantidad de números impares: {impares}")