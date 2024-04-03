import xmlrpc.client
import cliente2taller1
s = xmlrpc.client.ServerProxy('http://localhost:8001')

a = 0
while a != 7 :
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. potencia")
    print("6. serie fibonacci")
    print("7. listas")
    print("8. salir")

    a =int(input('Ingrese la operacion que desea realizar: '))

    if a == 1 or a == 2 or a == 3 or a == 4 or a == 5 : 
        b =int(input('Ingrese el primer numero: '))
        c=int(input('Ingrese el segundo numero: '))
        print("El resultado la operacion es: " + str(s.calculos(b, c, a)))

    elif a == 6:
        b =int(input('Ingrese cuántos números de la serie Fibonacci desea generar: '))
        c=0
        print("El resultado la operacion es: " + str(s.calculos(b, c, a)))
    
    elif a == 7:
        cliente2taller1.punto2(a)


    elif a==8:
        input("Adios...")
        print('\033c', end='')
        break

    

    a = 0
    input("Presione Enter para continuar...")
    print('\033c', end='')

