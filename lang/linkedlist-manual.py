class LinkedList:
    def __init__(self):
        self.node = None
        self.count = 0

    def add(self, data):
        if self.node is None:
            self.node = Node(data)
            self.node.setNext(None)
            self.count += 1
        else:
            oldnode = self.node 
            self.node = Node(data)
            self.node.setNext(oldnode)
            self.count += 1

    # creating a iterator in python
    # An iterable is any object in Python which has an __iter__ or a __getitem__ method defined which returns an iterator or can take indexes
    def __iter__(self):
        self.nextIndex = self.node
        self.totalCount = self.count
        self.iterationCount = 0
        return self

    # An iterator is any object in Python which has a next (Python2) or __next__ method defined.
    def __next__(self):
        if (self.iterationCount < self.totalCount):
            result = self.nextIndex
            self.nextIndex = self.nextIndex.next
            self.iterationCount += 1
            return result
        else: 
            raise StopIteration


class Node:
    def __init__(self, data):
        self.data = data

    def getData(self):
        return self.data

    def next(self):
        return self.next

    def setNext(self, next):
        self.next = next

linkedList = LinkedList() 
linkedList.add('1')
linkedList.add('2')
linkedList.add('3')
linkedList.add('4')

llIter = iter(linkedList)
for i in llIter:
    print(i.getData())

