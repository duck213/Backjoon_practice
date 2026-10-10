def solution(video_len, pos, op_start, op_end, commands):
    video_sec = int(video_len[0:2])*60 + int(video_len[3:])
    op_start_sec = int(op_start[0:2])*60 + int(op_start[3:])
    op_end_sec = int(op_end[0:2])*60 + int(op_end[3:])
    pos_sec = int(pos[0:2])*60 + int(pos[3:])
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec
        
    for i in commands:
        if i == 'next':
            if pos_sec+10 <= video_sec:
                pos_sec+=10
            elif pos_sec+10 > video_sec:
                pos_sec = video_sec    
        elif i == 'prev':
            if pos_sec-10 < 0:
                pos_sec=0
            else:
                pos_sec-=10
        
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
        #print(pos_sec)
    answer = str(pos_sec//60).zfill(2)+':'+str(pos_sec%60).zfill(2)
    return answer