from dataclasses import dataclass
from designer import *
import random
import time

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
    

def create_PinochleWorld_world() -> PinochleWorld:
    global truth_start
    global truth_trump_called
    global truth_start_tricks
    global truth_player_turn_in_round
    global truth_card_selected
    global truth_card_played
    global black_score
    global red_score
    global time_constant
    global truth_run_time
    global cards_played_list
    global round_number
    global lead_identifier
    global i
    truth_start = 0
    truth_trump_called = 0
    truth_start_tricks = 0
    truth_player_turn_in_round = 0
    truth_card_selected = 0
    truth_card_played = 0
    black_score = 0
    red_score = 0
    time_constant = 0
    truth_run_time = 0
    cards_played_list = []
    round_number = 0
    lead_identifier = 0
    i = 0
    return PinochleWorld(
        text("black", "Welcome to Pinochle", 50, center_x, center_y - 150),
        text("black", "To start play, press the space bar", 20, center_x, center_y - 100),
        player_hand_objs = create_player_hand_obj(-1000),
        player_obj = create_cpu_hand_obj("black",center_x,560),
        cpu1_obj = create_cpu_hand_obj("red",40,460),
        cpu2_obj = create_cpu_hand_obj("black",40,140),
        cpu3_obj = create_cpu_hand_obj("red",center_x,40),
        cpu4_obj = create_cpu_hand_obj("black",740,140),
        cpu5_obj = create_cpu_hand_obj("red",740,460),
        call_trump_message = text("black", "", 50, center_x, center_y - 100),
        call_clubs = image("Sized Pinochle Cards/ace_of_clubs.png", center_x-150, 300),
        call_diamonds = image("Sized Pinochle Cards/ace_of_diamonds.png", center_x-50, 300),
        call_spades = image("Sized Pinochle Cards/ace_of_spades2.png", center_x+50, 300),
        call_hearts = image("Sized Pinochle Cards/ace_of_hearts.png", center_x+150, 300),
        heading_left = text("black", "Trump called: ", 20, 10, 5, anchor="topleft"),
        heading_right = text("black", "Black Team Score: 0 | Red Team Score: 0", 20, 790, 5, anchor="topright"))

def press_key_start(world: PinochleWorld, key: str):
    global truth_start
    global truth_start_tricks
    if key == " " and truth_start == 0:
        truth_start = 1
        world.title.text = ""
        world.instructions1.text = ""
        world.call_trump_message.text = "What will you call trump?"
        world.player_hand_objs = create_player_hand_obj(580)
        box_move_funct(world,1)
    if key == " " and truth_trump_called == 2:
        world.instructions1.text = ""
        obj_list = [world.player_obj[2], world.cpu1_obj[2], world.cpu2_obj[2], world.cpu3_obj[2], world.cpu4_obj[2], world.cpu5_obj[2]]
        for obj in obj_list:
            obj.text = ""
        box_move_funct(world,2)
        truth_start_tricks = 1

#################################################################################################

def create_deck_list_funct():
    global list_of_cards
    list_of_cards = []
    label_list = ["9","jack","queen","king","10","ace"]
    suit_list = ["clubs","diamonds","hearts","spades"]
    for label in label_list:
        for suit in suit_list:
            if (label == "9") or (label == "10"):
                list_of_cards.append("Sized Pinochle Cards/"+label+"_of_"+suit+".png")
            if label == "ace":
                if suit == "spades":
                    list_of_cards.append("Sized Pinochle Cards/"+label+"_of_"+suit+"2.png")
                else:
                    list_of_cards.append("Sized Pinochle Cards/"+label+"_of_"+suit+".png")
            if (label == "jack") or (label == "queen") or (label == "king"):
                list_of_cards.append("Sized Pinochle Cards/"+label+"_of_"+suit+"2.png")
    count = 1
    new_list_of_cards = []
    while count <= 4:
        for card in list_of_cards:
            new_list_of_cards.append(card)
        count += 1
    list_of_cards = new_list_of_cards

def deal_cards_funct():
    global player_cards
    global cpu1_cards
    global cpu2_cards
    global cpu3_cards
    global cpu4_cards
    global cpu5_cards
    player_cards = []
    cpu1_cards = []
    cpu2_cards = []
    cpu3_cards = []
    cpu4_cards = []
    cpu5_cards = []
    remaining_card_count = 95
    while remaining_card_count > 0:
        #1
        card_number = random.randint(0,remaining_card_count)
        card = list_of_cards[card_number]
        cpu1_cards.append(card)
        del list_of_cards[card_number]
        remaining_card_count -= 1
        #2
        card_number = random.randint(0,remaining_card_count)
        card = list_of_cards[card_number]
        cpu2_cards.append(card)
        del list_of_cards[card_number]
        remaining_card_count -= 1
        #3
        card_number = random.randint(0,remaining_card_count)
        card = list_of_cards[card_number]
        cpu3_cards.append(card)
        del list_of_cards[card_number]
        remaining_card_count -= 1
        #4
        card_number = random.randint(0,remaining_card_count)
        card = list_of_cards[card_number]
        cpu4_cards.append(card)
        del list_of_cards[card_number]
        remaining_card_count -= 1
        #5
        card_number = random.randint(0,remaining_card_count)
        card = list_of_cards[card_number]
        cpu5_cards.append(card)
        del list_of_cards[card_number]
        remaining_card_count -= 1
        #Player
        card_number = random.randint(0,remaining_card_count)
        card = list_of_cards[card_number]
        player_cards.append(card)
        del list_of_cards[card_number]
        remaining_card_count -= 1
    sort_cards_funct(player_cards, "player_cards", 1)


def sort_cards_funct(cards_list: list[str], cards_list_str: str, run_truth: int):
    global player_cards
    global cpu1_cards
    global cpu2_cards
    global cpu3_cards
    global cpu4_cards
    global cpu5_cards
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
            player_cards = new_sorted_cards
        elif cards_list_str == "cpu1_cards":
            cpu1_cards = sorted_cards
            return cpu1_cards
        elif cards_list_str == "cpu2_cards":
            cpu2_cards = sorted_cards
            return cpu2_cards
        elif cards_list_str == "cpu3_cards":
            cpu3_cards = sorted_cards
            return cpu3_cards
        elif cards_list_str == "cpu4_cards":
            cpu4_cards = sorted_cards
            return cpu4_cards
        elif cards_list_str == "cpu5_cards":
            cpu5_cards = sorted_cards
            return cpu5_cards
    else:
        if cards_list_str == "cpu1_cards":
            return cpu1_cards
        elif cards_list_str == "cpu2_cards":
            return cpu2_cards
        elif cards_list_str == "cpu3_cards":
            return cpu3_cards
        elif cards_list_str == "cpu4_cards":
            return cpu4_cards
        elif cards_list_str == "cpu5_cards":
            return cpu5_cards

#################################################################################################

def create_player_hand_obj(y: int) -> list[DesignerObject]:
    player_obj_list = []
    x = center_x - (37.5*5.5) - 4.25
    for card in player_cards:
        player_obj_list.append(image(card, x, y))
        x += 28.125
    return player_obj_list
    
def create_cpu_hand_obj(color:str,x:int,y:int) -> list[DesignerObject]:
    return [rectangle(color, 25, 25, x, y), rectangle(color, 25, 25, x, y), text(color, "", 20, x, y, anchor="center"), image("Sized Pinochle Cards/ace_of_clubs.png", center_x, -1000)]

def box_move_funct(world: PinochleWorld, run_number: int):
    if run_number == 1:
        world.player_obj[0].width = 500
        world.player_obj[0].height = 94
        world.player_obj[0].y = 570
    if run_number == 2:
        obj_list = [world.player_obj[1], world.cpu1_obj[1], world.cpu2_obj[1], world.cpu3_obj[1], world.cpu4_obj[1], world.cpu5_obj[1]]
        for obj in obj_list:
            obj.y = abs(obj.y - 0.5*(obj.y - center_y))
            obj.x = abs(obj.x - 0.5*(obj.x - center_x))
            obj.border = 1
            obj.height = 111
            obj.width = 77

#################################################################################################

def call_trump_click(world: PinochleWorld, x:int, y:int):
    if truth_start == 1:
        global trump_suit
        global truth_trump_called
        if colliding(world.call_clubs, x, y):
            trump_suit = "Clubs"
            truth_trump_called = 1
        if colliding(world.call_diamonds, x, y):
            trump_suit = "Diamonds"
            truth_trump_called = 1
        if colliding(world.call_spades, x, y):
            trump_suit = "Spades"
            truth_trump_called = 1
        if colliding(world.call_hearts, x, y):
            trump_suit = "Hearts"
            truth_trump_called = 1
        if truth_trump_called == 1:
            world.call_trump_message.text = ""
            world.call_clubs.y = -1000
            world.call_diamonds.y = -1000
            world.call_spades.y = -1000
            world.call_hearts.y = -1000
            world.heading_left.text = "Trump called: " + trump_suit
            calc_meld_funct()
            manage_meld_world(world)
            truth_trump_called = 2

def calc_meld_funct():
    global meld_list
    cards_list = [player_cards, cpu1_cards, cpu2_cards, cpu3_cards, cpu4_cards, cpu5_cards]
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
            if name_suit == trump_suit:
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
            if trump_suit == "Clubs":
                is_trump = 1
                suit_symbol = "♣"
        elif suit == suits[1]:
            if trump_suit == "Diamonds":
                is_trump = 1
                suit_symbol = "♦"
        elif suit == suits[2]:
            if trump_suit == "Spades":
                is_trump = 1
                suit_symbol = "♠"
        elif suit == suits[3]:
            if trump_suit == "Hearts":
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
            if trump_suit == name_suit:
                add_meld_points = 4
            suit_symbol = "♣"
        elif suit == suits[1]:
            name_suit = "Diamonds"
            if trump_suit == name_suit:
                add_meld_points = 4
            suit_symbol = "♦"
        elif suit == suits[2]:
            name_suit = "Spades"
            if trump_suit == name_suit:
                add_meld_points = 4
            suit_symbol = "♠"
        elif suit == suits[3]:
            name_suit = "Hearts"
            if trump_suit == name_suit:
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
    global black_score
    global red_score
    global black_meld
    global red_meld
    black_meld = meld_list[0][0] + meld_list[2][0] + meld_list[4][0]
    red_meld = meld_list[1][0] + meld_list[3][0] + meld_list[5][0]
    black_score += black_meld
    red_score += red_meld
    world.heading_right.text = "Black Team Score: "+str(black_score)+" | Red Team Score: "+str(red_score)
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
        
#################################################################################################

def select_card_click(world: PinochleWorld, x:int, y:int):
    global truth_card_selected
    global truth_card_played
    global card_clicked
    global cards_played_list
    global truth_run_time
    global round_number
    if (truth_player_turn_in_round == 1) and (truth_card_selected == 0):
        card_count = 0
        for card in world.player_hand_objs:
            if colliding(card, x, y):
                card_count += 1
                if card_count <= 3:
                    card_clicked = card
        if (card_count > 0) and (card_count <= 3):
            card_clicked.y -= 20
            truth_card_selected = 1
    elif (truth_player_turn_in_round == 1) and (truth_card_selected == 1):
        card_count = 0
        for card in world.player_hand_objs:
            if colliding(card, x, y):
                card_count += 1
                if card_count <= 3:
                    new_card_clicked = card
        if (card_count > 0) and (card_count <= 3) and new_card_clicked != card_clicked:
            card_clicked.y += 20
            new_card_clicked.y -= 20
            card_clicked = new_card_clicked
        elif (card_count > 0) and (card_count <= 3) and new_card_clicked == card_clicked:
            card_clicked.x = world.player_obj[1].x
            card_clicked.y = world.player_obj[1].y
            cards_played_list.append(card_clicked)
            round_number += 1
            truth_card_played = 1
            truth_run_time = 1

def control_round_function(world: PinochleWorld):
    global truth_player_turn_in_round
    global time_constant
    global truth_run_time
    global truth_card_selected
    global truth_card_played
    global run_number_round
    global time_bound
    global cards_played_list
    global lead_identifier
    global i
    cpu_string_list = ["cpu1_cards", "cpu2_cards", "cpu3_cards", "cpu4_cards", "cpu5_cards","player_turn"]
    order_list = []
    for string in cpu_string_list[lead_identifier:]:
        order_list.append(string)
    for string in cpu_string_list[:lead_identifier]:
        order_list.append(string)
    if round_number == 1 and i == 0:    
        print("1")
        time_bound = 15
        run_number_round = 0
        i = 1
    if truth_start_tricks == 1 and not truth_card_played:
        truth_run_time = 0
        truth_player_turn_in_round = 1
    if round_number == 1 and truth_card_played:    
        print("a")
        time_bound = 15
        run_number_round = 0
    if truth_start_tricks == 1 and truth_card_played:
        truth_run_time = 1
        truth_player_turn_in_round = 0
        if order_list[run_number_round] == "player_turn":
            print("c")
            truth_player_turn_in_round = 1
            truth_run_time = 0
            truth_card_selected = 0
            truth_card_played = 0
        if time_constant == 3 and not truth_player_turn_in_round:
            print("d")
            if round_number > 1:
                hide(cards_played_list[-2])
            hide(world.cpu1_obj[3])
            hide(world.cpu2_obj[3])
            hide(world.cpu3_obj[3])
            hide(world.cpu4_obj[3])
            hide(world.cpu5_obj[3])
        elif time_constant == time_bound and not truth_player_turn_in_round:
            print("e")
            run_number_round += 1
            cpu_play_card_funct(world, (lead_identifier+run_number_round), order_list[run_number_round-1], 1)
            cpu_play_card_funct(world, (lead_identifier+run_number_round), order_list[run_number_round-1], 2)
            time_bound += 15
        if run_number_round == 5:    
            print("f")
            time_constant = 0
            run_number_round = 0
            time_bound = 15
            lead_identifier = 1
        
def cpu_play_card_funct(world: PinochleWorld, cpu_number: int, cpu_string: str, run_number: int):
    list_cpu_objs = [world.cpu1_obj,world.cpu2_obj,world.cpu3_obj,world.cpu4_obj,world.cpu5_obj]
    cpu_obj = list_cpu_objs[cpu_number-1]
    if run_number == 1:
        card_cpu_played = cpu_card_decision_helper(cpu_number, cpu_string)
        cpu_obj[3] = image(card_cpu_played,cpu_obj[1].x,-1000)
        show(cpu_obj[3])
        run_number = 2
    if run_number == 2:
        cpu_obj[3].y = cpu_obj[1].y

def cpu_card_decision_helper(cpu_number: int, cpu_string: str):
    global cpu1_cards
    global cpu2_cards
    global cpu3_cards
    global cpu4_cards
    global cpu5_cards
    global cards_played_list
    list_of_cpu_cards = [cpu1_cards,cpu2_cards,cpu3_cards,cpu4_cards,cpu5_cards]
    cpu_cards = list_of_cpu_cards[cpu_number-1]
    cards_played = cards_played_list[round_number-1]
    if round_number == 1:
        sorted_cpu_cards = sort_cards_funct(cpu_cards, cpu_string, 1)
    if round_number > 1:
        sorted_cpu_cards = sort_cards_funct(cpu_cards, cpu_string, 0)
    card_cpu_played = sorted_cpu_cards[round_number][2:]
    return card_cpu_played

#################################################################################################

def clock():
    global time_constant
    global truth_run_time
    if truth_run_time:
        time_constant += 1

when("starting", create_deck_list_funct)
when("starting", deal_cards_funct)
when("starting", create_PinochleWorld_world)
when("typing", press_key_start)
when("clicking", call_trump_click)
when("clicking", select_card_click)
when("updating", control_round_function)
when("updating", clock)

start()