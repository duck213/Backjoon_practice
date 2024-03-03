def solution(data, ext, val_ext, sort_by):
    answer = []
    srt = ["code","date","maximum","remain"]
    for i in range(len(data)):
        if data[i][srt.index(ext)] < val_ext: 
            answer.append(data[i])
    answer.sort(key=lambda x: x[srt.index(sort_by)])
    return answer