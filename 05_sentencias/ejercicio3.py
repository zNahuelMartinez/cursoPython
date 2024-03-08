edad = int(input("Que edad tenes?: "))
mensaje = None

if 0 <= edad < 10:
    mensaje = "Aguante jugar todo el dia"
elif 10  <= edad < 20:
     mensaje = "Y tenemos muchos cambios(Pelos en el culo)"
elif 20 <= edad < 30:
     mensaje = "Y Comienza la desgracia"
elif 30  <= edad < 50:
     mensaje = "Y sos un viejo verde"
elif 50  <= edad < 80:
     mensaje = "Ni idea, no creo llegar tan lejos"
else:
     mensaje = "Error, pone una edad valida"

print(f'Tu edad es: {edad}, {mensaje}')