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
input = open(args.textfile, "r")
content = input.read()
input.close()
shifted = ""
shift = args.shift



#shift the text
for x in range(len(content)):
    dec = ord(content[x])
    if (dec < 65 or (dec < 97 and dec > 90) or dec > 122):
        shifted += content[x]
    elif (args.mode == "cipher"):
        if (dec > 90): shifted += chr((dec+shift-97)%26+97) #Kleinbuchstabe
        else: shifted += chr((dec+shift-65)%26+65) #Grossbuchtabe
    else:
        if (dec > 90): shifted += chr((dec-shift-97)%26+97) #Kleinbuchstabe
        else: shifted += chr((dec-shift-65)%26+65) #Grossbuchtabe


#output result to a file
output = open(args.output, "w")
output.write(shifted)
output.close()

print("\n" + str(args.mode) + "ed your text! \n")


