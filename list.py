#list is collection of similar or different types of data items
# list can have duplicate items
# list is mutable, means changeble
# list can store items of various data types
# a list is created by placing items in [] seperated by commans

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Empty list
numbers1 = []
print (numbers[0])

# list with different types of items
items = [1, 2, 3, 'N', 'GO', 3.14159]

# Accessing elements of single-dimentional list . A list where elements are listed one after the other. Each element is alloted a unique index
#negavtive indexing
#Accessing elemens of multi-dimensional list

my_list = [5, 10, 15, 20]
# + Index  0  1    2    3
# - Index  -4 -3  -2   -1

# multi dimensional list is  a list containing another list
my_list2 = [[1, 2, 3], "Neso", [4, 5, 6]]
#index        0         1           2
#subindex    0  1  2    0123    0   1  2
print (my_list2[0][2])
print(my_list2[1])
print(my_list2[1][0])
print(my_list2[2])

# Add elements to the list - append, insert and extend methods
#append method is  is buil in method to add an item at the end of the list
languages = ["c", "C++"]
print(languages)
languages.append("java")
print(languages)
languages.append(["python", "javascript"])
print(languages)

# insert method is build in method to add an item ad a specific postion.
languages.insert(1, "Hari")
print(languages)

# Extend method is build in moethod to add all items of one list in antoher list
languages1 = ["Teleug", "English"]
languages.extend(languages1)
print(languages)



print("firs git change frim demo user")

print("First line from Stuff user")


##############
print("Added to the code to develop branch by Demo user")

##############
print("Added to the code to develop branch by STUFF user")

