'''Collatz Sequence'''
def collatz(number):
    '''Checks is number is even or odd'''
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

try:
    n = input("Give me a number: ")
    while n != 1:
        n = collatz(int(n))
except ValueError:
    print('Not a valid number!')
