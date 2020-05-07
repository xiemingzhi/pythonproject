# in python they are called lists
a = [1, 2, 3, 4, 5]

def printArr(arr):
   for x in arr:
     print(x)
	 
printArr(a)

# in python they are called dictionary
d = {'jack':'apple', 'jill':'pear', 'giant':'sheep'}

def printMap(map):
   for i, v in map.items():
     print(i, v)
		 
printMap(d)