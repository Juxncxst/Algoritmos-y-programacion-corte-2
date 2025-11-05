# Programa: Cálculo de CDT

# Solicitar datos al usuario
cantidad = float(input("Ingrese la cantidad de dinero invertido: "))
periodo = float(input("Ingrese el periodo de tiempo en días: "))
porcentaje_intereses = float(input("Ingrese el porcentaje de interés (1-100): "))

# Calcular el valor de los intereses
valor_intereses = (cantidad * (porcentaje_intereses / 100) * periodo) / 360
print("El valor de los intereses ganados es de:", valor_intereses)

# Calcular los impuestos sobre los intereses (7%)
valor_total = valor_intereses * 0.07
print("Los impuestos sobre el interés son de:", valor_total)

# Calcular el valor neto
neto = cantidad + valor_intereses - valor_total
print("La cantidad neta es de:", neto)
