from back import bg, temp

coor_x = []
coor_y = []
flg_bulla = []
def move_bullet(k) :
    for i in range(len(coor_x)):    
        if coor_y[i] < 205 + k and flg_bulla[i] :
            bg.canvas[coor_x[i]][coor_y[i]] = temp.canvas[coor_x[i]][coor_y[i]]
            bg.canvas[coor_x[i]][coor_y[i]  + 1] = temp.canvas[coor_x[i]][coor_y[i] + 1]
            # for i in range(1,5) :
            for j in range (1,5) :                
                temp.canvas[coor_x[i]][coor_y[i] + j] = bg.canvas[coor_x[i]][coor_y[i] + j] 
                # clear_obstacle(coor_x[i], coor_y[i] + i)
            clear_obstacle(coor_x[i], coor_y[i] + 1)
            clear_obstacle(coor_x[i], coor_y[i] + 2)
            clear_obstacle(coor_x[i], coor_y[i] + 3)
            clear_obstacle(coor_x[i], coor_y[i] + 4)
            coor_y[i] += 3
            bg.canvas[coor_x[i]][coor_y[i]] = '='
            bg.canvas[coor_x[i]][coor_y[i] + 1] = '>'
        else :
            flg_bulla[i] = 0
            bg.canvas[coor_x[i]][coor_y[i]] = temp.canvas[coor_x[i]][coor_y[i]]
            bg.canvas[coor_x[i]][coor_y[i]  + 1] = temp.canvas[coor_x[i]][coor_y[i] + 1]
 

def check_diag(x , y):
    co_x = x
    co_y = y
    # if(bg.canvas[co_x][co_y] == '\\') :
    while(bg.canvas[co_x][co_y] == '\\'):
        bg.canvas[co_x][co_y] = ' '
        co_x -= 1
        co_y -= 1
    co_x = x + 1
    co_y = y + 1
    while(bg.canvas[co_x][co_y] == '\\'):
        bg.canvas[co_x][co_y] = ' '
        co_x += 1
        co_y += 1
    co_x = x
    co_y = y + 1
    while(bg.canvas[co_x][co_y] == '\\'):
        bg.canvas[co_x][co_y] = ' '
        co_x += 1
        co_y += 1
    co_x = x - 1
    co_y = y 
    while(bg.canvas[co_x][co_y] == '\\'):
        bg.canvas[co_x][co_y] = ' '
        co_x -= 1
        co_y -= 1
def clear_obstacle(co_x, co_y):
    tem_x = co_x
    tem_y = co_y
    for i in range(-3 , 4) :
        check_diag(co_x + i , co_y + i)
    while(bg.canvas[co_x][co_y] == '|'):
        bg.canvas[co_x][co_y] = ' '
        co_x -= 1
    co_x = tem_x + 1
    while(bg.canvas[co_x][co_y] == '|'):
        bg.canvas[co_x][co_y] = ' '
        co_x += 1
    co_x = tem_x - 1
    while(bg.canvas[co_x][co_y + 1] == '|'):
        bg.canvas[co_x][co_y + 1] = ' '
        co_x -= 1
    co_x = tem_x + 1
    while(bg.canvas[co_x][co_y + 1] == '|'):
        bg.canvas[co_x][co_y + 1] = ' '
        co_x += 1

    co_x = tem_x
    co_y = tem_y

    while(bg.canvas[co_x][co_y] == '_'):
        bg.canvas[co_x][co_y] = ' '
        co_y += 1
    co_y = tem_y

    while(bg.canvas[co_x - 1][co_y] == '_'):
        bg.canvas[co_x - 1][co_y] = ' '
        co_y += 1
    co_y = tem_y
    while(bg.canvas[co_x + 1][co_y] == '_'):
        bg.canvas[co_x + 1][co_y] = ' '
        co_y += 1
    co_y = tem_y
    while(bg.canvas[co_x - 2][co_y] == '_'):
        bg.canvas[co_x - 2][co_y] = ' '
        co_y += 1
    co_y = tem_y
    while(bg.canvas[co_x + 2][co_y] == '_'):
        bg.canvas[co_x + 2][co_y] = ' '
        co_y += 1
    co_y = tem_y
