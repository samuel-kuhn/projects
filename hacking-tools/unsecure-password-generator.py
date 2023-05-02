print("\nThis is a simple tool to generate passwords based of a few keywords. \n")
import itertools
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", action="store", help="input file with words (one on each line)")
parser.add_argument("-l", "--long", help="make the list long", action="store_true")
parser.add_argument("-ll", "--longerthanlong", help="make the list really long", action="store_true")
parser.add_argument("-o", "--output", action="store", help="output file (default: %(default)s)", default="output.txt")
args = parser.parse_args()

#generate a list of possible passwords based of a few words
words = ["wordpress", "WordPress", "administrator", "test", "username", "patrick", "john"]
comb_char = "-_+/#%&@"
spec_char = "@%+\/'!#$?(){}[]~-_."
counter = 0


numbs = "0123456789"
o = open(args.output, "w")

#normal
for i in words:
    o.write(i+"\n")  #input
    o.write(i[0].upper()+i[1:] + "\n") #first uppercase
    o.write(i[:-1] + i[-1:].upper() + "\n") #last uppercase
    o.write(i.upper() + "\n") #all uppercase
    counter += 4

#backwards
for i in words:
    o.write(i[::-1]+"\n") #input
    o.write(i[-1:].upper() + i[-2::-1] + "\n") #first uppercase
    o.write(i[:0:-1] + i[0].upper() + "\n") #last uppercase
    o.write(i[::-1].upper() + "\n") #all uppercase
    counter += 4

#capseled
for i in words:
    o.write("\"" + i + "\"" + "\n")
    o.write("(" + i + ")" + "\n")
    o.write("[" + i + "]" + "\n")
    o.write("{" + i + "}" + "\n")
    o.write("<" + i + ">" + "\n")
    counter += 5


#with 1,2 or 3 special characters at start
for i in words:
    for j in spec_char: #1 char
        o.write(j + i + "\n")
        o.write(j + i.upper() +"\n")
        counter += 2
        if args.long or args.longerthanlong:
            for k in spec_char: #2 chars
                o.write( j + k + i + "\n")
                o.write( j + k + i.upper() + "\n")
                counter += 2
                if args.longerthanlong:
                    for l in spec_char: #3 chars
                        o.write(j + k + l + i + "\n")
                        o.write(j + k + l + i.upper() + "\n")
                        counter += 2

#other rules
for i in words:
    o.write("#1" + i + "\n")
    counter += 1


#Result:
print("Generated " + str(counter) + " passwords")
print("Output file: " + str(args.output))

