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

from collections import deque

class DequeQueue:
    def __init__(self):
        self.queue = deque()  # Initialize an empty deque

    def enqueue(self, item):
        self.queue.append(item)  # Add an item to the end of the deque

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")  # Raise exception if the queue is empty
        return self.queue.popleft()  # Remove and return the item at the front of the deque

    def is_empty(self):
        return len(self.queue) == 0  # Check if the deque is empty

    def size(self):
        return len(self.queue)  # Return the size of the deque


#Test Cases

dq = DequeQueue()

#enqueue
print("Is queue empty?", dq.is_empty())
dq.enqueue(15)
dq.enqueue(30)
dq.enqueue(45)
print("Is queue empty after the enqueue?", dq.is_empty())
print("What is the size of the queue now?", dq.size())


#dequeue
dq.dequeue()
print("The dequeue function has passed, What is the size of the queue now?", dq.size())
print("After the dequeue is the queue empty?", dq.is_empty())

dq.dequeue()
print("What is the size of the queue now?", dq.size())
print("After the second dequeue is the queue empty?", dq.is_empty())

dq.dequeue()
print("What is the size of the queue now?", dq.size())
print("After the third dequeue is the queue empty?", dq.is_empty())

#If the queue is empty, raise an exception
try:
    dq.dequeue()
except IndexError as e:
    print("Exception raised:", e)



#Remember, you don't have to put a value in the dq.dequeue() function because dequeue uses FIFO, meaning it removing 15 implicitly

