import sys

def whatis():
    if len(sys.argv) < 2:
        print("AssertionError: need an argument")
        return
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return 
    args = sys.argv[1]
    try: 
        nb = int(args)
        if (nb % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except:
        print("AssertionError: argument is not an integer")

whatis()