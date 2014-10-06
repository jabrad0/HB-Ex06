ratings = open("scores.txt")
restaurants = {}

for line in ratings:
    name, rating = line.split(":")
    
