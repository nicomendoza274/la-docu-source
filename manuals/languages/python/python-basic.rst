=============
Python Básico
=============

.. image:: ../../../_static/img/languages/python/logo.png
    :width: 400px
    :alt: Logo
    :align: center
    
.. |date| date::
.. |time| date:: %H:%M

Última edición el día |date| a las |time|.

.. contents:: Table de contenidos de la pagina
   :depth: 2
   :local:

Porque Aprender python?
#######################

En que Areas Puedo encontrar python
***********************************

* Frontend
* ``IOT``
* ``Inteligencia Artificial``
* ``Backend``
* DevOps
* ``Data Science``
* Videojuegos
* Desarrollo móvil

Empresas que utilizan python
****************************

* Google 
* Instagram
* Spotify
* Netflix
* Uber
* Pinterest

Ventajas 
*********

* Buenas Practicas: Identación
* Fácil: Muy fácil de aprender
* Elegante: Estructura definida

Editores de códigos e IDES - Consolas
######################################

* ``VSCODE``
* PyCharm

Consola
*******

* CMD
* Power Shell
* Cmder o gitbash

Instalación de Python
#####################

.. image:: ../../../_static/img/languages/python/win_installer.png
    :width: 800px
    :alt: Installer
    :align: center


Version de python 
******************

Entramos a nuestra consola y ejecutamos:

.. code-block:: console

    python --version 

Para salir de python ejecutamos:

.. code-block:: python

   >>> exit()

Operadores aritméticos
#######################

.. code-block:: python

    >>> 5 + 5
    >>> print(5+5)
    >>> 5 - 5
    >>> 2 * 5
    >>> 4 / 2
    >>> 4 // 2 #div entera
    >>> 4 % 2 #Modulo
    >>> 2 ** 2 #Potencia 2^2
    >>> import math
    >>> math.sqrt(9) # raiz cuadrada

Variables
#########

<identificador> = <valor> 

.. code-block:: python

    >>> numero1 = 5 #asignación
    >>> numero2 = 6 
    >>> numero1 + numero2 #11
    >>> numero1 - numero2 #-1
    >>> result = numero1 + numero2
    >>> result #11

.. note::
    El identificador de una variable no puede comenzar con un numero y debe estar en minúsculas. Las palabras dentro del mismo se separan con guion bajo (Snake_Case por Buenas practicas)

Tipos primitivos
################

* Números enteros
* Números de punto flotante (decimales)
* Texto (cadenas de caracteres o strings)
* Booleanos (verdadero o falso)

.. code-block:: python

    >>> nombre = "Nico"
    >>> nombre #'Nico'
    >>> nombre2 = "Mendoza"
    >>> nombre+nombre2 #'NicoMendoza'
    >>> nombre * 4 #'NicoNicoNicoNico'
    >>> nombre + ", " nombre2 #'Nico, Mendoza'
    >>> numero_decimal = 3.4 #no usar coma , para los decimales
    >>> es_programador = True
    >>> es_ingeniero = False

Convertir datos a otros tipos
#############################

.. code-block:: python

   >>> numero1 = input("Escribir un numero: ") #Escribir un numero: 4
   >>> numero1 #'4'
   >>> numero2 = input("Escribir un numero: ") #Escribir un numero: 5
   >>> numero2 #'5'
   >>> numero1 + numero2 #'45'
   >>> numero1 = int(numero1) 
   >>> numero1 #4
   >>> numero2 = int(numero2) 
   >>> numero2 #5
   >>> numero_decimal = 4.5
   >>> int(numero_decimal) #4 (quita la parte entera)
   >>> str(numero_decimal) #'4.5' (convierte a string)


Operadores lógicos y de comparación
#####################################

.. code-block:: python

    #Lógicos
    >>> es_estudiante = True
    >>> es_estudiante #True
    >>> trabaja = False
    >>> trabaja #False
    >>> es_estudiante and trabaja #False
    >>> es_estudiante or trabaja #True
    >>> not es_estudiante #False
    >>> not trabaja #True

    #comparación
    >>> numero1 = 5
    >>> numero2 = 5
    >>> numero3 = 7
    >>> numero1 #5
    >>> numero2 #5
    >>> numero1 == numero2 #True
    >>> numero1 != numero2 #False
    >>> numero1 > numero2 #False (se puede incluir el igual)
    >>> numero1 < numero3 #True (se puede incluir el igual)


Condicionales
#############

.. code-block:: python

    edad = int(input("Ingrese su edad: "))
    if edad > 17:
        print('Mayor de edad') #podemos poner pass cuando no sabemos que va en este bloque
    else:
        print('No es mayor de edad')

    numero = int(input("Escribe un numero: "))
    if numero > 5:
        print('Es mayor a 5')
    elif numero == 5:
        print('Es menor a 5')
    else:
        print('Es menor a 5')

Funciones
#########

.. code-block:: python

    def nombre_funcion(<parametros>):
        print("Mensaje")
        print("Bloque de código")

    nombre_funcion(<parametros>)

.. note::
    * Las funciones deben ser definidas antes de ser invocadas para funcionar.
    * return devuelve el valor de la variable que esta a continuación.


Métodos con strings
####################

.. code-block:: python

   >>> nombre = input("Ingresar nombre: ") #Ingresar nombre: nicolás
   >>> nombre.upper() #NICOLÁS
   >>> nombre.capitalize() #Nicolás
   >>> nombre = nombre.strip() #Quita los espacios adelante y atrás
   >>> nombre.lower() #nicolás (todo minusculas)
   >>> nombre = nombre.replace('o','a') #nicalás 
   >>> nombre[0] #n (puedo acceder a los caracteres)
   >>> len(nombre) #7

Slices
######

.. code-block:: python

   >>> nombre = "Nicolás"
   >>> nombre[0:3] #'Nic' (hasta antes del indice 3)
   >>> nombre[:3] #'Nic' (hasta antes del indice 3)
   >>> nombre[3:] #'olás' (parto del indice 3)
   >>> nombre[0:6:2] #'Ncl' (Del 0 al 6 en 2 pasos)
   >>> nombre[::] #'Nicolás'
   >>> nombre[::-1] #'sálociN' (pasos inversos)


Buenas practicas
################

Crear una función principal. corre el programa al principio (run o main)

.. code-block:: python

    def run():
        pass
    
También tenemos el entry point de un programa en python 

.. code-block:: python

    if __name__ == '__main__':
        run()

También es un buena practica dejar 2 espacios vacíos entre las funciones y el entry point 


Bucles
######

While
*****

Potencias de 2 hasta 1 millón

.. code-block:: python

    LIMITE = 1000000
    contador = 0
    portencia_2 = 2**contador
    while(portencia_2 <= LIMITE):
        print('2 elevado a ' + str(contador) +' es: ' + str(portencia_2))
        contador+=1
        portencia_2 = 2**contador
    

For
*****

Listado de números hasta 1000

.. code-block:: python

    LIMITE = 1000
    for contador in range(1,LIMITE+1):
        print(contador)


Imprimir las letras de un string

.. code-block:: python

    nombre = input("Escribe tu nombre: ")
    for letra in nombre:
        print(letra)


Break y Continue
################

Interrumpir ciclos

Continue
********

.. code-block:: python

    for contador in range(1000):
        if contador % 2 != 0:
            continue #Ejecuta hasta aquí y sigue con el ciclo
        print(contador)

Break
*****

.. code-block:: python

    for i in range(0, 10000):
        print(i)
        if i == 5678:
            break #Corta el ciclo y no se sigue ejecutando


Módulos
########

Paquete de código escrito en python

.. code-block:: python

   import random #Trae funciones para trabajar con números aleatorios

Todas las importaciones van al principio del programa


Listas
######

Es una estructura de datos que nos permite guardar varios valores de diferentes tipos (permite tipos distintos)
Las listas son dinámicas

.. code-block:: python

    >>> lista = [1, 3, 6 ,8, 9 ,45, 90]
    >>> objetos = ['Hola', 3, 4.5, True]
    >>> objetos[1] #3 Si me salgo del indice me da un error 
    >>> objetos.append(1) #['Hola', 3, 4.5, True, 1] (Agrego al final de la lista)
    >>> objetos.pop() #['Hola', 3, 4.5, True] (Quito el ultimo elemento)
    >>> objetos.pop(2) #['Hola', 3, True] (Quito el segundo elemento)

    # Recorrer una lista 

    for elemento in objetos:
        print(elemento)

    >>> objetos[::-1] #[True, 3, 'Hola'] (invierto la lista)

    # sumar listas

    >>> numeros1 = [1, 2, 3]
    >>> numeros2 = [4, 5, 6]
    >>> lista_final = numero1 + numero2
    >>> lista_final # [1, 2, 3, 4, 5, 6]
    >>> numeros1 * 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]


Tuplas
######

Parecido a las listas. Pero son inmutables (Estáticos). No permite hacer append.
Recorrido mas rápido con tuplas que con listas

.. code-block:: python

    >>> mi_tupla = (1, 2, 3, 4, 5)
    >>> mi_tupla #(1, 2, 3, 4, 5)

    for elemento in mi_tupla:
        print(elemento)


Diccionarios
############

Estructuras de datos de llaves y valores, no accedemos por indices, si no por llaves (nombres) y los valores

.. code-block:: python

    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    print(mi_diccionario) #{'llave1': 1, 'llave2': 2, 'llave3': 3}
    print(mi_diccionario['llave1']) #1
    print(mi_diccionario['llave2']) #2
    print(mi_diccionario['llave3']) #3
    


Operaciones en diccionarios
***************************

.. code-block:: python

    poblacion_paises = {
        'Argentina': 44_938_712,
        'Brasil': 210_147_125,
        'Colombia': 50_372_424
    }

* **.keys():** Retorna la clave de nuestro elemento.

.. code-block:: python

    for pais in poblacion_paises.keys():
        print(pais) #Argentina #Brasil #Colombia

* **.values():** Retorna una lista de elementos (valores del diccionario).

.. code-block:: python

    for pais in poblacion_paises.values():
        print(pais) #44_938_712 #210_147_125 #50_372_424

* **.items():** Devuelve lista de tuplas (primero la clave y luego el valor).

.. code-block:: python

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')
        # Argentina tiene 44938712 habitantes
        # Brasil tiene 210147125 habitantes
        # Colombia tiene 50372424 habitantes

* **.clear():** Elimina todos los items del diccionario.
* **.pop(n):** Elimina el elemento ingresado. n es la **key**
   
