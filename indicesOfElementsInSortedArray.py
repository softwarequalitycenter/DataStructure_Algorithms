def indicesOfElementsInSortedArray (arr, elem):
    indices =[]
    lar = len(arr)
    for i in range(0,lar):
        if  arr[i] == elem :
            indices.append(i)

    for i in indices:
        print (i)

arr = [2,3,4,5,5,6,7,8]
#print (len(arr))
a = indicesOfElementsInSortedArray(arr, 5)


