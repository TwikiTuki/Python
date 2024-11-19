from sys import argv

morse  = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',  'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
rev_morse = {item: key for key, item in morse.items()}
rev_morse['/'] = ' '

def encrypt():
	arguments = " ".join(argv[1:])
	print_str = ""
	for char in arguments:
		if (char == ' '):
			print_str += ' / '
		elif (not char.isalnum()):
			print(f"Error invalid character {char}")
			exit()
		else:
			print_str += morse[char.upper()] + ' '
	print(print_str)

def decrypt():
	arguments = " ".join(argv[2:])
	arguments = arguments.split(' ')
	print_str = ""
	for mors in arguments:
		if mors == "":
			continue
		if (mors not in rev_morse):
			print(f"Error invalid character {mors}")
			exit()
		char = rev_morse[mors]	
		print_str += char
	print(print_str)

if (len(argv) < 2):
    exit()
if (argv[1] == '-d'):
	decrypt()
else:
	encrypt();
