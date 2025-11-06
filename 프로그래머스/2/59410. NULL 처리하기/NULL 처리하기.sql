select ANIMAL_TYPE, 

case
when name is not null then NAME
else 'No name'
end NAME, 
SEX_UPON_INTAKE

from animal_ins
order by animal_id;