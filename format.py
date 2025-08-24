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
txt = f'Este producto es muy { 'Caro' if price > 50 else 'Barato'}'
print(txt)