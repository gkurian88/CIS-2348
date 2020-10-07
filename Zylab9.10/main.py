import csv

x = input()

y = {}

with open(x, 'r') as csvfile:
    cr = csv.reader(csvfile)
    for row in cr:
        for word in row:
            if word not in y.keys():
                y[word] = 1
            else:
                y[word] += 1

for i in y.keys():
    print(i + " " + str(y[i]))   
