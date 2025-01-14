# Crear un programa que funcione como librería personal en dónde estén todos los libros que he leído,
# estoy leyendo y quiero leer en un futuro, puedo ordenarlos por categoria, autor, etc.
# Uso de json, interfaz de usuario, etc.

import json,re

def to_dict(jsonfile):
    with open(jsonfile, 'r') as file:
        dic = json.load(file)
    return dic
def save_list(dic, jsonfile):
    with open(jsonfile, 'w') as file:
        json.dump(dic, file, indent=4)

def añadir(dic):
    print("\n    Añadir Libro Nuevo\n")
    while True:
        titulo = input("    Introduce el título del libro: ")
        if titulo in dic:
            print("      El libro ya existe.")
            #todo Añadir la opción de continuar o cancelar.
            continue
        else: break
    autor = input("    Introduce el autor del libro: ")
    #todo Añadir la opción de añadir un autor nuevo o usar uno ya existente.
    while True:
        paginas_leidas = input("    Introduce el número de páginas que llevas leidas: ")
        if not paginas_leidas.isdigit():
            print("      Introduce un número.")
            continue
        else: break
    while True:
        paginas_totales = input("    Introduce el número de páginas totales del libro: ")
        #todo Añadir un parametro para que no se pueda introducir un número menor a las páginas leidas.
        #todo si el numero es menor a las páginas leidas, preguntar si se quiere cambiar las páginas leidas.
        if not paginas_totales.isdigit():
            print("      Introduce un número.")
            continue
        else: break
    while True:
        estado = input('    Introduce el estado de lectura: "leido", "en progreso" o "pendiente": ').lower()
        if estado not in ["leido", "en progreso", "pendiente"]:
            print("      Estado no válido. Inténtalo de nuevo.")
            continue
        else: break
    categoria = input("    Introduce la categoría: ")
    
    #todo Añadir si es una nueva categoría o una ya existente.
    
    dic[titulo] = [autor, paginas_leidas, paginas_totales, estado, categoria]
    print(f"""
    El libro "{titulo}" fue añadido con éxito.
    
    Título: {titulo}
    Autor: {autor}
    Páginas Leidas: {paginas_leidas}
    Páginas Totales: {paginas_totales}
    Estado: {estado}
    Categoría: {categoria}
""")
    #todo Añadir la opción de añadir más libros.
    #todo desea cambiar algo de este libro o continuar?
    return dic
def eliminar(dic):
    print("\n    Eliminar Libro\n")
    while True:
        titulo = input("    Introduce el título del libro a eliminar: ")
        if titulo not in dic:
            print("      El libro no existe. Inténtalo de nuevo.")
            continue
        else:
            while True:
                print(f'\n    ¿Estás seguro de eliminar el libro "{titulo}"?')
                confirm = input("    Sí/No: ").lower()
                if confirm == "no":
                    print("\n    Operación cancelada.\n")
                    break
                elif confirm == "sí" or confirm == "si":
                    del dic[titulo]
                    print(f'\n    El libro "{titulo}" fue eliminado.\n')
                    return dic
                else:
                    print("      Opción no válida, introduce Sí o No.")
                    continue
            break
def modificar(dic):
    print("\n    Modificar Libro\n")
    while True:
        titulo_libro = input("    Introduce el título del libro a modificar: ")
        if titulo_libro not in dic:
            print("      El libro no existe. Inténtalo de nuevo.")
            continue
        else: break
    print(f"""\n    ¿Qué deseas modificar del libro "{titulo_libro}"?
    
    1) Título
    2) Autor
    3) Páginas
    4) Estado
    5) Categoría
""")
    while True:
        opcion = input("    Selecciona una opción para modificar: ")
        
        if opcion == "1" or opcion == "título" or opcion == "titulo":
            titulo(dic, titulo_libro)
        elif opcion == "2" or opcion == "autor":
            autor(dic, titulo_libro)
        elif opcion == "3" or opcion == "páginas" or opcion == "paginas":
            paginas(dic, titulo_libro)
        elif opcion == "4" or opcion == "estado":
            estado(dic, titulo_libro)
        elif opcion == "5" or opcion == "categoría" or opcion == "categoria":
            categoria(dic, titulo_libro)
        else:
            print("      Opción no válida, introduce un número del 1 al 5 o una palabra válida.")
            continue
        break

# Modificar
def titulo(dic, titulo):
    print("\n      Cambiar Título\n")
    viejo = titulo
    nuevo = input("      Introduce el nuevo título: ")
    #pregunta de verificación ¿estas seguro {nuevo}?
    dic[nuevo] = dic.pop(viejo)
    print(f'\n      El libro "{viejo}" ha cambiado de nombre a "{nuevo}".\n')
    return dic
def autor(dic, titulo):
    print(f"""\n      Cambiar Autor\n
        El autor actual de "{titulo}" es {dic[titulo][0]}.
""")
    #quieres cambiar el autor de {titulo}?
    autor = input("      Introduce el nuevo nombre del autor: ")
    dic[titulo][0] = autor
    print(f'\n      Ahora el autor de "{titulo}" es {autor}.\n')
    return dic
def paginas(dic, titulo):
    print(f"""\n      Cambiar Páginas\n
        El libro "{titulo}" tiene {dic[titulo][1]} páginas leidas y un total de {dic[titulo][2]} páginas.
""")
    #preguntar: seguir o cancelar?
    while True:
        opcion = input('      Escoge entre: "leidas", "totales" o "ambas": ').lower()
        if opcion not in ["leidas", "totales", "ambas"]:
            print("        Opción no válida. Inténtalo de nuevo.")
            continue
        else: break
    if opcion == "leidas":
        while True:
            paginas = input("      Introduce el número de páginas leidas: ")
            if not paginas.isdigit():
                print("        Introduce un número.")
                continue
            else: break
        #si el número es mayor a las páginas totales, preguntar si se quiere cambiar las páginas totales.
        dic[titulo][1] = paginas
        print(f'\n      Páginas leidas cambiadas, ahora llevas {paginas} páginas del libro "{titulo}".\n')
        return dic
    elif opcion == "totales":
        while True:
            paginas = input("      Introduce el número de páginas totales: ")
            if not paginas.isdigit():
                print("        Introduce un número.")
                continue
            else: break
        #si el número es menor a las páginas leidas, preguntar si se quiere cambiar las páginas leidas.
        dic[titulo][2] = paginas
        print(f'\n      Páginas totales cambiadas, ahora el libro "{titulo}" tiene un total de {paginas} páginas.\n')
        return dic
    elif opcion == "ambas":
        while True:
            paginas_leidas = input("      Introduce el número de páginas leidas: ")
            if not paginas_leidas.isdigit():
                print("        Introduce un número.")
                continue
            else: break
        while True:
            paginas_totales = input("      Introduce el número de páginas totales: ")
            if not paginas_totales.isdigit():
                print("        Introduce un número.")
                continue
            else: break
        
        #si el número es mayor a las páginas totales, preguntar si se quiere cambiar las páginas totales o las leidas.
        dic[titulo][1] = paginas_leidas
        dic[titulo][2] = paginas_totales
        print(f'\n      Páginas cambiadas, ahora llevas {paginas_leidas} páginas de {paginas_totales} del libro "{titulo}".\n')
        return dic
def estado(dic, titulo):
    print(f"""\n      Cambiar Estado\n
        El estado actual de "{titulo}" es {dic[titulo][3]}.
""")
    #¿quieres cambiar el estado de "{titulo}"?
    while True:
        estado = input('      Introduce el estado de lectura: "leido", "en progreso" o "pendiente": ')
        if estado.lower() not in ["leido", "en progreso", "pendiente"]:
            print("        Estado no válido. Inténtalo de nuevo.")
            continue
        else: break
    dic[titulo][3] = estado
    print(f'\n      El estado de "{titulo}" ha cambiado a {estado}.\n')
    return dic
def categoria(dic, titulo):
    print(f"""\n      Cambiar Categoría\n
        La categoría actual de "{titulo}" es {dic[titulo][4]}.
""")
    #todo añadir la opción de ver las categorías existentes o añadir una nueva.
    categoria = input("      Introduce la categoría: ")
    dic[titulo][4] = categoria
    print(f"\n      La categoría de {titulo} ha cambiado a {categoria}.\n")
    return dic

def leidos(dic):
    print("\n    Libros Leidos\n")
    for libro in dic:
        if dic[libro][3] == "leido":
            print(f"    - {libro}")
    print()
def en_progreso(dic):
    print("\n    Libros en Progreso\n")
    for libro in dic:
        if dic[libro][3] == "en progreso":
            print(f"    - {libro}")
    print()
def pendientes(dic):
    print("\n    Libros Pendientes\n")
    for libro in dic:
        if dic[libro][3] == "pendiente":
            print(f"    - {libro}")
    print()

# Filtrar
def filtrar(dic):
    print("""\n    Filtrar Libros por:
    
    1) Autor
    2) Estado
    3) Categoría
""")
    while True:
        opcion = input("    Selecciona una opción: ")
        
        if opcion == "1" or opcion == "autor":
            filtrar_autor(dic)
        elif opcion == "2" or opcion == "estado":
            filtrar_estado(dic)
        elif opcion == "3" or opcion == "categoría":
            filtrar_categoria(dic)
        else:
            print("      Opción no válida. Inténtalo de nuevo.")
            continue
        break
def filtrar_autor(dic):
    print("\n      Filtrar por Autor")
    while True:
        autor = input("      Introduce el autor: ")
        if not any(autor in dic[libro][0] for libro in dic):
            print("        Autor no encontrado. Inténtalo de nuevo.")
            continue
        else: break
    print(f"\n      Libros de {autor}:")
    for libro in dic:
        if dic[libro][0] == autor:
            print(f"      - {libro}")
    print()
def filtrar_estado(dic):
    print("\n      Libros por Estado de Lectura")
    while True:
        estado = input("      Introduce el estado: leido, en progreso o pendiente: ")
        if not any(estado in dic[libro][3] for libro in dic):
            print("        Estado no existe. Inténtalo de nuevo.")
            continue
        else: break
    print(f"\n      Libros con Estado {estado}:")
    for libro in dic:
        if dic[libro][3] == estado:
            print(f"      - {libro}")
    print()
def filtrar_categoria(dic):
    categorias = set(dic[libro][4] for libro in dic if libro != "_id")
    print("\n      Categorías Disponibles:")
    for categoria in categorias:
        print(f"        - {categoria}")
    print()
    
    while True:
        categoria = input("      Introduce la categoría: ")
        if not any(categoria in dic[libro][4] for libro in dic):
            print("        Categoría no disponible. Inténtalo de nuevo.")
            continue
        else: break
    print(f"\n      Libros con Categoría {categoria}:")
    for libro in dic:
        if dic[libro][4] == categoria:
            print(f"      - {libro}")
    print()

def lista_completa(dic):
    print("\n    Lista Completa de Libros\n")
    for libro in dic:
        if libro != "_id":
            print(f"    - {libro}")
    print()

#todo Añadir la opción de guardador automático o manual.

def main():
    print("\nBienvenido a tu librería personal.")
    opciones = """
    Opciones: Puedes usar numeros o palabras.
    
    1) Añadir           5) Leidos
    2) Eliminar         6) En Progreso
    3) Modificar        7) Pendientes
    4) Filtrar          8) Lista (Completa de Libros)
    
    salir | opciones | guardar
"""
    print(opciones)
    pattern = r'^[\w,\s-]+\.[Jj][Ss][Oo][Nn]$'
    while True:
        jsonfile = input("Introduce el archivo con .json: ")
        if re.match(pattern, jsonfile):
            try:
                libros = to_dict(jsonfile)
                if "_id" in libros and libros["_id"] == "libros":
                    break
                else:
                    print("Archivo no compatible con este programa.")
                    continue
            except FileNotFoundError:
                print("Archivo no encontrado. Inténtalo de nuevo.")
                continue
            else: break
        else: print("Introduce un archivo válido.")
    
    while True:
        opcion = input('Selecciona una opción: ').lower()
        if opcion == "1" or opcion == "añadir":
            añadir(libros)
            #todo añadir función para verficar el guardado automático.
            #todo hacer esto para todas las opciones.
            #   if autosave == True:
            #       save_list(libros, jsonfile)
            #       print("Guardado.")
            #   else:
            #       print("tienes cambios sin guardar, ¿quieres guardarlos?")
            #       save = input("Sí/No: ")
            #       if save == "sí":
            #           save_list(libros, jsonfile)
            #           print("Guardado.")
            #       elif save == "no":
            #           print("Cambios no guardados.")
            #       else:
            #           print("Opción no válida.")
        elif opcion == "2" or opcion == "eliminar":
            eliminar(libros)
        elif opcion == "3" or opcion == "modificar":
            modificar(libros)
        elif opcion == "4" or opcion == "filtrar":
            filtrar(libros)
        elif opcion == "5" or opcion == "leidos":
            leidos(libros)
        elif opcion == "6" or opcion == "en progreso":
            en_progreso(libros)
        elif opcion == "7" or opcion == "pendientes":
            pendientes(libros)
        elif opcion == "8" or opcion == "lista":
            lista_completa(libros)
        elif opcion == "salir":
            seguridad = input("¿Deseas guardar antes de salir?: ")
            if seguridad == "sí":
                save_list(libros, jsonfile)
                print("Guardado.")
                print("Hasta luego.")
            elif seguridad == "no":
                print("Cambios no guardados.")
                print("Hasta luego.")
            else:print("Opción no válida.")
            break
        elif opcion == "opciones":
            print(opciones)
        elif opcion == "guardar":
            save_list(libros, jsonfile)
            print("Guardado.")
        else:
            print("Opción no válida. Escriba 'opciones' para ver las opciones.")
            continue

if __name__ == "__main__":
    main()
    
# Programa terminado, falta añadir las mejoras y opciones que se mencionan en los comentarios.
# Se puede mejorar el código y la interfaz de usuario.
# Se puede añadir más opciones y funciones. Como guardado automático, libros recientes,
# interfaz bonita como porcentajes de lectura, etc.
# Pero en general el programa funciona como se espera y cumple con los requisitos.
# Hay que mejorar la consistencia y manejo de errores, así como la interfaz de usuario.
# En fin, doy este programa por terminado.