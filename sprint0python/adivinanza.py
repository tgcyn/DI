respuestas='''\nOpciones:
A) La policía
B) Batman
C) Hulk '''

print ('\nLa adivinanza es: Es el héroe de la comunidad y la cuida noche y día para conservar la seguridad.')
print (respuestas)
opc = input('\nTu respuesta: ')

while (opc != 'a') & (opc != 'b') & (opc != 'c'):
    print ('Respuesta no válida')
    opc = input('\nTu respuesta: ')

if (opc == 'a'):
    print ('\n\tRespuesta correcta')
else:
    print ('\n\tLa respuesta correcta era la A')