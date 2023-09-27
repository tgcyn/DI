error='No es posible realizar esta operación'
#suma
def suma(n1, n2):
    return n1+n2


#resta
def resta(n1, n2):
    if (n1 > n2):
        return n1-n2
    if (n2>n1):
        return n2-n1
    if (n1==n2):
        return n1-n2


#multiplicación
def mult(n1,n2):
    return n1+n2


#división
def div(n1,n2):
    if (n1==0) or (n2==0):
        return error
    return n1/n2