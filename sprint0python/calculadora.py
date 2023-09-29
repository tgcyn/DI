from operaciones import suma, resta, mult, div

otro='s'

while (otro=='s'):
    num1 = float(input('\nPrimer número: '))
    num2 = float(input('Segundo número: '))
    opc = input('\tQue operación quieres realizar (+, -, *, /): ')
    
    if (opc == '+'):
        resultado = suma(num1, num2)
    elif (opc == '-'):
        resultado = resta(num1,num2)
    elif (opc == '*'):
        resultado = mult(num1,num2)
    elif (opc == '/'):
        resultado = div(num1,num2)

    print('\nResultado ----> ' + str(resultado))

    otro = input ('Desea realizar otra operación (s/n): ')

print('\n\tCerrando programa...')