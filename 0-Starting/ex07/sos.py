import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def main():
	"""Program that takes a string as an argument and encodes it into Morse Code"""
	if len(sys.argv) != 2 or not all(x.isalpha() or x.isspace() for x in sys.argv[1]):
		print("AssertionError: the arguments are bad")
		return
	
	string = sys.argv[1].upper()
	ret = ""
	for i in string:
		if i in MORSE_CODE_DICT:
			ret += MORSE_CODE_DICT[i]
		else:
			ret += '/'
		ret += ' '
	print(ret[:-1])

if __name__ == "__main__":
    main()