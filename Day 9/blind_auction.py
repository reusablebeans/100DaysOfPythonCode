import blind_auction_art

print(blind_auction_art.logo)
print("Thank you for using the Silent Bidding Program! \nBegin by placing a bid.")

more_bidders = True
bidding_entries = {}

while more_bidders:
    name = input("Please enter your name: \n")
    bid = input("Please input your desired bid: \n")
    bidding_entries[name] = int(bid)
    repeat_decision = True
    while repeat_decision:
        continue_auction = input("Is there anyone else in this auction that would like to place a bid? \"yes\"/\"no\" ")
        if continue_auction.lower() == "yes":
            more_bidders = True
            repeat_decision = False
            print("\n" * 50)
        elif continue_auction.lower() == "no":
            more_bidders = False
            repeat_decision = False
            winning_bid = 0
            winner = ""
            for bidder in bidding_entries:
                if bidding_entries[bidder] > winning_bid:
                    winning_bid = bidding_entries[bidder]
                    winner = bidder
                elif bidding_entries[bidder] < winning_bid:
                    1 == 1
                elif bidding_entries[bidder] == winning_bid:
                    winner += " & " + bidder
            print(f"-------------------- AUCTION RESULTS -------------------- \n"
                  f"WINNING BIDDER(S): {winner.upper()} \n"
                  f"WINNING BID: ${winning_bid} \n")
        else:
            repeat_decision = True
