import operator
userProductDict = {};
productsTotal = set();

def readUserProducts():
	# read from file put into dictionary
	f = open('data.txt', 'r');
	for line in f:
		linearr = line.split("\t");
		if linearr[0] != "Shopper ID":
			if linearr[0] in userProductDict:
				userProductDict[linearr[0]].add(linearr[1]);
			else:
				userProductDict[linearr[0]] = set([linearr[1]]);
			# get the set of products
			productsTotal.add(linearr[1]);
	# close the file after reading
	f.close();

def calcJC(s1, s2):
  return len(s1.intersection(s2)) / float(len(s1.union(s2)));

def findHighestJC():
	highest = 0.0;
	highuser1 = "";
	highuser2 = "";
	for user1, products1 in userProductDict.items():
		for user2, products2 in userProductDict.items():
			if user1 != user2:
				if highest < calcJC(products1, products2):
					highest = calcJC(products1, products2);
					highuser1 = user1;
					highuser2 = user2;
	print ("highest=" + str(highest), "user1=" + highuser1, "user2=" + highuser2);

def findRecommendationForUser(user):
	purchasedProducts = userProductDict[user];
	# products to recommend
	torecommendProducts = set();
	productRecommendDict = {};
	for torecommend in productsTotal:
		if torecommend in purchasedProducts:
			torecommend;
		else:
			torecommendProducts.add(torecommend);
	for product in torecommendProducts:
		otherUserProductDict = {};
		for otherUser, otherUserProducts in userProductDict.items():
			if otherUser != user and product in otherUserProducts:
				otherUserProductDict[otherUser] = otherUserProducts;
		totalJC = 0.0;
		for otherUser, otherUserProducts in otherUserProductDict.items():
			totalJC += calcJC(purchasedProducts, otherUserProducts);
		recommendation = totalJC / len(otherUserProductDict);
		productRecommendDict[product] = recommendation;
	for product in sorted(productRecommendDict.items(), key=operator.itemgetter(1), reverse=True):
		print (product);

readUserProducts();
for user, products in userProductDict.items():
  print (user, products);

t1 = set(["3","6","9"]);
t2 = set(["3","5","7","9"]);
print (calcJC(t1, t2));

findHighestJC();
findRecommendationForUser("andrew");
