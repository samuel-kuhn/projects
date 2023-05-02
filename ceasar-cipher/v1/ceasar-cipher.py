print("\nThis is a simple tool to cipher/decipher messages with the ceasar cipher method \n \n")
#version 1.0

#parsed arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("mode", help="choose wether you want to cipher or decipher a text (modes: %(choices)s)", choices=['cipher', 'decipher'])
parser.add_argument("shift", help="amount of alphabet shifts", type=int)
parser.add_argument("textfile", help="file with the text to cipher/decipher")
parser.add_argument("-o", "--output", action="store", help="file where the output should be saved (default: %(default)s)", default="output.txt")
args = parser.parse_args()


#read the whole file at once
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
input = open(args.textfile, "r")
content = input.read()
input.close()
shifted = ""
shift = args.shift



#shift the text
for x in range(len(content)):
    if content[x] == " ":
        shifted += " "
    elif content[x] == "\n":
        shifted += "\n"
    if (args.mode == "cipher"):
        for i in range(26):
            if alphabet[i] == content[x]:
                shifted += str(alphabet[(i+shift) % 26])
    elif (args.mode == "decipher"):
        for i in range(26):
            if alphabet[i] == content[x]:
                shifted += str(alphabet[(i-shift) % 26])


#output result to a file
output = open(args.output, "w")
output.write(shifted)
output.close()

print("\n" + str(args.mode) + "ed your text! \n")


