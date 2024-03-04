#Operadores logicos
#and: Devuelve True si ambos operandos son True. por ej: a and b
#or: Devuelve True si alguno de los operandos es True. por ej: a and b
#not: Devuelve True si alguno de los operandos es False. por ej: not a

# a = True
# b = False

# resultado = a and b
# # print(resultado)

# resultado = a or b
# # print(resultado)

# resultado = not b
# print(resultado)

#<--------------------------------------------------------------->
#EJERCICIO OPERADOR AND
# valor = int(input("Escribir un valor: "))

# valorMinimo = 0
# valorMaximo = 10

# dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)

# if dentroRango:
#     print(f'El valor {valor} esta dentro del rango')
# else: 
#     print(f'El valor {valor} no esta dentro del rango')
    
#<--------------------------------------------------------------->

# EJERCICIO OPERADOR OR

# vacaciones = True
# diaDescanso = False

# if vacaciones or diaDescanso:
#     print("Puede asistir")
# else:
#     print("Tiene trabajo")

#<--------------------------------------------------------------->

#EJERCICIO OPERADOR NOT

vacaciones = False
diaDescanso = False

if not (vacaciones or diaDescanso):
    print("Tiene trabajo")
else:
    print("Puede asistir")

# <---------------------------------------------------------------------->
#Ejercicio preguntar edad
edad = int(input("Cual es tu edad? : "))

# veintes = edad >= 20 and edad < 30
# print(veintes)
# treintas = edad >= 30 and edad <= 55
# print(treintas)

# if veintes or treintas:
#     print("Dentro del rango de edad")
#     if veintes:
#         print("entre 20 y 30")
#     elif treintas:
#         print("entre 30 y 55")
# else: 
#     print("No esta dentro del rango, es muy joven o muy viejo")

#<---------------------------------------------------------------->
#La otra manera de hacerlo sin variables.

# if (edad >= 20 and edad < 30) or (edad >= 30 and edad <= 55):
#     print("Dentro del rango de edad")
# else: 
#     print("No esta dentro del rango, es muy joven o muy viejo")  


#<---------------------------------------------------------------->
#Simplificar la sintaxis AND
if (20 <= edad < 30) or (30 <= edad <= 55):
    print("Dentro del rango de edad")
else: 
    print("No esta dentro del rango, es muy joven o muy viejo")  
