# read from file put into dictionary
f = open('data.txt', 'r');
userProductDict = {};

for line in f:
  linearr = line.split("\t");
  if linearr[0] != "User ID":
    if linearr[0] in userProductDict:
      #print(linearr[0] + " " + linearr[1]);
      #print(userProductDict[linearr[0]]);
      # type(userProductDict[linearr[0]]);
      userProductDict[linearr[0]].add(linearr[1]);
    else:
      userProductDict[linearr[0]] = set([linearr[1]]);

for user, products in userProductDict.items():
  print (user, products);

# close the file after reading
f.close();
