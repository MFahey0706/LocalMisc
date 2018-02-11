#!/usr/bin/python
#modify existing function to observe all adjacent cells (replace while with for)
#build out your own view of the board as you explore it
#if you find no dirt in the visible radius, look instead for unobserved cells
#use radar to find unobserved cells and travel towards nearest one

#!/usr/bin/python
def next_move(posr, posc, board):
    global moveset
    global dirset
    global observed
    
    #Record immediate surroundings
    for m in moveset[0:3]: #only (0,1), (1,0), and (1,1) are visible
        for d in dirset:
            search = [min(max(posr+m[0]*d[0],0),4),
                  min(max(posc+m[1]*d[1],0),4)]
            
            observed[search[0]][search[1]] = board[search[0]][search[1]]
            
    #find visible dirt
    dirtfound = False
    go_to= []
    move_i = 0
    dir_i = 0
    while not dirtfound and move_i < len(moveset):
        search = [min(max(posr+moveset[move_i][0]*dirset[dir_i][0],0),4),
                  min(max(posc+moveset[move_i][1]*dirset[dir_i][1],0),4)]
        
        if observed[search[0]][search[1]] == 'd':
            dirtfound = True
            go_to = search
        else:
            dir_i += 1
            if dir_i > 3:
                move_i += 1
                dir_i = 0
    
    #if dirtfound, go get it
    if dirtfound:
        #Action
        if posr - go_to[0] != 0:
            print 'UP' if posr - go_to[0] > 0 else 'DOWN'
        elif posc - go_to[1] != 0:
            print 'LEFT' if posc - go_to[1] > 0 else 'RIGHT'
        else:
            print'CLEAN'
        return
        
    # if no dirtfound, chart new territory
    else:
        scout = False
        go_to= []
        move_i = 4 #start at (2,0)
        dir_i = 0
        while not scout and move_i < len(moveset):
            search = [min(max(posr+moveset[move_i][0]*dirset[dir_i][0],0),4),
                      min(max(posc+moveset[move_i][1]*dirset[dir_i][1],0),4)]
            if observed[search[0]][search[1]] == 'o':
                scout = True
                go_to = search
            else:
                dir_i += 1
                if dir_i > 3:
                    move_i += 1
                    dir_i = 0
                    
    #go to the new land                
    if scout:
        if posr - go_to[0] != 0:
            print 'UP' if posr - go_to[0] > 0 else 'DOWN'
        elif posc - go_to[1] != 0:
            print 'LEFT' if posc - go_to[1] > 0 else 'RIGHT'
        else:
            print 'LOOK UNDER YOURSELF, ROBOT'
        return
        
    #the world has been explored, and has been found to be clean
    else:
        return
                    
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    moveset = [(x,y) for x in range(5) for y in range(5) for i in range(9) if x+y == i]
    moveset.sort(key=sum)
    dirset = [(1,1), (-1,1), (1,-1), (-1,-1)]
    observed = [['o','o','o','o','o'],['o','o','o','o','o'],['o','o','o','o','o'],['o','o','o','o','o'],['o','o','o','o','o']]
    next_move(pos[0], pos[1], board)
