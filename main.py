from back import *
from person import *
import random
import numpy,time
import os
from obstacle import *
from colorama import *
from coins import *
from check import *
from person import *
from bullet import *
init()
srow = 54
scol = 210

k = 0
dat = []  
start = background(54,210)

with open('start.txt') as f:
    board = f.readlines()
board = [row.rstrip('\n') for row in board]

with open('gameover.txt') as f:
    data = f.readlines()
data = [row.rstrip('\n') for row in data]

# # print(dat)
for i in range(len(board)):
    for j in range(len(board[i])):
        start.canvas[15 + i][25 +  j] = board[i][j]

for i in range(srow):
    for j in range(k,scol+k):
        print(start.canvas[i][j], end = "")
    print()
print('\033[0;0H')
time.sleep(2)


# game = open("gameover.txt" , "r")
# for line in game:
#     number_strings = line.split() 
#     data.append(number_strings)
# print(data)
test = person(srow)
sec = []
for i in range(150,2000,60):
     sec.append(i)
obs = [0,1,2]
for i in range(len(sec) - 2):
    t = (random.randint(0,10))%3
    if_coin = random.randint(0,3)
    ranx = random.randint(1,38)
    rany = random.randint(sec[i], sec[i + 1])
    if t == 0:
        obs1 = strt_obstacle(ranx,rany)
        # print("one"  , end = "")
        if if_coin != 0:
            c1 = coin(ranx, rany, sec[i] , sec[i+1])
    if t == 1:
        obs2 = hrzn_obstacle(ranx,rany)
        if if_coin != 0:
            c2 = coin(ranx, rany, sec[i] , sec[i+1])
        # print("o2e"  , end = "")
    if t == 2:
        obs3 = diag_obstacle(ranx,rany)
        if if_coin != 0:
            c3 = coin(ranx, rany, sec[i] , sec[i+1])
        # print("o3e"  , end = "")
# lives = 1
# obs1 = strt_obstacle(10,100)
# obs2 = hrzn_obstacle(30,200)
# obs2 = diag_obstacle(30,150)
flg = 1
nit = 0;
# coins = 0
# getch = _Getch()
# print ("Please enter something: ")
# print(repr(readchar.readchar()))
# print x



while True:
    # test.placejetpack(srow)
    if flg == 1:
        bg.canvas[0][k] = 'C'
        bg.canvas[0][k + 1] = 'O'
        bg.canvas[0][k + 2] = 'I'
        bg.canvas[0][k + 3] = 'N'
        bg.canvas[0][k + 4] = 'S'
        bg.canvas[0][k + 5] = '=' 
        bg.canvas[0][k + 6] = int(person.coins/100)
        bg.canvas[0][k + 7] = int((person.coins/10)%10)
        bg.canvas[0][k + 8] = int((person.coins)%10)
        bg.canvas[0][k + 9] = person.lives
        

        # bg.canvas[0][k+50] = flg
        for i in range(srow):
            for j in range(k,scol+k):
                print(bg.canvas[i][j], end = "")
            print()
        print('\033[0;0H')
    # for i in range(2,srow - 2):
    #     for j in range(k,scol+k):
    #         print(bg.canvas[i][j], end = "")
    #     print()
    # print('\033[0;0H')
    # for i in range(srow - 2, srow):
    #     for j in range(k,scol+k):
    #         print(bg.canvas[i][j], end = "")
    #     print()
    # print('\033[0;0H')
    if(nit == 1) :
        nittime = time.time()
        if time.time() - nittime >= 10 :
            nit = 0
    if person.lives > 0:
        k += 1
        test.moveperson(k , nit)
        move_bullet(k)
        # print(bullet.coor)
    else :
        if checkindex(person.jeta + 2 , person.jetb) == 'ok': 
            time.sleep(0.01)
            for i in range(3):
                for j in range(3):
                        bg.canvas[person.jeta + i][person.jetb + j] = ' '
            person.jeta += 1;
            if check_obs(person.jeta,person.jetb) == 1 :
                    person.lives -= 1
            for i in range(3):
                for j in range(3):
                    bg.canvas[person.jeta + i][person.jetb + j] = stick1[i][j]
        else :
            for i in range(3):
                    for j in range(3):
                        bg.canvas[person.jeta + i][person.jetb + j] = stick1[i][j]
            bg.canvas[person.jeta + i][person.jetb + j + 5] = ']'  
            time.sleep(0.5)

            for i in range(len(data)):
                for j in range(len(data[0])):
                    bg.canvas[30 + i][k + 40 + j] = data[i][j]
            for i in range(srow):
                for j in range(k,scol+k):
                    print(bg.canvas[i][j], end = "")
                print()
            print('\033[0;0H')







