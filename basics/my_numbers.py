from decimal import Decimal, getcontext
age = 30
big_int = 1234556568764213
decimal = 3.1415

print(age)
print(type(age))
print(big_int)
print(type(big_int))
print(decimal)
print(type(decimal))

number_complex = 2 + 3j
print(number_complex)
print(type(number_complex))

getcontext().prec = 10
num1 = Decimal('10.1233123124124146876798241234215451')
num2 = Decimal('2.1')

result = num1 * num2
print(type(result))
print(result)
