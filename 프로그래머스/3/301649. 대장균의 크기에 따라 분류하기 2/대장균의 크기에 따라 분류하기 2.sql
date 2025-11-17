SELECT ID, case
    when rk.pk <= 0.25 then 'CRITICAL'
    when rk.pk <= 0.5 then 'HIGH'
    when rk.pk <= 0.75 then 'MEDIUM'
    else 'LOW'
end 'COLONY_NAME'
FROM (SELECT ID, PERCENT_RANK() OVER 
      (ORDER BY size_of_colony DESC) as pk FROM ecoli_data) rk
order by id
