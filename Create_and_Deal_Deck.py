from bakery import assert_equal
import random
import Global_Variables

remaining_card_count = 95

def create_deck_list_funct():
    '''
    Creates a list of strings representing the paths to different card images for a standard pinochle deck
    and holds that in "list_of_cards". The path is in the format: 
        "Sized-Pinochle-Cards/(number/name)_of_(suit).png" | (Exception: Ace of Spades ends in *2.png instead)
    
    The deck consists of 4 copies of each "9, jack, queen, king, 10, ace" for each suit of "clubs, diamonds,
    hearts, spades".
    '''
    global list_of_cards
    list_of_cards = []
    label_list = ["9","jack","queen","king","10","ace"]
    suit_list = ["clubs","diamonds","hearts","spades"]
    for label in label_list:
        for suit in suit_list:
            if (label == "9") or (label == "10"):
                list_of_cards.append("Sized-Pinochle-Cards/"+label+"_of_"+suit+".png")
            if label == "ace":
                if suit == "spades":
                    list_of_cards.append("Sized-Pinochle-Cards/"+label+"_of_"+suit+"2.png")
                else:
                    list_of_cards.append("Sized-Pinochle-Cards/"+label+"_of_"+suit+".png")
            if (label == "jack") or (label == "queen") or (label == "king"):
                list_of_cards.append("Sized-Pinochle-Cards/"+label+"_of_"+suit+"2.png")
    count = 1
    new_list_of_cards = []
    while count <= 4:
        for card in list_of_cards:
            new_list_of_cards.append(card)
        count += 1
    list_of_cards = new_list_of_cards

def deal_cards_helper(cards_list: list[str]):
    '''
    Helper for the "deal_cards_funct"

    Chooses a random card from the remaining cards in "list_of_cards" and appends it to the given player's
    hand. It then removes the 'dealt' card from "list_of_cards" and appropriately decreases the global
    "remaining_card_count".

    Arg:
        cards_list ([str]): Represents the appropriate player/computer hand into which the card is dealt 
    '''
    global list_of_cards
    global remaining_card_count
    card_number = random.randint(0,remaining_card_count)
    card = list_of_cards[card_number]
    cards_list.append(card)
    del list_of_cards[card_number]
    remaining_card_count -= 1

def deal_cards_funct():
    '''
    Main function to control dealing the "list_of_cards" to each computer/player and then sorting the
    player's cards. Results in "list_of_cards" being emptied, but "list_of_cards" does not carry over to
    Pinochle.py anyway.
    '''
    while remaining_card_count > 0:
        deal_cards_helper(Global_Variables.cpu1_cards)
        deal_cards_helper(Global_Variables.cpu2_cards)
        deal_cards_helper(Global_Variables.cpu3_cards)
        deal_cards_helper(Global_Variables.cpu4_cards)
        deal_cards_helper(Global_Variables.cpu5_cards)
        deal_cards_helper(Global_Variables.player_cards)
    sort_cards_funct(Global_Variables.player_cards, "player_cards")

def sort_cards_helper(cards_list: list[str]) -> list:
    '''
    Helper for the "sort_cards_funct"

    This takes in a list representing the appropriate player/computer hand and returns the hand sorted.
    Sorting follows this priority:
        suits - clubs, diamonds, spades, hearts
        label (high to low) - ace, 10, king, queen, jack, nine

    Arg:
        cards_list ([str]): Represents the appropriate player/computer hand into which the card is dealt
    
    Return:
        list: represents the cards_list sorted according to the priority above
    '''
    sorted_cards = []
    clubs = []
    diamonds = []
    spades = []
    hearts = []
    suits = [clubs, diamonds, spades, hearts]
    for card in cards_list:
        if "clubs" in card:
            card = "1" + card
            clubs.append(card)
        elif "diamonds" in card:
            card = "2" + card
            diamonds.append(card)
        elif "spades" in card:
                card = "3" + card
                spades.append(card)
        elif "hearts" in card:
            card = "4" + card
            hearts.append(card)
    for suit in suits:
        index_count = 0
        for card in suit:
            if "9" in card:
                card_prio = 1
            elif "jack" in card:
                card_prio = 2
            elif "queen" in card:
                card_prio = 3
            elif "king" in card:
                card_prio = 4
            elif "10" in card:
                card_prio = 5
            elif "ace" in card:
                card_prio = 6
            card = card[0] + str(card_prio) + card[1:]
            suit[index_count] = card
            index_count += 1
        suit.sort(reverse=True)
        for card in suit:
            sorted_cards.append(card)
    return sorted_cards

def sort_cards_funct(cards_list: list[str], cards_list_str: str):
    '''
    Main function for sorting the given list representing the appropriate player/computer hand.
    Sorting follows this priority:
        suits - clubs, diamonds, spades, hearts
        label (high to low) - ace, 10, king, queen, jack, nine

    Arg:
        cards_list ([str]): Represents the appropriate player/computer hand into which the card is dealt
        cards_list_str (str): Represents the string title of the appropriate player/computer hand
            - Valid args: "player_cards", "cpu1_cards", "cpu2_cards", (etc. for cpu 3, 4, 5)
    '''
    sorted_cards = sort_cards_helper(cards_list)
    new_sorted_cards = []
    for card in sorted_cards:
            card = card[2:]
            new_sorted_cards.append(card)
    if cards_list_str == "player_cards":
        Global_Variables.player_cards = new_sorted_cards
    elif cards_list_str == "cpu1_cards":
        Global_Variables.cpu1_cards = new_sorted_cards
    elif cards_list_str == "cpu2_cards":
        Global_Variables.cpu2_cards = new_sorted_cards
    elif cards_list_str == "cpu3_cards":
        Global_Variables.cpu3_cards = new_sorted_cards
    elif cards_list_str == "cpu4_cards":
        Global_Variables.cpu4_cards = new_sorted_cards
    elif cards_list_str == "cpu5_cards":
        Global_Variables.cpu5_cards = new_sorted_cards