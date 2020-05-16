#List is a collection which is ordered and changeable. Allows duplicate members.
# in python they are called lists
a = [1, 2, 3, 4, 5]

def printArr(arr):
   for x in arr:
     print(x)
	 
printArr(a)

#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# in python they are called dictionary
d = {'jack':'apple', 'jill':'pear', 'giant':'sheep'}

def printMap(map):
   for i, v in map.items():
     print(i, v)
		 
printMap(d)

#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#In Python tuples are written with round brackets.
#Tuples are immutable
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Set is a collection which is unordered and unindexed. No duplicate members.
#In Python sets are written with curly brackets.
#you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
thisset.remove("banana")
print(thisset)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print('set union', set3)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print('set intersection', z)
