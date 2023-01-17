import sys
import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_hand = []
dealers_hand = []

def main():
	play_again = True
	while play_again:
		start_the_game()
		do_i_want_another_card = True
		while do_i_want_another_card:
			deal_cards(my_hand, 1)
			print(f"Your hand is {my_hand} for a sum of {sum(my_hand)}")
			# Check if your hand is over 21
			do_i_want_another_card = outcome(my_hand, dealers_hand)










		play_again = continuing_playing


def outcome(list0, list1):
	if sum(list0) > 21:
		print("You busted. You lost")
		return False
	elif sum(list1) > 21:
		print("Dealer busted. You win")
		return False
	elif sum(list0) > sum(list1):
		print("You win!")
		return False
	elif sum(list0) < sum(list1):
		print("You lose")
		return False
	else:
		print("It's a draw")
		return False	


def deal_cards(list, n):
	for i in range(n):
		list.append(random.choice(cards))


def continuing_playing():
	while True:
		response = input("Would you like to play again? Type 'y' for yes and 'n' for no. ").lower()
		if response in ["y", "n"]:
				break
		else:
			print("Invalid input - Please enter 'y' or 'n'")

	if response == 'y':
		os.system('clear')
		return True
	else:
		print("Goodbye")
		return False

def do_i_want_another_card():
	while True:
			response = input("Would you like another card? Type 'y' to hit or 'n' to stand ").lower()
			if response in ["y", "n"]:
				break
			else:
				print("Invalid input - Please enter 'y' or 'n'")
	if response == 'y':
		return True
	else:
		return False

def start_the_game():
	my_hand = []
	dealers_hand = []
	print(logo)
	deal_cards(my_hand, 2)
	deal_cards(dealers_hand, 2)
	print(f"Your hand is {my_hand} for a sum of {sum(my_hand)}")
	print(f"and the dealer's face up card is {dealers_hand[1:]}")


main()
