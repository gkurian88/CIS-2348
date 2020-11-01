#Githin Kurian
#1580561

''' Type your code here. '''
x = input()

x = x.split(" ")

y = {}

for i in x:
    if i in y:
        y[i] = y[i] + 1 
    else:
        y[i] = 1

for i in x:
    print(i, y[i])
