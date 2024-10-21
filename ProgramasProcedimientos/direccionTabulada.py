"""direcconTabulada.py
Descripción.
        Muestra el uso de la biblioteca tabulate
        Muestra cómo imprimir una tabla con arreglo de areglos
        
        
    
Instalación.
    >python -m pip install tabulate

Ejecución como comando
    tabulate -1 -f html datosDireccion.txt
    
    
Referencia.
    Tablas con estilo con Tabulate
    Disponible en:https://python-para-impacientes.blogspot.com/2017/01/tablas-con-estilo-con-tabulate.html
    Consultado:20oct24

"""
from tabulate import tabulate
from expresionesDireccionPlantel import *
#define cabecera de tabla

#imprime todos los datos tabulados
print(tabulate(arrayDatos),end="\n\n")

#imprime datos tabulados con cabecera
print(tabulate(arrayDatos, headers='firstrow'))
print(end='\n')

#imprime datos tabulados con cabecera e index
print(tabulate(arrayDatos, headers='firstrow',
               showindex=True),end='\n')
print(end='\n')

#imprime datos tabulados con cabecera, index,formato
print(tabulate(arrayDatos, headers='firstrow',
               showindex=True,tablefmt='grid'))
print(end='\n')

#imprime datos tabulados con cabecera, index,formato
print(tabulate(arrayDatos, headers='firstrow',
               showindex=True,tablefmt='fancy_grid'))
print(end='\n')

#imprime datos tabulados con cabecera, index,formato
print(tabulate(arrayDatos, headers='firstrow',
               showindex=True,tablefmt='fancy_grid',
               stralign='center'))
print(end='\n')








