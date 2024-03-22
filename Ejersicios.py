# Cree cuatro variables llamadas mi_entero, mi_decimal, mi_string y mi_booleano. Asigne a cada variable un valor del 
#tipo que le corresponda. Luego muestre en pantalla el tipo de cada variable usando la función type() combinando 
#todo con la función print().


print("Ejercicio 1")
mensaje = "Buen día"
print(mensaje)
input("Escriba un mensaje que ve en pantalla: ")
print()

nuevo_mensaje = ()
input("Escriba otro mensaje que quiera: ")
print()

print("Ejersicio 2")

nombre = input("Ingresa tú nombre: ")
print(f"Hola {nombre} ¿Te gustaría aprender programación?")
print()

print("Ejercicio 3")

suma1 = 5  
suma2 = 3   
resta1 = 18   
resta2 = 10     
multi1 = 3
multi2 = 2.67 
divi1 = 32 
divi2 = 4  

suma = (suma1 + suma2)
resta = (resta1 - resta2)
multiplicacion = (multi1 * multi2)
division = (divi1 / divi2)

print("Suma")
print(f"La suma de {suma1} + {suma2} es: {suma}")

print("Resta")
print(f"La resta de {resta1} - {resta2} es: {resta}")

print("Multiplicación")
print(f"La multiplicación de {multi1} * {multi2} es: {multiplicacion}")

print("División")
print(f"La división de {divi1} / {divi2} es: {division}")

print("Ejersicio 4")
print("variables")
mi_string = "hola"
mi_entero = 4
mi_decimal = 7.29
mi_booleano = True
mi_booleano1 = False

print (type(mi_string))
print (type(mi_entero))
print (type(mi_decimal))
print (type(mi_booleano1))
print (type(mi_booleano))

print("Ejercicio 5")

numero_decimal = (input("Ingresa un número decimal: "))
numero_entero = (numero_decimal)
print(f"El número decimal {numero_decimal} truncado es: {numero_entero}")

print("Ejersicio 6")

print("¿Cuál es la salida de las siguientes expresiones?")
1 != 2
print(True)
True == 1
print(True)
False != False
print(False)
False > 0
print(False)
1.0 < 1
print(False)
test = "test"
print(True)
1.0 >= 1
print(False)

print("Ejersicio 7")
nombre = ()
edad = ()
cien_años_en = ()
año_actual = 2024
input("Ingrese su nombre: ")
input("Ingrese du edad: ")
cien_años_en = 100 + año_actual 
print(cien_años_en)

print("Ejersicio 8")
Fahrenheit = (9.0/5.0)
celsius = float(input("Ingrese la temperatura actual en Celsius: "))
convercion = Fahrenheit * celsius + 32
print(f"Los {celsius} grados Celsius son equivalentes a {convercion} grados Fahrenheit")

print("Ejersicio 9")
primer_numero = float (input("Ingrese el primer numero: "))
segundo_numero = float(input("Ingrese el segundo numero: "))
print()
sumar = primer_numero + segundo_numero
restar = primer_numero - segundo_numero
multiplicar = primer_numero * segundo_numero
dividir = primer_numero / segundo_numero
potencia = primer_numero ** segundo_numero
print(f"La suma del {primer_numero} y del {segundo_numero} es {sumar}")
print(f"La resta del {primer_numero} y del {segundo_numero} es {restar}")
print(f"La multiplicacion del {primer_numero} y del {segundo_numero} es {multiplicar}")
print(f"La division del {primer_numero} y del {segundo_numero} es {dividir}")
print(f"La potenciacion de {primer_numero} y del {segundo_numero} es {potencia}")

print("Ejercicio 10")

numero_ingresado = int(input("Ingrese el número: "))
divisible2 = numero_ingresado % 2
divisible3 = numero_ingresado % 3
divisible4 = numero_ingresado % 4
divisible5 = numero_ingresado % 5

if divisible2 == 0:
    print(f"El número {numero_ingresado} es divisible por 2")
elif divisible3 == 0:
    print(f"El número {numero_ingresado} es divisible por 3")
elif divisible4 == 0:
    print(f"El número {numero_ingresado} es divisible por 4")
elif divisible5 == 0:
    print(f"El número {numero_ingresado} es divisible por 5")
    
print("Ejercicio 10")
numero = input("Escribe el número: ")
ingresado = int(numero) % 10
div2 = ingresado % 2
sum = 0
# Numeros diisibles por 2
if div2 == 0 or ingresado == 0: 
    print(f"El número {numero} es divisible por 2")

tam = len(numero)
for i in range(tam):  
    sum = sum + int(numero[i])
    
# Numeros divisibles por 3
div3 = sum % 3
if div3 == 0:
    print(f"El número {numero} ingresado es divisible por 3")
    
# Numeros divisibles por 4
ultimas = int(numero) % 100
div4 = ultimas % 4
if div4 == 0:
    print(f"El número ingresado {numero} es divisible por 4")
    
# Numeros divisibles por 5
div5 = ultimas % 5
if div5 == 0:  
    print(f"El número ingresado {numero} es divisible por 5")
    
print("Ejersicio 11")

input = int("Ingrese un número: ")
numeraso = int = input("Ingrese un número: ")  % 2 == 0
if numeraso % 2 == 0:
  print(f"El numero ingresado {numeraso} es par")
elif numeraso % 3 == 0:
  print(f"El numero que ingreso {numeraso} es impar")
else:
  print("Intente de nuevo.")
  
print("Ejersicio 12")
edad = int(input("Ingese su edad: "))

if edad <= 4:
  print(f"La edad {edad} es la de un bebe")
elif 5 <= edad < 10:
  print(f"La edad {edad} es la de un niño")
elif 11 <= edad < 17:
  print(f"La edad {edad} es la de un adolecente")
elif 18 <= edad < 35:
  print(f"La edad {edad} es la de un adulto joven")
elif 36 <= edad < 50:
  print(f"La edad {edad} es la de un adulto")
elif 51 <= edad < 100:
  print(f"La edad {edad} es la de un abuelo")
else:
  print("Ingrese una edad.")
  
print("Ejersicio 13")

ingreso_mensual = 200
gasto_mensual = 100

gastos = float(input("Ingrese su gasto mensual: "))
if gasto_mensual > gastos:
  print(f"Tu gasto es bajo, tenes margen de ganancia.")
elif gasto_mensual == gastos:
  print("Estas gastando lo que corresponde, todo bien.")
elif gasto_mensual < gastos:
  print(f"Estas gastando por encima de tu gasto mensual de {gasto_mensual}")
  print("Relaizar las cuentas bien.")
else:
  print("Ingrese un numero.")
  
def BuenPago(pago):
    gastos_mensuales_sudamerica = 350
    restante = pago - gastos_mensuales_sudamerica

    if pago > gastos_mensuales_sudamerica:
        print(f"Estás bien en tus cuentas, estás ahorrando {restante} al mes.")
        if pago >= 10000:
         print("Estás bien económicamente en cualquier país del mundo.")
         print("Puedo trabajar comodamente.")
        elif pago >= 5000:
         print("Estás bien económicamente en Europa, Asia y Oceania.")
         print("Puedo trabajar comodamente.")
        elif pago >= 2000:
         print("Estás bien económicamente en America del Sur.")
         print("Puedo trabajar comodamente.")
        elif pago >= 700:
         print("Estás bien económicamente en Argentina.")
         print("Puedo trabajar comodamente.")
        else:
          print("Buscar otro trabajo bien rentable y legal.")
    elif pago < gastos_mensuales_sudamerica:
        print(f"Estás en déficit, tu salario de: {pago} no alcanza para pagar tus cuentas de: {gastos_mensuales_sudamerica}.")
    else:
        print("Capacítate y trabaja en otro rubro si o sí.")

    return pago

sueldo_del_programador = int(input("Ingresa tu sueldo: "))

pago = BuenPago(sueldo_del_programador)
if pago <= 350:
    print("No puede trabajar, el sueldo es muy bajo.")
  
print("Ejercicio 14")

sueldo = int(input("Escribe el sueldo que ganaste: "))
gasto_fijos = 350
extra = 50
gasto_imprevisto = 60
sueldo_base = 450

if sueldo > gasto_fijos + extra:
    print(f"Facturaste bien, ganaste {sueldo} y alcanza para vivir bien y ahorrar algo.")
    
    if sueldo < gasto_fijos + gasto_imprevisto:
        print(f"Tu sueldo de {sueldo} no te alcanza, fíjate en los gastos fijos {gasto_fijos} + extra {extra} que haces.")
    elif sueldo > sueldo_base:
        print(f"El sueldo {sueldo} que ganaste está por encima del básico {sueldo_base}, seguí así.")
    else:
        print("Estás piola.")
        
elif sueldo == gasto_fijos + extra:
    print(f"Cuida la plata, tu sueldo {sueldo} se queda justo con el gasto fijo {gasto_fijos} + extra {extra}.")
    
elif sueldo < gasto_fijos + extra:
    print(f"Fíjate que gastaste poco, tu sueldo de {sueldo} no te permite cubrir tus gastos fijos {gasto_fijos} y extra {extra}.")
    
else:
    print("Eres un seco, debes trabajar y facturar.")
    
    
print("Ejersicio 15")
#3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir caracteres. 
usuario = str(input("Ingrese un texto: "))
lista = [usuario]
for strings in usuario:
  if strings not in lista:
    lista.append(usuario)
    print(f"Los caracteres que escribie aparecen en esta lista {lista}.")
    
print("Ejersicio 16")
#4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios.
usuario = str(input("Ingrese un texto: "))
palabras = usuario.split()
palabras_sin_espacios = "".join(palabras)
print(f"Los caracteres que escribie aparecen en esta lista {palabras_sin_espacios}.")

# Otra forma de hacerla es la siguiente.

cadena = input("Ingrese una cadena de texto: ")

lista_sin_espacios = []

for caracter in cadena:
    if caracter != ' ': 
        lista_sin_espacios.append(caracter)

print("Lista de caracteres sin espacios en la cadena:")
print(lista_sin_espacios)

print("Ejersicio 17")

#5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
usuario = int(input("Ingrese números: "))
numero = usuario in tupla
if numero in tupla:
 print(f"Los caracteres que escribie aparecen en esta lista {tupla}.")
elif numero not in tupla: 
 print(f"Los números que escribiste, no aparecen en la lista {tupla}")

#5) Es otra manera de hacer el ejersicio que se pide.

datos_guardados = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
persona = int(input("Ingresar número: "))
datos_que_se_repite = datos_guardados.count(persona)
if datos_que_se_repite > 0:
 print(f"Los caracteres que escribie aparecen en esta lista {datos_guardados}.")
elif datos_que_se_repite < 0: 
 print(f"Los números que escribiste, no aparecen en la lista {datos_guardados}")
else:
  print("Intente nuevamente ingresando un número.")
  
print("Ejersicio 17")
#1) Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo para un rango de números indicado por un usuario. 

print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
ingresa = input("Ingrese números del 1 al 20: ")
numeros_validos = ingresa
if numeros_validos in ingresa:
  print(f"Los números que ingreso {numeros_validos} aparecen en la lista mostrada")
elif numeros_validos not in ingresa:
  print(f"Los números que ingreso {numeros_validos} no se encuentra en la lista que se mostraba")
else:
  print("Vuelve a intentar ingresar otro número.")

# Otra manera de hacer el ejersicio.

lista_de_numeros = list(range(1, 21))
print(lista_de_numeros)

ingresa = input("Ingrese números del 1 al 20: ")
if ingresa.isdigit(): 
    numeros_validos = int(ingresa)
    if numeros_validos in lista_de_numeros:
        print(f"El número que ingresó ({numeros_validos}) está en la lista mostrada.")
    else:
        print(f"El número que ingresó ({numeros_validos}) no está en la lista mostrada.")
else:
    print("Por favor, ingrese un número válido.")


print("Ejersicio 18")
# Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. 
# Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50 

ingresa_numero = int(input("Ingrese un número del 1 al 10: "))
factor = ingresa_numero  
desde = 1  
hasta = 10  

for f in range(desde, hasta + 1):
    resultado = factor * f
    print(f'{factor} x {f} = {resultado}')

# Otra forma de hacer el ejersicio.
ingreso_numero = int(input("Ingrese un número del 1 al 10 para mostrar su tabla de multiplicar: "))
tabla_multiplicar = []

for f in range(1, 11):
    resultado = ingreso_numero * f
    tabla_multiplicar.append(resultado)

print(f'La tabla de multiplicar del número {ingreso_numero} es: {tabla_multiplicar}')

print("Ejersicio 19")
# Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir caracteres. 

cadena = input("Dame una cadena: ")
lista = [cadena]

for texto in cadena:
  if texto not in lista:
    lista.append(texto)

print(f"La cadena que redactaste es: {cadena}")


print("Ejercicio 20")
# Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios.
cadena = input("Dame una cadena: ")
cadena_sin_espacios = cadena.replace(" ", "")
print("La cadena sin espacios es:", cadena_sin_espacios)

print("Ejersicio 21")

# Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

numeros = tuple(range(1, 21))
print(numeros)

escribe = int(input("Ingresa números en el teclado de los que se ven en pantalla: "))
repetidos = (escribe,)

contar_numeros = numeros.count(escribe)

print(f"El número {escribe} se repite {contar_numeros} veces en la tupla.")

# Otra manera de crear solución al ajersicio.

lista_de_numeros = tuple(range(1, 21))
print(lista_de_numeros)

numeros = int(input("Ingrese un número del 1 al 20: "))
numeros_repetidos = (numeros,)
if numeros_repetidos.count(numeros,): 
    numeros_contados = int(numeros)
    if numeros_contados in lista_de_numeros:
        print(f"El número que ingresó ({numeros_contados}) está en la lista mostrada.")
    else:
        print(f"El número que ingresó ({numeros_contados}) no está en la lista mostrada.")
else:
    print("Por favor, ingrese un número válido.")

print("Ejersicio 21")

# Crea una tupla con los meses del año, pedir números al usuario. 
# Si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición, sino, muestra un mensaje de error. 
# El programa termina cuando el usuario introduce un cero 

meses_del_año = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
print(meses_del_año)

escribir = int(input("Ingresa un número: "))

if 1 <= escribir <= len(meses_del_año):
    print(f"El número que ingresaste es: {escribir} y corresponde al mes del año de: {meses_del_año[escribir - 1]}")
elif escribir not in range(1, len(meses_del_año) + 1):
    print("Inténtalo otra vez.")
else:
    print("Programa finalizado.")
    
# Se puede realizar de criterios distintos, asimilando un código más facil.

tupla = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
        "Agosto","Septiembre","Octubre","Noviembre","Diciembre")
 
print(tupla)
 
numero = int(input("Ingrese el número del mes que desea mostrar: "))
 
print(tupla[numero-1])

print("Ejersicio 22")

# Crea una tupla con números e indica el número con mayor valor y el que menor tenga.

numeros = tuple(range(0,9 ))
print(numeros)
escribi = int(input("Ingrese un número que ve en la consola: "))
if escribi in numeros:
  print(f"El número {escribi} que ingresaste, se registra en la consola.")
elif escribi not in numeros:
  print(f"El número {escribi} no se encuentra en la consola.")
else:
  print("Vuelve a intertar.")
  
print("Ejersicio 23")
# Crea una tupla con números e indica el número con mayor valor y el que menor tenga.

numeros = tuple(range(0,9))
print(numeros)
escribi1 = int(input("Ingrese un número más alto que ve en la lista: "))
escribi2 = int(input("Ingrese un número más bajo que ve en la lista: "))

if escribi1 > escribi2:
  print(f"El número {escribi1} es mayor que el número {escribi2}.")
elif escribi1 < escribi2:
  print(f"El número {escribi1} es menor que el número {escribi2}.")
else:
  print("Vuelve a intertar.")
  
print("Ejersicio 24")

agenda = {
    "alexis": "415443554",
    "bombui": "644561841",
}

print(agenda)

while True:
    nombre = input("Ingrese un nombre que se ve en consola o presione '*' para salir: ")

    if nombre == '*':
        break

    if nombre in agenda:
        print(f'El nombre {nombre} está en la agenda y su número de teléfono es: {agenda[nombre]}')
        modificar_telefono = input("¿Desea modificar el NÚMERO de TELEFÓNO? (Sí / No): ").lower()

        if modificar_telefono == 'si':
            nuevo_telefono = input("Ingrese el nuevo NÚMERO de TELEFÓNO: ")
            agenda[nombre] = nuevo_telefono
            print(f'Número de teléfono de {nombre} ha sido actualizado a: {nuevo_telefono}')

        elif modificar_telefono == 'no':
            print(f'No se cambia ningún teléfono.')
        else:
            print("Opción no válida.")

    else:
        print(f"El nombre {nombre} no está en la agenda.")
        agregar_nombre = input("¿Desea agregarlo a la agenda? (Sí / No): ").lower()

        if agregar_nombre == 'si':
            nuevo_telefono = input(f"Ingrese el NÚMERO de TELEFÓNO para {nombre}: ")
            agenda[nombre] = nuevo_telefono
            print(f'{nombre} ha sido agregado a la agenda con el número: {nuevo_telefono}')

        elif agregar_nombre == 'no':
            print(f'No se ha agregado el nombre {nombre} a la agenda.')
        else:
            print("Opción no válida.")

print("Programa finalizado.")

# Otra solución del ejersicio.

agenda = {
    "nombre1": "alexis",
    "telefóno1": "415443554",
    "nombre2": "bombui",
    "telefóno2": "644561841",
}

print(agenda)

while True:
    nombre = input("Ingrese un nombre que se ve en consola o presione '*' para salir: ")

    if nombre == '*':
        break

    if nombre in agenda:
        print(f'El nombre {nombre} está en la agenda y su número de teléfono es: {agenda[nombre]}')
        modificar_telefono = input("¿Desea modificar el NÚMERO de TELEFÓNO? (Sí / No): ").lower()

        if modificar_telefono == 'si':
            nuevo_telefono = input("Ingrese el nuevo NÚMERO de TELEFÓNO: ")
            agenda[nombre] = nuevo_telefono
            print(f'Número de teléfono de {nombre} ha sido actualizado a: {nuevo_telefono}')
        else:
            print("No se ha modificado el número de teléfono.")
    else:
        agregar_nombre = input(f"El nombre {nombre} no está en la agenda. ¿Desea agregarlo a la agenda? (Sí / No): ").lower()
        if agregar_nombre == 'si':
            nuevo_telefono = input(f"Ingrese el NÚMERO de TELEFÓNO para {nombre}: ")
            agenda[nombre] = nuevo_telefono
            print(f'{nombre} ha sido agregado a la agenda con el número: {nuevo_telefono}')
        else:
            print(f"No se ha agregado el nombre {nombre} a la agenda.")

print("Programa finalizado.")

print("Ejersicio 25")
# Mete los valores del 1 al 100 en una lista y mostrarlos en la consula.
numeros = list(range(1 , 101))
print(numeros)

print("Ejersicio 26")
#Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. 
# Por último, muestra los números ordenados de menor a mayor.
print("Digite el número '0' para no ingresar más números.")
usuario = input("Ingrese números que quiera: ")
numeros = [int(numero) for numero in usuario.split()]
letras = str()

if len(numeros) > 0:
    numeros.sort()
    print(f"Ingreso los siguientes números a la consola: {numeros}")
    
elif 0 in numeros:
    print("Ingreso un número '0' y por esa razón, el programa se cerró.")
else:
    print("intente de nuevo porfavor.")
    
print("Ejersicio 27")
#Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. 
# Por último, muestra los números ordenados de mayor a menor.
print("Digite el número '0' para no ingresar más números.")
usuario = input("Ingrese números que quiera: ")
numeros = [int(numero) for numero in usuario.split()]
letras = str()

if len(numeros) > 0:
    numeros.sort(reverse = True)
    print(f"Ingreso los siguientes números a la consola: {numeros}")
    
elif 0 in numeros:
    print("Ingreso un número '0' y por esa razón, el programa se cerró.")
else:
    print("intente de nuevo porfavor.")

print("Ejersicio 28")
# #Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. 
# Por último, muestra los números ordenados de mayorr a menor.
print("Escriba los nombres de los alumnos en el curso, se organizarán nombres del más largo al más corto.")
usuario = input("Ingrese nombrs que quiera: ")
nombres = [str(nombres) for nombres in usuario.split()]

if len(nombres) > 0:
    nombres.sort(reverse = True)
    print(f"Ingreso los siguientes números a la consola: {nombres}")
    
elif 0 in nombres:
    print("Ingreso un número '0' y por esa razón, el programa se cerró.")
else:
    print("intente de nuevo porfavor.")

print("Ejersicio 29")
# Imprime la secuencia de Fibonacci en una función.
def fibonacci(Fn_1, Fn_2):
    resultado = Fn_1 + Fn_2
    return resultado

# Llamando a la función
resultado_fibonacci = fibonacci(9, 6)
print(resultado_fibonacci)

print("Ejersicio 30")
# Imprime la en una función la serie de Fibonacci y que devuelva los n primeros numeros.
def Fibonacci(Number):
    if(Number==0):
        return 0
    elif(Number==1):
        return 1
    else:
        return (Fibonacci(Number-2)+Fibonacci(Number-1))
n=int(input("Ingresar la cantidad de 'n' números que quieres ver de la secuencia Fibonacci: "))
print("Secuencia Fibonacci:")
for n in range(0, n):
  print(Fibonacci(n))
  
# Otra manera de resolver el código bien.

def fibonacci(n):
    fib_series = []

    for i in range(n):
        if i == 0:
            fib_series.append(0)
        elif i == 1:
            fib_series.append(1)
        else:
            fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series

print("Si quiere ver los primeros 3 números, ingrese el número 3.")
n = int(input("Ingrese la cantidad de números de la serie de Fibonacci que quiere ver: "))
result = fibonacci(n)
print(f"Los primeros {n} números de la serie de Fibonacci son: {result}")

# Versión del código corregida con Chat GPT integrando robustes al código con.
# Integrando Funciones Descriptivas: Se cambiaron los nombres de las funciones para que sean más descriptivos y sigan la convención de nombres de Python.

def generar_serie_fibonacci(n):
    fib_series = [0, 1]  # Inicializamos la serie con los dos primeros números

    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series
# Manejo de Entrada del Usuario Mejorado: Se agregó un bucle while en la función obtener_numero_usuario() 
# para manejar de manera más robusta las entradas incorrectas del usuario.
# icialización de la Serie: La serie ahora se inicializa con los dos primeros números [0, 1], evitando el uso de condiciones dentro del bucle.
def obtener_numero_usuario():
    while True:
        try:
            n = int(input("Ingrese la cantidad de números de la serie de Fibonacci que quiere ver: "))
            if n >= 0:
                return n
            else:
                print("Por favor, ingrese un número no negativo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
# Separación del Código Principal: El código principal se ha movido a una función main() para mejorar la organización.
def main():
    print("Si quiere ver los primeros 3 números, ingrese el número 3.")
    n = obtener_numero_usuario()
    result = generar_serie_fibonacci(n)
    print(f"Los primeros {n} números de la serie de Fibonacci son: {result}")

if __name__ == "__main__":
    main()
    
print("Ejersicio 31")
# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS
#   las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.

def anagramas(frase1, frase2):
    if sorted(frase1) == sorted(frase2):
        print(f"Las palabras ingresadas '{frase1}' y '{frase2}' SON anagramas.")
    else:
        print(f"Las palabras ingresadas '{frase1}' y '{frase2}' NO SON anagramas.")

# Solicitar palabras al usuario
usuario1 = input("Ingrese la primera palabra para crear un anagrama: ")
usuario2 = input("Ingrese la segunda palabra para crear un anagrama: ")

# Llamar a la función con las palabras del usuario
anagramas(usuario1, usuario2)

print("Ejersicio 32")
# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.
def calcular_area():
    try:
        a = float(input("Ingrese la longitud de la base de la superficie: "))
        p = float(input("Ingrese la altura de la base de la superficie: "))
        resultado = a * p / 2
        print(f"El área del polígono es: {resultado}")
    except ValueError:
        print("Ingrese valores numéricos, intente de nuevo.")
        calcular_area()

calcular_area()

print("Ejersicio 33")
# Crea un programa que se encargue de transformar un número de
# decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

usuario = int(input("Ingresar un número decimal ejemplo '70.5' para convertirlo en binario: "))
numero_usuario = usuario
residuos_obtenidos = []

while usuario > 0:
    residuo = usuario % 2
    residuos_obtenidos.append(residuo)
    usuario = usuario // 2

residuos_obtenidos = residuos_obtenidos[::-1]

print(f"Número ingresado por el usuario es: {numero_usuario}")
print("Conseguimos los siguiente números binarios:", residuos_obtenidos)

print("Ejersicio 34")
# Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
# Los signos de puntuación no forman parte de la palabra. Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
usuario = input("Ingresa las palabras para contar las veces que se repiten: ")
palabras = usuario.split()
contar_palabras = input("Ingresa las palabras a contar: ")
cantidad_de_veces_que_aparecen = palabras.count(contar_palabras)
print(f"La cantidad de veces que aparece una palabra es {cantidad_de_veces_que_aparecen}")

print("Ejersicio 35")
# Crea un programa se encargue de transformar un número.
# * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
usuario = float(input("ingrese un número: "))
entero = int(usuario)
binario = bin(entero)
print(f"El número que ingresó {usuario} se convirtió en el número binario: {binario}")

print("Ejersicio 36")
def palabras (vocales):
  mayusculas = ""
  minusculas = "" 
  for vocales in letras:
      if vocales.isupper():
       mayusculas += vocales
      elif vocales.islower():
       minusculas += vocales
       
  print("MAYUSCULAS" , mayusculas)
  print("MINUSCULAS" , minusculas)
  
letras = str(input("Ingrese una frase: "))
palabras(letras)


def separar_mayusculas_minusculas(frase):
    mayusculas = ""
    minusculas = "" 

    for letra in frase:
        if letra.isupper():
            mayusculas += letra
        elif letra.islower():
            minusculas += letra

    print("Mayúsculas:", mayusculas)
    print("Minúsculas:", minusculas)

def main():
    frase = input("Ingrese una frase: ")
    separar_mayusculas_minusculas(frase)

if __name__ == "__main__":
    main()
    
print("Ejersicio 37")

# Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.

def invertir_palabras(frase):
    palabras = frase.split() 
    palabras_invertidas = palabras[::-1]  
    frase_invertida = ' '.join(palabras_invertidas)  
    return frase_invertida
  
def main():
   frase_original = input("Ingresar una frase: ")
   frase_invertida = invertir_palabras(frase_original)
   print(f"La Frase original es la siguiente: {frase_original} y la frase invertida es: {frase_invertida}")

if __name__ == "__main__":
  main()

# El mismo ejersicio solo que con objeto y componentes que dan salida clara de mensajes, instancias de excepción de mensaje y robustez.

# Objeto de código llamado "Polindromo".
class Polindromo:
  # Atributos del código de Polindromo
    def invertir_palabras(self, frase):
      # Mensaje con excepción de no ingreso de texto.
        if not frase:
            print("No se ha ingresado ninguna frase.")
            return
        # Atributos del Objeto.
        palabras = frase.split() # Segmento la "frase" en "palabras" y uso metodo ".split()" para invertir las palabras.
        palabras_invertidas = palabras[::-1] # Las palabras invertidas, se reacomodan para leerse de derecha a izquierda con el llamado "palabras[::-1]".
        frase_invertida = ' '.join(palabras_invertidas) # Las palabras invertidas y posicionadas para leerse inversamente, se reacomodan con "' '.join(palabras_invertidas)".
        return frase_invertida # retornando la frase que conseguimos invertir para mostrarse en un "print".
# Metodos (Tareas o Funcionalidades principales del código y objeto.)
def main(): 
    polindromo = Polindromo()  # Se llama la función principal que contiene el elemento a trabajar llamado "polindromo" que pertenece al objeto de "Polindromo".
    # Ciclo While con Condiciones if y elif.
    while True:
        frase_original = input("Ingrese una frase: ")
        if not frase_original: 
            print("Por favor, ingrese una frase válida.") 
            continue
        elif frase_original.isdigit(): # Condición de devolución en caso de que se ingrese un número y no letras con el metordo ".isdigit()". 
            print("ingrese una frase y no números.")
            continue
        frase_invertida = polindromo.invertir_palabras(frase_original)  # Llamamos al método de la instancia
        print(f"La Frase original es la siguiente: '{frase_original}' y la frase invertida es: '{frase_invertida}'")
        break
# Se da creación al objeto y llamado a su actividad principal de metodo con su nombre de "main". 
if __name__ == "__main__":
    main()
    
print("Ejersicio 38")
# Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.

class Sandwich:
    def __init__(self):
        self.condimentos = []

    def agregar_condimento(self, condimento):
        """Agrega un condimento al sandwich."""
        self.condimentos.append(condimento)

    def eliminar_condimento(self, indice):
        """Elimina un condimento del sandwich dado su índice."""
        if 0 <= indice < len(self.condimentos):
            del self.condimentos[indice]
            print("Condimento eliminado del sandwich.")
        else:
            print("Número de condimento inválido.")

    def mostrar_sandwich(self):
        """Muestra los condimentos actuales en el sandwich."""
        if self.condimentos:
            print("Condimentos en el sandwich:")
            for i, condimento in enumerate(self.condimentos, start=1):
                print(f"{i}: {condimento}")
        else:
            print("No hay condimentos en el sandwich.")

def imprimir_condimentos(condimentos):
    """Imprime la lista de condimentos disponibles."""
    print("Lista de condimentos disponibles:")
    for num, condimento in condimentos.items():
        print(f"{num}: {condimento}")

def main():
    condimentos = {
        1: "Mayonesa",
        2: "Sabora",
        3: "Ketchup",
        4: "Salsa de Apio",
        5: "Salsa de Queso"
    }

    imprimir_condimentos(condimentos)  # Imprimir lista de condimentos disponibles

    sandwich = Sandwich()  # Crear objeto Sandwich

    while True:
        opcion = input("Ingrese el número del condimento que desea agregar, o '0' para terminar, o 'eliminar' para quitar un condimento: ")
        if opcion == "0":
            print("Pedido finalizado.")
            break
        elif opcion.lower() == "eliminar":
            sandwich.mostrar_sandwich()
            eliminar = input("Ingrese el número del condimento que desea eliminar: ")
            if eliminar.isnumeric():
                sandwich.eliminar_condimento(int(eliminar) - 1)
            else:
                print("Ingrese un número válido.")
        elif opcion.isnumeric():
            opcion = int(opcion)
            if opcion in condimentos:
                condimento_elegido = condimentos[opcion]
                sandwich.agregar_condimento(condimento_elegido)
                sandwich.mostrar_sandwich()
            else:
                print("El condimento que desea no existe en la lista de condimentos.")
        else:
            print("Ingrese un número válido.")

if __name__ == "__main__":
    main()
    
print("Ejersicio 39")

import tkinter as tk

class Administrador:
    def __init__(self):
        self.nombre_de_empresa = ""
        self.nombre_de_proyecto = ""
        self.presupuesto = 0
        self.tiempo = ""
        self.servicios = ""

    def informacion_propuesta(self):
        self.nombre_de_empresa = empresa_entry.get()
        self.nombre_de_proyecto = proyecto_entry.get()

    def presupuesto_del_proyecto(self):
        self.presupuesto = presupuesto_entry.get()

    def ingresar_tipo_de_proyecto(self):
        self.servicios = servicios_entry.get()

    def ingresar_tiempos_de_trabajo(self):
        self.tiempo = tiempo_entry.get()

    def resumen_proyectos_viables(self):
        resumen_viables_label.config(text=f"Nombre de la Empresa: {self.nombre_de_empresa}\n"
                                           f"Nombre del Proyecto: {self.nombre_de_proyecto}\n"
                                           f"Presupuesto en Dólares: {self.presupuesto}\n"
                                           f"Tiempo de Duración del Proyecto: {self.tiempo}")

    def resumen_proyectos_iviables(self):
        resumen_iviables_label.config(text=f"Nombre de la Empresa: {self.nombre_de_empresa}\n"
                                            f"Nombre del Proyecto: {self.nombre_de_proyecto}\n"
                                            f"Presupuesto en Dólares: {self.presupuesto}\n"
                                            f"Tiempo de Duración del Proyecto: {self.tiempo}")

def registrar_proyecto():
    proyecto = Administrador()
    proyecto.informacion_propuesta()
    proyecto.presupuesto_del_proyecto()
    proyecto.ingresar_tipo_de_proyecto()
    proyecto.ingresar_tiempos_de_trabajo()
    proyecto.resumen_proyectos_viables()
    proyecto.resumen_proyectos_iviables()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Administrador - Análisis de Presupuesto de Proyectos")

# Sección para ingresar información del proyecto
empresa_label = tk.Label(root, text="Nombre de la Empresa:")
empresa_label.grid(row=0, column=0, sticky="w")
empresa_entry = tk.Entry(root)
empresa_entry.grid(row=0, column=1)

proyecto_label = tk.Label(root, text="Nombre del Proyecto:")
proyecto_label.grid(row=1, column=0, sticky="w")
proyecto_entry = tk.Entry(root)
proyecto_entry.grid(row=1, column=1)

presupuesto_label = tk.Label(root, text="Presupuesto en Dólares:")
presupuesto_label.grid(row=2, column=0, sticky="w")
presupuesto_entry = tk.Entry(root)
presupuesto_entry.grid(row=2, column=1)

servicios_label = tk.Label(root, text="Servicios:")
servicios_label.grid(row=3, column=0, sticky="w")
servicios_entry = tk.Entry(root)
servicios_entry.grid(row=3, column=1)

tiempo_label = tk.Label(root, text="Tiempo de Duración del Proyecto:")
tiempo_label.grid(row=4, column=0, sticky="w")
tiempo_entry = tk.Entry(root)
tiempo_entry.grid(row=4, column=1)

# Botón para registrar el proyecto
registrar_button = tk.Button(root, text="Registrar Proyecto", command=registrar_proyecto)
registrar_button.grid(row=5, columnspan=2)

# Sección para visualizar proyectos viables e inviables
resumen_viables_label = tk.Label(root, text="Proyectos Viables")
resumen_viables_label.grid(row=6, column=0, columnspan=2)

resumen_iviables_label = tk.Label(root, text="Proyectos Inviables")
resumen_iviables_label.grid(row=7, column=0, columnspan=2)

root.mainloop()

print("Ejersicio 40")



