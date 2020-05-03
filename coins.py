from back import bg
from random import randint
class coin:
    def __init__(self , stx , sty , secs , sece):
        if(stx - 5  > 3 and sty - secs > 20):
            # print(stx)
            self.nx = randint(3,stx) 
            self.ny = randint(secs,sty)
            for i in range(self.nx,self.nx + 5):
                for j in range(self.ny, self.ny + 20):
                    bg.canvas[i][j] = '0'
        elif (stx + 5 < 52 and sty - secs > 20):
            self.nx = randint(stx,47)
            self.ny = randint(secs,sty)
            for i in range(self.nx,self.nx + 5):
                for j in range(self.ny, self.ny + 20):
                    bg.canvas[i][j] = '0'
        elif (stx - 5 > 3 and sece - sty > 20):
            self.nx = randint(3, stx)
            self.ny = randint(sty , sece)
            for i in range(self.nx,self.nx + 5):
                for j in range(self.ny, self.ny + 20):
                    bg.canvas[i][j] = '0'
        elif (stx + 5 < 52 and sece - sty > 20):
            self.nx = randint(stx,47) 
            self.ny = randint(sty,sece)
            for i in range(self.nx,self.nx + 5):
                for j in range(self.ny, self.ny + 20):
                    bg.canvas[i][j] = '0'            
