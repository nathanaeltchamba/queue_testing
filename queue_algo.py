

class Node:

    def __init__(self, value, node = None):
        self.value = value
        self.next_node = node

    def get_value(self):
        return self.get_value

    def set_value(self, new_value):
        new_value = input("What food item would you like to enter?: ")
        self.value = new_value


    def get_next_node(self):
        return self.get_next_node

    def set_next_node(self, node):
        self.next_node = node

    def __repr__(self):
        return f'<Node: {self.value}'

class Queue:
    def __init__(self, root=None):
        self.root = root
        self.size = 0
        self.queue = []

    def add_to_queue(self, food):
        new_node = Node(food, self.root)
        self.root = new_node
        self.size += 1

    def remove_from_queue(self, food):

        # ~ What needs to happen ~
        # We need to remove the node at the 0 index of the list because that is the first node that was placed in the list

        current_node = self.root

        prev_node = None

        while current_node:
            if current_node.get_value() == food:
                if prev_node:
                    prev_node.set_next_node(current_node())
                else:
                    self.root = current_node.next_node()
                self.size -= 1
                return 'Node Removed'
            else:
                prev_node = current_node
                current_node = current_node.get_next_node()
        return 'Node not found'
    
    def find_in_queue(self, food):
        current_node = self.root
        prev_node = None

        while current_node:
            if current_node.get_value() == food:
                return True
            else:
                current_node = current_node.next_node()
        return None

    def get_root(self):
        return self.root

    def get_size(self):
        return self.size



# que = Queue()

# que.add_to_queue('mushrooms')
# que.add_to_queue('potatoes')
# que.remove_from_queue()
# print(que.get_size())