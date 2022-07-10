'''Import and global variables'''
import time
import sys


def zigzag():
    '''Pattern functions'''

    indent = 0
    indent_increasing = True

    try:
        while True: # Main program loop
            print(' ' * indent, end='')
            print("********")
            time.sleep(0.1) # Pause for 1/10 of a second.

            if indent_increasing:
                # Increase the number of spaces.
                indent += 1
                if indent == 20:
                    # Changes direction.
                    indent_increasing = False
            else:
                # Decrease the number of spaces.
                indent -= 1
                if indent == 0:
                    indent_increasing = True
    except KeyboardInterrupt:
        sys.exit()

zigzag()
