salario = float(input("¿Cuál es tu salario?: "))

# Calcular los aportes
salud = salario * 0.04
pension = salario * 0.04

# Mostrar resultados
print("El aporte que debe realizar para salud es de:", salud)
print("El aporte que debe realizar para la pensión es de:", pension)

# Calcular salario neto
salario_neto = salario - salud - pension
print("Su salario neto después de los aportes es de:", salario_neto)
