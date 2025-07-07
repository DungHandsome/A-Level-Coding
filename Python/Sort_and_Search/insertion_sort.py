def selection_sort(arr):
    for i in range(1, len(arr)):
        n=i
        swap=True
        while swap==True:
            if n==0:
                swap=False
            elif arr[n] < arr[n-1]:
                arr[n],arr[n-1] = arr[n-1],arr[n]
                n -= 1
            else:
                swap=False
    
    return arr

#print(selection_sort([1221,2134,5,2,324,5,2,1,35,667]))