from dataclasses import dataclass
from designer import *
from Side_Programs.Create_and_Deal_Deck import create_deck_list_funct, deal_cards_funct, sort_cards_funct
from Side_Programs.Control_Meld import calc_meld_funct, manage_meld_world
from Side_Programs.Inputs import press_key_start, call_trump_click, select_card_click
from Side_Programs.Create_Objs import create_player_hand_obj, create_cpu_hand_obj, box_move_funct
import Global_Variables as GV
from Global_Variables import PinochleWorld
import time

center_x = get_width() / 2
center_y = get_height() / 2

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



#################################################################################################



def control_round_function(world: PinochleWorld):
    cpu_string_list = ["cpu1_cards", "cpu2_cards", "cpu3_cards", "cpu4_cards", "cpu5_cards","player_turn"]
    order_list = []
    for string in cpu_string_list[GV.lead_identifier:]:
        order_list.append(string)
    for string in cpu_string_list[:GV.lead_identifier]:
        order_list.append(string)
    if GV.round_number == 1 and GV.i == 0:    
        #print("1")
        GV.time_bound = 15
        GV.run_number_round = 0
        GV.i = 1
    if GV.truth_start_tricks == 1 and not GV.truth_card_played:
        GV.truth_run_time = 0
        GV.truth_player_turn_in_round = 1
    if GV.round_number == 1 and GV.truth_card_played:    
        #print("a")
        GV.time_bound = 15
        GV.run_number_round = 0
    if GV.truth_start_tricks == 1 and GV.truth_card_played:
        GV.truth_run_time = 1
        GV.truth_player_turn_in_round = 0
        if order_list[GV.run_number_round] == "player_turn":
            #print("c")
            GV.truth_player_turn_in_round = 1
            GV.truth_run_time = 0
            GV.truth_card_selected = 0
            GV.truth_card_played = 0
        if GV.time_constant == 3 and not GV.truth_player_turn_in_round:
            #print("d")
            if GV.round_number > 1:
                hide(GV.cards_played_list[-2])
            hide(world.cpu1_obj[3])
            hide(world.cpu2_obj[3])
            hide(world.cpu3_obj[3])
            hide(world.cpu4_obj[3])
            hide(world.cpu5_obj[3])
        elif GV.time_constant == GV.time_bound and not GV.truth_player_turn_in_round:
            #print("e")
            GV.run_number_round += 1
            cpu_play_card_funct(world, (GV.lead_identifier+GV.run_number_round), order_list[GV.run_number_round-1], 1)
            cpu_play_card_funct(world, (GV.lead_identifier+GV.run_number_round), order_list[GV.run_number_round-1], 2)
            GV.time_bound += 15
        if GV.run_number_round == 5:    
            #print("f")
            GV.time_constant = 0
            GV.run_number_round = 0
            GV.time_bound = 15
            GV.lead_identifier = 1
        
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
    list_of_cpu_cards = [GV.cpu1_cards,GV.cpu2_cards,GV.cpu3_cards,GV.cpu4_cards,GV.cpu5_cards]
    cpu_cards = list_of_cpu_cards[cpu_number-1]
    cards_played = GV.cards_played_list[GV.round_number-1]
    if GV.round_number == 1:
        sort_cards_funct(cpu_cards, cpu_string)
        sorted_cpu_cards = cpu_cards
    if GV.round_number > 1:
        sorted_cpu_cards = cpu_cards
    card_cpu_played = sorted_cpu_cards[GV.round_number]
    return card_cpu_played

#################################################################################################

def clock():
    if GV.truth_run_time:
        GV.time_constant += 1

when("starting", create_deck_list_funct)
when("starting", deal_cards_funct)
when("starting", create_PinochleWorld_world)
when("typing", press_key_start)
when("clicking", call_trump_click)
when("clicking", select_card_click)
when("updating", control_round_function)
when("updating", clock)

start()