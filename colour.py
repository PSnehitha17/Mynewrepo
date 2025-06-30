def sort_colours(user_input):
    temp=[]
    for colour in user_input:
        while temp and temp[-1]>colour:
             temp.pop()
             temp.append(colour)
             sort_colours(temp)
    return temp
user_input=list(map(int,input("Enter colours:").split()))
print("sorted colours:",sort_colours(user_input))
