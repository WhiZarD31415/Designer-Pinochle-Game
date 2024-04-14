from designer import *
import Global_Variables as GV
from Global_Variables import PinochleWorld
from .Control_Meld import calc_meld_funct, manage_meld_world
from .Create_Objs import create_player_hand_obj, box_move_funct

def press_key_start(world: PinochleWorld, key: str):
    if key == " " and GV.truth_start == 0:
        GV.truth_start = 1
        world.title.text = ""
        world.instructions1.text = ""
        world.call_trump_message.text = "What will you call trump?"
        world.player_hand_objs = create_player_hand_obj(580)
        box_move_funct(world,1)
    if key == " " and GV.truth_trump_called == 2:
        world.instructions1.text = ""
        obj_list = [world.player_obj[2], world.cpu1_obj[2], world.cpu2_obj[2], world.cpu3_obj[2], world.cpu4_obj[2], world.cpu5_obj[2]]
        for obj in obj_list:
            obj.text = ""
        box_move_funct(world,2)
        GV.truth_start_tricks = 1

def call_trump_click(world: PinochleWorld, x:int, y:int):
    if GV.truth_start == 1:
        if colliding(world.call_clubs, x, y):
            GV.trump_suit = "Clubs"
            GV.truth_trump_called = 1
        if colliding(world.call_diamonds, x, y):
            GV.trump_suit = "Diamonds"
            GV.truth_trump_called = 1
        if colliding(world.call_spades, x, y):
            GV.trump_suit = "Spades"
            GV.truth_trump_called = 1
        if colliding(world.call_hearts, x, y):
            GV.trump_suit = "Hearts"
            GV.truth_trump_called = 1
        if GV.truth_trump_called == 1:
            world.call_trump_message.text = ""
            world.call_clubs.y = -1000
            world.call_diamonds.y = -1000
            world.call_spades.y = -1000
            world.call_hearts.y = -1000
            world.heading_left.text = "Trump called: " + GV.trump_suit
            calc_meld_funct()
            manage_meld_world(world)
            GV.truth_trump_called = 2

def select_card_click(world: PinochleWorld, x:int, y:int):
    if (GV.truth_player_turn_in_round == 1) and not GV.truth_card_selected:
        card_count = 0
        for card in world.player_hand_objs:
            if colliding(card, x, y):
                card_count += 1
                if card_count <= 3:
                    GV.card_clicked = card
        if (card_count > 0) and (card_count <= 3):
            GV.card_clicked.y -= 20
            GV.truth_card_selected = 1
    elif (GV.truth_player_turn_in_round == 1) and GV.truth_card_selected:
        card_count = 0
        for card in world.player_hand_objs:
            if colliding(card, x, y):
                card_count += 1
                if card_count <= 3:
                    new_card_clicked = card
        if (card_count > 0) and (card_count <= 3) and new_card_clicked != GV.card_clicked:
            GV.card_clicked.y += 20
            new_card_clicked.y -= 20
            GV.card_clicked = new_card_clicked
        elif (card_count > 0) and (card_count <= 3) and new_card_clicked == GV.card_clicked:
            GV.card_clicked.x = world.player_obj[1].x
            GV.card_clicked.y = world.player_obj[1].y
            for card in GV.player_cards:
                if card == GV.card_clicked.filename:
                    card_clicked_string = card
            #removing card from player_card
            count = 0
            i = 0
            for card in GV.player_cards:
                if card == card_clicked_string and i == 0:
                    del GV.player_cards[count]
                    i=1
                count+=1
            GV.cards_played_list[GV.round_number-1].append(card_clicked_string)
            GV.truth_card_played = 1