def palindrome(number):
    reverseNumber = number[::-1]
    if reverseNumber == number:
        return True
    return False

def bubbleSort(numbers, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] < numbers[j+1]:
                tmp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = tmp

def run():
    print('Programa que calcula el palindromo más grande del producto de 2 números de 3 cifras')
    numbers = []
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            number = i * j
            if palindrome(str(number)):
                numbers.append(number)
    n = len(numbers)
    bubbleSort(numbers, n)
    print(numbers[0])
    
    

if __name__ == "__main__":
    run()