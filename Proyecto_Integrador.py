'''
Ejercicio Integrador Python Inicial
Autor: Victor Lionel Castillo
Version: 1.0

Descripcion: programa que funciona como la agenda de un dentista en el que el usuario 
puede agregar, modificar y eliminar clientes de un archivo. Otras funciones son 
mostrar en pantalla los turnos de los clientes y su informacion personal, ademas de 
los servicios y sus precios guardados en un diccionario. En el programa se utilizan:
    - Variables
    - Condicionales
    - Bucles
    - Funciones
    - Manejo de diccionarios
    - Manejo de archivos CSV (Comma Separated Values)
'''

import csv
import herramientas


def menu_principal():
    # La funcion se encarga de mostrar en pantalla las funciones que el
    # usuario puede realizar en el programa, pide el numero para 
    # interactuar en el menu.
    print('\n')
    print('Bienvenido, ingrese un numero para interactuar en el menu')
    print('1:Agregar nuevo cliente')
    print('2:Modificar datos personles y/o turnos')
    print('3:Mostrar precios')
    print('4:Mostrar turnos')
    print('5:Mostrar informacion personal')
    print('6:Eliminar cliente')
    print('7:Salir')

    while True:
     try:
         numero = int(input("Ingrese una opcion del menu pricipal: "))
         seleccion_menu(numero)
         break
     except ValueError:
         print("No ha ingresado un numero entero, vuelva a intentar")


def seleccion_menu(numero):
    # Con el numero ingresado por el usuario, se ingresa  
    # de acuerdo a la condicion que cumple.

    if numero == 1:
        nuevo_cliente()
    elif numero == 2:
        modificar_datos_turno()
    elif numero == 3:
        precios()
    elif numero == 4:
        turnos()
    elif numero == 5:
        informacion_personal()
    elif numero == 6:
        eliminar_cliente()
    elif numero == 7:
        salir()    
    else:
        print('vuelva a intentar')

        print('\n')
        
        menu_principal() 


def nuevo_cliente():
    # Esta funcion permite al usuario ingresar un nuevo cliente,
    # para ello pide al usuario ingresar los datos del mismo 
    # para luego guardarlos en el archivo csv.
 
    id_cliente = herramientas.generar_id()
    nombre_cliente = str(input('ingrese el nombre: '))
    while True:
            try:
                dni_cliente = int(input('ingrese el dni: '))
                break
            except ValueError:
                print("No ha ingresado un numero, vuelva a intentar")
    while True:
            try:
                telefono_cliente = int(input('ingrese el telefono: '))
                break
            except ValueError:
                print("No ha ingresado un numero, vuelva a intentar")
    while True:
            try:
                dia_cliente = int(input('ingrese el dia del turno: '))
                break
            except ValueError:
                print("No ha ingresado un numero, vuelva a intentar")                        
    mes_cliente = str(input('ingrese el mes del turno: '))
    while True:
            try:
                hora_cliente = int(input('ingrese la hora del turno: '))
                break
            except ValueError:
                print("No ha ingresado un numero, vuelva a intentar")

    csvfile = open('clientes.csv', 'a') 
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    datos_nuevo_cliente ={
        'id' : id_cliente,
        'nombre' : nombre_cliente,
        'dni' : dni_cliente,
        'telefono' : telefono_cliente,
        'dia' : dia_cliente,
        'mes' : mes_cliente,
        'hora' : hora_cliente}    
    writer.writerow(datos_nuevo_cliente)   
    csvfile.close()

    print('\n')

    menu_principal()


def modificar_datos_turno():
    # La siguiente funcion se utiliza para modificar los datos
    # de un cliente. Primero se realiza un print para ubservar 
    # la posicion del cliente para poder ingresarla y asi 
    # modificar sus datos.

    with open('clientes.csv', 'r') as c:
        data = list(csv.DictReader(c)) 
        for r in data:
            print(r['id'], r['nombre'])

    while True:
     try:
         numero_cliente = int(input("Ingrese el numero del cliente a modificar: "))
         break
     except ValueError:
         print("No ha ingresado un numero entero, vuelva a intentar")

    with open('clientes.csv') as c:
        datos = list(csv.DictReader(c))

        orden_cliente = numero_cliente - 1

        print('nombre actual:', datos[orden_cliente]['nombre'])
        nombre_cliente = str(input('ingrese el nuevo nombre: '))
        while True:
            try:
                print('dni actual:', datos[orden_cliente]['dni'])
                dni_cliente = int(input('ingrese el nuevo dni: '))
                break
            except ValueError:
                print("No ha ingresado un numero, vuelva a intentar")
        while True:
            try:
                print('telefono actual:', datos[orden_cliente]['telefono'])
                telefono_cliente = int(input('ingrese el nuevo telefono: '))
                break
            except ValueError:
                print("No ha ingresado un numero, vuelva a intentar")
        while True:
            try:
                print('dia actual:', datos[orden_cliente]['dia'])
                dia_cliente = int(input('ingrese el dia del turno: '))
                break
            except ValueError:
                print("No ha ingresado un numero, vuelva a intentar")           
        print('mes actual:', datos[orden_cliente]['mes'])
        mes_cliente = str(input('ingrese el mes del turno: '))
        while True:
            try:
                print('hora actual:', datos[orden_cliente]['hora'])
                hora_cliente = int(input('ingrese la hora del turno: '))
                break
            except ValueError:
                print("No ha ingresado un numero, vuelva a intentar")  
        print('hora actual:', datos[orden_cliente]['hora'])
        hora_cliente = int(input('ingrese la hora del turno: '))
   
    csvfile = open('clientes.csv', 'r')
    clientes = list(csv.DictReader(csvfile))
    csvfile.close()


    csvfile = open('clientes.csv', 'w', newline='')
    header = ['id', 'nombre', 'dni', 'telefono', 'dia', 'mes', 'hora']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader() 
    clientes[orden_cliente]= {
        'id' : numero_cliente,
        'nombre' : nombre_cliente,
        'dni' : dni_cliente,
        'telefono' : telefono_cliente,
        'dia' : dia_cliente,
        'mes' : mes_cliente,
        'hora' : hora_cliente}
    writer.writerows(clientes)
    csvfile.close()

    print('\n')

    menu_principal()


def precios():
    # Esta funcion accede al diccionario donde se encuentran 
    # los servicios con sus precios y los muestra en pantalla.
    print('Los precios de los servicios son:')
    for k, v in precios_servicios.items():
        print(k, 'tiene un costo de ', v, 'pesos')

    print('\n')
    
    menu_principal()    


def turnos():
    # Esta funcion accede al archivo csv e imprime en 
    # pantalla el nombre del cliente y la fecha del turno.

    with open('clientes.csv', 'r') as c:
        horario = list(csv.DictReader(c))
        for c in horario:
            print(c['nombre'], c['dia'], 'de', c['mes'], c['hora'],'hs')

    print('\n')

    menu_principal()


def informacion_personal():
    # Esta funcion accede al archivo csv e imprime 
    # en pantalla los datos personales del cliente.

    with open('clientes.csv', 'r') as c:
        informacion = list(csv.DictReader(c))
        for c in informacion:
            print('id:',c['id'],c['nombre'], 'dni:',c['dni'], 'telefono:',c['telefono'])

    print('\n')
    
    menu_principal()


def eliminar_cliente():
    # Esta funcion pide al usuario ingresar al usuario el
    # nombre del cliente a eliminar, lo busca en la informacion 
    # del archivo y elimina la informacion del cliente si lo encuentra. 
    nombre_cliente = str(input('ingrese el nombre del cliente a eliminar: '))

    with open('clientes.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))

    encontrado = False
    for cliente in data:
        if nombre_cliente == cliente.get('nombre'):
            herramientas.eliminar_de_lista(data, cliente)
            encontrado = True
            break

    if encontrado == False:
        print('no se ha encontrado al cliente', nombre_cliente)
        return
    else:
        with open('clientes.csv', 'w', newline='') as csvfile:
            header = ['id', 'nombre', 'dni', 'telefono', 'dia', 'mes', 'hora']
            writer = csv.DictWriter(csvfile, fieldnames=header)

            writer.writeheader()
            writer.writerows(data)

    herramientas.reordenar_ids()        

    print('\n')

    menu_principal()


def salir():
    # Funcion para salir del programa.

    print('hasta luego')


if __name__ == '__main__':
    precios_servicios = {
    'cansulta': 500, 
    'limpieza': 1500, 
    'extraccion': 2000, 
    'implante': 3000, 
    'ortodoncia': 2500, 
    'cirugia': 4000}

    with open('clientes.csv', 'w',  newline='') as csvfile:
        fieldnames = ['id', 'nombre', 'dni', 'telefono', 'dia', 'mes', 'hora'] 
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'id': 1,
                        'nombre': 'lucas cano',
                        'dni': 33486297,
                        'telefono': 3794735197,
                        'dia': 15,
                        'mes': 'agosto',
                        'hora': 16})   
        writer.writerow({'id': 2,
                        'nombre': 'lucia rios',
                        'dni': 41259175,
                        'telefono': 3795726519,
                        'dia': 15,
                        'mes': 'agosto',
                        'hora': 18})
        writer.writerow({'id': 3,
                        'nombre': 'alejandra benitez',
                        'dni': 36820176,
                        'telefono': 3794721665,
                        'dia': 15,
                        'mes': 'agosto',
                        'hora': 19})
        writer.writerow({'id': 4,
                        'nombre': 'andres montiel',
                        'dni': 39387261,
                        'telefono': 3794821066,
                        'dia': 16,
                        'mes': 'agosto',
                        'hora': 18})                                

    print('Empieza el programa')

    menu_principal()                                      

                         
