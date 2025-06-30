def linearSearch(arr, n, x):
    n=len(arr)
    position=n
    for i in range(0, n):
        if (arr[i] == x):
            return i
        elif arr[i] >x:
            position = i
            break
    arr.append(0)  
    for i in range(n, position, -1):
        arr[i] = arr[i - 1]  

    arr[position] = x 
    return arr
arr = [16,5,17,3,6,1]
x = 7
n = len(arr)
result = linearSearch(arr, n, x)
if(result == -1):
    print("Element not found")
        
else:
    print("Element found at index: ",result)
