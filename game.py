from random import choice, randrange
from datetime import datetime

# Operadores posibles
# operators = ["+", "-", "/", "*"]
operators = ["/"]



# Cantidad de cuentas a resolver
times = 5

# Contador de aciertos y errores 
good = 0
bad = 0

# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.

init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):

# Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)


# Obtenemos el resultado de la operación asignada
    match operator:
        case "+":
            x = number_1 + number_2
        case "-":
            x = number_1 - number_2
        case "/":
            while float(number_2) == 0.0:
                number_2 = randrange(10)
            
            x = float(number_1 / number_2)
            x = ("{:.2f}".format(x)) # Se redondea la respuesta, restringiendo el uso máximo de 2 decimales.
        case "*":
            x = number_1 * number_2


# Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")

# Le pedimos al usuario el resultado
    result = float(input("resultado: "))
        
# Comparamos el resultado de la operación con el valor ingresado por el usuario.
# Se imprime la respuesta en pantalla.

    if result == float(x):
        print ("BIEN!!!")
        good = good + 1
    else:
        print (f"Mal, la respuesta correcta era: {x}")
        bad = bad + 1

        
        
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()

# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time

# Mostramos ese tiempo en segundos y la cantidad de aciertos/errores obtenidos por el usuario.
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n Tuviste {good} aciertos y {bad} errores")