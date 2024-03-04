#Ejercicio datos de un libro
print("Dame los siguentes datos del libro que quieras: ")
nombre = input("Como se llama el libro?: ")
idLibro = int(input("Id del libro: "))
precio = float(input("Precio: "))
envio = input("El envio es gratis?(Si o No): ")

if envio == "Si":
    envio = True
    envio = "Si"
elif envio == "No":
    envio = False
    envio = "No"
else:
    envio = "valor incorrecto, escribir True o False"

print(f'''El nombre del libro es: {nombre}
      id: {idLibro} 
      el precio es: {precio} 
      El envio es gratis?: {envio}''')