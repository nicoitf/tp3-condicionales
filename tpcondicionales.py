#nicolas copertino comision 12

# EJERCICIO 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# EJERCICIO 2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# EJERCICIO 3
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# EJERCICIO 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# EJERCICIO 5
contraseña = input("Ingrese su contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# EJERCICIO 6
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No hay un sesgo claro")

# EJERCICIO 7
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in 'aeiou':
    frase += "!"
print(frase)

# EJERCICIO 8
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 (mayúsculas), 2 (minúsculas) o 3 (primera letra mayúscula): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida")

# EJERCICIO 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# EJERCICIO 10
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
else:
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"

print(f"Estación: {estacion}")
