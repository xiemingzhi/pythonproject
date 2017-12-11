# read from file put into dictionary
f = open('data.txt', 'r');

for line in f:
  print line;
  
# close the file after reading
f.close();