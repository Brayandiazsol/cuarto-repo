#numeros enteros
def suma_digitos(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma

numero = 123
print(f"La suma de los dígitos de {numero} es {suma_digitos(numero)}")