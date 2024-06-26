# Cómo obtener el día y la fecha actuales, con el módulo DateTime

import datetime as dt

ahora = dt.datetime.now()
print(ahora)
print(type(ahora))

# Con este método podemos cambiar a nuestro antojo la forma en que aparece la fecha y hora
# Muy importante si son mayúsculas o minúsculas pueden joder todo
print(ahora.strftime('%d/%m/%Y %H:%M:%S'))
print(ahora.strftime('%d/%m/%y %H:%M:%S')) # Simplifica el año de 4 dígitos a solo 2