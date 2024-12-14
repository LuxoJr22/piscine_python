import sys


def main():
    """Program which takes a single string argument and displays the sums of its upper-case characters, lower-case characters, punctuation characters, digits and spaces.""""

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    if len(sys.argv) < 2:
        print("You have to provide a string")
        return
    arg = sys.argv[1]
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    print(arg)

    print(f"The text contains {len(arg)} characters:")
    print(f"{sum(1 for upper in arg if upper.isupper())} upper letters")
    print(f"{sum(1 for lower in arg if lower.islower())} lower letters")
    print(f"{sum(1 for punc in arg if punc in punctuation)} punctuation mark")
    print(f"{sum(1 for space in arg if space.isspace())} spaces")

    print(f"{sum(1 for digit in arg if digit.isdigit())} digit")


if __name__ == "__main__":
    main()
