lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))

# FIXME (1): Finish reading other items into variables, then output the three ingredients
   
# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients

# FIXME (3): Convert and output the ingredients from (2) to gallons
   
cups_water = float(input('Enter amount of water (in cups):\n'))
cups_agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
cups_serving = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields %.2f servings' %(cups_serving))
print('%.2f cup(s) lemon juice' %(lemon_juice_cups))
print('%.2f cup(s) water'%(cups_water))
print('%.2f cup(s) agave nectar'%(cups_agave_nectar))

cups_serving_needed = float(input('\nHow many servings would you like to make?\n'))

lemon_juice_for_one = lemon_juice_cups/cups_serving
water_for_one= cups_water/cups_serving
agave_nectar_for_one = cups_agave_nectar/cups_serving

cups_lemon_juice_needed = lemon_juice_for_one*cups_serving_needed
cups_water_needed = water_for_one*cups_serving_needed
cups_agave_nectar_needed = agave_nectar_for_one*cups_serving_needed

print('\nLemonade ingredients - yields %.2f servings' %(cups_serving_needed))
print('%.2f cup(s) lemon juice' %(cups_lemon_juice_needed))
print('%.2f cup(s) water'%(cups_water_needed))
print('%.2f cup(s) agave nectar'%(cups_agave_nectar_needed))

gallons_lemon_juice = cups_lemon_juice_needed/16
gallons_water = cups_water_needed/16
gallons_agave_nectar = cups_agave_nectar_needed/16

print('\nLemonade ingredients - yields %.2f servings' %(cups_serving_needed))
print('%.2f gallon(s) lemon juice' %(gallons_lemon_juice))
print('%.2f gallon(s) water'%(gallons_water))
print('%.2f gallon(s) agave nectar'%(gallons_agave_nectar))
