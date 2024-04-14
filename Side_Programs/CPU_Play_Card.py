from designer import *
import Global_Variables as GV
from Global_Variables import PinochleWorld

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
    if GV.suit_led:
        on_suit_cards = []
        for card in sorted_cpu_cards:
            if GV.suit_led in card:
                on_suit_cards.append(card)
        if on_suit_cards:
            card_cpu_played = on_suit_cards[0]
            return card_cpu_played
    card_cpu_played = sorted_cpu_cards[0]
    return card_cpu_played