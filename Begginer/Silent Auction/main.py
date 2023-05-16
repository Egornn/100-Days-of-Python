import os 
gavel="""

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\ 
                         `'-------'`
                       .-------------.
                      /_______________\ """
def solve(dictionary):
    if dictionary=={}:
        return ("Dictionary is empty!")
        
    highest_person, highest_bid = next(iter(dictionary)),dictionary[next(iter(dictionary))]
    for key, value in dictionary.items():
        if value>highest_bid:
            highest_person, highest_bid = key, value
    highest_person= highest_person[highest_person.find(" ")+1:]
    return f"The winner is {highest_person} with a bid of ${highest_bid}"



is_all_entered=False
while not is_all_entered:
    print(gavel+"\n")
    print('Welcome, to the Blind Auction!')    
    participant = {}
    participant_number=1
    name = input("What is your name? ")
    is_input_correct=False
    while not is_input_correct:
        bid = input("What is your bid? $")
        try:
            bid = int(bid)
            is_input_correct=True
        except:
            print("Your bid is incorrect, please input a number.")
    participant[f"{participant_number} "+name] = bid
    participant_number+=1
    is_input_correct=False
    while not is_input_correct:
        to_continue=input("Is there another bidder? Type \"yes\" or \"no\" ").lower()
        if to_continue == "yes": 
            is_input_correct=True
            os.system("cls")
        elif to_continue=="no":
            is_input_correct=True
            is_all_entered =True
        else:
            print("The input is incorrect.")
        
print(solve(participant))

            