def primeNumber(number):
    if number == 1:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def run():
    prime = 0
    primes = []
    j = 1
    while prime <= 10001:
        for i in range(j, j+1):
            if primeNumber(j):
                prime += 1
                primes.append(j)
            j += 1
    print(primes[-1])

if __name__ == "__main__":
    run()