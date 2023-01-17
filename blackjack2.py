import sys
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def main():
	

	my_hand = []
	dealers_hand = []

	deal_cards(my_hand, 2)
	deal_cards(dealers_hand, 2)

	print_hands(list0 = my_hand, list1 = dealers_hand)
	

	deal = True
	# bust = False
	# while not bust:

	while deal:
		while True:
			response = input("Would you like to hit or stand? Type 'y' to hit or 'n' to stand ").lower()
			if response in ["y", "n"]:
				break
			else:
				print("Invalid input - Please enter 'y' or 'n'")

		if response == 'y':
			deal_cards(my_hand, 1)
			print(f"Your hand is {my_hand} for a sum of {sum(my_hand)}")
			bust(my_hand)
		else:
			deal = False


	deal = True
	while deal:
		deal_cards(dealers_hand, 1)
		print(f"The dealer has {dealers_hand} for a sum of {sum(dealers_hand)}")
		if sum(dealers_hand) > 21:
			print("The dealer busted. You win!")
			deal = False
			sys.exit(0)
		else:
			if sum(dealers_hand) > 16:
				if sum(my_hand) > sum(dealers_hand):
					print("You win!")
					deal = False
					sys.exit(0)
				else:
					if sum(my_hand) == sum(dealers_hand):
						print("Draw")
						deal = False
						sys.exit(0)
					else:
						print("You lose")
						deal = False
						sys.exit(0)






def bust(list):
	if sum(list) > 21:
		print("Sorry you busted. Game over")
		sys.exit(0)








def print_hands(list0, list1):
	print(f"Your hand is {list0} for a sum of {sum(list0)}")
	print(f"and the dealer's face up card(s) are {list1[1:]}")





def deal_cards(list, n):
	for i in range(n):
		list.append(random.choice(cards))









main()