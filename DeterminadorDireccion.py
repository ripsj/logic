
def esPar(num):
    if (num % 2) == 0:
        return True
    else:
        return False
    
T = int(input("How many matrices would you like to test?"))
arregloPares = []

for x in range(T):
    arregloPares.append(input("Enter 'N' and 'M' values for matrix number " + str(x+1) + ", spaced by a whitespace: "))
    
for i in range(len(arregloPares)):
    arregloSeparado = arregloPares[i].split()
    fila = int(arregloSeparado[0])
    columna = int(arregloSeparado[1])

    if fila == columna:
        if esPar(fila):
            print("L")
        else:
            print("R")
    elif fila < columna:
        if esPar(fila):
            print("L")
        else:
            print("R")
    elif fila > columna:
        if esPar(columna):
            print("U")
        else:
            print("D")


    

