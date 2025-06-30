def linear_search_and_insert(arr, key):
    n = len(arr)
    position = n
    for i in range(n):
        if arr[i] == key:
            print(f"Element {key} found at index {i}.")
            return arr
        elif arr[i] > key:
            position = i
            break
        arr.append(0)  
    for i in range(n, position, -1):
        arr[i] = arr[i - 1]  

    arr[position] = key 
    return arr


sorted_array = [1, 3, 5, 7, 9]
key_to_insert = 6
print(sorted_array)
result = linear_search_and_insert(sorted_array, key_to_insert)
print(key_to_insert)
print("Updated array:",result)
