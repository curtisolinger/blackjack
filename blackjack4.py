import sys
import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def main():
	print(logo)
	my_hand = []
	dealers_hand = []

	deal_cards(my_hand, 2)
	deal_cards(dealers_hand, 2)
	print_hands(list0 = my_hand, list1 = dealers_hand)
	
	my_deal = True
	while my_deal:
		while True:
			response = input("Would you like another card? Type 'y' to hit or 'n' to stand ").lower()
			if response in ["y", "n"]:
				break
			else:
				print("Invalid input - Please enter 'y' or 'n'")

		if response == 'y':
			deal_cards(my_hand, 1)
			print(f"Your hand is {my_hand} for a sum of {sum(my_hand)}")
			my_deal = not bust(my_hand)
		else:
			

			my_deal = False
			dealer_deal = True
			while dealer_deal:
				deal_cards(dealers_hand, 1)
				print(f"The dealer has {dealers_hand} for a sum of {sum(dealers_hand)}")
				if sum(dealers_hand) > 21:
					print("The dealer busted. You win!")
					dealer_deal = False
				else:
					if sum(dealers_hand) > 16:
						if sum(my_hand) > sum(dealers_hand):
							print("You win!")
							dealer_deal = False
						else:
							if sum(my_hand) == sum(dealers_hand):
								print("Draw")
								dealer_deal = False
							else:
								print("You lose")
								dealer_deal = False

	while True:
		response = input("Would you like to play again? Type 'y' for yes and 'n' for no. ")
		if response in ["y", "n"]:
				break
		else:
			print("Invalid input - Please enter 'y' or 'n'")

	if response == 'y':
		os.system('clear')
		main()
	else:
		print("Goodbye")
		sys.exit(0)


def outcome(list0, list1):
	if sum(list0) > 21:
		print("You busted. You lost")
	elif sum(list1) > 21:
		print("Dealer busted. You win")
	elif sum(list0) > sum(list1):
		print("You win!")
	elif sum(list0) < sum(list1):
		print("You lose")
	else:
		print("It's a draw")



def bust(list):
	if sum(list) > 21:
		print("Sorry you busted. Game over")
		return True
	else:
		return False







def print_hands(list0, list1):
	print(f"Your hand is {list0} for a sum of {sum(list0)}")
	print(f"and the dealer's face up card is {list1[1:]}")





def deal_cards(list, n):
	for i in range(n):
		list.append(random.choice(cards))









main()