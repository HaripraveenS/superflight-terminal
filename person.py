import signal, os
import numpy as np
import time
from back import bg
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from check import *
from bullet import *
stick = [[' ','o', '_' ] , ['[' ,'|' ,'\\'], [' ', '^' , ' ']]
stick1 = [[' ',' ', ' ' ] , [' ' ,'|' ,' '], ['o', '--' , '<']]
def bulle( x , y):
    coor_y.append(y + 3)
    coor_x.append(x)
    src_x = x
    src_y = y + 3
    flg_bulla.append(1)
    temp.canvas[src_x][src_y] = bg.canvas[src_x][src_y]
    temp.canvas[src_x][src_y + 1] = bg.canvas[src_x][src_y + 1] 
    bg.canvas[src_x][src_y] = '='
    bg.canvas[src_x][src_y + 1] = '>'
class person:
    jeta = 26
    jetb = 100
    lives = 10
    coins = 0

    def __init__(self,rowx):
        self.x=rowx
        # bg.canvas[26][100] = 'O'
        # bg.canvas[27][100] = 'O'
        for i in range(3):
            for j in range(3):
                bg.canvas[person.jeta + i][person.jetb + j] = stick[i][j]

    # def bullets(self, k):
    #     src_x = person.jeta
    #     src_y = person.jetb
    #     bg.canvas[src_x][src_y + 2] = '='
    #     bg.canvas[src_x][src_y + 3] = '>'
    #     if src_y < 210 + k :
    #         bg.canvas[src_x][src_y + 2] = ' '
    #         bg.canvas[src_x][src_y + 3] = ' '
    #         src_y += 2
    #         bg.canvas[src_x][src_y + 2] = '='
    #         bg.canvas[src_x][src_y + 3] = '>'
    


    def moveperson(self , k, nitro):   
        def alarmhandler(signum, frame):
                raise AlarmException

        def user_input(timeout=0.1):
            # ''' input method '''
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        char = user_input()
        if nitro :
            nitro_che = 1
        else :
            nitro_che = 0
        if char == 'q':
            quit()
        if person.jetb <= k :
            person.coins += check_coin(person.jeta, k+3)
            for i in range(3):
                for j in range(3):
                    bg.canvas[person.jeta + i][person.jetb + j] = ' '
            # person.jetaa -= 4;
            
            person.jetb = k + 3;
            if check_obs(person.jeta,person.jetb) == 1 :
                person.lives -= 1          
            for i in range(3):
                for j in range(3):
                    bg.canvas[person.jeta + i][person.jetb + j] = stick[i][j]


        if char == 'w' and checkindex(person.jeta - 2 - 2*nitro_che, person.jetb) == 'ok' :
            # bg.canvas[person.jeta][person.jetb] = ' '
            # bg.canvas[person.jeta + 1][person.jetb] = ' '
            # bg.canvas[person.jeta - 4][person.jetb] = 'O'
            # bg.canvas[person.jeta - 3][person.jetb] = 'O'
            person.coins += check_coin(person.jeta - 2 , person.jetb)
            for i in range(3):
                for j in range(3):
                    bg.canvas[person.jeta + i][person.jetb + j] = ' '
            if nitro:
                person.jeta -= 2
                person.coins += check_coin(person.jeta, person.jetb)
                for i in range(3):
                    for j in range(3):
                        bg.canvas[person.jeta + i][person.jetb + j] = ' '
            person.jeta -= 2;
            if check_obs(person.jeta,person.jetb) == 1 :
                person.lives -= 1
            for i in range(3):
                for j in range(3):
                    bg.canvas[person.jeta + i][person.jetb + j] = stick[i][j]
                # person.person.jetb += 1;

        if char == 's' and checkindex(person.jeta + 2 + 2*nitro_che, person.jetb) == 'ok':
            # bg.canvas[person.jeta][person.jetb] = ' '
            # bg.canvas[person.jeta + 1][person.jetb] = ' '
            # bg.canvas[person.jeta + 2][person.jetb] = 'O'
            # bg.canvas[person.jeta + 3][person.jetb] = 'O'
            person.coins += check_coin(person.jeta + 2 , person.jetb)
            for i in range(3):
                for j in range(3):
                    bg.canvas[person.jeta + i][person.jetb + j] = ' '
            if nitro:
                person.jeta += 2
                person.coins += check_coin(person.jeta, person.jetb)
                for i in range(3):
                    for j in range(3):
                        bg.canvas[person.jeta + i][person.jetb + j] = ' '
            person.jeta += 2;

            if check_obs(person.jeta,person.jetb) == 1 :
                person.lives -= 1
            for i in range(3):
                for j in range(3):
                    bg.canvas[person.jeta + i][person.jetb + j] = stick[i][j]
            # person.jeta += 2;


        if char == 'a' and checkindex(person.jeta , person.jetb - 1 - nitro_che) == 'ok':
            # bg.canvas[person.jeta][person.jetb] = ' '
            # bg.canvas[person.jeta + 1][person.jetb] = ' '
            # bg.canvas[person.jeta][person.jetb - 1] = 'O'
            # bg.canvas[person.jeta + 1][person.jetb - 1] = 'O'
            person.coins += check_coin(person.jeta , person.jetb - 1)
            for i in range(3):
                for j in range(3):
                    bg.canvas[person.jeta + i][person.jetb + j] = ' '
            if nitro:
                person.jetb -= 1;
                person.coins += check_coin(person.jeta, person.jetb)
                for i in range(3):
                    for j in range(3):
                        bg.canvas[person.jeta + i][person.jetb + j] = ' '
            person.jetb -= 1
            if check_obs(person.jeta,person.jetb) == 1 :
                person.lives -= 1            
            # person.jeta -= 4;
            for i in range(3):
                for j in range(3):
                    bg.canvas[person.jeta + i][person.jetb + j] = stick[i][j]


        if char == 'd' and checkindex(person.jeta , person.jetb + 2 + 2*nitro_che) == 'ok':
            # print("madarchod" , end = "")
            # bg.canvas[person.jeta][person.jetb] = ' '
            # bg.canvas[person.jeta + 1][person.jetb] = ' '
            # bg.canvas[person.jeta][person.jetb + 2] = 'O'
            # bg.canvas[person.jeta + 1][person.jetb + 2] = 'O'
            person.coins += check_coin(person.jeta, person.jetb + 2)
            for i in range(3):
                for j in range(3):
                    bg.canvas[person.jeta + i][person.jetb + j] = ' '
            # person.jeta -= 4;
            if nitro:
                person.jetb += 2
                person.coins += check_coin(person.jeta, person.jetb)
                for i in range(3):
                    for j in range(3):
                        bg.canvas[person.jeta + i][person.jetb + j] = ' '
            person.jetb += 2;
            if check_obs(person.jeta,person.jetb) == 1 :
                person.lives -= 1
            for i in range(3):
                for j in range(3):
                    bg.canvas[person.jeta + i][person.jetb + j] = stick[i][j]

        elif checkindex(person.jeta + 1 , person.jetb) == 'ok':
        #     bg.canvas[person.jeta][person.jetb] = ' '
        #     bg.canvas[person.jeta + 1][person.jetb] = ' '
        #     bg.canvas[person.jeta + 2][person.jetb] = 'O'
        #     bg.canvas[person.jeta + 3][person.jetb] = 'O'
            person.coins += check_coin(person.jeta + 1 , person.jetb)
            for i in range(3):
                for j in range(3):
                    bg.canvas[person.jeta + i][person.jetb + j] = ' '
            # person.jeta -= 4;
            person.jeta += 1;
            if check_obs(person.jeta,person.jetb) == 1 :
                person.lives -= 1
            for i in range(3):
                for j in range(3):
                    bg.canvas[person.jeta + i][person.jetb + j] = stick[i][j]
            # person.jeta += 2;   
        if char == 'j' :
            b1 = bulle(person.jeta , person.jetb)

    # def person_dead(self):
        # while checkindex(person.jeta + 2 , person.jetb) == 'ok': 
        #     for i in range(3):
        #         for j in range(3):
        #                 bg.canvas[person.jeta + i][person.jetb + j] = ' '
        #     person.jeta += 2;
        #     if check_obs(person.jeta,person.jetb) == 1 :
        #             person.lives -= 1
        #     for i in range(3):
        #         for j in range(3):
        #             bg.canvas[person.jeta + i][person.jetb + j] = stick[i][j]
            # person.jeta += 2;



