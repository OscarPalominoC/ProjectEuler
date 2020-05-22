''' Tripleta pitágorica. '''
def pithagoricTriplet():
    while True:
        for a in range (1, 1000):
            for b in range (a+1, 1000):
                for c in range (b+1, 1000):
                    if a**2 + b**2 == c**2:
                        print('{}^2 + {}^2 = {}^2'.format(a, b, c))
                        print('{} + {} + {} = {}'.format(a, b, c, a+b+c))
                        if (a + b + c) == 1000:
                            print('{} * {} * {} = {}'.format(a, b, c, a*b*c))
                            return False
        return True

if __name__ == "__main__":
    pithagoricTriplet()