def run():
    sum = 0
    tmp = 0
    a = 0
    b = 1
    while b < 4000000:
        tmp = b
        b += a
        a = tmp
        print(b)
        if b%2 == 0:
            sum += b
        
    print(sum)

if __name__ == '__main__':
    run()