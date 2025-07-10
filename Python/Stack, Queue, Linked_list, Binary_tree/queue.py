#Given queue of [63, 51, 66, 47, 10, 22] with:
#- frontPointer = 4 (i.e., queue[4] = 10)
#- rearPointer = 0 (i.e., queue[0] = 63)
#- perform the following operations:
#    - Dequeue
#    - Enqueue 51
#    - Enqueue 66

queue = [63, None, None, None, 10, 22]
frontPointer = 4
rearPointer = 0
currentqueuesize = 3
#(frontPointer == rearPointer + 1 or (frontPointer == 0 and rearPointer == len(queue) - 1)) and queue[rearPointer] == None
def dequeue():
    global frontPointer
    global currentqueuesize
    global initial_value
    if currentqueuesize == 0:
        print("The queue is empty")
    else:
        initial_value = queue[frontPointer]
        currentqueuesize -= 1
        queue[frontPointer] = None
        if frontPointer == len(queue) - 1:
            frontPointer = 0
        else:
            frontPointer += 1
    print(queue)
    print(frontPointer,rearPointer)
    return initial_value
    

def enqueue(value):
    global rearPointer
    global currentqueuesize
    if currentqueuesize == 6:
        print("the queue is full")
    else:
        currentqueuesize += 1
        if rearPointer == len(queue) - 1:
            rearPointer = 0
        else:
            rearPointer += 1
        queue[rearPointer] = value
    print(queue)
    print(frontPointer,rearPointer)


print(queue)
print(frontPointer,rearPointer)

for i in range(0,10):
    print(dequeue()) # print 10 in the first iteration

for i in range(0, 10):
    enqueue(i)

