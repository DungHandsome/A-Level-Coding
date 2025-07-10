#valueList = [20,30,50,40,44,60]
#leftIndex = [None,0,3, None,None,None]
#rightIndex = [None,2,5,4,None,None]

valueList = [20,15,40,12,16,35,50,17]
leftIndex = [1,3,5,None,None,None,None,None]
rightIndex = [2,4,6,None,7,None,None,None]
stack = []

middle_number_position = 0

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

def in_order(value):
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

in_order(middle_number_position)
print(stack)
for i in range(0, len(stack)):
    print(valueList[stack[i]])

#print(valueList)
#print(leftIndex)
#print(rightIndex)