#Githin Kurian
#1580561

''' Type your code here. '''

num_values = input()



list_values = [int(num) for num in num_values.split()

if int(num) >= 0]


list_values.sort()



for value in list_values:

    print(value, end = ' ')
