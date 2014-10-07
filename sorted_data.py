ratings = open("scores.txt")
restaurants = {}

for line in ratings:
    name, rating = line.rstrip().split(":")
    restaurants[name] = rating

rest_list = restaurants.keys()
rest_list.sort()

for item in rest_list:
    print "Restaurant %s is rated at %s" % (item, restaurants[item])
