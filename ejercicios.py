from functools import reduce #---> Esto es para los ejercicios de "reduce"
#---EJERCICIO 1----
def frecuencia_letras(texto):
    frecuencias = {}
    texto_limpio = texto.replace(" ", "").lower()
    for letra in texto_limpio:
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

# ---EJERCICIO 2----
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))

# ---EJERCICIO 3----
def buscar_palabra(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]

# ---EJERCICIO 4----
lista1 = [10, 20, 30]
lista2 = [5, 10, 15]
diferencias = list(map(lambda x, y: x - y, lista1, lista2))

# ---EJERCICIO 5----
def evaluar_media(lista, nota_aprobado=5):
    media = sum(lista) / len(lista)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

# ---EJERCICIO 6----
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# ---EJERCICIO 7----
lista_tuplas = [("Hola", "Mundo"), ("Python", "Mola")]
lista_strings = list(map(lambda t: " ".join(t), lista_tuplas))

# ---EJERCICIO 8----
def programa_division():
    try:
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        print(f"Resultado: {n1 / n2}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"No fue exitosa: {e}")

# ---EJERCICIO 9----
def filtrar_mascotas(lista):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, lista))

# ---EJERCICIO 10----
def promedio_con_error(lista):
    if not lista:
        raise ValueError("La lista está vacía")
    return sum(lista) / len(lista)

try:
    promedio_con_error([])
except ValueError as e:
    print(e)

# ---EJERCICIO 11----
def verificar_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if 0 <= edad <= 120:
            print(f"Edad válida: {edad}")
        else:
            print("Error: Edad fuera de rango (0-120).")
    except ValueError:
        print("Error: Debes introducir un valor numérico.")

# ---EJERCICIO 12----
def longitudes_palabras(frase):
    return list(map(len, frase.split()))

# ---EJERCICIO 13----
def mayusculas_minusculas(caracteres):
    letras_unicas = sorted(list(set(caracteres)))
    return list(map(lambda l: (l.upper(), l.lower()), letras_unicas))

# ---EJERCICIO 14----
def palabras_por_letra(lista, letra):
    return list(filter(lambda p: p.lower().startswith(letra.lower()), lista))

# ---EJERCICIO 15----
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

# ---EJERCICIO 16----
def palabras_largas(texto, n):
    palabras = texto.split()
    return list(filter(lambda p: len(p) > n, palabras))

# ---EJERCICIO 17----
def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)

# ---EJERCICIO 18----
def filtrar_estudiantes(estudiantes):
    return list(filter(lambda e: e['calificacion'] >= 90, estudiantes))

# ---EJERCICIO 19----
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# ---EJERCICIO 20----
def solo_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))

# ---EJERCICIO 21----
calcular_cubo = lambda x: x**3

# ---EJERCICIO 22----
def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)

# ---EJERCICIO 23----
def concatenar_palabras(lista):
    return reduce(lambda x, y: x + " " + y, lista)

# ---EJERCICIO 24----
def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)

# ---EJERCICIO 25----
def contar_caracteres(cadena):
    return len(cadena)

# ---EJERCICIO 26----
resto_division = lambda x, y: x % y

# ---EJERCICIO 27----
def promedio_lista(lista):
    return sum(lista) / len(lista) if lista else 0

# ---EJERCICIO 28----
def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

# ---EJERCICIO 29----
def enmascarar_cadena(variable):
    cadena = str(variable)
    if len(cadena) <= 4:
        return cadena
    return "#" * (len(cadena) - 4) + cadena[-4:]

# ---EJERCICIO 30----
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

# ---EJERCICIO 31----
def buscar_en_lista():
    nombres = ["Xaden", "Violet", "Tairn", "Sgaeyl"]
    nombre_buscado = input("Introduce un nombre para buscar: ")
    if nombre_buscado in nombres:
        print(f"{nombre_buscado} ha sido encontrado.")
    else:
        raise ValueError("El nombre no está en la lista.")

# ---EJERCICIO 32----
def puesto_empleado(nombre_completo, lista_empleados):
    return lista_empleados.get(nombre_completo, "La persona no trabaja aquí")

# ---EJERCICIO 33----
sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

# ---EJERCICIO 34----
class Arbol:
    def __init__(self):
        self.longitud_tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.longitud_tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)

    def info_arbol(self):
        return {
            "tronco": self.longitud_tronco, 
            "num_ramas": len(self.ramas), 
            "longitudes_ramas": self.ramas
        }

# ---EJERCICIO 35----
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No puedes transferir más de lo que tienes")
        self.saldo -= cantidad
        otro_usuario.agregar_dinero(cantidad)

# ---EJERCICIO 36----
def contar_palabras(texto):
    diccionario = {}
    for palabra in texto.split():
        diccionario[palabra] = diccionario.get(palabra, 0) + 1
    return diccionario

def reemplazar_palabras(texto, vieja, nueva):
    return texto.replace(vieja, nueva)

def eliminar_palabra(texto, palabra):
    return " ".join([p for p in texto.split() if p != palabra])

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    
# ---EJERCICIO 37----
def momento_dia(hora):
    if 6 <= hora <= 12:
        return "Es de día"
    elif 13 <= hora <= 20:
        return "Es de tarde"
    else:
        return "Es de noche"

# ---EJERCICIO 38----
def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "Nota no válida"

# ---EJERCICIO 39----
def calcular_area(figura, datos):
    if figura == "rectangulo":
        # datos = (base, altura)
        return datos[0] * datos[1]
    elif figura == "circulo":
        # datos = (radio,)
        import math
        return math.pi * (datos[0] ** 2)
    elif figura == "triangulo":
        # datos = (base, altura)
        return (datos[0] * datos[1]) / 2

# ---EJERCICIO 40----
def tienda_online():
    try:
        precio = float(input("Precio original del artículo: "))
        tiene_cupon = input("¿Tienes un cupón? (sí/no): ").lower()
        
        if tiene_cupon == "sí" or tiene_cupon == "si":
            valor_cupon = float(input("Valor del cupón: "))
            if valor_cupon > 0:
                precio -= valor_cupon
            else:
                print("Cupón no válido.")
        
        print(f"Precio final: {max(0, precio)}")
    except ValueError:
        print("Error: Introduce valores numéricos válidos.")