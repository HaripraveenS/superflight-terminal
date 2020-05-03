from back import bg

class strt_obstacle:
    def __init__(self ,st_x,st_y):
        self.obs_st_x = st_x
        self.obs_st_y = st_y
        for i in range(self.obs_st_x , self.obs_st_x + 15):
            bg.canvas[i][self.obs_st_y] = '|'
            bg.canvas[i][self.obs_st_y + 1] = '|'

class diag_obstacle:
    def __init__(self ,st_x,st_y):
        self.obs_st_x = st_x
        self.obs_st_y = st_y
        for i in range(15):
            bg.canvas[self.obs_st_x + i][self.obs_st_y + i] = '\\'
            bg.canvas[self.obs_st_x + i][self.obs_st_y + i + 1] ='\\' 
class hrzn_obstacle:
    def __init__(self ,st_x,st_y):
        self.obs_st_x = st_x
        self.obs_st_y = st_y
        for i in range(25):
            bg.canvas[ self.obs_st_x][self.obs_st_y + i] = '_'
            bg.canvas[ self.obs_st_x + 1][self.obs_st_y + i] = '_'





