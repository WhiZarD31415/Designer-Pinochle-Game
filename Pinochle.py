from bakery import assert_equal
from dataclasses import dataclass
from designer import *
from Side_Programs.Create_and_Deal_Deck import create_deck_list_funct, deal_cards_funct, sort_cards_funct
from Side_Programs.Inputs import press_key_start, call_trump_click, select_card_click
from Side_Programs.Create_Objs import create_player_hand_obj, create_cpu_hand_obj, box_move_funct
import Global_Variables as GV
from Global_Variables import PinochleWorld
import time

center_x = get_width() / 2
center_y = get_height() / 2

def create_PinochleWorld_world() -> PinochleWorld:
    '''
    Create the initial world
    '''
    return PinochleWorld(
        text("black", "Welcome to Pinochle", 50, center_x, center_y - 150),
        text("black", "To start play, press the space bar", 20, center_x, center_y - 100),
        player_hand_objs = create_player_hand_obj(-1000),
        player_obj = create_cpu_hand_obj("black",center_x,560),
        cpu1_obj = create_cpu_hand_obj("red",40,460),
        cpu1_image = image("Sized-Pinochle-Cards/ace_of_clubs.png", center_x, -1000),
        cpu2_obj = create_cpu_hand_obj("black",40,140),
        cpu2_image = image("Sized-Pinochle-Cards/ace_of_clubs.png", center_x, -1000),
        cpu3_obj = create_cpu_hand_obj("red",center_x,40),
        cpu3_image = image("Sized-Pinochle-Cards/ace_of_clubs.png", center_x, -1000),
        cpu4_obj = create_cpu_hand_obj("black",740,140),
        cpu4_image = image("Sized-Pinochle-Cards/ace_of_clubs.png", center_x, -1000),
        cpu5_obj = create_cpu_hand_obj("red",740,460),
        cpu5_image = image("Sized-Pinochle-Cards/ace_of_clubs.png", center_x, -1000),
        call_trump_message = text("black", "", 50, center_x, center_y - 100),
        call_clubs = image("Sized-Pinochle-Cards/ace_of_clubs.png", center_x-150, 300),
        call_diamonds = image("Sized-Pinochle-Cards/ace_of_diamonds.png", center_x-50, 300),
        call_spades = image("Sized-Pinochle-Cards/ace_of_spades2.png", center_x+50, 300),
        call_hearts = image("Sized-Pinochle-Cards/ace_of_hearts.png", center_x+150, 300),
        heading_left = text("black", "Trump called: ", 20, 10, 5, anchor="topleft"),
        heading_right = text("black", "Black Team Score: 0 | Red Team Score: 0", 20, 790, 5, anchor="topright"))



#################################################################################################

def control_round_function(world: PinochleWorld):
    '''
    Controls whose turn it is in the round.
    '''
    if GV.truth_start_tricks:
        if not GV.i:
            cpu_string_list = ["player_turn","cpu1_cards", "cpu2_cards", "cpu3_cards", "cpu4_cards", "cpu5_cards"]
            GV.order_list = []
            for string in cpu_string_list[GV.lead_identifier:]:
                GV.order_list.append(string)
            for string in cpu_string_list[:GV.lead_identifier]:
                GV.order_list.append(string)
            GV.i = 1
        if GV.truth_card_played:
            GV.truth_run_time = 1
            GV.truth_player_turn_in_round = 0
        if GV.time_constant == GV.time_bound:
            GV.time_constant += 1
            GV.current_turn = GV.order_list[0]
            check_turn_funct(world)
        elif GV.time_constant == (GV.time_bound*2):
            GV.time_constant += 1
            GV.current_turn = GV.order_list[1]
            check_turn_funct(world)
        elif GV.time_constant == (GV.time_bound*3):
            GV.time_constant += 1
            GV.current_turn = GV.order_list[2]
            check_turn_funct(world)
        elif GV.time_constant == (GV.time_bound*4):
            GV.time_constant += 1
            GV.current_turn = GV.order_list[3]
            check_turn_funct(world)
        elif GV.time_constant == (GV.time_bound*5):
            GV.time_constant += 1
            GV.current_turn = GV.order_list[4]
            check_turn_funct(world)
        elif GV.time_constant == (GV.time_bound*6):
            GV.time_constant += 1
            GV.current_turn = GV.order_list[5]
            check_turn_funct(world)
        if len(GV.cards_played_list[GV.round_number-1]) == 6 and GV.time_constant == 120:
            clear_played_card_objs(world)
            count = 0
            i = 0
            for card in GV.cards_played_list[-1]:
                if GV.high_card == card and i == 0:
                    GV.lead_identifier = (GV.lead_identifier + count)%6
                    i = 1
                count += 1
            GV.i = 0
            GV.cards_played_list.append([])
            GV.time_constant = 0
            GV.round_number += 1
            
def check_turn_funct(world: PinochleWorld):
    '''
    Checks which cpu's turn it is and plays a card
    '''
    if GV.current_turn == "player_turn":
        GV.truth_card_played = 0
        GV.truth_player_turn_in_round = 1
        GV.truth_run_time = 0
    elif GV.current_turn == "cpu1_cards":
        cpu_play_card_funct(world, 1, "cpu1_cards", 1)
        cpu_play_card_funct(world, 1, "cpu1_cards", 2)
    elif GV.current_turn == "cpu2_cards":
        cpu_play_card_funct(world, 2, "cpu2_cards", 1)
        cpu_play_card_funct(world, 2, "cpu2_cards", 2)
    elif GV.current_turn == "cpu3_cards":
        cpu_play_card_funct(world, 3, "cpu3_cards", 1)
        cpu_play_card_funct(world, 3, "cpu3_cards", 2)
    elif GV.current_turn == "cpu4_cards":
        cpu_play_card_funct(world, 4, "cpu4_cards", 1)
        cpu_play_card_funct(world, 4, "cpu4_cards", 2)
    elif GV.current_turn == "cpu5_cards":
        cpu_play_card_funct(world, 5, "cpu5_cards", 1)
        cpu_play_card_funct(world, 5, "cpu5_cards", 2)

def cpu_play_card_funct(world: PinochleWorld, cpu_number: int, cpu_string: str, run_number: int):
    '''
    Cpu plays a card based on decision helper
    '''
    list_cpu_objs = [world.cpu1_obj,world.cpu2_obj,world.cpu3_obj,world.cpu4_obj,world.cpu5_obj]
    list_cpu_images = [world.cpu1_image,world.cpu2_image,world.cpu3_image,world.cpu4_image,world.cpu5_image]
    list_of_cpu_cards = [GV.cpu1_cards,GV.cpu2_cards,GV.cpu3_cards,GV.cpu4_cards,GV.cpu5_cards]
    cpu_obj = list_cpu_objs[cpu_number-1]
    cpu_image = list_cpu_images[cpu_number-1]
    cpu_cards = list_of_cpu_cards[cpu_number-1]
    if run_number == 1:
        card_cpu_played = cpu_card_decision_helper(cpu_cards, cpu_string)
        GV.cards_played_list[GV.round_number-1].append(card_cpu_played)
        cpu_image.filename = card_cpu_played
        #removing card from cpu_cards
        count = 0
        i = 0
        for card in cpu_cards:
            if card == card_cpu_played and i == 0:
                del cpu_cards[count]
                count+=1
                i = 1
    if run_number == 2:
        cpu_image.x = cpu_obj[1].x
        cpu_image.y = cpu_obj[1].y

def cpu_card_decision_helper(sorted_cpu_cards: list[str], cpu_string: str) -> str:
    '''
    Picks a card for a cpu to play
    '''
    card_cpu_played = sorted_cpu_cards[0]
    return card_cpu_played

def tracking_round_result(world: PinochleWorld):
    list_played_card_image = [GV.card_clicked, world.cpu1_image,world.cpu2_image,world.cpu3_image,world.cpu4_image,world.cpu5_image]
    copy_list_card_image = []
    for string in list_played_card_image[GV.lead_identifier:]:
        copy_list_card_image.append(string)
    for string in list_played_card_image[:GV.lead_identifier]:
        copy_list_card_image.append(string)
    list_objs = [world.player_obj,world.cpu1_obj,world.cpu2_obj,world.cpu3_obj,world.cpu4_obj,world.cpu5_obj]
    copy_list_objs = []
    for string in list_objs[GV.lead_identifier:]:
        copy_list_objs.append(string)
    for string in list_objs[:GV.lead_identifier]:
        copy_list_objs.append(string)
    if GV.truth_start_tricks:
        current_cards = GV.cards_played_list[GV.round_number-1]
        if len(current_cards) == 6:
            #
            count = 0
            for obj in list_objs:
                if count%2:
                    list_objs[count][1].color = "red"
                else:
                    list_objs[count][1].color = "black"
                count += 1
            #
            suits = ["clubs", "diamonds", "spades", "hearts"]
            card_led = GV.cards_played_list[-1][0]
            for suit in suits:
                if suit in card_led:
                    GV.suit_led = suit
            #
            onsuit_cards = []
            for card in current_cards:
                if GV.suit_led in card:
                    onsuit_cards.append(card)
            GV.high_card = find_high_card(onsuit_cards)
            trump_cards = []
            for card in current_cards:
                if GV.trump_suit.lower() in card:
                    trump_cards.append(card)
                    GV.high_card = find_high_card(trump_cards)
            #
            count = 0
            i = 0
            for obj in copy_list_card_image:
                if GV.high_card == obj.filename and i == 0:
                    copy_list_objs[count][1].color = "yellow"
                    i = 1
                count += 1
                    
def find_high_card(cards: list[str]) -> str:
    high_card = ""
    prio_list = ["ace", "10", "king", "queen", "jack", "9"]
    for prio in prio_list:
        for card in cards:
            if not high_card:
                if prio in card:
                    high_card = card
    return high_card

def clear_played_card_objs(world: PinochleWorld):
    list_cpu_images = [world.cpu1_image,world.cpu2_image,world.cpu3_image,world.cpu4_image,world.cpu5_image]
    for obj in world.player_hand_objs:
        if obj.y == 430:
            obj.y = 1000
    for obj in list_cpu_images:
        obj.y = 1000

#################################################################################################

def clock():
    '''
    World clock. Updates 30 times a second.
    '''
    if GV.truth_run_time:
        """ if GV.time_constant in [17,32,47,62,77,92]:
            GV.time_constant  """
        GV.time_constant += 1

when("starting", create_deck_list_funct)
when("starting", deal_cards_funct)
when("starting", create_PinochleWorld_world)
when("typing", press_key_start)
when("clicking", call_trump_click)
when("clicking", select_card_click)
when("updating", control_round_function)
when("updating", clock)
when("updating", tracking_round_result)

start()