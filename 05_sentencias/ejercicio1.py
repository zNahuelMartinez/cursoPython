#Numero a texto

numero = int(input("Poner un numero de 1 a 3: "))

numeroTexto = ""

if numero == 1:
    numeroTexto = "Numero uno"
elif numero == 2:
    numeroTexto = "Numero dos"
elif numero == 3:
    numeroTexto = "Numero tres"
else:
    numeroTexto = "Error, numero fuera de rango"

print(f'Numero puesto: {numero} : {numeroTexto}')