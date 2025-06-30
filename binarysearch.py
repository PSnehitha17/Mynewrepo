def binary_search(list,low,high,elem):
    if(low<=high):
        mid=(low+high)//2
        if list[mid]==elem:
            return mid
        elif(list[mid]>elem):
            return binary_search(list,low,mid-1,elem)
        else:
            return binary_search(list,mid+1,high,elem)
    else:
        return -1
list=[1,3,6,9]
elem_ser=3
my_result=binary_search(list,0,len(list)-1,elem_ser)
if my_result==-1:
    print("not found")
else:
    print("Element found at index:",my_result)
