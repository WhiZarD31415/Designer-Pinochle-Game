#Run this program to test Create_and_Deal_Deck.py functionality
from Create_and_Deal_Deck import *
import Global_Variables

def test_decklist() -> bool:
    print("Test Decklist:")
    create_deck_list_funct()
    
    #Total cards
    total_card_count = 0
    for card in Global_Variables.list_of_cards:
        total_card_count += 1
    if total_card_count == 96:
        total_card_bool = True
    else:
        print("    Error: Total Card Count = " + str(total_card_count) + ". Not 96")
        total_card_bool = False
    
    
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
    all_cards_format_bool = True
    for i in twoD_count_list:
        for count in i:
            if count == 4:
                all_cards_format_bool = all_cards_format_bool and True
            else:
                all_cards_format_bool = all_cards_format_bool and False
    if not all_cards_format_bool:
        print("    Error: Not all cards with correct format counted. 2D count (suit x label ascending L-R):")
        print("    " + str(twoD_count_list))
    
    print("  Result = " + str(total_card_bool and all_cards_format_bool))

#Function calls
test_decklist()
