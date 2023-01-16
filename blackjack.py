import sys
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

my_hand = []
dealers_hand = []

deal_cards(1)




under_limit = True

while under_limit:
	while True:
		hit = input("Would you like to hit or stand? Type 'y' to hit or 'n' to stand ").lower()
		if deal_again in ["y", "n"]:
			if deal_again == "y":
				hit = True
			else:
				hit = False
			break
		else:
			print("Invalid input - Please enter 'y' or 'n'")

	
	if hit:
		deal_cards(1)
		if over_limit(my_hand):
			print(f"The sum of your cards is {sum(my_hand)}. You lose")
			sys.exit(0)
		elif over_limit(dealers_hand):
			print(f"The dealer busted with the cards {dealers_hand} and a sum of {sum(dealers_hand)}. You win!")
			sys.exit(0)
		elif !


		

	elif !hit:
		under_limit = False

def deal_cards(n):
	for i in range(n):
		my_hand.append(random.choice(cards))
		dealers_hand.append(random.choice(cards))
	print(f"Your hand is: {my_hand} for a sum of {sum(my_hand)}")
	print(f"and the dealer's face up card(s) are {dealers_hand[1:]}")


def over_limit(list0):
	if sum(list0) > 21:
		return True
	return False


def check_for_winner(list0, list1):
	sum0 = sum(list0)
	sum1 = sum(list1)

	if sum0 == sum1:
		print("Draw")
		sys.exit(0)
	elif sum0 > sum1:
		print("You win!")
		sys.exit(0)
	else:
		print("You lose.")
		sys.exit(0)












