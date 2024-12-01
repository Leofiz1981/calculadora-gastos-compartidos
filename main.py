def calcular_gastos(gastos):
    # Validar que todos los valores sean numericos y no negativos
    for persona, gasto in gastos.items():
        if not isinstance(gasto, (int, float)):  # Asegura que el gasto sea un número
            raise ValueError(f"El gasto de {persona} no es un número válido.")
        if gasto < 0:  # Asegura que el gasto no sea negativo
            raise ValueError(f"El gasto de {persona} no puede ser negativo.")

    total_gasto = sum(gastos.values())
    por_persona = total_gasto / len(gastos) if len(gastos) > 0 else 0  # Protege contra división por cero
    deudas = {persona: por_persona - gasto for persona, gasto in gastos.items()}
    return deudas

def obtener_gastos_usuario():
    gastos = {}
    while True:
        persona = input("Ingrese el nombre de la persona (o 'fin' para terminar): ").strip()
        if persona.lower() == 'fin':
            break
        try:
            gasto = float(input(f"Ingrese el gasto de {persona}: "))
            if gasto < 0:
                print("El gasto no puede ser negativo. Intente nuevamente.")
            else:
                gastos[persona] = gasto
        except ValueError:
            print("Por favor, ingrese un número válido para el gasto.")
    return gastos

if __name__ == "__main__":
    gastos = obtener_gastos_usuario()
    
    if len(gastos) > 0:
        print("Deudas por persona:", calcular_gastos(gastos))
    else:
        print("No se ingresaron gastos.")
