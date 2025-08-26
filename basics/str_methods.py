name = 'Gerardo'
course = 'Curso de Python'

name_upper = name.upper()

print(name_upper)
print(course.lower())

#capitalize
print('------ Capitalize')
words = 'curso de python'
print(words.capitalize()) #primera letra del str convertida a mayuscula
print(words.title()) #cada primera letra del conjunto de str convertida a mayuscula

words = '    Hola Gerardo.'
print(words.strip())
print(words.lstrip())
print(words.rstrip())
#quita espacios en blanco, como para dar formato

print('------------ REPLACE ')
text = 'Hola Java'
print(text.replace('Java', 'Python'))
print(text.replace('Hola', 'Lenguaje de programacion').replace('Java', ': Python'))


print('------------- DATALIST')
text = 'Java, Angular, JavaScript, C++'
data_list = text.split(',')
print(data_list)
print('LENGUAJE: ' + data_list[3])
print('LENGUAJE: ' + data_list[2])


data = ['Java', 'Angular', 'JavaScript', 'C++']
text = '\n'.join(data)
print(text)


text = 'Hola, Gerardo como estas'
print(text.find('Gerardo'))
print(text.index('como'))

print(text.startswith('Hola'))
print(text.endswith('estas'))


number = '1234'
decimal = '1234,45'
text = 'Python'
mix = 'Python3'


print(number.isnumeric())
print(decimal.isdecimal())
print(text.isalnum())
print(mix.isalpha())
print(mix.isalnum())


text = '       hola Gerardo, como estas... esta es una prueba del uso general de todo.'
text_clean = text.strip().capitalize()
print(text_clean)

new_text = text_clean.replace('estas', 'estas?')
print(new_text)
