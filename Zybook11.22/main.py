#Githin Kurian
#1580561

''' Type your code here. '''
x = input()

x = x.split(" ")

d = {}

for each in x:
    if each in d:
        d[each] = d[each] + 1 
    else:
        d[each] = 1

for each in x:
    print(each, d[each])
