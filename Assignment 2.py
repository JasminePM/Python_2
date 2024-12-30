# Step 1: Define the Node Class
class Node:
    def __init__(self, data):
        self.data = data  # Stores data
        self.next = None  # Pointer to the next node

# Step 2: Define the Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None  # The head will usually have no data

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # If the list is empty, make this new node the head of the list
            self.head = new_node
        else:  # Traverse to the end of the list and append the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Update the head to the new node

    def remove(self, data):
        # Remove the node with the specified data
        if not self.head:  # If the list is empty
            print("List is empty. Nothing to remove.")
            return

        if self.head.data == data:  # If the head needs to be removed
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:  # Traverse the list
            current = current.next

        if current.next:  # If the node was found
            current.next = current.next.next
        else:
            print(f"Node with data {data} not found.")

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Example Usage
Linked_list = LinkedList()
Linked_list.append(20)
Linked_list.append(30)
Linked_list.prepend(5)
Linked_list.print_list()  # Output: 5 -> 20 -> 30 -> None

Linked_list.remove(20)
Linked_list.print_list()  # Output: 5 -> 30 -> None

Linked_list.remove(50)  # Output: Node with data 50 not found.

