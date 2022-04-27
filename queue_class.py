

class Queue:
    def __init__(self, order):
        self.food = []
        self.order = order

    def add_item():
        pass

    def remove_item():
        pass


    def run(self):

        print(" Taking orders now... \n")
        print(" Add your order to the queue by entering in your food selection. \n")
        print(" Please enter in ONE item at a time. When you're done, press enter/return.\n")

        while True:

            # Placing Order

            self.order = input(" Cart Options: 'V' to view order, 'R' to remove from order, 'Q' to quit order: ").lower()

            # Order Actions

            if self.order == 'v':
                print(self.food)
                if len(self.food) == 0:
                    print("Your cart is empty.")

            elif self.order == 'r':
                removed_food_item = self.food.pop(0)
                print("Removing: " + removed_food_item)
               
            elif self.order == 'q':
                break

            else:
                self.food.append(self.order)

            # (run a test to see if the length is greater than one word)

            if len(self.order.split()) > 1:
                print("Invalid Entry: Enter ONE item at a time")
                self.food.pop() == len(self.order.split()) > 1

            else: 
                continue

food_order = Queue(order=None)
food_order.run()


