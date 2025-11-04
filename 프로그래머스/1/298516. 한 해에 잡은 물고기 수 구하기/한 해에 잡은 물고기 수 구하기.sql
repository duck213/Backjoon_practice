-- 코드를 작성해주세요
select count(if(length > 10,length,0)) FISH_COUNT
from FISH_INFO
where time like '2021%';

