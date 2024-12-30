#Factorials
#reminder: factorials are numbers times every number before it
        #so, the factorial of 6 would be 720 (6x5x4x3x2x1)

#We defined a function called factorial that takes a number "n"
#and we are saying, if n == 0 then return 1 otherwise (this is where the recursion comes in)
#return n and times it by our function which is now (n - 1), it will keep doing this until we get a 1

def factorial(n):
    #basecase
    if n == 0:
        return 1
    #recursive case.
    else:
        return n * factorial(n - 1)


#Testing
print(factorial(5))
print(factorial(4))
print(factorial(0))