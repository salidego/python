#!/usr/bin/env python
# coding: utf-8

# # Planteamiento de la situación
# 
#  
# 
# En una granja acaban de adquirir una máquina que le permitirá a una empresa de huevos aumentar la rapidez con la que son dispuestos sus productos para la distribución al usuario final. Se requiere un ingeniero de sistemas  para que programe esta máquina bajo ciertos estándares.
# 
# Los huevos son clasificados según su calidad y su peso. Para identificar la calidad de los huevos existen tres categorías A, B y C. Los huevos de categoría A son huevos frescos sin defectos y aptos para el consumo humano. Los huevos de categoría B son huevos de calidad normal que han sido sometidos a procesos de conservación. Los huevos tipo C son huevos que deben ser pasados por procesos industriales para ser considerados aptos para el consumo.
# 
# Los huevos de categoría A son clasificados según su peso como:
# 
#  * Huevos A cuyo peso va desde los 53 g. hasta un peso menor de 60 g.
# 
#  * Huevos AA cuyo peso va desde los 60 g. hasta un peso menor de 67 g.
# 
#  * Huevos AAA cuyo peso es igual o está por encima de los 67 g.
# 
# 
# y los tipo B y C o BC como:
# 
#  * Huevos B cuyo peso va desde 46 g. hasta un peso menor de 53 g.
# 
#  * Huevos C cuyo peso es menor de 46 g.
# 
# 
# Escriba una función llamada

# In[ ]:


clasificacion_huevos


# que de entrada, reciba una lista de datos tipo flotantes asociada al peso de un conjunto de huevos. La lista puede tener cualquier número de datos. Un ejemplo de esta lista de datos puede ser:
# 
# [46.5, 60.8, 58.7, 70.0, 49.8]
# 
# donde cada ítem como se mencionó, está asociado al peso de cada huevo, es decir el primer ítem pertenece a un huevo que pesa 46.5 gr.
# 
# La función debe ser capaz de clasificar los huevos de acuerdo al peso que se especifique en la lista anteriormente mencionada. Los huevos deben ser clasificados si son A, AA, AAA o si son BC (Una única clasificación para los huevos B y C). Es decir el primer huevo pesa 46.5 gr lo que indica que el huevo es de categoría BC.
# 
# Al clasificar los huevos determine el total de huevos de cada uno de los tipos de huevos, A, AA, AAA y BC. Habiendo determinado el número de huevos de acuerdo a cada clasificación, desarrolle una función adicional, llamada
# 
# 

# In[ ]:


calcular_bandejas


# que permita calcular cuántas bandejas de huevos se pueden obtener para cada una de las categorías, considerando que los huevos tipo A se empacan en grupos de 30 huevos, los tipo AA en grupos de 24 huevos, los tipo AAA en grupos de 12 huevos y los tipo BC en grupos de 30 huevos. Esta función debe recibir como parámetro de entrada el número de huevo y los huevos por bandeja. Se añade una bandeja si y solo si se completa, esto es, en caso de que haya 40 huevos A, se destinará solo una bandeja.
# 
# La función clasificacion_huevos debe retornar una lista de directorios con la siguiente información y estructura:
# 
# [
# 
# {‘tipo_huevos’: ‘A’, ‘numero_huevos’: 70, ‘numero_bandejas’: 2},
# 
# {‘tipo_huevos’: ‘AA’, ‘numero_huevos’: 120, ‘numero_bandejas’: 5},
# 
# {‘tipo_huevos’: ‘AAA’, ‘numero_huevos’: 170, ‘numero_bandejas’: 14},
# 
# {‘tipo_huevos’: ‘BC’, ‘numero_huevos’: 80, ‘numero_bandejas’: 2}
# 
# ]
# 
# Debe tenerse en cuenta el orden de cada una de las distintas clases de huevos. Tenga en cuenta que los huevos tipo BC son la unión de los huevos tipo B y los tipo C.

# # Planteamiento del reto
# 
# 
# Con respecto a lo planteado anteriormente, 
# 1. ¿Cómo se podría automatizar el proceso de clasificación de huevos mediante el uso de una función escrita en Python de tal manera que a partir de un conjunto de datos relacionados con el peso de un conjunto de huevos, se llegue a la clasificación de huevos tipo A, AA, AAA, y B y C? 
# 
# 2. Adicionalmente, ¿Cómo se podría definir una segunda función que permita calcular cuántas bandejas de huevos se pueden obtener por cada una de las clasificaciones?

# # Acciones de aprendizaje
# 
#  
# 
# Entienda claramente cuál es la problemática que se requiere resolver y para qué se quiere hacer.
# 
# Identifique y declare todas las variables necesarias para llevar a cabo cada una de las clasificaciones correspondientes.
# 
# Identifique y declare todas las variables necesarias para almacenar la información que se requiere precisar.
# 
# Identifique la funcionalidad que debe tener el algoritmo a desarrollar dentro de la función.
# 
# A partir de los puntos anteriores escriba la función en Python que permita tomar los parámetros de entrada y procesarlos, de tal manera que al final retorne los valores establecidos en el enunciado, en el orden en que se han especificado.

# In[ ]:


# Entregables: 2 funciones
1. Clasificación de huevos (A, AA, AAA, BC) con entrada del peso 
2. Calcular cantidad de bandejas de huevos por cada clasificación


# # Resultado de código 

# In[1]:


lista = []

def clasificacion_huevos (lista):
    result = []

    huevos_AAA = 0
    huevos_AA = 0
    huevos_A = 0
    huevos_BC = 0
    
    
    bandejas_AAA = 0
    bandejas_AA = 0
    bandejas_A = 0
    bandejas_BC = 0
    
    
    for huevo in lista:
        # extrae aca el tipo de huevo con base en el peso (puedes usar una funcion para esto)
        # incrementa el contador de la categoria del huevo respectiva

        if huevo < 53:
            huevos_BC += 1

        if huevo >= 53 and huevo < 60:
            huevos_A += 1

        if huevo >= 60 and huevo < 67:
            huevos_AA += 1

        if huevo >= 67:
            huevos_AAA += 1
            
    #Estos print es para validar que este funcionando la categorización              
    #print(f'A: ', huevos_A)
    #print(f'AA: ', huevos_AA)
    #print(f'AAA: ', huevos_AAA)
    #print(f'BC: ', huevos_BC)
    
    # conociendo el numero de huevos por categoria, calcula las bandejas por categoria 
    #(puedes usar una funcion para esto)
    
    bandejas_AAA = huevos_AAA/12
    bandejas_AAA = int(bandejas_AAA)
    #print(bandejas_AAA)
    
    bandejas_AA = int(huevos_AA/24)
    bandejas_AA = int(bandejas_AA)
    #print(bandejas_AA)
    
    bandejas_A = int(huevos_A/30)
    bandejas_A = int(bandejas_A)

    #print(bandejas_A)

    bandejas_BC = int(huevos_BC/30)
    bandejas_BC = int(bandejas_BC)
    #print(bandejas_BC)

    
    
    # crea el diccionario de resultados con 
  
    result = [{'tipo_huevo': 'A', 'numero_huevos': huevos_A, 'numero_bandejas': bandejas_A},
              {'tipo_huevo': 'AA', 'numero_huevos': huevos_AA, 'numero_bandejas': bandejas_AA},
              {'tipo_huevo': 'AAA', 'numero_huevos': huevos_AAA, 'numero_bandejas': bandejas_AAA},
              {'tipo_huevo': 'BC', 'numero_huevos': huevos_BC, 'numero_bandejas': bandejas_BC}
    ]

    return result

