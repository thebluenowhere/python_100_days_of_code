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

def blackjack():
  print(logo)
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
  
  def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0 
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  def compare(user_score, computer_score):
    if user_score == computer_score:
      return "Draw"
      
    elif computer_score == 0:
      return "You lose, computer has blackjack!"
      
    elif user_score == 0:
      return "You win with blackjack!"
  
    elif user_score > 21:
      return "You lose"
  
    elif computer_score > 21:
      return "You win"
  
    else:
      if computer_score > user_score:
        return "You lose"
      else:
        return "You win"
        
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card is: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else: 
      deal_again = input("  Type 'y' to get another card, type 'n' to pass: ")
      
      if deal_again == 'y'.lower().strip():
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"  Your final hand: {user_cards} and the final score is: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? 'y' for yes, 'n' for no: ") == 'y':
  clear()
  blackjack()
