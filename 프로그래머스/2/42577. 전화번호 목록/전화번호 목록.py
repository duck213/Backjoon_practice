def solution(phone_book):
    answer = True
    book = sorted(phone_book)
    if len(book) == 1:
        return answer

    for i in range(0,len(book)-1):
        if book[i+1].startswith(book[i]):
            answer = False
            return answer
        else:
            pass
            
    return answer
