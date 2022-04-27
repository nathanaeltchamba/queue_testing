# Queue for ordering food

def food_order():

    food = []

    print(" Taking orders now... \n")
    print(" Add your order to the queue by entering in your food selection. \n")
    print(" Please enter in ONE item at a time. When you're done, press enter/return.\n")

    while True:

        # Placing Order

        order = input(" Cart Options: 'V' to view order, 'R' to remove from order, 'Q' to quit order: ").lower()
            
    
        # Order Actions

        if order == 'v':
            print(food)
            if len(food) == 0:
                print("Your cart is empty.")

        elif order == 'r':
            removed_food_item = food.pop(0)
            print("Removing: " + removed_food_item)

        elif order == 'q':
            break

        else:
            food.append(order)

        # (test if length is greater than one word)

        if len(order.split()) > 1:
            print("Only provide one item")
            food.pop() == len(order.split()) > 1

        else:
            continue
            

food_order()




