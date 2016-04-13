# program to test out variable scopes
a = 1;

def test1():
  a = 2;

def test2(): # this is a docstring try to modify a
  global a;
  a = 3;
  
test1();
print a; # this will print 1
test2();
print a; # this will print 3