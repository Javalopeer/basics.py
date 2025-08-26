
number = 5

match number:
    case 1:
        print('Seleccionaste la opcion 1')
    case 2:
        print(f'Seleccionaste la opcion 2')
    case 3:
        print('Seleccionaste la opcion 3')
    case _: #Aqui seria el default digamos
        print('Opcion no valida')

def option(number):
    if number == 1:
        return 'Seleccionaste la opcion 1'
    elif number == 2:
        return 'Seleccionaste la opcion 2'
    elif number == 3:
        return 'Seleccionaste la opcion 3'
    else:
        print('Opcion no valida')

result = option(4)
print(result)

name = input('Ingresa el nombre: ')

match name:
    case 'Pepe' | 'Juan' | 'Maria':
        print(f'Hola {name}')
    case 'John' | 'Josefa':
        print(f'Hola padre: {name}')
    case 'Andres':
        print(f'Hola primo {name}')
    case _:
        print(f'El nombre no se conoce: {name}')
