-- 코드를 입력하세요
SELECT HOUR(datetime) HOUR, count(HOUR(datetime)) COUNT
from animal_outs
where 09 <= HOUR(datetime) and 19 >= HOUR(datetime)
group by HOUR(datetime)
order by HOUR(datetime);
# SELECT date_format(datetime, '%h:%i:%s') FROM `sandbox2` WHERE id=1