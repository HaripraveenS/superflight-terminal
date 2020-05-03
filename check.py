from back import bg
from person import *
from bullet import *

def checkindex(in_x , in_y):
    obs = 'ok';
    if in_x < 2 or in_x + 2 > 50:
        obs = 'wall'
    # for i in range(in_x, in_x + 3):
    #     for j in range(in_y , in_y + 3):
    #         if bg.canvas[i][j] == '_' or bg.canvas[i][j] == '|' or bg.canvas[i][j] == '\\' :
    #             obs = 'obs
    return obs

        
def check_coin(in_x, in_y):
    coin = 0
    for i in range(in_x, in_x + 3):
        for j in range(in_y , in_y + 3):
            if bg.canvas[i][j] == '0':
                coin += 1
    return coin


def check_obs(in_x, in_y):
    for i in range(in_x, in_x + 3):
        for j in range(in_y , in_y + 3):
            if bg.canvas[i][j] == '_' or bg.canvas[i][j] == '|' or bg.canvas[i][j] == '\\' :
                if in_x > 0 or in_x + 2 < 51:
                    return 1
    return -1
