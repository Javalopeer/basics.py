
for i in range (5):
    print(i)

print('Decremento')
#DESPUES DEL 10 SERIA EL INCREMENTO O DECREMENTO
for numero in range(10,-1, -1):
    print(numero)

print('Incremento ')

for i in range (1, 11, 1):
    print(i)

print('Nuevo ')
for i in range (10, -1, -1):
    print(i)

print('- Lista Iterandola')
names = ['Jose', 'Alberto', 'Marin', '1000', '3.41241', '123j+2']
for name in names:
    print(name)
print('======================= ')
for name in names:
    for char in name:
        print(char)
print('=======================  ')
email = 'gerardo@gmail.com'
for email in email:
    print(email)



