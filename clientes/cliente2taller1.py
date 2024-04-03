import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:8001')

def punto2(a):
    b = input('Ingrese su usuario: ')
    c = input('Ingrese su contraseña: ')

    x = (s.calculos(b, c, a))
    
    if x == True:
        print('\033c', end='')
        print ("Acceso concedido")
        lista = "lista.txt"
        lista_numerica = []

        while len(lista_numerica) < 15:
            
            elemento = input(f"Ingrese el elemento {len(lista_numerica) + 1} de la lista: ")

            if len(lista_numerica) < 15 and elemento.isdigit():
                lista_numerica.append(int(elemento))
                print("Elemento agregado exitosamente.")
            else:
                print("No se pudo agregar el elemento. La lista ya está llena o el elemento no es un número entero.")
        
        with open(lista, 'wb') as archivo:
            for elemento in lista_numerica:
                # Convertir el elemento en bytes y escribirlo en el archivo
                bytes_elemento = elemento.to_bytes(2, byteorder='big')  # Suponiendo que los elementos son números enteros de 16 bits
                archivo.write(bytes_elemento)
                            

        print('\033c', end='')
        print("Opciones de listas")
        print("1.invertir lista en el archivo")
        print("2.numero mas repetido en la lista del archivo")
        
        a =int(input('Ingrese la operacion que desea realizar: '))

        if a == 1:
            lista_invertida = []
            print ("Esta es la lista que se agrego al archivo: ",lista_numerica)

         
            archivo_invertido = s.invertir_lista_en_archivo(xmlrpc.client.Binary(open("lista.txt", "rb").read()))
            archivo_invertido = archivo_invertido.data

            for i in range(0, len(archivo_invertido), 2):  # Suponiendo que cada número entero ocupa 2 bytes
                numero_entero = int.from_bytes(archivo_invertido[i:i+2], byteorder='big')
                lista_invertida.append(numero_entero)
            
            print ("Esta es la lista invertida que devolvio el servido en un archivo : ",lista_invertida)
            input("Presione Enter para continuar...")
            print('\033c', end='')

        if a == 2:
            print ("Esta es la lista que se agrego al archivo: ",lista_numerica)

         
            archivo_mas_repetido = s.encontrar_mas_repetido(xmlrpc.client.Binary(open("lista.txt", "rb").read()))
            archivo_mas_repetido = archivo_mas_repetido.data
          
            numero_entero = int.from_bytes(archivo_mas_repetido[0:2], byteorder='big')

            
            print ("Esta es el numero que mas se repite en la lista que enviamos en el archivo : ",numero_entero)
            input("Presione Enter para continuar...")
            print('\033c', end='')

    else:
        print('\033c', end='')
        print("El usuario o contrasena no coinciden precione enter para continuar...")
