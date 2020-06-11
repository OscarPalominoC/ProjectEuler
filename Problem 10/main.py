import math
def isPrime(number):
    half = math.ceil(number/2) + 1 
    """ Esta es la optimización, si llego a la mitad + 1 del número en cuestión, el resultado va a ser 2, suponiendo que sea divisible, si no es divisible, el resultado de la división va a ser 1.x, y eso, ya lo podría calificar como número primo. """
    if number == 1:
        return False
    for i in range (2, half):
        if number % i == 0:
            return False
    return True

def run():
    sum = 0
    for i in range (1, 2000000):
        if isPrime(i):
            print(i)
            sum += i
    print(sum)

if __name__ == "__main__":
    run()