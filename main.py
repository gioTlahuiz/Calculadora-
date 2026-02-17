#escribir un codigo de una calculadora que haga tome 2 numeros y luego los sume
num_1 = int(input("Ingresa el numero: "))
num_2 = int(input("Ingresa el numero: "))

resultado = num_1 + num_2
print(resultado)

def calculadora(num_1,num_2,num_3):
    operacion = input("Ingresa la operacion que deseas hacer: ")
    if  operacion == "suma":
        suma = num_1 + num_2
        print(suma) 
    elif operacion == "resta":
        resta = num_1 - num_2
        print(resta)
    elif operacion == "multiplicacion":
        multiplicacion = num_1 * num_2
        print(multiplicacion)
    elif operacion == "division":
        division = num_1/num_2
        print(division)
    elif operacion == "modulo":
        modulo = num_1 % num_2
        print(modulo)
    elif operacion == "suma2":
        suma_2 = num_1 + num_2 + num_3
        print(suma_2)
    elif operacion == "multiple":
        multiple = num_3 * num_1 + num_2 / num_1
        print(multiple)
    
    
    
calculadora(1,4,3)