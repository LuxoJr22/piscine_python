import sys

def main():
    """Program that output a list of words from S that have a length greater than N. (with S and N passed as arguments)"""
    if len(sys.argv) != 3 or type(sys.argv[1]) != str:
        print("AssertionError: the arguments are bad")
        return
    arg = sys.argv[1]
    args = sys.argv[2]

    try:
        nb = int(args)
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    words = arg.split()
    is_len = lambda a : len(a) > nb
    ret = [x for x in words if is_len(x)]
    print(ret)


if __name__ == "__main__":
    main()
