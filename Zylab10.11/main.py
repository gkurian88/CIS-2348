#Githin Kurian
#1580561

class FoodItem:

    def __init__(self, name="None", fat=0.0, carb=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carb
        self.protein = protein

       
    def get_calories(self, servings):
     
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * servings;
        return calories
       
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

if __name__ == "__main__":
    
    fd1 = FoodItem()
   
    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())
   
    fd2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
      
    servings = float(input())
      
    fd1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings, 
                          fd1.get_calories(servings)))
                           
    print()
                           
    fd2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings, 
                          fd2.get_calories(servings)))
    
