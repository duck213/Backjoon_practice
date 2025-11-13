select SUM(g.SCORE) SCORE, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
from HR_GRADE g
join HR_EMPLOYEES e on g.EMP_NO=e.EMP_NO
group by emp_no
order by SCORE DESC
limit 1
