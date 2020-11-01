#Githin Kurian
#1580561

class ItemToPurchase:



    def __init__(x):

        x.item_name = "none"

        x.item_price = 0

        x.item_quantity = 0

  

    def print_item_cost(x):


        print(x.item_name + ' ' + str(x.item_quantity) + ' @ $' + str(x.item_price) + ' = $' + str( x.item_price * x.item_quantity ))

if __name__ == "__main__":


    print("Item 1")


    i1 = ItemToPurchase()

    i2 = ItemToPurchase()

    i1.item_name = input('Enter the item name:\n')

    i1.item_price = int(input('Enter the item price:\n'))

    i1.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nItem 2")


    i2.item_name = input('Enter the item name:\n')

    i2.item_price = int(input('Enter the item price:\n'))

    i2.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nTOTAL COST")


    i1.print_item_cost()

    i2.print_item_cost()


    total = (i1.item_price*i1.item_quantity)+(i2.item_price * i2.item_quantity)


    print("\nTotal: $" + str(total))
