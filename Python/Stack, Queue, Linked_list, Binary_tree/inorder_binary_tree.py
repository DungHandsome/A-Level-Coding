valueList = [20,30,50,40,44,60]
leftIndex = [None,0,3, None,None,None]
rightIndex = [None,2,5,4,None,None]
stack = []

middle_number_position = 1

def checknone(value) -> bool:
    if value == None:
        return True

def insert(value):
    position = middle_number_position
    loop = True
    while loop == True:
        if value > valueList[position]:
            if checknone(rightIndex[position]) == True:
                valueList.append(value)
                leftIndex.append(None)
                rightIndex.append(None)
                rightIndex[position] = len(valueList) - 1
                loop == False
                break
            else:
                position = rightIndex[position]
        elif value < valueList[position]:
            if checknone(leftIndex[position]) == True:
                valueList.append(value)
                leftIndex.append(None)
                rightIndex.append(None)
                leftIndex[position] = len(valueList) - 1
                loop == False
                break
            else:
                position = leftIndex[position]
        else:
            print("An error occur!")

def in_order():
    value = middle_number_position
    if leftIndex[value] != None:
        in_order(leftIndex[value])
    stack.append(value)
    if rightIndex[value] != None:
        in_order(rightIndex[value])

def find(value) -> int:
    position = middle_number_position
    loop = True
    while loop == True:
        if value == valueList[position]:
            loop = False
            return position
        elif value < valueList[position]:
            position = leftIndex[position]
        elif value > valueList[position]:
            position = rightIndex[position]



#print(valueList)
#print(leftIndex)
#print(rightIndex)