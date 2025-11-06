-- 코드를 입력하세요
SELECT b.book_id, a.author_name, date_format(b.published_date,'%Y-%m-%d') published_date
from BOOK b
join AUTHOR a on a.author_id=b.author_id
where category='경제'
order by 3;