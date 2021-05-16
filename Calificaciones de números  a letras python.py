#!/usr/bin/env python
# coding: utf-8


# ### Planteamiento de la situación
# 
# Eres docente de una institución y necesitas automatizar el cálculo de la calificación de tus alumnos. Tu has estado realizando pruebas con una nota en el rango de 0 a 5, con los siguientes pesos para la calificación final:
# 
# 1. 60% corresponde al examen escrito.
# 2. 20% corresponde a las lecciones
# 3. 15% corresponde a las tareas.
# 4. 5% corresponde a las prácticas en el laboratorio
# 
#  
# La institución dónde laboras da notas de manera cualitativa, y no cuantitativa. Por lo anterior, se te solicita dar la calificación a tu estudiante usando la siguiente tabla de equivalencias:
# 
# Nota cuantitativa y Nota cualitativa
# 
# Por debajo o igual a 2   E
# Por debajo o igual a 3   D
# Por debajo o igual a 3.5 C
# Por debajo o igual a 4   B
# Por debajo o igual a 4.5 B+
# Por encima de 4.5        A
# 
# 
# Debes entregar a tu alumno la nota cualitativa con base en las calificaciones que obtuvo en su examen, lecciones, tareas y practicas.
# 
#    
# 
# ### Planteamiento del reto
# 
# Con respecto a la situación planteada, ¿De qué manera crees que puedes automatizar el proceso de cálculo y entrega de la nota?,  considerando que la cantidad de alumnos es numerosa, demandando mucho tiempo para realizar los cálculos de forma manual, y la alta probabilidad de equivocarse;  entonces, se te solicita diseñar un algoritmo desde un lenguaje de programación, que simplifique el tiempo empleado y minimice la probabilidad de error humano al realizar las operaciones necesarias para dar la calificación final.
# 
# 
# 
# ### Acciones de aprendizaje
# 
# a. Analizar, identificar y declarar las variables que considere necesarias para realizar los cálculos del cálculo de la nota final, así como su conversión a una nota cualitativa.
# b. Determinar desde las variables identificadas, cual(es) corresponden a los datos de entrada, las operaciones entre ellas que dan solución al reto, y cual(es) son los datos para presentar como salida.
# c. Diseñar el algoritmo desde un lenguaje de programación que facilite las tareas de automatización, depuración y verificación de la solución propuesta.
# 
#  
# #### Planteamiento de la solución del reto:
# 
# Escriba el algoritmo diseñado para solucionar el reto.
# 
#  
# 
# ### Notas adicionales
# 
# 1. Lectura de entradas: Debes leer la calificación de examenes, lecciones y demás usando input():
# examen = input()
# leccion = input()
# tarea = input()
# practica = input()
# 
# 
# 2. La salida la debes dar con la función print: print(resultado)
# 3. No usar más de un print en el código ni escribir nada dentro del método input(), para que las pruebas unitarias no les den problemas


examen = input()
leccion = input()
tarea = input()
practica = input()

examen = float(examen)
leccion = float(leccion)
tarea = float(tarea)
practica = float(practica)

nota = ((examen*0.6) +(leccion*0.2) + (tarea*0.15) + (practica*0.05))


resultado = 0

if (nota >4.5 and nota <=5):
    resultado = 'A'
    
elif (4 < nota <= 4.5):
    resultado = 'B+'
    
elif (3.5 < nota <= 4):
    resultado = 'B'

elif (3 < nota <= 3.5):
    resultado = 'C'

elif (2 < nota <= 3):
    resultado = 'D'
    
elif (0 < nota <= 2):
    resultado = 'E'


print(resultado)
