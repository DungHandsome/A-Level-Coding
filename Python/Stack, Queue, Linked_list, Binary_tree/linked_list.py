myList = [5,12,8, None, None, None]
myPointers = [1,2,-1, None, None, None]

startPointer = 0 #list starts at index 0
heapStartPointer = 3 #index 3 is the first free node

def insertion_between(insert_var, var1, var2, heapStartPointer):
    for i in range(len(myList)):
        if myList[i] == var1:
            first_index = myPointers[i]
            first_index_index = i
        if myList[i] == var2:
            second_index = myPointers[i]
            second_index_index = i
    
    if second_index > first_index:
        myList[heapStartPointer] = insert_var
        myPointers[heapStartPointer] = second_index_index
        myPointers[first_index_index] = heapStartPointer
    else:
        myList[heapStartPointer] = insert_var
        myPointers[heapStartPointer] = first_index_index
        myPointers[second_index_index] = heapStartPointer

    heapStartPointer += 1
def delete(deleted_var, heapStartPointer):
    for a in range(len(myList)):
        if myList[a] == deleted_var:
            position = a
            pointer_var = myPointers[a]
            break

    for n in range(len(myPointers)):
        if myPointers[n] == position:
            myPointers[n] = pointer_var
            break
    if heapStartPointer == position:
        heapStartPointer -= 1
    myList[a] = None
    myPointers[a] = None
    


print(myList)
print(myPointers)

insertion_between(10,5,12, heapStartPointer)
delete(8, heapStartPointer)

print(myList)
print(myPointers)