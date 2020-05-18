def sumSquares(number):
    sum = 0
    for i in range(number):
        sum += (i + 1)**2
    return sum

def squareSum(number):
    sum = 0
    for i in range(number):
        sum += (i + 1)
    return sum**2

def run():
    result = squareSum(100) - sumSquares(100)
    return print(result)

if __name__ == "__main__":
    run()