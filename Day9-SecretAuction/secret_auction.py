import os

print("Welcome to the secret auction program.")

bidders = {}
bid_status = "yes"
while bid_status == "yes":
    name =  input("What is your name: ")
    bid  =  int(input("What is your bid: $"))
    bidders[name] = bid
    
    
    bid_status = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    os.system('cls')
    
    
highest_bidder = max(bidders, key=bidders.get)
print(f"The winner is {highest_bidder} with a bid of ${bidders[highest_bidder]}.")