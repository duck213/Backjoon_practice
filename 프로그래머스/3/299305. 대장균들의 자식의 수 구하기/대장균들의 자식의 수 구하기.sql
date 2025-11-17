select ID, (
    select count(*)
    from ECOLI_DATA
    where parent_id = e.id
) CHILD_COUNT
from ECOLI_DATA e
order by id
