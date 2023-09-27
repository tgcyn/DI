punt=0
respuestas='''\nOpciones:
A) La policía
B) Batman
C) Hulk '''
respuestas2='''\nOpciones:
A) Judía
B) Guisante
C) Garbanzo'''
respuestas3='''\Opciones:
A) El aire
B) El tiempo 
C) El viento'''

#primera adivinanza
print ('\nPrimera adivinanza: Es el héroe de la comunidad y la cuida noche y día para conservar la seguridad.')
print (respuestas)
opc = input('\nTu respuesta: ')

while (opc != 'a') & (opc != 'b') & (opc != 'c'):
    print ('Respuesta no válida')
    opc = input('\nTu respuesta: ')

if (opc == 'a'):
    print ('\n\tRespuesta correcta\tPuntuación +10')
    punt = punt + 10 
else:
    print ('\n\tLa respuesta correcta era la A\t\tPuntuación -5')
    punt = punt-5


#segunda adivinanza
print ('\n\nSegunda adivinanza: Dentro de una vaina estoy y ni espada ni sable soy. ¿Qué soy?')
print (respuestas2)
opc = input('\nTu respuesta: ')

while (opc != 'a') & (opc != 'b') & (opc != 'c'):
    print ('Respuesta no válida')
    opc = input('\nTu respuesta: ')

if (opc == 'b'):
    print ('\n\tRespuesta correcta\tPuntuación +10')
    punt = punt + 10 
else:
    print ('\n\tLa respuesta correcta era la B\t\tPuntuación -5')
    punt = punt-5


#tercera adivinanza
print ('\n\nTercera adivinanza: ¿Qué cosa es? ¿Qué cosa es? Que corre mucho y no tiene pies.')
print (respuestas3)
opc = input('\nTu respuesta: ')

while (opc != 'a') & (opc != 'b') & (opc != 'c'):
    print ('Respuesta no válida')
    opc = input('\nTu respuesta: ')

if (opc == 'c'):
    print ('\n\tRespuesta correcta\tPuntuación +10')
    punt = punt + 10 
else:
    print ('\n\tLa respuesta correcta era la C\t\tPuntuación -5')
    punt = punt-5


#puntuación final
total = str(punt)
print('\n\n\tPuntuación total -------------> '+ total)