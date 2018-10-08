"""Restaurant rating lister."""


# put your code here
import sys
import random

filename = sys.argv[1]

with open(filename) as file:
	restaurant_ratings = {}

	for line in file:
		restaurant_name, restaurant_rating = line.split(":")
		restaurant_ratings[restaurant_name] = restaurant_rating.rstrip("\n")

	add_restaurant = input("Would you like to enter a restaurant? [yes/no] ")
	
	# do you want to enter a restaurant?
	while add_restaurant.lower() == "yes":
		
		prompt_restaurant_name = input("Enter a restaurant name: ")
		while prompt_restaurant_name == "":
			print("Please enter a valid restaurant name.")
			prompt_restaurant_name = input("Enter a restaurant name: ")

		prompt_restaurant_rating = input("Rate the restaurant from 1 to 5: ")
		while not prompt_restaurant_rating.isdigit() or int(prompt_restaurant_rating) > 5:
			print("Please enter a valid restaurant rating.")
			prompt_restaurant_rating = input("Rate the restaurant from 1 to 5: ")

		restaurant_ratings[prompt_restaurant_name] = prompt_restaurant_rating
		add_restaurant = input("Would you like to enter a restaurant? [yes/no] ")

	# do you want to update a random restaurant rating?
	update_random_restaurant = input("Would you like to update a random restaurant rating? [yes/no] ")

	while update_random_restaurant.lower() == "yes":
		restaurant_keys = list(restaurant_ratings.keys())
		random_restaurant = random.choice(restaurant_keys)
		update_rating = input("What rating would you give {} from 1 to 5 ".format(random_restaurant))
		
		while int(update_rating) > 5 or int(update_rating) < 1 or update_rating == '':
			print("please give a rating between 1 and 5")
			update_rating = input("What rating would you give {} from 1 to 5 ".format(random_restaurant))
		restaurant_ratings[random_restaurant] = update_rating
		update_random_restaurant = input("Would you like to update a random restaurant rating? [yes/no] ")

	# do you want to update a resaturant rating of your choice?
	update_restaurant_user_choice = input("Would you like to update a restaurant rating of your choosing? [yes/no] ")

	while update_restaurant_user_choice == "yes":
		print("Here is a list of all the restaurants:")
		
		for k in restaurant_ratings:
			print(k)
		user_choice = input("Which restaurant would you like to update? ")
		
		while not restaurant_ratings.get(user_choice):
			print("Please enter a valid resaturant name.")
			user_choice = input("Which restaurant would you like to update? ")

		user_rating = input("Give {} a rating from 1 to 5: ".format(user_choice))
		while int(user_rating) > 5 or int(user_rating) < 1 or user_rating == '':
			print("please give a rating between 1 and 5")
			user_rating = input("What rating would you give {} from 1 to 5 ".format(user_choice))

		restaurant_ratings[user_choice] = user_rating
		update_restaurant_user_choice = input("Would you like to update another restaurant rating of your choosing? [yes/no] ")







	for k, v in sorted(restaurant_ratings.items()):
	 	print("{} is rated at {}.".format(k, v))
