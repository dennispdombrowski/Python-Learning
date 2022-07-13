'''Examples of working with lists'''
def main():
    '''Function to get a list of cat names from the user'''
    cat_names = []
    while True:
        print('Enter the name of cat ' + str(len(cat_names) + 1) +
            ' (Or enter nothing to stop.):')
        name = input()
        if name == '':
            break
        cat_names = cat_names + [name] # list concatenation

    print('The cats are: ')
    for name in cat_names:
        print(' ' + name)

main()
