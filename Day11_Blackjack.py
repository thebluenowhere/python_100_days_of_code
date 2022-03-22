############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
from replit import clear

def deal_card():
  return random.choice(cards)

def calculate_score():
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

stop_game = False
#while not stop_game: 
choice = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
if choice == "y".lower().strip():
  computer_cards = []
  player_cards = []
  print(logo)
  computer_cards.append(deal_card())
  player_cards.append(deal_card())
  player_cards.append(deal_card())
  current_score = player_cards[0] + player_cards[1]
  print(f"\tYour cards: {player_cards}, current score: {current_score}")
  print(f"\tComputer's first card: {computer_cards[0]}")
else:
  print("not it bro")

