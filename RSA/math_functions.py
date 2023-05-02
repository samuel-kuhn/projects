import math
def are_coprime(a, b): #teilerfremd
    return math.gcd(a, b) == 1
def is_natural_number(num):
    return isinstance(num, int) and num > 0
def calc_m(r, E):
    x = 0
    while True:
        a = (x*r+1)/E
        if (is_natural_number(a)): 
            return x
            break
        x += 1
