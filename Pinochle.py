from dataclasses import dataclass
from designer import *
from Create_and_Deal_Deck import create_deck_list_funct, deal_cards_funct, sort_cards_funct
import Global_Variables
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
        call_clubs = image("Sized-Pinochle-Cards/ace_of_clubs.png", center_x-150, 300),
        call_diamonds = image("Sized-Pinochle-Cards/ace_of_diamonds.png", center_x-50, 300),
        call_spades = image("Sized-Pinochle-Cards/ace_of_spades2.png", center_x+50, 300),
        call_hearts = image("Sized-Pinochle-Cards/ace_of_hearts.png", center_x+150, 300),
        heading_left = text("black", "Trump called: ", 20, 10, 5, anchor="topleft"),
        heading_right = text("black", "Black Team Score: 0 | Red Team Score: 0", 20, 790, 5, anchor="topright"))

def press_key_start(world: PinochleWorld, key: str):
    if key == " " and Global_Variables.truth_start == 0:
        Global_Variables.truth_start = 1
        world.title.text = ""
        world.instructions1.text = ""
        world.call_trump_message.text = "What will you call trump?"
        world.player_hand_objs = create_player_hand_obj(580)
        box_move_funct(world,1)
    if key == " " and Global_Variables.truth_trump_called == 2:
        world.instructions1.text = ""
        obj_list = [world.player_obj[2], world.cpu1_obj[2], world.cpu2_obj[2], world.cpu3_obj[2], world.cpu4_obj[2], world.cpu5_obj[2]]
        for obj in obj_list:
            obj.text = ""
        box_move_funct(world,2)
        Global_Variables.truth_start_tricks = 1

#################################################################################################


#################################################################################################

def create_player_hand_obj(y: int) -> list[DesignerObject]:
    player_obj_list = []
    x = center_x - (37.5*5.5) - 4.25
    for card in Global_Variables.player_cards:
        player_obj_list.append(image(card, x, y))
        x += 28.125
    return player_obj_list
    
def create_cpu_hand_obj(color:str,x:int,y:int) -> list[DesignerObject]:
    return [rectangle(color, 25, 25, x, y), rectangle(color, 25, 25, x, y), text(color, "", 20, x, y, anchor="center"), image("Sized-Pinochle-Cards/ace_of_clubs.png", center_x, -1000)]

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
    if Global_Variables.truth_start == 1:
        global trump_suit
        if colliding(world.call_clubs, x, y):
            trump_suit = "Clubs"
            Global_Variables.truth_trump_called = 1
        if colliding(world.call_diamonds, x, y):
            trump_suit = "Diamonds"
            Global_Variables.truth_trump_called = 1
        if colliding(world.call_spades, x, y):
            trump_suit = "Spades"
            Global_Variables.truth_trump_called = 1
        if colliding(world.call_hearts, x, y):
            trump_suit = "Hearts"
            Global_Variables.truth_trump_called = 1
        if Global_Variables.truth_trump_called == 1:
            world.call_trump_message.text = ""
            world.call_clubs.y = -1000
            world.call_diamonds.y = -1000
            world.call_spades.y = -1000
            world.call_hearts.y = -1000
            world.heading_left.text = "Trump called: " + trump_suit
            calc_meld_funct()
            manage_meld_world(world)
            Global_Variables.truth_trump_called = 2

def calc_meld_funct():
    global meld_list
    cards_list = [Global_Variables.player_cards, Global_Variables.cpu1_cards, Global_Variables.cpu2_cards, Global_Variables.cpu3_cards, Global_Variables.cpu4_cards, Global_Variables.cpu5_cards]
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
            Global_Variables.i = 0
            for count in count_list:
                if count == 1 and Global_Variables.i == 0:
                    Global_Variables.i = 1
                elif count == 1 and Global_Variables.i == 1:
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
    Global_Variables.black_score += black_meld
    Global_Variables.red_score += red_meld
    world.heading_right.text = "Black Team Score: "+str(Global_Variables.black_score)+" | Red Team Score: "+str(Global_Variables.red_score)
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
    global card_clicked
    if (Global_Variables.truth_player_turn_in_round == 1) and (Global_Variables.truth_card_selected == 0):
        card_count = 0
        for card in world.player_hand_objs:
            if colliding(card, x, y):
                card_count += 1
                if card_count <= 3:
                    card_clicked = card
        if (card_count > 0) and (card_count <= 3):
            card_clicked.y -= 20
            Global_Variables.truth_card_selected = 1
    elif (Global_Variables.truth_player_turn_in_round == 1) and (Global_Variables.truth_card_selected == 1):
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
            Global_Variables.cards_played_list.append(card_clicked)
            Global_Variables.round_number += 1
            Global_Variables.truth_card_played = 1
            Global_Variables.truth_run_time = 1

def control_round_function(world: PinochleWorld):
    global run_number_round
    global time_bound
    cpu_string_list = ["cpu1_cards", "cpu2_cards", "cpu3_cards", "cpu4_cards", "cpu5_cards","player_turn"]
    order_list = []
    for string in cpu_string_list[Global_Variables.lead_identifier:]:
        order_list.append(string)
    for string in cpu_string_list[:Global_Variables.lead_identifier]:
        order_list.append(string)
    if Global_Variables.round_number == 1 and Global_Variables.i == 0:    
        #print("1")
        time_bound = 15
        run_number_round = 0
        Global_Variables.i = 1
    if Global_Variables.truth_start_tricks == 1 and not Global_Variables.truth_card_played:
        Global_Variables.truth_run_time = 0
        Global_Variables.truth_player_turn_in_round = 1
    if Global_Variables.round_number == 1 and Global_Variables.truth_card_played:    
        #print("a")
        time_bound = 15
        run_number_round = 0
    if Global_Variables.truth_start_tricks == 1 and Global_Variables.truth_card_played:
        Global_Variables.truth_run_time = 1
        Global_Variables.truth_player_turn_in_round = 0
        if order_list[run_number_round] == "player_turn":
            #print("c")
            Global_Variables.truth_player_turn_in_round = 1
            Global_Variables.truth_run_time = 0
            Global_Variables.truth_card_selected = 0
            Global_Variables.truth_card_played = 0
        if Global_Variables.time_constant == 3 and not Global_Variables.truth_player_turn_in_round:
            #print("d")
            if Global_Variables.round_number > 1:
                hide(Global_Variables.cards_played_list[-2])
            hide(world.cpu1_obj[3])
            hide(world.cpu2_obj[3])
            hide(world.cpu3_obj[3])
            hide(world.cpu4_obj[3])
            hide(world.cpu5_obj[3])
        elif Global_Variables.time_constant == time_bound and not Global_Variables.truth_player_turn_in_round:
            #print("e")
            run_number_round += 1
            cpu_play_card_funct(world, (Global_Variables.lead_identifier+run_number_round), order_list[run_number_round-1], 1)
            cpu_play_card_funct(world, (Global_Variables.lead_identifier+run_number_round), order_list[run_number_round-1], 2)
            time_bound += 15
        if run_number_round == 5:    
            #print("f")
            Global_Variables.time_constant = 0
            run_number_round = 0
            time_bound = 15
            Global_Variables.lead_identifier = 1
        
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
    list_of_cpu_cards = [Global_Variables.cpu1_cards,Global_Variables.cpu2_cards,Global_Variables.cpu3_cards,Global_Variables.cpu4_cards,Global_Variables.cpu5_cards]
    cpu_cards = list_of_cpu_cards[cpu_number-1]
    cards_played = Global_Variables.cards_played_list[Global_Variables.round_number-1]
    if Global_Variables.round_number == 1:
        sorted_cpu_cards = sort_cards_funct(cpu_cards, cpu_string, 1)
    if Global_Variables.round_number > 1:
        sorted_cpu_cards = sort_cards_funct(cpu_cards, cpu_string, 0)
    card_cpu_played = sorted_cpu_cards[Global_Variables.round_number][2:]
    return card_cpu_played

#################################################################################################

def clock():
    if Global_Variables.truth_run_time:
        Global_Variables.time_constant += 1

when("starting", create_deck_list_funct)
when("starting", deal_cards_funct)
when("starting", create_PinochleWorld_world)
when("typing", press_key_start)
when("clicking", call_trump_click)
when("clicking", select_card_click)
when("updating", control_round_function)
when("updating", clock)

start()