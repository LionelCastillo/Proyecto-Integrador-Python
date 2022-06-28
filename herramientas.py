'''
Funciones de apoyo para el proyecto integrador, como son
generar los id de los clientes, reordenarlos cuando se 
eliminan los clientes. (funciones 'robadas' del ejercicio del ropero :D) '''

import csv

def generar_id():
    with open('clientes.csv', 'r') as csvfile:
        # Leer archivo CSV y almacenar los resultados en data
        data = list(csv.DictReader(csvfile))

    # Obtener ultima fila del CSV leído
    ultima_fila = data[-1]

    # Obtener el ID de la última fila
    ultimo_id = int(ultima_fila.get('id'))
    
    # Aumentar en 1 el ID encontrado, y retornarlo
    return ultimo_id + 1


def reordenar_ids():


    with open('clientes.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))

    for i in range(len(data)):
        # Asignar como id de una prenda, su índice en la lista + 1, para no asignarle a nadie el ID = 0
        data[i]['id'] = i + 1

    with open('clientes.csv', 'w') as csvfile:
        # Especificar cuales serán las columnas del CSV
        header = ['id', 'nombre', 'dni', 'telefono', 'dia', 'mes', 'hora']

        # Construir el objeto writer, que se encargará de escribir el csv
        writer = csv.DictWriter(csvfile, fieldnames = header)

        # Escribir los nombres de las columnas
        writer.writeheader()

        # Escribir las prendas
        writer.writerows(data)


def eliminar_de_lista(lista, elemento):
    '''
    Esta función se encarga de eliminar un elemento de una lista
    ¿Cómo funciona?
    
    1. La función busca el índice de dicho elemento usando él método .index(elemento)
        lista = ['a', 'e', 'i', 'o', 'u']
        indice_i = lista.index('i')
        print(indice_i)
        >>> 2

    2. La función utiliza el método .pop(indice) para eliminar un elemento de la lista
        lista = ['a', 'e', 'i', 'o', 'u']
        indice_i = lista.index('i')
        lista.pop(indice_i)
        print(lista)
        >>> ['a', 'e', 'o', 'u']
    '''
    lista.pop(lista.index(elemento))