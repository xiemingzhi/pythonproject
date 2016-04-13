# file io example
f = open('README.md', 'r');

for line in f:
  print line;
  
# close the file after reading
f.close();