from designer import *
from dataclasses import dataclass

@dataclass
class PinochleWorld:
    title: DesignerObject
    instructions1: DesignerObject
    player_hand_objs: list[DesignerObject]
    player_obj: list[DesignerObject]
    cpu1_obj: list[DesignerObject]
    cpu1_image: Image
    cpu2_obj: list[DesignerObject]
    cpu2_image: Image
    cpu3_obj: list[DesignerObject]
    cpu3_image: Image
    cpu4_obj: list[DesignerObject]
    cpu4_image: Image
    cpu5_obj: list[DesignerObject]
    cpu5_image: Image
    call_trump_message: DesignerObject
    call_clubs: DesignerObject
    call_diamonds: DesignerObject
    call_spades: DesignerObject
    call_hearts: DesignerObject
    heading_left: DesignerObject
    heading_right: DesignerObject

#Create and Deal Deck Vars
remaining_card_count = 95
list_of_cards = []
player_cards = []
cpu1_cards = []
cpu2_cards = []
cpu3_cards = []
cpu4_cards = []
cpu5_cards = []

#Initializing World
truth_start = 0
truth_trump_called = 0
truth_start_tricks = 0
black_score = 0
red_score = 0
time_constant = 15


#Control Meld
trump_suit = ""

#Control Round
truth_player_turn_in_round = 0
truth_card_selected = 0
truth_card_played = 0
truth_run_time = 0
round_number = 1
lead_identifier = 0
order_list = []
i = 0
cards_played_list = [[]]
card_clicked = Image
current_turn = "player_turn"
time_bound = 15

suit_led = ""
high_card = ""