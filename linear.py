list=[]
n=int(input("Enter the size of array"))
for i in range(n):
    numbers=int(input("Enter the arr %d element:".format(n)))
    list.append(numbers)
x=int(input("Search element"))
def rec_linear(arr,l,r,x):
    if r<l:
        return -1
    if arr[l]==x:
        return l
    if arr[r]==x:
        return r
return rec_linear(arr,l+1,r-1,x)
res=rec_linear(list,0,len(list)-1,x)
if res!=-1:
    print('{}was found at index{}'.format(x,res))
else:
    print('{}was not found'.format(x))

    
