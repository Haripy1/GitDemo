#Change list of itmes

list = ["Hari", "Prasu", "Bhavik", "Chandu"]
print (list)

list[0] = "Riha"
print (list)

list1 = ["Hari", "Prasu", "Bhavik", "Chandu", "XY", "Z"]
list1[4:6] = ["Karthi", "Praha"]
print(list1)

list1.insert(6, "siva")
print(list1)

# Remove methods - remove() , pop(), del keyworkd, clear()
list1.remove("siva")
print(list1)

#pop method used to remove based on index
list1.pop(5)
print(list1)
# remove using the del keyword with specified index, also can remove teh complete list
#del list1
del list1[4]
print(list1)

# emppty the list that means, dont delete teh list and clear the data
list1.clear()
print(list1)

# list comprehension - provides a shorter syntax while creating a new list from the existing list
# syntax: list = [expression for item in iterable if condition = =True]
names = ['john', 'james', 'emmy', 'michel', 'jimmy']
j_names = [name for name in names if 'j' in name]
names_copy = [name for name in names]
# for name in names:
#     if 'j' in name:
#         j_names.append(name)

print(j_names)
print("added by prasnahti")
print(names_copy)
