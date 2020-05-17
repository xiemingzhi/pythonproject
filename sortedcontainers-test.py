#The bintrees project now recommends using Sorted Containers instead and has stopped development. 
#The API differs significantly but the supported functionality is the same. 
#The Tree object in bintrees is most similar to SortedDict. 
#All of the mapping methods and set methods are available using either SortedDict or SortedKeysView.
from sortedcontainers import SortedDict

sd = SortedDict()

sd.update({'jack':'apple', 'jill':'pear', 'giant':'sheep'})

print('sorteddict', sd)

#Return an iterator over the keys of the sorted dict.
myiter = iter(sd)
for k in myiter:
    print('key', k, 'value', sd.get(k))

