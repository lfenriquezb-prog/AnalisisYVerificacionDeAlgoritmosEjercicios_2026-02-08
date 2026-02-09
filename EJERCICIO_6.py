# Sistema de votación con candidatos predefinidos

# Diccionario con candidatos predefinidos (todos inician con 0 votos)
candidatos = {
    "Luis": 0,
    "Fernando": 0,
    "Veronica": 0,
    "Alejandra": 0
}

def registrar_voto(candidatos, nombre):
    """Registra un voto para un candidato existente"""
    # Verificar si el candidato existe
    if nombre in candidatos:
        candidatos[nombre] += 1
        print(f"¡Voto registrado para {nombre}!")
    else:
        print(f"Error: El candidato '{nombre}' no existe en la lista.")

def mostrar_resultados(candidatos):
    """Muestra los resultados finales de la votación"""
    print("\n===== RESULTADOS FINALES =====")
    
    # Mostrar votos por candidato
    for candidato, votos in candidatos.items():
        print(f"{candidato}: {votos} votos")
    
    # Determinar el ganador
    ganador = max(candidatos, key=candidatos.get)
    print(f"\n¡El ganador es: {ganador} con {candidatos[ganador]} votos!")

# Bucle principal para registrar votos
print("SISTEMA DE VOTACIÓN")
print("Candidatos disponibles: Luis, Fernando, Veronica, Alejandra")
print("Escriba 'fin' para terminar la votación.\n")

while True:
    entrada = input("Ingrese el nombre del candidato: ").strip()
    
    # Verificar si el usuario quiere terminar
    if entrada.lower() == "fin":
        break
    
    # Registrar el voto
    registrar_voto(candidatos, entrada)

# Mostrar resultados al finalizar
mostrar_resultados(candidatos)