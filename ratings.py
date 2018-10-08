"""Restaurant rating lister."""


# put your code here
import sys

filename = sys.argv[1]

with open(filename) as file:
	restaurant_ratings = {}

	for line in file:
		restaurant_name, restaurant_rating = line.split(":")
		restaurant_ratings[restaurant_name] = restaurant_rating.rstrip("\n")

	add_restaurant = input("Would you like to enter a restaurant? [yes/no] ")
	if add_restaurant.lower() == "yes":
		prompt_restaurant_name = input("Enter a restaurant name: ")
		while prompt_restaurant_name == "":
			print("Please enter a valid restaurant name.")
			prompt_restaurant_name = input("Enter a restaurant name: ")

		prompt_restaurant_rating = input("Rate the restaurant from 1 to 5: ")
		while not prompt_restaurant_rating.isdigit() and int(prompt_restaurant_rating) > 5:
			print("Please enter a valid restaurant rating.")
			prompt_restaurant_rating = input("Rate the restaurant from 1 to 5: ")

		restaurant_ratings[prompt_restaurant_name] = prompt_restaurant_rating

	for k, v in sorted(restaurant_ratings.items()):
		print("{} is rated at {}.".format(k, v))
