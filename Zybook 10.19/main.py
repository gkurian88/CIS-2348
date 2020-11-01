#Githin Kurian
#1580561

class purchase:
   def __init__(self, name='none', price=0, quantity=0, desc='none'):
       self.it_name=name
       self.it_desc=desc
       self.it_pr=price
       self.it_quan=quantity

   def print_it_desc(self):
       print('%s: %s' % (self.it_name, self.it_desc))

      
class cart:
  
   def __init__(self, cust_name = 'none', current_date = 'January 1, 2016', cart_items = []):
       self.cust_name = cust_name
       self.current_date = current_date
       self.cart_items = cart_items  
      

   def add_i(self, itpr):
       self.cart_items.append(itpr)  
      
  
   def remove_i(self, itemName):
      
       tr_item = False
     
       for item in self.cart_items:
           if item.it_name == itemName:
               self.cart_items.remove(item)
               tr_item = True
               break
     
       if not tr_item:          
           print('Item not found in cart. Nothing removed.')
              
           
   def modify_i(self, itpr):  
      
       tmodify_item = False
      
       for i in range(len(self.cart_items)):
          
           if self.cart_items[i].it_name == itpr.it_name:
               tmodify_item = True
               self.cart_items[i].it_quan = itpr.it_quan
               break
      
    
       if not tmodify_item:      
           print('Item not found in the cart. Nothing modified')  

       
   def get_num_items_in_cart(self):
       num_items = 0
       for item in self.cart_items:
           num_items = num_items + item.it_quan
       return num_items
  
  
   def get_cost_of_cart(self):
       total_cost = 0
       cost = 0
       for item in self.cart_items:
           cost = (item.it_quan * item.it_name)
           total_cost += cost
       return total_cost
              
         
   def print_total(self):
       total_cost = self.get_cost_of_cart()
       if (total_cost == 0):
           print('SHOPPING CART IS EMPTY')
       else:
           print('{}\'s Shopping Cart - {}'.format(self.cust_name, self.current_date))
           print('Number of Items: %d\n' %self.get_num_items_in_cart())
           for item in self.cart_items:
               total = item.it_name * item.it_quan
               print('%s %d @ $%d = $%d' % (item.it_name, item.it_quan, item.it_name, total))
              
           print('\nTotal: $%d' %(total_cost))
          
     
   def print_descriptions(self):
       if len(self.cart_items) == 0:
           print('SHOPPING CART IS EMPTY')
       else:  
           print('{}\'s Shopping Cart - {}'.format(self.cust_name, self.current_date))
           print('\nItem Descriptions')
           for item in self.cart_items:
               item.print_it_desc()  
              
       
def print_menu(newCart):
   customer_Cart = newCart
   menu = ('\nMENU\n'
       'a - Add item to cart\n'
       'r - Remove item from cart\n'
       'c - Change item quantity\n'
       "i - Output items' descriptions\n"
       'o - Output shopping cart\n'
       'q - Quit\n')
      
   command = ''
   while(command != 'q'):
       print(menu)
       command = input('Choose an option:\n')
       while(command != 'a' and command != 'o' and command != 'i' and command != 'q' and command != 'r' and command != 'c'):
           command = input('Choose an option:\n')
       if(command == 'a'):
           print("\nADD ITEM TO CART")
           it_name = input('Enter the item name:\n')
           it_desc = input('Enter the item description:\n')
           it_name = int(input('Enter the item price:\n'))
           it_quan = int(input('Enter the item quantity:\n'))
           pr = purchase(it_name, it_name, it_quan, it_desc)
           customer_Cart.add_i(pr)
      
       elif(command == 'o'):
           print('\nOUTPUT SHOPPING CART')
           customer_Cart.print_total()  
       elif(command == 'i'):
           print('\nOUTPUT ITEMS\' DESCRIPTIONS')
           customer_Cart.print_descriptions()
       elif(command == 'r'):
           print('REMOVE ITEM FROM CART')
           itemName = input('Enter name of item to remove:\n')
           customer_Cart.remove_i(itemName)
       elif(command == 'c'):
           print('\nCHANGE ITEM QUANTITY')
           itemName = input('Enter name of item :\n')
           qty = int(input('Enter the new quantity :\n'))
           itpr = purchase(itemName,0,qty)
           customer_Cart.modify_i(itpr)
      
if __name__ == "__main__":
   cust_name = input("Enter customer's name:\n")
   current_date = input("Enter today's date:\n")
   print("\nCustomer name: %s" %cust_name)
   print("Today's date: %s" %current_date)
   newCart = cart(cust_name, current_date)
   print_menu(newCart)  
