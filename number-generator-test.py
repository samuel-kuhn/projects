import random
numbers = 5
tests = int(1e+6)
distribution = []

for i in range(numbers):
    distribution.append(0)

for i in range(tests):
    distribution[random.randint(0, numbers-1)] += 1

for i in range(numbers):
    print(str(i+1) + ":  " + str(distribution[i]/tests*100) + "%")