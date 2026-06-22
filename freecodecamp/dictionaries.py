dictionary1 = {
    "Mango": "Fruit",
    "Table": "Furniture"
}

dictionary2 = dict(vagonr = "car", corrola = "sedan car")

print(dictionary1)
print(dictionary2)

#How to Access Items from a dictionaries
print(dictionary1["Mango"])
print(dictionary2.get("corrola"))

#But if you only want to list keys in the dictionaries
print(dictionary1.keys())
#If you only want to list values in the dictionaries
print(dictionary1.values())

#To print dicts as tuples
print(dictionary1.items())

#To verify if some value exist
print("guitar" in dictionary1)

#To Add values in a dictionary
dictionary2["civic"] = "Another sedan car"
print(dictionary2)
#or
dictionary2.update({"Fortuner" : "SUV car"})

#To change an item from a dictionary
dictionary2["corrola"] = ["changed"]
print(dictionary2)

#To remove an item from a dictionary
dictionary2.pop("civic")
print(dictionary2)


dictionary1.popitem() #Removes the last inserted item and returns it as a tuple.

#But If you want to delete or clear the whole dictionary
dictionary1.clear()
print(dictionary1)
del(dictionary1)

#To copy a dictionary
dictionary10 = dictionary2 #This will not create a new dictionary, but a reference to the original dictionary. Any changes made to 10 will also affect 1 and vice versa.
dictionary11 = dictionary2.copy() #This will create a shallow copy of the original dictionary. Any changes made to 11 will not affect 1 and vice versa.
dictionary12 = dict(dictionary2) #This will also create a shallow copy of the original dictionary. Any changes made to dictionary


#Sets 
nums = {1, 2, 3, 4, 5, 5, 5} #Sets do not allow duplicate values, So there will be only one 5 in the set
#or
nums2 = set((6, 7, 8, 9, 10))

print(nums)
print(nums2)

nums.add(False)
print(nums)

nums3 = {True, 1, 2, 3, False, 0} #In sets, True is considered as 1 and False is considered as 0, So there will be only one True and one False in the set. and In the output True and false will be displayed before any number.
print(nums3)

#You cannot refer to an element in a set with a index value.

nums.update(nums2) #This will add elements from nums2 to nums. But if there are any duplicate values, they will be ignored.
print(nums)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

nums4 = set1.union(set2) #This will combine both sets and remove any duplicate values

print(nums4)

set1.intersection_update(set2) #This will keep only the elements that are present in both sets
print(set1)

print("Program Successful")