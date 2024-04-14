from designer import *
import Global_Variables
from Global_Variables import PinochleWorld

center_x = get_width() / 2
center_y = get_height() / 2

def create_player_hand_obj(y: int) -> list[DesignerObject]:
    player_obj_list = []
    x = center_x - (37.5*5.5) - 4.25
    for card in Global_Variables.player_cards:
        player_obj_list.append(image(card, x, y))
        x += 28.125
    return player_obj_list
    
def create_cpu_hand_obj(color:str,x:int,y:int) -> list[DesignerObject]:
    return [rectangle(color, 25, 25, x, y), rectangle(color, 25, 25, x, y), text(color, "", 20, x, y, anchor="center")]

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