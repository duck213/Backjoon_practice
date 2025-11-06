select HISTORY_ID, CAR_ID, date_format(start_date,'%Y-%m-%d') START_DATE, date_format(end_date,'%Y-%m-%d') END_DATE, 
  CASE 
  WHEN (DATEDIFF(END_DATE,START_DATE)+1) >= 30 THEN '장기 대여'
  ELSE '단기 대여'
END 'RENT_TYPE'
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where date_format(start_date,'%Y-%m') = '2022-09'
order by history_id desc;