#Sistema de calificaciones
nota = int(input("Que nota te sacaste? :"))
mensaje = None

if 9 <= nota < 10:
    mensaje = "Tu calificaciones A"
elif 8 <= nota < 9:
    mensaje = "Tu calificaciones B"
elif 7 <= nota < 8:
    mensaje = "Tu calificaciones C"
elif 6 <= nota < 7:
    mensaje = "Tu calificaciones D"
elif 0 <= nota < 6:
    mensaje = "Tu calificaciones F (TREMENDO PETE JAJAJA)"
else:
    mensaje = "Error"

if mensaje == "Error":
    print("poner tu calificacion de 1 a 10")
else:
    print(f'Te sacaste un {nota} y {mensaje}')
