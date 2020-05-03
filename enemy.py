from person import *
from back import bg

enem = [['E' for i in range(6)] for j in range(10)]

with open('enemy.txt') as f:
    en = f.readlines()
en = [row.rstrip('\n') for row in en]

class enemy:
    def __init__(co_x, k) :
        for i in range(len(en)) :
            for j in range(len(en[i])):
                


    
