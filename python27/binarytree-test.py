#Bintrees Development Stopped
#Use sortedcontainers instead: https://pypi.python.org/pypi/sortedcontainers
from bintrees import BinaryTree

#TypeError: 'int' object is not iterable
#tree = BinaryTree([1,None,2,3])
#tree.items([1,null,2,3])
tree = BinaryTree({'jack':'apple', 'jill':'pear', 'giant':'sheep'})

def collect(key, value):
    print('key', key, 'value', value)

#foreach(f, [order]) -> visit all nodes of tree (0 = 'inorder', -1 = 'preorder' or +1 = 'postorder') and call f(k, v) for each node, O(n)
tree.foreach(collect)
print('\n')
print('inorder')
tree.foreach(collect, 0)
print('\n')
print('preorder')
tree.foreach(collect, -1)
print('\n')
print('postorder')
tree.foreach(collect, 1)

