valueList = [20,30,50,40,44,60]
leftIndex = [None,0,3, None,None,None]
rightIndex = [None,2,5,4,None,None]
middle_number_position = 1

values_of_preorder = []

def preOrder(position_value):
    values_of_preorder.append(position_value)
    if leftIndex[position_value] != None:
        preOrder(leftIndex[position_value])
    if rightIndex[position_value] != None:
        preOrder(rightIndex[position_value])

preOrder(middle_number_position)
