-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, 
    if(FREEZER_YN is null,'N',FREEZER_YN) FREEZER_YN
from food_warehouse
where WAREHOUSE_NAME like '%경기%'
order by warehouse_id asc;


