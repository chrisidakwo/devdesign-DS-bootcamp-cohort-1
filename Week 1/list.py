# Lists are ordered, mutable (can be changed) collections
# Tuples are ordered, immutable (cannot be changed) collections

namesList = ["Chris", "Mike", "Jane", "Blessing", "Peter", "Joe", "Sarah", "Daniel"]
print(namesList)

namesTuple = ("Chris", "Mike", "Jane", "Blessing", "Peter", "Joe", "Sarah", "Daniel")
print(namesTuple)

# Retrieve the total number of items in a list and a tuple
print(len(namesList))
print(len(namesTuple))

# Concatenation (Merging)
studentReg1 = ["YURRI898", "HIFR7973", "BKDB90854"]
studentReg2 = ["LEIRPEI898", "IORPW7973", "MKLSW90854"]

# You concatenate (merge) lists using the '+' symbol
# You can also merge tuples
mergedList = studentReg1 + studentReg2
print(mergedList)

# Accessing items in a list using their index position
print(mergedList[0]) # Index positions start from a count of zero(0), and would return the first item in the list
print(mergedList[1]) # Would return the 2nd item in the list
print(mergedList[2]) # Would return the 3rd item in the list
print(mergedList[3]) # Would return the 4th item in the list

# You can access the items in a list/tuple using negative indexing
print(mergedList[-1]) # Would return the last item in the list
print(mergedList[-2]) # Would return the second to the last item in the list

# Slicing  (to get a chunk/part of a list)
print(mergedList[1:]) # Returns all list items from index position 1
print(mergedList[2:4]) # Returns all list items from index position 2 to 3
print(mergedList[:3]) # Returns all list items from index position 0 to 3 

dates1Tuple = ("20/02/2025", "15/08/2024", "31/01/2025")
dates2Tuple = ("17/04/2023", "12/07/2022", "13/09/2021")

mergedTuple = dates1Tuple + dates2Tuple
print(mergedTuple)
print(mergedTuple[1:])
print(mergedTuple[2:4])

# Add to a list/tuple
mergedList.append("REGON-8053853")
mergedList.append("DATA-SCIENCE-8053853")
mergedList.append("DEV-DESIGN-8053853")
print(mergedList)

# Update a value in a list

mergedList[6] = "ABC"
mergedList[7] = "XYZ"
mergedList[8] = "YOZ"
mergedList.append(90) # Cannot define an index position

print(mergedList)

mergedList.insert(6, "EXAMPLE")
print(mergedList)

# Checking/asserting membership
checkExist = 90 in mergedList
print(checkExist)