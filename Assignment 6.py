#Fibonacci Number: a sequence in which each number is the sum of the two numbers that precede it

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#Test Cases

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(20))


