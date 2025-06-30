def sort_colours(user_input):
    return sorted(user_input)
user_input=list(map(int, input("Enter colours(0-red,1-white,2-blue):").split()))
print("sorted colours:",sort_colours(user_input))
