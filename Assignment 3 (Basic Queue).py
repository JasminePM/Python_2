#ASSIGNMENT TASK:
#Implement a class Queue with the following methods:
#enqueue(item): Adds an item to the end of the queue.
#is_empty(): Returns True if the queue is empty, False otherwise.
#size(): Returns the number of items in the queue.
#Write a few test cases to demonstrate the functionality of the queue.



#Defining an empty list
class Queue:
    def __init__(self):
        self.queue = []

#Function to Add an item to the list
    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

#Test Cases

#Storing the class queue inside the queue variable
queue = Queue()

print("Is the queue empty?", queue.is_empty())

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Size of the queue:", queue.size())
print("Dequeue item: ", queue.dequeue())

