stack = [4, 7, 12, 9, None, None]
basePointer = 0
topPointer = 3

def push(value):
    if topPointer == len(stack) - 1:
        print("The stack is full, you would like to pop first!")
    else:
        stack[topPointer+1] = value
        topPointer += 1

def pop():
    if topPointer < basePointer:
        print("The stack is already empty, you would like to push a value!")
    else:
        stack.remove(topPointer)
        topPointer += 1

