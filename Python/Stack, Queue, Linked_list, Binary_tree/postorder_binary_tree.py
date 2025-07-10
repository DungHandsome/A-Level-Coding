valueList = [20,30,50,40,44,60]
leftIndex = [None,0,3, None,None,None]
rightIndex = [None,2,5,4,None,None]
middle_number_position = 1

values_of_postorder = []

def postOrder(value_position):
    if leftIndex[value_position] != None:
        postOrder(leftIndex[value_position])
    if rightIndex[value_position] != None:
        postOrder(rightIndex[value_position])
    values_of_postorder.append(value_position)
    

postOrder(middle_number_position)