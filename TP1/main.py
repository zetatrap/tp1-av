# 1
def ordenar_lista(lista):
    return sorted(lista)

# 2
def gestionar_conjunto():
    conjunto = set()
    while True:
        opcion = input("Ingrese un numero para agregar al conjunto o 'salir' para terminar: ")
        if opcion.lower() == 'salir':
            break
        conjunto.add(int(opcion))
    
    print("Conjunto actual:", conjunto)
    elemento = input("Ingrese un numero para eliminar: ")
    if int(elemento) in conjunto:
        conjunto.remove(int(elemento))
        print(f"{elemento} eliminado. Conjunto actualizado: {conjunto}")
    else:
        print(f"{elemento} no esta en el conjunto.")

# 3
def diferencias_conjuntos(conjunto1, conjunto2):
    return conjunto1 - conjunto2, conjunto2 - conjunto1

# 4
def eliminar_duplicados(lista):
    return list(set(lista))

# 5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 6
def contar_ocurrencias(lista, elemento):
    return lista.count(elemento)

# 7
def suma_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + suma_recursiva(n - 1)

# 8
class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_info(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.año_publicacion}"

class LibroDigital(Libro):
    def __init__(self, titulo, autor, año_publicacion, formato):
        super().__init__(titulo, autor, año_publicacion)
        self.formato = formato

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Formato: {self.formato}"