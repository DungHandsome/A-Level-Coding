def bubble_sort(arr):
    for i in range(len(arr)):
        n=0
        for n in range(len(arr)-1-i):
            if arr[n]>arr[n+1]:
                arr[n], arr[n+1] = arr[n+1], arr[n]
    return(arr)

#print(bubble_sort([1221,2134,5,2,324,5,2,1,35,667]))