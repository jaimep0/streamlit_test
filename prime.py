import math

def is_prime(number):
    """Evalua si n es primo."""
    if number <= 1:
        return False
    for i in range(2,int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

def main():

    """tiene toda la lógica principal"""

    for i in range(100):
        if is_prime(i):
            print (i, end=' ')
    print()

if __name__ == '__main__':
    main()
