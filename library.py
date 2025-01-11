# Crear un programa que funcione como librería personal en dónde estén todos los libros que he leído,
# estoy leyendo y quiero leer en un futuro, puedo ordenarlos por categoria, autor, etc.
# Uso de json, interfaz de usuario, etc.

import json,re,datetime

def to_dict(jsonfile):
    with open(jsonfile, 'r') as file:
        dic = json.load(file)
    return dic
def save_list(dic, jsonfile):
    with open(jsonfile, 'w') as file:
        json.dump(dic, file, indent=4)

def añadir(dic):
    while True:
        titulo = input("Introduce el título del libro: ")
        if titulo in dic:
            print("El libro ya existe.")
            break
        else:
            autor = input("Introduce el autor del libro: ")
            while True:
                paginas_leidas = input("Introduce el número de páginas que llevas leidas: ")
                if not paginas_leidas.isdigit():
                    print("Introduce un número.")
                    continue
                else: break
            while True:
                paginas_totales = input("Introduce el número de páginas totales del libro: ")
                if not paginas_totales.isdigit():
                    print("Introduce un número.")
                    continue
                else: break
            while True:
                estado = input('Introduce el estado de lectura: "leido", "en progreso" o "pendiente": ')
                if estado.lower() not in ["leido", "en progreso", "pendiente"]:
                    print("Estado no válido.")
                    continue
                else: break
            categoria = input("Introduce la categoría: ")
            break
    
    dic[titulo] = [autor, paginas_leidas, paginas_totales, estado, categoria]
    print(f"El libro {titulo} fue añadido con éxito.")
    return dic
def eliminar(dic):
    while True:
        titulo = input("Introduce el título del libro a eliminar: ")
        if titulo not in dic:
            print("El libro no existe.")
            continue
        else:
            while True:
                print(f"¿Estás seguro de eliminar {titulo}?")
                confirm = input("Sí/No: ").lower()
                if confirm == "no":
                    print("Operación cancelada.")
                    break
                elif confirm == "sí" or confirm == "si":
                    del dic[titulo]
                    print(f"El libro {titulo} fue eliminado.")
                    return dic
                else:
                    print("Opción no válida, introduce Sí o No.")
                    continue
            break

# Modificar
def modificar(dic):
    print("""
    1) Cambiar Título
    2) Cambiar Autor
    3) Cambiar Páginas
    4) Cambiar Estado
    5) Cambiar Categoría
    """)
    while True:
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            titulo(dic)
        elif opcion == "2":
            autor(dic)
        elif opcion == "3":
            paginas(dic)
        elif opcion == "4":
            estado(dic)
        elif opcion == "5":
            categoria(dic)
        else:
            print("Opción no válida, introduce un número del 1 al 5.")
            continue
        break
def titulo(dic):
    while True:
        viejo = input("Introduce el título actual: ")
        if viejo not in dic:
            print("El libro no existe.")
            continue
        else: break
    nuevo = input("Introduce el nuevo título: ")
    dic[nuevo] = dic.pop(viejo)
    print(f'El libro "{viejo}" ha cambiado de nombre a "{nuevo}".')
    return dic
def autor(dic):
    while True:
        titulo = input("Introduce el título del libro: ")
        if titulo not in dic:
            print("El libro no existe.")
            continue
        else: break
        
    autor = input("Introduce el nuevo nombre del autor: ")
    dic[titulo][0] = autor
    print(f"Ahora el autor de {titulo} es {autor}.")
    return dic
def paginas(dic):
    while True:
        titulo = input("Introduce el título del libro: ")
        if titulo not in dic:
            print("El libro no existe.")
            continue
        else: break
    while True:
        opcion = input('Escoge entre: "leidas", "totales" o "ambas": ').lower()
        if opcion not in ["leidas", "totales", "ambas"]:
            print("Opción no válida, intenta de nuevo.")
            continue
        else: break
    if opcion == "leidas":
        while True:
            paginas = input("Introduce el número de páginas leidas: ")
            if not paginas.isdigit():
                print("Introduce un número.")
                continue
            else: break
        dic[titulo][1] = paginas
        print(f"Páginas leidas cambiadas, ahora llevas {paginas} páginas del libro {titulo}.")
        return dic
    elif opcion == "totales":
        while True:
            paginas = input("Introduce el número de páginas totales: ")
            if not paginas.isdigit():
                print("Introduce un número.")
                continue
            else: break
        dic[titulo][2] = paginas
        print(f"Páginas totales cambiadas, ahora el libro {titulo} tiene un total de {paginas} páginas.")
        return dic
    elif opcion == "ambas":
        while True:
            paginas_leidas = input("Introduce el número de páginas leidas: ")
            if not paginas_leidas.isdigit():
                print("Introduce un número.")
                continue
            else: break
        while True:
            paginas_totales = input("Introduce el número de páginas totales: ")
            if not paginas_totales.isdigit():
                print("Introduce un número.")
                continue
            else: break
            
        dic[titulo][1] = paginas_leidas
        dic[titulo][2] = paginas_totales
        print(f"Páginas cambiadas, ahora llevas {paginas_leidas} de {paginas_totales} páginas del libro {titulo}.")
        return dic
def estado(dic):
    while True:
        titulo = input("Introduce el título del libro: ")
        if titulo not in dic:
            print("El libro no existe.")
            continue
        else: break
    while True:
        estado = input('Introduce el estado de lectura: "leido", "en progreso" o "pendiente":')
        if estado.lower() not in ["leido", "en progreso", "pendiente"]:
            print("Estado no válido.")
            continue
        else: break
    dic[titulo][3] = estado
    print(f"El estado de {titulo} ha cambiado a {estado}.")
    return dic
def categoria(dic):
    while True:
        titulo = input("Introduce el título del libro: ")
        if titulo not in dic:
            print("El libro no existe.")
            continue
        else: break
    categoria = input("Introduce la categoría: ")
    dic[titulo][3] = categoria
    print(f"La categoría de {titulo} ha cambiado a {categoria}.")
    return dic

def leidos(dic):
    print("\nLibros Leidos")
    for libro in dic:
        if dic[libro][3] == "leido":
            print(f"- {libro}")
def en_progreso(dic):
    for libro in dic:
        if dic[libro][3] == "en progreso":
            print(f"\nLibros en Progreso\n- {libro}")
def pendientes(dic):
    for libro in dic:
        if dic[libro][3] == "pendiente":
            print(f"\nLibros Pendientes\n- {libro}")

def filtrar_autor(dic):
    while True:
        autor = input("Introduce el autor: ")
        if not any(autor in dic[libro][0] for libro in dic):
            print("Autor no encontrado.")
            continue
        else: break
    for libro in dic:
        if dic[libro][0] == autor:
            print(f"Libros de {autor}\n- {libro}")
def filtrar_categoria(dic):
    while True:
        categoria = input("Introduce la categoría: ")
        if not any(categoria in dic[libro][4] for libro in dic):
            print("Categoría no encontrada.")
            continue
        else: break
    for libro in dic:
        if dic[libro][4] == categoria:
            print(f"Libros con Categoría {categoria}\n- {libro}")
def filtrar_estado(dic):
    estado = input("Introduce el estado: ")
    for libro in dic:
        if dic[libro][3] == estado:
            print(libro)
def lista_completa(dic):
    for libro in dic:
        print(f"- {libro}")


def main():
    opciones = """
    Opciones:
    1) Añadir           5) Leidos
    2) Eliminar         6) En Progreso
    3) Modificar        7) Pendientes
    4) Lista Completa   8) Filtrar
    
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
        opcion = input("\nSelecciona una opción: ")
        if opcion not in ["1", "2", "3", "4", "5", "6", "7", "8", "salir", "opciones", "guardar"]:
            print("Opción no válida.")
            continue
        if opcion == "1":
            añadir(libros)
        elif opcion == "2":
            eliminar(libros)
        elif opcion == "3":
            modificar(libros)
        elif opcion == "4":
            lista_completa(libros)
        elif opcion == "5":
            leidos(libros)
        elif opcion == "6":
            en_progreso(libros)
        elif opcion == "7":
            pendientes(libros)
        elif opcion == "8":
            print("""
        1) Autor
        2) Categoría
        3) Estado
    """)
            opcion = input("Selecciona una opción: ")
            if opcion == "1":
                filtrar_autor(libros)
            elif opcion == "2":
                filtrar_categoria(libros)
            elif opcion == "3":
                filtrar_estado(libros)
        elif opcion == "salir":
            print("Hasta luego.")
            return
        elif opcion == "opciones":
            print(opciones)
        elif opcion == "guardar":
            save_list(libros, jsonfile)
            print("Guardado.")
        else:
            print("Las opciones son: numeros del 1 al 8, salir, opciones o guardar.")
            continue

if __name__ == "__main__":
    main()