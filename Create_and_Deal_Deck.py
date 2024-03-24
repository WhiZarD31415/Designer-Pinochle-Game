import random
import Global_Variables

def create_deck_list_funct():
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

def deal_cards_funct():
    remaining_card_count = 95
    while remaining_card_count > 0:
        #1
        card_number = random.randint(0,remaining_card_count)
        card = list_of_cards[card_number]
        Global_Variables.cpu1_cards.append(card)
        del list_of_cards[card_number]
        remaining_card_count -= 1
        #2
        card_number = random.randint(0,remaining_card_count)
        card = list_of_cards[card_number]
        Global_Variables.cpu2_cards.append(card)
        del list_of_cards[card_number]
        remaining_card_count -= 1
        #3
        card_number = random.randint(0,remaining_card_count)
        card = list_of_cards[card_number]
        Global_Variables.cpu3_cards.append(card)
        del list_of_cards[card_number]
        remaining_card_count -= 1
        #4
        card_number = random.randint(0,remaining_card_count)
        card = list_of_cards[card_number]
        Global_Variables.cpu4_cards.append(card)
        del list_of_cards[card_number]
        remaining_card_count -= 1
        #5
        card_number = random.randint(0,remaining_card_count)
        card = list_of_cards[card_number]
        Global_Variables.cpu5_cards.append(card)
        del list_of_cards[card_number]
        remaining_card_count -= 1
        #Player
        card_number = random.randint(0,remaining_card_count)
        card = list_of_cards[card_number]
        Global_Variables.player_cards.append(card)
        del list_of_cards[card_number]
        remaining_card_count -= 1
    sort_cards_funct(Global_Variables.player_cards, "player_cards", 1)


def sort_cards_funct(cards_list: list[str], cards_list_str: str, run_truth: int):
    if run_truth:
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
        new_sorted_cards = []
        if cards_list_str == "player_cards":
            for card in sorted_cards:
                card = card[2:]
                new_sorted_cards.append(card)
            Global_Variables.player_cards = new_sorted_cards
        elif cards_list_str == "cpu1_cards":
            Global_Variables.cpu1_cards = sorted_cards
            return Global_Variables.cpu1_cards
        elif cards_list_str == "cpu2_cards":
            Global_Variables.cpu2_cards = sorted_cards
            return Global_Variables.cpu2_cards
        elif cards_list_str == "cpu3_cards":
            Global_Variables.cpu3_cards = sorted_cards
            return Global_Variables.cpu3_cards
        elif cards_list_str == "cpu4_cards":
            Global_Variables.cpu4_cards = sorted_cards
            return Global_Variables.cpu4_cards
        elif cards_list_str == "cpu5_cards":
            Global_Variables.cpu5_cards = sorted_cards
            return Global_Variables.cpu5_cards
    else:
        if cards_list_str == "cpu1_cards":
            return Global_Variables.cpu1_cards
        elif cards_list_str == "cpu2_cards":
            return Global_Variables.cpu2_cards
        elif cards_list_str == "cpu3_cards":
            return Global_Variables.cpu3_cards
        elif cards_list_str == "cpu4_cards":
            return Global_Variables.cpu4_cards
        elif cards_list_str == "cpu5_cards":
            return Global_Variables.cpu5_cards