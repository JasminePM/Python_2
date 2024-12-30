#ASSIGNMENT TASK:
#Task: Implement a singly linked list class with the following methods:
#append(data): Adds a new node with the specified data at the end of the list.
#prepend(data): Adds a new node with the specified data at the beginning of the list.
#print_list(): Prints all the elements in the list.



# Step 1: Define the Node Class

# A class is a placeholder for what we're trying to do
# __init__ : function to reference itself
class Node:
    def __init__(self, data):
        self.data = data  # Stores data
        self.next = None  # Pointer


# Step 2: Define the Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None  # The head will usually have no data

    def append(self, data):
        new_node = Node(data)  # This is how we initiate the call for a new node by creating a variable

        if not self.head:  # if the list is empty make this new node the head of the list
            self.head = new_node
        else:  # It will keep looping across all the data inside the list and once it reaches the end, it will append the new value at the end
            current = self.head
            while current.next:
                current = current.next
            # Set the last node pointer to the new node
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        # make the new node the head, and link it to the current head
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

Linked_list = LinkedList()

Linked_list.append(20)
Linked_list.append(30)
Linked_list.prepend(5)

Linked_list.print_list()