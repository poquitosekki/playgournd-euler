# Problem 2

#minimum generated terms is 10
def fib(to=10):
    a = 0
    b = 1
    for i in range(to):
        #print(a, b)
        # temp = a + b
        # a = b
        # b = temp
        a, b = b, a + b
        # print(b, " ", end="")
        # Generator object that we can iterate through
        yield b

# Calling the Function
print([i for i in fib()])
