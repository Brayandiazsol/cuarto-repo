#numeros primos y enteros
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_primes_in_range(a, b):
    return sum(i for i in range(min(a, b), max(a, b) + 1) if is_prime(i))
a, b = 10, 20
print(f"Suma de primos entre {a} y {b}: {sum_primes_in_range(a, b)}")