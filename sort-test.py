 # for each element in the array
 #  do for each element in the subarray starting from the back
 #   check if element[j-1] > element[j]
 #    then swap(element[j],element[j-1])
 # worst case O(n2)
def bsort(inputArr):
    for i in range(0, len(inputArr)-1, 1):
        for j in range(len(inputArr)-1, i, -1):
            if inputArr[j - 1] > inputArr[j]:
                swap(inputArr, j - 1, j)
                

def swap(inputArr, i, j):
    tmp = inputArr[i]
    inputArr[i] = inputArr[j]
    inputArr[j] = tmp

a = [3, 2, 1, 1, 2, 3, 4, 5]
bsort(a)
print(a)

