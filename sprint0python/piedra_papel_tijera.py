import random

menu = '''\nMenú
----
1. Piedra
2. Papel
3. Tijera'''

empate = '\tEmpate'
gy = '\tHas ganado' 
gm = '\tHa ganado la máquina'

cont = 0
cy = 0
cm = 0

while (cont<5):
    yo = 0
    maq = 0
    resultado = 0
    print(menu)
   
    #determinar la jugada de cada uno
    while (yo!='1') and (yo!='2') and (yo!='3'):
        yo = input('\nSelecciona tu jugada (1/2/3): ')
        if (yo!='1') and (yo!='2') and (yo!='3'):
            print('\tNúmero no válido')
    maq = random.randint(1,3)

    #determinar q pasa según la jugada
   
    if (yo=='1') and (maq==2):
        resultado = 3
        cont = cont + 1
    elif (yo=='1') and (maq==3):
        resultado = 1
        cont = cont + 1
    elif (yo=='2') and (maq==1):
        resultado = 1
        cont = cont + 1
    elif (yo=='2') and (maq==3):
        resultado = 3
        cont = cont + 1
    elif (yo=='3') and (maq==1):
        resultado = 3
        cont = cont + 1
    elif (yo=='3') and (maq==2):
        resultado = 1
        cont = cont + 1
    else:
        resultado = 2
    
    #asignarle un valor a cada uno de los números
    if (yo=='1'):
        yo = 'piedra'
    elif (yo=='2'):
        yo = 'papel'
    elif (yo=='3'):
        yo = 'tijera'

    if (maq==1):
        maq = 'piedra'
    elif (maq==2):
        maq = 'papel'
    elif (maq==3):
        maq = 'tijera'
  
    #imprimir cual es el resultado final
    print ("\nHas sacado ---------------> " + str(yo))
    print ("La máquina ha sacado -----> " + str(maq))
    
    if (resultado == 1):
        print (gy)
        cy = cy + 1
    elif (resultado == 2):
        print (empate)
    elif (resultado == 3):
        print (gm)
        cm = cm + 1

    print ('\nPartidas jugadas -----> ' + str(cont))        
    
#una vez hechas las 5 partidas dar el ganador del juego
print('\n\n\tRESULTADOS FINALES')
print('\t------------------')
if (cy > cm):
    print ("Has ganado con " + str(cy) + ' victorias')
    print ("La máquina ha perdido con " + str(cm) + ' victorias')
elif (cm > cy):
    print ("Ha ganado la máquina con " + str(cm) + ' victorias')
    print ("Has perdido con " + str(cy) + ' victorias')



