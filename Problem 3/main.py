def primeNumber(number):
    if number == 1:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def run():
    primeFactor = 600851475143
    j = 2
    while True:
        multiple = 1
        for i in range(j-1, j):
            if primeNumber(j):
                if primeFactor % j == 0:
                    primeFactor = primeFactor / j
                    print(j)
                    multiple = multiple * j
            j = j + 1  
        if primeFactor == 1:
            return False
            
            

if __name__ == '__main__':
    run()