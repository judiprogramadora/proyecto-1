def n_ultimo(a,b):
    penultimo = a
    ultimo=b

def perfecto(a):
    suma=0 
    for i in range(1,a):
        if (a%i==0):
            suma=suma+i
        if (suma > a):
            break    
    if (suma == a):
        return True
    else:
        return False

def primo(a):
    esPrimo  = True and (a != 1)
    for i in range(2, a):
        if(a % i == 0):
            esPrimo = False
            break
       
    if(esPrimo):
        return(True)
    else:
        return(False)

def suma(a,b):
    return a + b 
def resta(a,b):
    return a-b

def imprimirmenu ():
    print(" menu:")
    print("1- SUMA\n2- RESTA \n3- COMPROBAR SI ES PRIMO ")
    print("4- COMPROBAR SI ES PERFECTO\n5- MOSTRAR LO ULTIMOS DOS NUMEROS INGRESADOS")
    print("6- SALIR ")


def menu():
    numero1=0
    numero2=0

    while(True):
        imprimirmenu()
        opcion= int(input( "Ingrese una opcion "))
        if (opcion==1):
            numero1= int(input("Ingrese el primer numero a sumar "))
            numero2= int(input("Ingrese el segundo numero a sumar "))
            print( "La suma es "+ str (suma(numero1,numero2)))
            n_ultimo(  numero1, numero2)
            
        elif (opcion==2):
            numero1= int(input("Ingrese el primer numero a restar "))
            numero2= int(input("Ingrese el segundo numero a restar " ))
            print( "La resta es " + str (resta(numero1, numero2)) ) 
            n_ultimo(  numero1, numero2)


        elif (opcion==3):
            numero1=int(input("Ingrese un numero para comprobar si en primo " ))
            if primo(numero1):
                print("El número " + str(numero1) + " es primo")
            else:
                print("El número " + str(numero1) + " no es primo")
            n_ultimo(  numero2, numero1)

        elif (opcion==4):
            numero1=int(input("Ingrese un numero para comprobar si es perfecto "))
            if perfecto(numero1):
                print("El número " + str(numero1) + " es perfecto")
            else:
                print("El número " + str(numero1) + " no es perfecto")
            n_ultimo(  numero2, numero1)

        elif (opcion==5):
            print ("Los últimos numeros ingresados fuero " +str(numero1)+ " " + str( numero2))
        elif (opcion==6):
            break

menu()
