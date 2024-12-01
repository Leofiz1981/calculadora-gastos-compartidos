def calcular_gastos(gastos):
    total_gasto = sum(gastos.values())
    por_persona = total_gasto / len(gastos)
    deudas = {persona: por_persona - gasto for persona, gasto in gastos.items()}
    return deudas

if __name__ == "__main__":
    gastos = {"Juan": 50, "Ana": 30, "Luis": 20}
    print("Deudas por persona:", calcular_gastos(gastos))