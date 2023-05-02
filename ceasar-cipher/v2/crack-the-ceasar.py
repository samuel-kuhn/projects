print("\nThis is a simple tool to crack a message encrypted with the ceasar cipher method. \n \n")
#version 1.0

#parsed arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("textfile", help="file with the text to cipher/decipher")
parser.add_argument("-o", "--output", action="store", help="file where the output should be saved (default: %(default)s)", default="output.txt")
args = parser.parse_args()


#read the whole file at once
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
input = open(args.textfile, "r")
content = input.read()
input.close()

#try every number
output = open(args.output, "w")
output.write("")
output = open(args.output, "a")

for shift in range(26):
    output.write("Shifts: " + str(shift) + "\n \n")
    for x in range(len(content)):
        dec = ord(content[x])
        if (dec < 65 or (dec < 97 and dec > 90) or dec > 122):
            output.write(content[x])
        elif (dec > 90): output.write(chr((dec-shift-97)%26+97)) #Kleinbuchstabe
        else: output.write(chr((dec-shift-65)%26+65)) #Grossbuchtabe

    output.write("\n")


#output result to a file

output.close()

print("Tried every number of shifts. Check you output file!")



