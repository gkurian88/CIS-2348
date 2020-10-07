import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wall_height = int(input('Enter wall height (feet):\n'))

   
width=int(input("Enter wall width (feet):\n"));
area=wall_height * width; 
print("Wall area:",area,"square feet"); 
total=350.0;
need=area/total; 
print("Paint needed: {0:.2f} gallons".format(need));
p=math.ceil(need)
print('Cans needed: {0} can(s)\n'.format(p))
x=input('Choose a color to paint the wall:\n')
c=paint_colors[x.lower()]*p
print('Cost of purchasing',x,'paint: ${0}'.format(c))
