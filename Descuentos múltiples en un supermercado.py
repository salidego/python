#!/usr/bin/env python
# coding: utf-8

# # Descuentos múltiples en un supermercado

# ## Acciones de aprendizaje
# 
# a. Analizar, identificar y declarar las variables que considere necesarias para realizar los cálculos de descuentos y total a pagar
# 
# b. Analizar, identificar e implementar iteradores que permitan extraer datos a través de listados ordenados de datos
# 
# c. Diseñar el algoritmo desde un lenguaje de programación que facilite las tareas de automatización, depuración y verificación de la solución propuesta.

# # Planteamiento de la situación
# 
# Una linea de supermercados de renombre en tu país te ha contratado y encomendado la tarea de automatizar el cálculo de la suma a pagar por parte de sus clientes durante una campaña agresiva para mover inventario. La campaña consiste en dar descuentos para algunos productos de hasta el 30%. Adicionalmente, si la fecha de vencimiento del producto es el día de hoy, se aplicará un 20% adicional sobre el precio a pagar (si el producto tenía descuento sobre este subtotal-nuevo precio se aplicaría el 20% extra.
# 
#  
# 
# La cadena de supermercados ya tiene un software que se encarga de registrar y ordenar los datos de los productos del cliente, utilizando listas y diccionarios, siguiendo la siguiente estructura:

# In[ ]:


productos = [
    {'sku': 1, 'fecha_expiracion': '', 'precio': 423.646, 'descuento': 0},
    {'sku': 2, 'fecha_expiracion': '', 'precio': 45.117, 'descuento': 24},
    {'sku': 3, 'fecha_expiracion': 'hoy', 'precio': 485.603, 'descuento': 0}
]


# dónde:
# 
# 1. sku corresponde a la llave de identificador único del producto
# 2. fecha_expiracion corresponde a la llave de la fecha de expiración, si el producto vence el día de hoy, tendrá el valor "hoy", en caso contrario, irá vacía
# 3. precio corresponde a la llave con el precio del producto
# 4. descuento corresponde a la llave con el descuento de la campaña para rotar inventario. Este descuento es un número entero, representando el porcentaje a aplicar, es decir, si la llave trae el valor 30 deberás aplicar un 30% de descuento al precio del producto
#  
# ### ¿Qué hay que dar como resultado?
# Se te solicita calcular el precio a pagar por el cliente luego de descuentos, con hasta dos cifras decimales de precisión.
# 
# Solucione el reto, escribiendo el código que represente la automatización del proceso de registro de empleados y visitantes.
# 
# 

# # Notas Adicionales a tener en cuenta
# 1. Lectura de entradas:
# 
# Para leer los datos de entrada es necesario que utilices el módulo json de python, de la siguiente manera: 

# In[ ]:


import json
productos = json.loads(input())


# 2. La salida la debes dar con la función print:

# In[ ]:


print(resultado)


# 3. Utilizar la función round() para aproximar el resultado:

# In[ ]:


resultado = round(resultado, 2)


# 4. No usar más de un print en el código ni escribir nada dentro del método input(), para que las pruebas unitarias no les den problemas

# # Datos de Entrada
# 

# In[58]:


[{"sku": 1, "fecha_expiracion": "", "precio": 846.599, "descuento": 17}, 
 {"sku": 2, "fecha_expiracion": "hoy", "precio": 539.478, "descuento": 0}, 
 {"sku": 3, "fecha_expiracion": "", "precio": 536.319, "descuento": 0}, 
 {"sku": 4, "fecha_expiracion": "", "precio": 404.469, "descuento": 0}, 
 {"sku": 5, "fecha_expiracion": "hoy", "precio": 240.95, "descuento": 0}, 
 {"sku": 6, "fecha_expiracion": "hoy", "precio": 279.162, "descuento": 0}, 
 {"sku": 7, "fecha_expiracion": "hoy", "precio": 681.996, "descuento": 24}]


# # SOLUCIÓN AL RETO

# In[56]:


import json
productos = json.loads(input())

Total = 0.0
descuento_vencimiento = 80

for i in productos:
    fecha = i['fecha_expiracion']
    precio = i['precio']
    descuento = i['descuento']
    
    if fecha == 'hoy':
        subtotal = ((precio - (precio*(descuento/100)))*(descuento_vencimiento/100))
                    
    else:
        subtotal = (precio - (precio*(descuento/100))) 

    Total = Total + subtotal
    
print(round(Total,2))

