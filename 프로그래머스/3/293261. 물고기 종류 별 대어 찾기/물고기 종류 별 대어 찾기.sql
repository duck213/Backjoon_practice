SELECT i.ID, na.FISH_NAME, i.LENGTH
FROM fish_info i
JOIN FISH_NAME_INFO na ON i.FISH_TYPE=na.FISH_TYPE
where (na.fish_type, i.LENGTH) IN (
    select fish_type, MAX(length)
    from fish_info
    group by fish_type)
ORDER BY i.ID asc;