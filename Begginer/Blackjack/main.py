import random as rnd
from art import logo
from os import system 
DECK = {'A':11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

def continue_playing(message: str)->str:
    scontinue_play = ""
    while not (scontinue_play in ('y','n')): 
        scontinue_play = input(message.lower())
    return scontinue_play

def initial_deal() ->dict: 
    current_deal = {"player": [], "dealer": []}
    for i in range(2):
        current_deal["player"].append(rnd.choice(list(DECK)))
        current_deal["dealer"].append(rnd.choice(list(DECK)))
    return current_deal

def evaluate_hand(hand:list) -> int:
    score = 0
    number_aces = 0
    for card in hand:
        if card == "A":
            number_aces += 1
        score += DECK[card]
    while number_aces > 0 and score > 21:
        number_aces -= 1
        score -= 10
    return score
    
def check_initial_deal(hands:dict) -> bool:
    score = evaluate_hand(hands['player'])    
    if score == 21:
        return True
    else:
        return False
    
def print_hand(hands:dict, key: str):
    player_hand = str(hands[key])
    player_hand=player_hand.replace("'","")
    return (f'Your cards: {player_hand}, current score: {evaluate_hand(hands[key])}')

def print_card (hands:dict):
    dealer_card = str(hands['dealer'][0])
    dealer_card=dealer_card.replace("'","")
    return (f"Computer's first card: {dealer_card}")

def player_turn(hands:dict)->dict:
    is_continue = True
    while is_continue and evaluate_hand(hands["player"])<21:
        print(print_hand(hands, "player"))
        print(print_card(hands))
        player_descission = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        match player_descission:
            case "n":
                is_continue = False
            case 'y':
                hands["player"].append(rnd.choice(list(DECK)))
                if evaluate_hand(hands['player']) >= 21:
                    is_continue = False
            case "_":
                print('Wrong input! Please read the instruction!')
    return hands

def dealer_turn(hands:dict)->dict:
    while evaluate_hand(hands['dealer']) <= 16:
        hands["dealer"].append(rnd.choice(list(DECK)))
    return hands

def result(hands:dict): 
    player_score = evaluate_hand(hands['player'])
    dealer_score = evaluate_hand(hands["dealer"])
    print(print_hand(hands, "player").replace('current', "final"))
    print(print_hand(hands, "dealer").replace('current', "final").replace("Your", "Dealer's"))
    if player_score > 21:  
        print("You busted! You lose 😤")
    elif dealer_score > 21:
        print("Oppent went over. You win 😁")
    elif player_score == 21 and len(hands['player']) == 2:
        if dealer_score == 21 and len(hands['dealer']) == 2:
            print("It's a draw!")
        else:
            print('Blackjack! You win 😁')
    elif player_score == dealer_score:
         print("It's a draw!")
    elif player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print ("You lose!")
    else:
        print("You should not see this")


def game_loop():
    
    status_game =  continue_playing("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if status_game == "n":
        exit()
    system("cls")
    while status_game == "y":
        
        print(logo)
        hands_delt = initial_deal()
        hands_delt = player_turn(hands_delt)
        hands_delt = dealer_turn(hands_delt)
        result(hands_delt) 
        status_game = continue_playing("Do you want to play another game? Type 'y' or 'n': ")
        if status_game == "y":
            system('cls') 



game_loop()