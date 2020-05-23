def isPrime(number):
    if number == 1:
        return False
    for i in range (2, number):
        if number % i == 0:
            return False
    return True

def run():
    sum = 0
    for i in range (1, 2000000):
        if (i%10000 == 0):
            print(i)
        if isPrime(i):
            sum += i
    print(sum)

if __name__ == "__main__":
    run()