select count(*) FISH_COUNT
from fish_info
group by length
having length<10 or length is null;