def LinearSearch(arr):
    item = int(input('Input the item to be found'))
    found = False
    for i in range(len(arr)):
        if arr[i] == item:
            found =True
            break

    if found:
        print('Item is found in ', i)
    else:
        print("Item is not found")

#LinearSearch([1,2,3,4,5,6,7,8,9,10])