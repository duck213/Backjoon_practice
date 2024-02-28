def solution(wallpaper):
    min_x,min_y,max_x,max_y = len(wallpaper),len(wallpaper[0]),0,0
    for row in range(len(wallpaper)):
        for item in range(len(wallpaper[row])):
            if wallpaper[row][item] == '#':
                if min_x > row:
                    min_x = row
                if max_x < row:
                    max_x = row
                if min_y > item:
                    min_y = item
                if max_y < item:
                    max_y = item
    return [min_x,min_y,max_x+1,max_y+1]