SELECT f.flavor
FROM FIRST_HALF f
JOIN ICECREAM_INFO info on f.flavor=info.flavor 
WHERE f.TOTAL_ORDER > 3000 and info.ingredient_type='fruit_based'
ORDER BY TOTAL_ORDER desc;