class background:
    def __init__(self,rowx,colx):
        self.canvas = [[' ' for i in range(colx)] for j in range(rowx)]
        self.rowx = rowx
        self.colx = colx
        for j in range(0,colx -2, 3): 
            self.canvas[0][j] = '_'
            self.canvas[0][j+1] = '|'
            self.canvas[0][j+2] = '_'
        for j in range(0,colx -2, 3): 
            self.canvas[1][j] = '_'
            self.canvas[1][j+1] = '_'
            self.canvas[1][j+2] = '|'
        for j in range(colx):
            self.canvas[rowx - 3][j] = '_'
            # self.canvas[rowx - 1][j+1] = '|'
        for j in range(0,colx-2,3):
            self.canvas[rowx - 2][j] = '_'
            self.canvas[rowx - 2][j+1] = '|'
            self.canvas[rowx - 2][j+2] = '_'
        for j in range(0,colx-2,3):
            self.canvas[rowx - 1][j] = '_'
            self.canvas[rowx - 1][j+1] = '_'
            self.canvas[rowx - 1][j+2] = '|'  
        # self.canvas[0][40] = 'J'

bg = background(54,2000)
temp = background(54,2000)