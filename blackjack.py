# A blackjack game!
import sys
import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# players_hand = []
# dealers_hand = []

def main():
	play_again = True
	while play_again:
		# Start the game
		players_hand = []
		dealers_hand = []
		print(logo)
		deal_cards(players_hand, 2)
		deal_cards(dealers_hand, 2)
		print(f"Your hand is {players_hand} for a sum of {sum(players_hand)}")
		print(f"and the dealer's face up card is {dealers_hand[1:]}")
		
		do_i_want_another_card = True
		while do_i_want_another_card:
			# Ask if the user would like another card
			while True:
				response = input("Would you like another card? Type 'y' to hit or 'n' to stand ").lower()
				if response in ["y", "n"]:
					break
				else:
					print("Invalid input - Please enter 'y' or 'n'")
			if response == 'y':
				# Dealer deals user another card
				deal_cards(players_hand, 1)
				print(f"Your hand is {players_hand} for a sum of {sum(players_hand)}")
				# Check to see if the sum of the players hand is over 21
				if sum(players_hand) > 21:
					print("You busted. You lose.")
					break
			else:
				do_i_want_another_card = False

		
				# Check if dealer has blackjack
				if sum(dealers_hand) == 21:
					if sum(players_hand) == sum(dealers_hand):
						print("Draw")
					else:
						print("You lose")	

				else:
					# Let dealer continuing drawing cards until game is over
					deal = True
					while deal:
						deal_cards(dealers_hand, 1)
						print(f"The dealer has {dealers_hand} for a sum of {sum(dealers_hand)}")
						if sum(dealers_hand) > 21:
							print("The dealer busted. You win!")
							deal = False
						else:
							if sum(dealers_hand) > 16:
								if sum(players_hand) > sum(dealers_hand):
									print("You win!")
								else:
									if sum(players_hand) == sum(dealers_hand):
										print("Draw")
									else:
										print("You lose")
								deal = False


		# Ask if player would like to play agian
		while True:
			response = input("Would you like to play again? Type 'y' for yes and 'n' for no. ").lower()
			if response in ["y", "n"]:
					break
			else:
				print("Invalid input - Please enter 'y' or 'n'")

		if response == 'y':
			os.system('clear')
		else:
			print("Goodbye")
			play_again = False


def deal_cards(list, n):
	for i in range(n):
		list.append(random.choice(cards))


main()
