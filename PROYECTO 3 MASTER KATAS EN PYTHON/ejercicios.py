from functools import reduce #---> Esto es para los ejercicios de "reduce"

#---EJERCICIO 1----
def frecuencia_letras(texto):
    frecuencias = {}
    texto_limpio = texto.replace(" ", "").lower()
    for letra in texto_limpio:
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

print("--- Ejercicio 1 ---", frecuencia_letras("programacion"))


# ---EJERCICIO 2----
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print("--- Ejercicio 2 ---", dobles)


# ---EJERCICIO 3----
def buscar_palabra(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]

print("--- Ejercicio 3 ---", buscar_palabra(["casa", "perro", "casita", "árbol"], "casa"))


# ---EJERCICIO 4----
lista1 = [10, 20, 30]
lista2 = [5, 10, 15]
diferencias = list(map(lambda x, y: x - y, lista1, lista2))
print("--- Ejercicio 4 ---", diferencias)


# ---EJERCICIO 5----
def evaluar_media(lista, nota_aprobado=5):
    media = sum(lista) / len(lista)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

print("--- Ejercicio 5 ---", evaluar_media([6, 7, 8, 4]))


# ---EJERCICIO 6----
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("--- Ejercicio 6 ---", factorial(5))


# ---EJERCICIO 7----
lista_tuplas = [("Hola", "Mundo"), ("Python", "Mola")]
lista_strings = list(map(lambda t: " ".join(t), lista_tuplas))
print("--- Ejercicio 7 ---", lista_strings)


# ---EJERCICIO 8----
def programa_division():
    try:
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        print(f"Resultado: {n1 / n2}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"No fue exitosa: {e}")
# (Nota: El input del ejercicio 8 se puede dejar comentado o probar manualmente para no bloquear la ejecución automática)
# programa_division()


# ---EJERCICIO 9----
def filtrar_mascotas(lista):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, lista))

print("--- Ejercicio 9 ---", filtrar_mascotas(["Perro", "Mapache", "Gato", "Tigre"]))


# ---EJERCICIO 10----
def promedio_con_error(lista):
    if not lista:
        raise ValueError("La lista está vacía")
    return sum(lista) / len(lista)

try:
    promedio_con_error([])
except ValueError as e:
    print("--- Ejercicio 10 --- Excepción capturada:", e)


# ---EJERCICIO 11----
def verificar_edad():
    pass # (Input interactivo)


# ---EJERCICIO 12----
def longitudes_palabras(frase):
    return list(map(len, frase.split()))

print("--- Ejercicio 12 ---", longitudes_palabras("Hola mundo python"))


# ---EJERCICIO 13----
def mayusculas_minusculas(caracteres):
    letras_unicas = sorted(list(set(caracteres)))
    return list(map(lambda l: (l.upper(), l.lower()), letras_unicas))

print("--- Ejercicio 13 ---", mayusculas_minusculas("python"))


# ---EJERCICIO 14----
def palabras_por_letra(lista, letra):
    return list(filter(lambda p: p.lower().startswith(letra.lower()), lista))

print("--- Ejercicio 14 ---", palabras_por_letra(["casa", "perro", "coche", "gato"], "c"))


# ---EJERCICIO 15----
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))
print("--- Ejercicio 15 ---", sumar_tres([1, 2, 3]))


# ---EJERCICIO 16----
def palabras_largas(texto, n):
    palabras = texto.split()
    return list(filter(lambda p: len(p) > n, palabras))

print("--- Ejercicio 16 ---", palabras_largas("Hola programacion en python avanzado", 4))


# ---EJERCICIO 17----
def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)

print("--- Ejercicio 17 ---", lista_a_numero([5, 7, 2]))


# ---EJERCICIO 18----
def filtrar_estudiantes(estudiantes):
    return list(filter(lambda e: e['calificacion'] >= 90, estudiantes))

print("--- Ejercicio 18 ---", filtrar_estudiantes([{"nombre": "Ana", "calificacion": 95}, {"nombre": "Juan", "calificacion": 80}]))


# ---EJERCICIO 19----
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))
print("--- Ejercicio 19 ---", filtrar_impares([1, 2, 3, 4, 5]))


# ---EJERCICIO 20  (CORRECCIÓN) ----
def solo_enteros(lista):
    return list(filter(lambda x: type(x) is int, lista))

print("--- Ejercicio 20 ---", solo_enteros([1, "hola", 3, True, 5]))


# ---EJERCICIO 21----
calcular_cubo = lambda x: x**3
print("--- Ejercicio 21 ---", calcular_cubo(3))


# ---EJERCICIO 22----
def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)

print("--- Ejercicio 22 ---", producto_total([2, 3, 4]))


# ---EJERCICIO 23----
def concatenar_palabras(lista):
    return reduce(lambda x, y: x + " " + y, lista)

print("--- Ejercicio 23 ---", concatenar_palabras(["Hola", "mundo", "python"]))


# ---EJERCICIO 24----
def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)

print("--- Ejercicio 24 ---", diferencia_total([50, 10, 5]))


# ---EJERCICIO 25----
def contar_caracteres(cadena):
    return len(cadena)

print("--- Ejercicio 25 ---", contar_caracteres("ciberseguridad"))


# ---EJERCICIO 26----
resto_division = lambda x, y: x % y
print("--- Ejercicio 26 ---", resto_division(10, 3))


# ---EJERCICIO 27----
def promedio_lista(lista):
    return sum(lista) / len(lista) if lista else 0

print("--- Ejercicio 27 ---", promedio_lista([10, 20, 30]))


# ---EJERCICIO 28----
def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

print("--- Ejercicio 28 ---", primer_duplicado([1, 2, 3, 2, 4]))


# ---EJERCICIO 29----
def enmascarar_cadena(variable):
    cadena = str(variable)
    if len(cadena) <= 4:
        return cadena
    return "#" * (len(cadena) - 4) + cadena[-4:]

print("--- Ejercicio 29 ---", enmascarar_cadena("1234567890"))


# ---EJERCICIO 30----
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

print("--- Ejercicio 30 ---", son_anagramas("amor", "roma"))


# ---EJERCICIO 31----
# (Función con input interactivo)


# ---EJERCICIO 32----
def puesto_empleado(nombre_completo, lista_empleados):
    return lista_empleados.get(nombre_completo, "La persona no trabaja aquí")

print("--- Ejercicio 32 ---", puesto_empleado("Juan Pérez", {"Juan Pérez": "Analista"}))


# ---EJERCICIO 33----
sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))
print("--- Ejercicio 33 ---", sumar_listas([1, 2, 3], [4, 5, 6]))


## ---EJERCICIO 34----
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

#  Árbol (CORRECCION)
try:
    print("--- CASO DE USO ÁRBOL ---")
    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(2)
    print(arbol.info_arbol())
except Exception as e:
    print("Error:", e)


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

#  Banco con Alicia y Bob (CORRECCIÓN)
try:
    print("\n--- CASO DE USO BANCO ---")
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    bob.agregar_dinero(20)

    try:
        bob.transferir_dinero(alicia, 80)
    except ValueError as e:
        print("Error en transferencia:", e)

    alicia.retirar_dinero(50)
    print("Saldo final de Alicia:", alicia.saldo)
    print("Saldo final de Bob:", bob.saldo)
except Exception as e:
    print("Error:", e)


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

print("--- Ejercicio 36 ---", procesar_texto("hola mundo hola", "contar"))
    

# ---EJERCICIO 37----
def momento_dia(hora):
    if 6 <= hora <= 12:
        return "Es de día"
    elif 13 <= hora <= 20:
        return "Es de tarde"
    else:
        return "Es de noche"

print("--- Ejercicio 37 ---", momento_dia(15))


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

print("--- Ejercicio 38 ---", calificacion_texto(85))


# ---EJERCICIO 39----
def calcular_area(figura, datos):
    if figura == "rectangulo":
        return datos[0] * datos[1]
    elif figura == "circulo":
        import math
        return math.pi * (datos[0] ** 2)
    elif figura == "triangulo":
        return (datos[0] * datos[1]) / 2

print("--- Ejercicio 39 ---", calcular_area("rectangulo", (5, 3)))


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