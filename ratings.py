"""Restaurant rating lister."""


# put your code here
import sys

filename = sys.argv[1]

with open(filename) as file:
	restaurant_ratings = {}

	for line in file:
		restaurant_name, restaurant_rating = line.split(":")
		restaurant_ratings[restaurant_name] = restaurant_rating.rstrip("\n")

	for k, v in sorted(restaurant_ratings.items()):
		print("{} is rated at {}.".format(k, v))
