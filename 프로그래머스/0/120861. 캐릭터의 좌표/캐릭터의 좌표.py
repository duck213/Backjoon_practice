def solution(keyinput, board):
    x,y = 0,0
    x_limit,y_limit = board
    x_limit,y_limit = (x_limit-1)//2,(y_limit-1)//2
    for item in keyinput:
        if -x_limit<x and item=='left':
            x-=1
        elif -y_limit<y and item=='down':
            y-=1
        elif y_limit>y and item=='up':
            y+=1
        elif x_limit>x and item=='right':
            x+=1
    return [x,y]