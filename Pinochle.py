from dataclasses import dataclass
from designer import *
from Side_Programs.Create_and_Deal_Deck import create_deck_list_funct, deal_cards_funct, sort_cards_funct
from Side_Programs.Control_Meld import calc_meld_funct, manage_meld_world
import Global_Variables
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
        if colliding(world.call_clubs, x, y):
            Global_Variables.trump_suit = "Clubs"
            Global_Variables.truth_trump_called = 1
        if colliding(world.call_diamonds, x, y):
            Global_Variables.trump_suit = "Diamonds"
            Global_Variables.truth_trump_called = 1
        if colliding(world.call_spades, x, y):
            Global_Variables.trump_suit = "Spades"
            Global_Variables.truth_trump_called = 1
        if colliding(world.call_hearts, x, y):
            Global_Variables.trump_suit = "Hearts"
            Global_Variables.truth_trump_called = 1
        if Global_Variables.truth_trump_called == 1:
            world.call_trump_message.text = ""
            world.call_clubs.y = -1000
            world.call_diamonds.y = -1000
            world.call_spades.y = -1000
            world.call_hearts.y = -1000
            world.heading_left.text = "Trump called: " + Global_Variables.trump_suit
            calc_meld_funct()
            manage_meld_world(world)
            Global_Variables.truth_trump_called = 2
        
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
        sort_cards_funct(cpu_cards, cpu_string)
        sorted_cpu_cards = cpu_cards
    if Global_Variables.round_number > 1:
        sorted_cpu_cards = cpu_cards
    card_cpu_played = sorted_cpu_cards[Global_Variables.round_number]
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