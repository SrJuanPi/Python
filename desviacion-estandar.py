x1,x2,x3,x4,x5 = 5, 7, 6, 5, 6 # Notas del 3°A
mediax = (x1+x2+x3+x4+x5)/5
f1,f2,f3,f4,f5 = 2, 1, 2, 2, 2
desviacion1 = ((f1*(mediax-x1)**2 + f2*(mediax-x2)**2 + f3*(mediax-x3)**2 + f4*(mediax-x4)**2 + f5*(mediax-x5)**2)/5)**0.5

y1,y2,y3,y4,y5 = 1, 4, 7, 7, 7 # Notas del 3°B
mediay = (y1+y2+y3+y4+y5)/5
g1,g2,g3,g4,g5 = 1, 1, 3, 3, 3
desviacion2 = ((g1*(mediay-y1)**2 + g2*(mediay-y2)**2 + g3*(mediay-y3)**2 + g4*(mediay-y4)**2 + g5*(mediay-y5)**2)/5)**0.5

print(f"Desviacion estandar 1: {desviacion1:.2f}")
print(f"Desviacion estandar 2: {desviacion2:.2f}")
print(f"La desvacion estandar menor es: {min(desviacion1, desviacion2):.2f}")
print(f"El promedio 1 es: {mediax:.2f}")
print(f"El promedio 2 es: {mediay:.2f}")

# LLegué al resultado correcto, pero cometí un error en la ejecución
# Al calcular las frecuencias, eran solo 3 datos, no 5
# Esto debido a que los datos eran repetidos
# Se ve de manera más clara con una tabla de frecuencias

# Notas del 3°A
# | Nota | Frecuencia |
# |------|------------|
# | 5    | 2          |         Como se puede ver, solo hay 3 notas diferentes
# | 6    | 2          |
# | 7    | 1          |

# Notas del 3°B
# | Nota | Frecuencia |
# |------|------------|
# | 1    | 1          |         y también aquí
# | 4    | 1          |
# | 7    | 3          |

# Misión cumplida, pero a medias. Lo bueno es que ahora entiendo mejor la formula
# Por otro lado me sirvió como práctica para Python después de un tiempo sin usarlo
# Como tarea o meta, debo hacer un programa que calcule la desviación estándar de un conjunto de datos
# y que permita ingresar los datos de manera dinámica, sin tener que modificar el código cada vez