-- 오랜 기간 보호한 동물 order by로 sort하고 limit으로 추출하기
SELECT animal_outs.animal_id,animal_outs.name
from animal_ins, animal_outs
where animal_ins.animal_id = animal_outs.animal_id
order by (animal_outs.datetime - animal_ins.datetime) DESC 
limit 2;