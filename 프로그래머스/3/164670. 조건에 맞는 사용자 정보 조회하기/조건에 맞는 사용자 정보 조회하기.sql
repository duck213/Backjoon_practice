SELECT u.USER_ID, u.NICKNAME, 
CONCAT(u.CITY,' ',u.STREET_ADDRESS1, ' ',u.STREET_ADDRESS2) '전체주소', 
CONCAT(substring(TLNO, 1, 3),'-',substring(TLNO, 4, 4),'-', substring(TLNO, 8, 4)) '전화번호'

FROM USED_GOODS_BOARD b
JOIN USED_GOODS_USER u ON b.WRITER_ID=u.USER_ID
#WHERE b.status = 'DONE'
group by u.user_id
having COUNT(b.board_id) >= 3 and COUNT(b.status='DONE') >= 3
ORDER BY u.user_id DESC;
