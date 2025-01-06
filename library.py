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
    titulo = input("Introduce el título del libro: ")
    autor = input("Introduce el autor del libro: ")
    paginas_leidas = input("Introduce el número de páginas leidas: ")
    paginas_totales = input("Introduce el número de páginas totales: ")
    estado = input("Introduce el estado de lectura: ")
    categoria = input("Introduce la categoría: ")
    
    dic[titulo] = [autor, paginas_leidas, paginas_totales, estado, categoria]
    return dic

# Modificar
def cambiar_titulo(dic):
    viejo = input("Introduce el título actual: ")
    nuevo = input("Introduce el nuevo título: ")
    dic[nuevo] = dic.pop(viejo)
    return dic
def eliminar(dic):
    titulo = input("Introduce el título del libro a eliminar: ")
    del dic[titulo]
    return dic
def autor(dic):
    titulo = input("Introduce el título del libro: ")
    autor = input("Introduce el autor del libro: ")
    dic[titulo][0] = autor
    return dic
def paginas(dic):
    titulo = input("Introduce el título del libro: ")
    
    opcion = input('Escoge entre: "leidas", "totales" o "ambas": ').lower()
    if opcion == "leidas":
        paginas = input("Introduce el número de páginas leidas: ")
        dic[titulo][1] = paginas
        dic[titulo][5] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return dic
    elif opcion == "totales":
        paginas = input("Introduce el número de páginas totales: ")
        dic[titulo][2] = paginas
        return dic
    elif opcion == "ambas":
        paginas_leidas = input("Introduce el número de páginas leidas: ")
        paginas_totales = input("Introduce el número de páginas totales: ")
        dic[titulo][1] = paginas_leidas
        dic[titulo][2] = paginas_totales
        dic[titulo][5] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return dic
def estado(dic):
    titulo = input("Introduce el título del libro: ")
    estado = input("Introduce el estado de lectura: ")
    dic[titulo][3] = estado
    dic[titulo][5] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return dic
def categoria(dic):
    titulo = input("Introduce el título del libro: ")
    categoria = input("Introduce la categoría: ")
    dic[titulo][3] = categoria
    return dic

def leidos(dic):
    for libro in dic:
        if dic[libro][3] == "leido":
            print(libro)
def en_progreso(dic):
    for libro in dic:
        if dic[libro][3] == "en progreso":
            print(libro)
def pendientes(dic):
    for libro in dic:
        if dic[libro][3] == "pendiente":
            print(libro)
def filtrar_autor(dic):
    autor = input("Introduce el autor: ")
    for libro in dic:
        if dic[libro][0] == autor:
            print(libro)
def filtrar_categoria(dic):
    categoria = input("Introduce la categoría: ")
    for libro in dic:
        if dic[libro][4] == categoria:
            print(libro)
def filtrar_estado(dic):
    estado = input("Introduce el estado: ")
    for libro in dic:
        if dic[libro][3] == estado:
            print(libro)
def lista_completa(dic):
    for libro in dic:
        print(f"- {libro}")

def recientes(dic):
    libros_modificados = sorted(dic.items(), key=lambda x: x[1][5], reverse=True)
    for libro in libros_modificados[:5]:
        print(f"{libro[0]} - Última modificación: {libro[1][5]}")
    

def main():
    opciones = """
    Opciones:
    1) Añadir           6) Leidos
    2) Modificar        7) En Progreso
    3) Eliminar         8) Pendientes
    4) Recientes        9) Filtrar
    5) Buscar           0) Lista Completa
    
    salir | opciones | guardar
"""
    print(opciones)
    pattern = r'^[\w,\s-]+\.[Jj][Ss][Oo][Nn]$'
    while True:
        jsonfile = input("Introduce el archivo con .json: ")
        if re.match(pattern, jsonfile):
            try: libros = to_dict(jsonfile)
            except FileNotFoundError:
                print("Archivo no encontrado. Inténtalo de nuevo.")
                continue
            else: break
        else: print("Introduce un archivo válido.")
        
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        añadir(libros)
    elif opcion == "2":
        print("""
        1) Cambiar Título
        2) Cambiar Autor
        3) Cambiar Páginas
        4) Cambiar Estado
        5) Cambiar Categoría
        """)
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            cambiar_titulo(libros)
        elif opcion == "2":
            autor(libros)
        elif opcion == "3":
            paginas(libros)
        elif opcion == "4":
            estado(libros)
        elif opcion == "5":
            categoria(libros)
    elif opcion == "3":
        eliminar(libros)
    elif opcion == "4":
        recientes(libros)
    elif opcion == "5":pass
    elif opcion == "6":
        leidos(libros)
    elif opcion == "7":
        en_progreso(libros)
    elif opcion == "8":
        pendientes(libros)
    elif opcion == "9":
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
    elif opcion == "0":
        lista_completa(libros)
    elif opcion == "salir":
        print("Hasta luego.")
        return
    elif opcion == "opciones":
        print(opciones)
    elif opcion == "guardar":
        save_list(libros, jsonfile)

if __name__ == "__main__":
    main()