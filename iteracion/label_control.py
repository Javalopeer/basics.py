for number in range (10):
    if number == 5:
        #break -> se sale de la iteracion al cumplir
        #pass -> util como placeholder no hace nada basicamente
        continue
    print(number)

user = ['Gerardo', 'Alberto', 'Anonimo', 'Marco', 'Pedro', 'Juan']

for users in user:
    if users == 'Anonimo':
        print('/Aqui falla/Usuario restringido')
        continue
    print(f'Bienvenido, {users}')
