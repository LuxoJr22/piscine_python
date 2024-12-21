import sys

def main():
    if len(sys.argv) > 3:
        print("AssertionError: more than 2 arguments are provided")
        return
    if len(sys.argv) < 3:
        print("You have to provide a string and an int")
        return
    arg = sys.argv[1]
    args = sys.argv[2]

    try:
        nb = int(args)
    except ValueError:
        print("AssertionError: 2nd argument is not an integer")
        return

    words = arg.split()
    ret = [x for x in words if len(x) >= nb]
    print(ret)


if __name__ == "__main__":
    main()
