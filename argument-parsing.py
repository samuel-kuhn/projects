import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
parser.add_argument("--verbosity", "-v", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbosity:
    print("verbosity was set to true")
print(args.square**2)