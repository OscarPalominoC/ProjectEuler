def loop(number):
    for i in range(20):
        if number % (i + 1) != 0:
            return False
    return True

def run():
    j = 11
    while True:
        for i in range(j, j+2):
            if loop(j):
                print(j)
                return False
            j = j + 1
            

if __name__ == "__main__":
    run()