import random

name = 'Andres '
question = 'Eres una maquina ?'
answer = ''
random_number = random.randint(1,9)



if random_number == 1:
  answer = 'Si, Definitivamente'
elif random_number == 2:
  answer = 'Definitivamente es Asi'
elif random_number == 3:
  answer = 'Sin Duda'
elif random_number == 4:
  answer = 'Respuesta confuza intenta otra vez'
elif random_number == 5:
  answer = 'Pregunta de nuevo más tarde.'
elif random_number == 6:
  answer = 'Mejor no decirte ahora.'
elif random_number == 8:
  answer = 'Mis fuentes dicen que no.'
elif random_number == 9:
  answer = 'Muy dudoso'
else:
  print(ERROR)

print(name + 'Pregunta: ' + question )
print("Magic 8-Ball's answer: " + answer)