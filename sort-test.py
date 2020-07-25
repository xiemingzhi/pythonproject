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
print('bubblesort',a)

# start from second element i=1 to length of array
# set temp variable to hold current element
# if the previous value is bigger > than current element then set array at current element to next element
# move smaller elements down at the end set the position for the current element
# psuedo code
# for i=1 to len(arr)
#  curr = arr[i], j=i
#  while (j > 0 and arr[j-1] > curr)
#   arr[j] = arr[j-1]
#   j--
#  arr[j] = curr
# worst case O(n2)
def isort(inputArr):
    for i in range(1, len(inputArr) - 1, 1):
        curr = inputArr[i]
        j = i
        while j > 0 and inputArr[j - 1] > curr:
            inputArr[j] = inputArr[j - 1]
            j -= 1
        inputArr[j] = curr

a = [3, 2, 1, 1, 2, 3, 4, 5]
isort(a)
print('insertsort',a)
