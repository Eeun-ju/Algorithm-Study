SELECT animal_ins.ANIMAL_ID, animal_ins.name
from animal_ins, animal_outs
where animal_ins.datetime > animal_outs.datetime and animal_ins.animal_id = animal_outs.animal_id
order by animal_ins.datetime;