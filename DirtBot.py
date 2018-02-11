#!/usr/bin/python
def next_move(posr, posc, board):
    global moveset
    global dirset
    #DirtRadar
    dirtfound = False
    go_to= []
    move_i = 0
    dir_i = 0
    while not dirtfound and move_i < len(moveset):
        search = [min(max(posr+moveset[move_i][0]*dirset[dir_i][0],0),4),
                  min(max(posc+moveset[move_i][1]*dirset[dir_i][1],0),4)]
        if board[search[0]][search[1]] == 'd':
            dirtfound = True
            go_to = search
        else:
            dir_i += 1
            if dir_i > 3:
                move_i += 1
                dir_i = 0
                
    #end if no dirt found
    if not dirtfound:
        return 
        
    #Action
    if posr - go_to[0] != 0:
        print 'UP' if posr - go_to[0] > 0 else 'DOWN'
    elif posc - go_to[1] != 0:
        print 'LEFT' if posc - go_to[1] > 0 else 'RIGHT'
    else:
        print'CLEAN'
    return 
                  
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    moveset = [(x,y) for x in range(5) for y in range(5) for i in range(5) if x+y == i]
    moveset.sort(key=sum)
    dirset = [(1,1), (-1,1), (1,-1), (-1,-1)]
    next_move(pos[0], pos[1], board)