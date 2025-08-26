name = 'Gerardo'
age = 22

text = f'Me llamo {name} y tengo {age} años.'
print(text)

# Usar mejor esta forma 'f' es mas legible y eficaz

a = 5
b = 3

print(f'La suma de {a} y {b} es {a + b}')

result = f'El precio es  {a * b}$'
print(result)

price = 50
txt = f'Este producto es muy { 'caro.' if price >= 50 else 'barato.'}'
print(txt)

fruit = 'Manzanas'
txt = f'Me encantan las { fruit.upper() }'
print(txt)

#PLANTILLA DE INTERPOLACION
price = 50
text = 'El precio es {price} $'
print(text.format(price=price))


#PARA USAR FLOAT, DEBEMOS COLOCAR LA CANTIDAD DE DECIMALES ANTES DEL 'f'
txt = 'Oferta por solo {price:.2f} $'
print(txt.format(price=60))