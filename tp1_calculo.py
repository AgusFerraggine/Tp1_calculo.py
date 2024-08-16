# -*- coding: utf-8 -*-
"""Tp1_calculo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Kc_INWAgqRrk0SNmOwmw17bJcxLaDcyC
"""

students = [
    {"nombre": "José", "notas": [85, 90, 78, -10]},
    {"nombre": "Carlos", "notas": [88, 72, 94, 102]},
    {"nombre": "María", "notas": [95, 85, 87,'A++']},
    {"nombre": "lujan", "notas": [180,-20,200,-65]},
    {"nombre": "juan", "notas": []}
]

#con esto 'saco' los datos del diccionario y los imprimo
for student in students:
  nombre = student["nombre"]
  notas = student["notas"]

#creo listas que me dividen las notas válidas que son enteros dentro del rango 0-100, y las invalidas (string, nros. mayores a 100 y menores a 0)
  notas_validas = []
  notas_invalidas = []

  print ("nombre: ",nombre ,", sus notas son: ",notas)

#condicional. para cada nota en la lista del diccionario de cada alumno, me fijo si entra en mi rango y si es un nro. entero, entonces pasa a la lista de 'notas validas'
  for nota in notas:
    if isinstance(nota,int) and 0<nota<100:
     notas_validas.append(nota)
    else:
      notas_invalidas.append(nota)
  if notas_invalidas:
    print("error en la nota de",nombre,": " "nota inválida ",notas_invalidas)

#verifico si la lista 'notas validas' tiene elementos en ella para calcular el promedio del alumno
  if notas_validas:
    promedio = sum(notas_validas)/len(notas_validas)
    print("nota final = ",promedio)
  else:
    print(nombre," no tiene notas válidas para calcular su promedio.")
  
  print("--------------------------------")
