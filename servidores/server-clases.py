# -*- coding: utf-8 -*-
"""
clase sistemas distribuidos

@author: Usuario UTP
"""
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.server

class funciones_rpc:

    def calculos(self, p, q, a):
        if a == 1:
           return(self.suma(p,q))
        elif a == 2:
           return(self.resta(p,q))
        elif a == 3:
           return(self.multi(p,q))
        elif a == 4:
           return(self.divi(p,q))
        elif a == 5:
           return(self.pote(p,q))
        elif a == 6:
           return(self.fibonacci(p))
        elif a == 7:
           return(self.verificar_credenciales(p, q))
        else:
            return "Operación no válida"

        

    def suma(self, p, q):
        return p+q
    def resta(self, p, q):
        return p-q

    def multi(self, p, q):
        return p*q
    
    def divi(self, p, q):
        return p/q
    
    def pote(self, p, q):
        return p**q
    
    def fibonacci(self,n):
        fibonacci_sequence = [0, 1]  # Inicializamos la secuencia con los dos primeros números
        
        for i in range(2, n):
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Calculamos el siguiente número
            fibonacci_sequence.append(next_number)  # Agregamos el siguiente número a la secuencia
        
        return fibonacci_sequence
    
    def verificar_credenciales(self, usuario, contrasena):
        if usuario == "user1" and contrasena == "123":
            return True
        else :
            return False

    def invertir_lista_en_archivo(self, archivo):
        lista = "lista_invertida.txt"
        lista_recibida = []
        archivo = archivo.data
        for i in range(0, len(archivo), 2):  # Suponiendo que cada número entero ocupa 2 bytes
            numero_entero = int.from_bytes(archivo[i:i+2], byteorder='big')
            lista_recibida.append(numero_entero)

        
        lista_invertida = list(reversed(lista_recibida))
        
        
        with open(lista, 'wb') as archivo:
            for elemento in lista_invertida:
                # Convertir el elemento en bytes y escribirlo en el archivo
                bytes_elemento = elemento.to_bytes(2, byteorder='big')  # Suponiendo que los elementos son números enteros de 16 bits
                archivo.write(bytes_elemento)

        return xmlrpc.client.Binary(open("lista_invertida.txt", "rb").read())

    def encontrar_mas_repetido(self, archivo):
        lista = "lista_invertida.txt"
        archivo = archivo.data

        # Suponiendo que cada número entero ocupa 2 bytes
        lista_numeros = [int.from_bytes(archivo[i:i+2], byteorder='big') for i in range(0, len(archivo), 2)]

        # Diccionario para contar la frecuencia de cada número
        conteo_numeros = {}
        for numero in lista_numeros:
            conteo_numeros[numero] = conteo_numeros.get(numero, 0) + 1

        # Encontrar el número que más se repite
        numero_mas_repetido = max(conteo_numeros, key=conteo_numeros.get)

        with open(lista, 'wb') as archivo:
            bytes_elemento = numero_mas_repetido.to_bytes(2, byteorder='big')  # Suponiendo que los elementos son números enteros de 16 bits
            archivo.write(bytes_elemento)

        return xmlrpc.client.Binary(open("lista_invertida.txt", "rb").read())

    


        
   

        

        
    

server = SimpleXMLRPCServer(("localhost", 8001), allow_none=True)
server.register_instance(funciones_rpc())
print("soy un servidor implementado con clases")
server.serve_forever()

