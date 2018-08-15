shopping_list = ['Bread', 'Butter', 'Ice Cream']

# str() function cast the expected integer retrieved from the .index method to a string
print(shopping_list[2] + " is at index value " + str(shopping_list.index(shopping_list[2])))

# shopping_list[i] where i is the index number and shopping_list is the name of the list
print(shopping_list[1] + " is at index value " + str(shopping_list.index(shopping_list[1])))

# shopping_list.index(argument) retrieves the index number or int that is requested. It could also be used to retrieve the exact value, such as shopping.list('Ice Cream') which would return the index value 2
print(shopping_list[0] + " is at index value " + str(shopping_list.index(shopping_list[0])))