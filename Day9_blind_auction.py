from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction!")

bidding_list = {}
more_bidders = True

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_list[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount 
      winner = bidder
  print(f"The winner is {winner} with a bid of £{highest_bid}")

while more_bidders == True: 
  name = input("What is your name?:\n")
  bid = int(input("What is your bid?: £"))
  bidding_list[name] = bid
  another_bidder = input("Is there another bidder? Yes/No:\n")
  if another_bidder == "yes".lower().strip():
    clear()
  elif another_bidder == "no".lower().strip():
    more_bidders = False
    highest_bidder(bidding_list)
  else:
    print("Please choose 'Yes' or 'No'. ")
