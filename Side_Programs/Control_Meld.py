from dataclasses import dataclass
from designer import *
import Global_Variables as GV

center_x = get_width() / 2
center_y = get_height() / 2

@dataclass
class PinochleWorld:
    title: DesignerObject
    instructions1: DesignerObject
    player_hand_objs: list[DesignerObject]
    player_obj: list[DesignerObject]
    cpu1_obj: list[DesignerObject]
    cpu2_obj: list[DesignerObject]
    cpu3_obj: list[DesignerObject]
    cpu4_obj: list[DesignerObject]
    cpu5_obj: list[DesignerObject]
    call_trump_message: DesignerObject
    call_clubs: DesignerObject
    call_diamonds: DesignerObject
    call_spades: DesignerObject
    call_hearts: DesignerObject
    heading_left: DesignerObject
    heading_right: DesignerObject

def calc_meld_funct():
    global meld_list
    cards_list = [GV.player_cards, GV.cpu1_cards, GV.cpu2_cards, GV.cpu3_cards, GV.cpu4_cards, GV.cpu5_cards]
    meld_list = []
    for card_list in cards_list:
        meld = [0]
        clubs = []
        diamonds = []
        spades = []
        hearts = []
        suits = [clubs, diamonds, spades, hearts]
        for card in card_list:
            if "clubs" in card:
                clubs.append(card)
            elif "diamonds" in card:
                diamonds.append(card)
            elif "spades" in card:
                spades.append(card)
            elif "hearts" in card:
                hearts.append(card)
        meld_arounds_helper(suits, meld)
        meld_runs_helper(suits, meld)
        meld_marriages_helper(suits, meld)
        meld_pinochle_helper(suits, meld)
        #9s
        count_9s = 0
        for suit in suits:
            if suit == suits[0]:
                name_suit = "Clubs"
                suit_symbol = "♣"
            elif suit == suits[1]:
                name_suit = "Diamonds"
                suit_symbol = "♦"
            elif suit == suits[2]:
                name_suit = "Spades"
                suit_symbol = "♠"
            elif suit == suits[3]:
                name_suit = "Hearts"
                suit_symbol = "♥"
            if name_suit == GV.trump_suit:
                for card in suit:
                    if "9" in card:
                        count_9s += 1
        count = 0
        meld_string = ""
        while count < count_9s:
            meld_string += "9"
            count += 1
        if count_9s:
            meld[0] += count_9s
            meld.append(meld_string+suit_symbol)
        meld_list.append(meld)
        
def meld_arounds_helper(suits: list[list], meld: list):
    around_list = ["Jack","Queen","King","Ace"]
    for around_card in around_list:
        if around_card == "Jack":
            add_meld_points = 4
            card_symbol = "J"
        elif around_card == "Queen":
            add_meld_points = 6
            card_symbol = "Q"
        elif around_card == "King":
            add_meld_points = 8
            card_symbol = "K"
        elif around_card == "Ace":
            add_meld_points = 10
            card_symbol = "A"
        count_list = []
        around = True
        around1 = False
        around2 = False
        around3 = False
        around4 = False
        for suit in suits:
            card_count = 0
            for card in suit:
                if around_card.lower() in card:
                    card_count += 1
            count_list.append(card_count)
        for count in count_list:
            if count == 0:
                around = False
            elif count == 1 and around:
                around1 = True
            elif count == 2 and around:
                around2 = True
            elif count == 3 and around:
                around3 = True
            elif count == 4 and around:
                around4 = True
        if around:
            if around1:
                meld[0] += add_meld_points
                meld.append(card_symbol+"♣♦♠♥")
            elif around2:
                meld[0] += (add_meld_points*10)
                meld.append(card_symbol+card_symbol+"♣♦♠♥")
            elif around3:
                meld[0] += (add_meld_points*15)
                meld.append(card_symbol+card_symbol+card_symbol+"♣♦♠♥")
            elif around4:
                meld[0] += (add_meld_points*20)
                meld.append(card_symbol+card_symbol+card_symbol+card_symbol+"♣♦♠♥")

def meld_runs_helper(suits: list[list], meld: list):
    for suit in suits:
        is_trump = 0
        if suit == suits[0]:
            if GV.trump_suit == "Clubs":
                is_trump = 1
                suit_symbol = "♣"
        elif suit == suits[1]:
            if GV.trump_suit == "Diamonds":
                is_trump = 1
                suit_symbol = "♦"
        elif suit == suits[2]:
            if GV.trump_suit == "Spades":
                is_trump = 1
                suit_symbol = "♠"
        elif suit == suits[3]:
            if GV.trump_suit == "Hearts":
                is_trump = 1
                suit_symbol = "♥"
        if is_trump:
            add_meld_points = 15
            needed_cards_list = ["jack","queen","king","10","ace"]
            count_list = []
            run = True
            run1 = False
            run2 = False
            run3 = False
            run4 = False
            for needed_card in needed_cards_list:
                card_count = 0
                for card in suit:
                    if needed_card in card:
                        card_count += 1
                count_list.append(card_count)
            for count in count_list:
                if count == 0:
                    run = False
                elif count == 1 and run:
                    run1 = True
                elif count == 2 and run:
                    run2 = True
                elif count == 3 and run:
                    run3 = True
                elif count == 4 and run:
                    run4 = True
            if run:
                if run1:
                    meld[0] += add_meld_points
                    meld.append("A10KQJ" + suit_symbol)
                elif run2:
                    meld[0] += (add_meld_points*10)
                    meld.append("A10KQJ" + suit_symbol)
                elif run3:
                    meld[0] += (add_meld_points*15)
                    meld.append("A10KQJ" + suit_symbol)
                elif run4:
                    meld[0] += (add_meld_points*20)
                    meld.append("A10KQJ" + suit_symbol)

def meld_marriages_helper(suits: list[list], meld: list):
    run = False
    for combo in meld:
        if combo != meld[0]:
            if "A10KQJ" in combo:
                run = True
    for suit in suits:
        add_meld_points = 2
        if suit == suits[0]:
            name_suit = "Clubs"
            if GV.trump_suit == name_suit:
                add_meld_points = 4
            suit_symbol = "♣"
        elif suit == suits[1]:
            name_suit = "Diamonds"
            if GV.trump_suit == name_suit:
                add_meld_points = 4
            suit_symbol = "♦"
        elif suit == suits[2]:
            name_suit = "Spades"
            if GV.trump_suit == name_suit:
                add_meld_points = 4
            suit_symbol = "♠"
        elif suit == suits[3]:
            name_suit = "Hearts"
            if GV.trump_suit == name_suit:
                add_meld_points = 4
            suit_symbol = "♥"
        count_list = []
        mar = True
        mar1 = False
        mar2 = False
        mar3 = False
        mar4 = False
        needed_cards_list = ["queen","king"]
        for needed_card in needed_cards_list:
            card_count = 0
            for card in suit:
                if needed_card in card:
                    card_count += 1
            count_list.append(card_count)
        if run and add_meld_points == 4:
            i = 0
            for count in count_list:
                if count == 1 and i == 0:
                    i = 1
                elif count == 1 and i == 1:
                    count_list[1] = 0
        for count in count_list:
                if count == 0:
                    mar = False
                elif count == 1 and mar:
                    mar1 = True
                elif count == 2 and mar:
                    mar2 = True
                elif count == 3 and mar:
                    mar3 = True
                elif count == 4 and mar:
                    mar4 = True
        if mar:
                if mar1:
                    meld[0] += add_meld_points
                    meld.append("KQ" + suit_symbol)
                elif mar2:
                    meld[0] += (add_meld_points*2)
                    meld.append("KKQQ" + suit_symbol)
                elif mar3:
                    meld[0] += (add_meld_points*3)
                    meld.append("KKKQQQ" + suit_symbol)
                elif mar4:
                    meld[0] += (add_meld_points*4)
                    meld.append("KKKKQQQQ" + suit_symbol)

def meld_pinochle_helper(suits: list[list], meld: list):
    count_list = []
    pino = True
    pino1 = False
    pino2 = False
    pino3 = False
    pino4 = False
    card_count = 0
    for card in suits[1]:
        if "jack" in card:
            card_count += 1
    count_list.append(card_count)
    card_count = 0
    for card in suits[2]:
        if "queen" in card:
            card_count += 1
    count_list.append(card_count)
    for count in count_list:
        if count == 0:
            pino = False
        elif count == 1 and pino:
            pino1 = True
        elif count == 2 and pino:
            pino2 = True
        elif count == 3 and pino:
            pino3 = True
        elif count == 4 and pino:
            pino4 = True
    if pino:
        if pino1:
            meld[0] += 4
            meld.append("Q♠J♦")
        elif pino2:
            meld[0] += 30
            meld.append("QQ♠JJ♦")
        elif pino3:
            meld[0] += 150
            meld.append("QQQ♠JJJ♦")
        elif pino4:
            meld[0] += 300
            meld.append("QQQQ♠JJJJ♦")

def manage_meld_world(world: PinochleWorld):
    global black_meld
    global red_meld
    black_meld = meld_list[0][0] + meld_list[2][0] + meld_list[4][0]
    red_meld = meld_list[1][0] + meld_list[3][0] + meld_list[5][0]
    GV.black_score += black_meld
    GV.red_score += red_meld
    world.heading_right.text = "Black Team Score: "+str(GV.black_score)+" | Red Team Score: "+str(GV.red_score)
    world.instructions1.text = "Press the space bar to continue"
    world.instructions1.y = center_y
    create_meld_text_funct(world)
    
def create_meld_text_funct(world):
    obj_list = [world.player_obj[2], world.cpu1_obj[2], world.cpu2_obj[2], world.cpu3_obj[2], world.cpu4_obj[2], world.cpu5_obj[2]]
    iteration_count = 0
    for obj in obj_list:
        obj.y = abs(obj.y - 0.4*(obj.y - center_y))
        obj.x = abs(obj.x - 0.4*(obj.x - center_x))
        meld_text = ""
        for meld_str in meld_list[iteration_count]:
            if isinstance(meld_str, str):
                meld_text += meld_str + ", "
        meld_text = meld_text[:-2]
        obj.text = meld_text
        iteration_count += 1