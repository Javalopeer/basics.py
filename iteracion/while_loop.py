


i = 1

while i <= 5:
    print(f'El contador es {i}')
    i += 1

print('\nIterar con un while\n')


names = ['Andres', 'Luna', 'Juan', 'Maria']
count = 1
while count < len(names):
    print(f'Posicion {count} : {names[count]}')
    count += 1


#DO WHILE NO EXISTE EN PYTHON PERO SE PUEDE EMULAR

print('\nPRINT DO WHILE\n')
i = 0
while True:
    print(i)
    i += 1
    if i > 10:
        break


print('\nPRINT DO WHILE EJEMPLO PRACTICO\n')
correct_number = 7
while True:
    attempt = int(input('Ingresa un numero: '))
    if attempt == correct_number:
        print('El numero es correcto')
        break
    else:
        print('El numero no es correcto')
