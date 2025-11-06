select round(avg(COALESCE(length, 10)),2) AS AVERAGE_LENGTH
from fish_info;