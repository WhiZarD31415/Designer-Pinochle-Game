#Run this program to test Create_and_Deal_Deck.py functionality
from Create_and_Deal_Deck import *
import Global_Variables

valid_cards = open("Sized-Pinochle-Cards/valid_cards.txt")
list_of_valid_cards = valid_cards.read().split("\n")

def test_decklist() -> bool:
    '''
    Testing for "create_deck_list_funct"

    Checks if there are 96 cards in the appropriate global "list_of_cards". If there is not, it prints an
    error with a description. It also checks if there is four of every card formatted correctly (all at one
    time for simplicity). Checks this by counting every card into a 2D list with elements for every
    corresponding card. If there is not, it prints an error with the 2D list for reference. At the end,
    prints the eventual return boolean.

    Return:
        bool: represents if the test passed all checks
    '''
    print("Test Decklist:")
    create_deck_list_funct()
    passing_bool = True
    total_card_bool = True
    valid_card_bool = True
    all_cards_format_bool = True
    
    #Total cards
    total_card_count = 0
    for card in Global_Variables.list_of_cards:
        total_card_count += 1
    if total_card_count == 96:
        total_card_bool = True
    else:
        print("    Error: Total Card Count = " + str(total_card_count) + ". Not 96")
        total_card_bool = False
    
    #Validate Cards
    for card in Global_Variables.list_of_cards:
        if card in list_of_valid_cards:
            valid_card_bool = valid_card_bool and True
        else:
            print("    Error: Card named '" + card
                  + "' was not in correct path string format")
            valid_card_bool = valid_card_bool and False

    #Accounting for every card in correct format
    values = ["9", "jack", "queen", "king", "10", "ace"]
    suits = ["clubs", "diamonds", "spades", "hearts"]
    twoD_count_list = [[0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0]]
    
    index1 = 0
    index2 = 0
    for suit in suits:
        index2 = 0
        for value in values:
            for card in Global_Variables.list_of_cards:
                #Exception
                if suit == "spades" and value == "ace":
                    if card == "Sized-Pinochle-Cards/ace_of_spades2.png":
                        new_count = twoD_count_list[index1][index2] + 1
                        twoD_count_list[index1][index2] = new_count
                #Face Cards
                elif "jack" in card or "queen" in card or "king" in card:
                    if card == "Sized-Pinochle-Cards/"+value+"_of_"+suit+"2.png":
                        new_count = twoD_count_list[index1][index2] + 1
                        twoD_count_list[index1][index2] = new_count
                #Nonface Cards
                else:
                    if card == "Sized-Pinochle-Cards/"+value+"_of_"+suit+".png":
                        new_count = twoD_count_list[index1][index2] + 1
                        twoD_count_list[index1][index2] = new_count
            index2 += 1
        index1 += 1
    for i in twoD_count_list:
        for count in i:
            if count == 4:
                all_cards_format_bool = all_cards_format_bool and True
            else:
                all_cards_format_bool = all_cards_format_bool and False
    if not all_cards_format_bool:
        print("    Error: Not all cards with correct format counted correctly. 2D count "
              + "(suit x label ascending L-R):")
        print("    " + str(twoD_count_list))
    
    #Conclusion
    passing_bool = passing_bool and total_card_bool and valid_card_bool and all_cards_format_bool
    print("  Result = " + str(passing_bool))
    return passing_bool

def test_deal_helper() -> bool:
    '''
    Testing for "deal_cards_helper"

    Checks (Unfinished docstring)

    Return:
        bool: represents if the test passed all checks
    '''
    print("Test Deal Helper:")
    Global_Variables.remaining_card_count = 95
    passing_bool = True
    remaining_count_bool = True
    player_count_bool = True
    valid_card_bool = True
    loop_number = 1

    #Repeatability
    while loop_number <= 16:
        deal_cards_helper(Global_Variables.player_cards)

        #Remaining Card Count
        if Global_Variables.remaining_card_count == (95 - loop_number):
            remaining_count_bool = True
        else: 
            print("    Error: Remaining cards after " + str(loop_number) + " deal(s) = "
                  + str(Global_Variables.remaining_card_count + 1) + ". Not " + str(96 - loop_number))
            remaining_count_bool = False

        #Player Card Count
        if len(Global_Variables.player_cards) == loop_number:
            player_count_bool = player_count_bool and True
        else:
            print("    Error: Number of player cards after " + str(loop_number) + " deal(s) = "
                + str(len(Global_Variables.player_cards)) + ". Not " + str(loop_number))
            player_count_bool = False
        loop_number += 1

    #Validate Cards
    for card in Global_Variables.player_cards:
        if card in list_of_valid_cards:
            valid_card_bool = valid_card_bool and True
        else:
            print("    Error: Card named '" + card
                    + "' was not in correct path string format")
            valid_card_bool = False

    #Conclusion
    passing_bool = passing_bool and remaining_count_bool and player_count_bool and valid_card_bool
    print("  Result = " + str(passing_bool))
    return passing_bool


#Function calls
test_decklist()
test_deal_helper()
print("")

valid_cards.close()