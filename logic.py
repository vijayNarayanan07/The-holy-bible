""" 
Writing a program using linear search using function to find an element
Vijay Narayanan
9-08-2024 
"""
def linear_search(shopping_list, element):
    k = len(shopping_list)
    for x in range(k):
        if element == shopping_list[x]:
            print(element, "found at index number =", x)
            break
    else:
        print(element, "not found")

# The shopping list
shopping_list = []
n = int (input ("enter a number"))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    shopping_list.append(element)


# Take user input
p = int(input("Enter the element: "))

# Call the function
linear_search(shopping_list, p)
