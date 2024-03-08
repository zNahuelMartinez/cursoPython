# for i in range(5):
#     if i % 2 == 0: #Solo imprime los pares
#         print(f'valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')

#Python continue, al igual que Python break, inicialmente interrumpe el bucle,
#pero lo reanuda tan pronto como se produzca un nuevo valor. 
#De esta manera solo se salta una parte del bucle si se cumple una determinada condición.