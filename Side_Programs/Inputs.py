from designer import *
import Global_Variables
from Global_Variables import PinochleWorld
from .Control_Meld import calc_meld_funct, manage_meld_world
from .Create_Objs import create_player_hand_obj, box_move_funct

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

def select_card_click(world: PinochleWorld, x:int, y:int):
    if (Global_Variables.truth_player_turn_in_round == 1) and (Global_Variables.truth_card_selected == 0):
        card_count = 0
        for card in world.player_hand_objs:
            if colliding(card, x, y):
                card_count += 1
                if card_count <= 3:
                    Global_Variables.card_clicked = card
        if (card_count > 0) and (card_count <= 3):
            Global_Variables.card_clicked.y -= 20
            Global_Variables.truth_card_selected = 1
    elif (Global_Variables.truth_player_turn_in_round == 1) and (Global_Variables.truth_card_selected == 1):
        card_count = 0
        for card in world.player_hand_objs:
            if colliding(card, x, y):
                card_count += 1
                if card_count <= 3:
                    new_card_clicked = card
        if (card_count > 0) and (card_count <= 3) and new_card_clicked != Global_Variables.card_clicked:
            Global_Variables.card_clicked.y += 20
            new_card_clicked.y -= 20
            Global_Variables.card_clicked = new_card_clicked
        elif (card_count > 0) and (card_count <= 3) and new_card_clicked == Global_Variables.card_clicked:
            Global_Variables.card_clicked.x = world.player_obj[1].x
            Global_Variables.card_clicked.y = world.player_obj[1].y
            Global_Variables.cards_played_list.append(Global_Variables.card_clicked)
            Global_Variables.round_number += 1
            Global_Variables.truth_card_played = 1
            Global_Variables.truth_run_time = 1