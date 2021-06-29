-- 보호소 중성화 동물 글자 비교는 like사용하기
SELECT animal_outs.animal_id, animal_outs.ANIMAL_TYPE,animal_outs.name
from animal_ins,animal_outs
where animal_ins.animal_id = animal_outs.animal_id
and animal_ins.SEX_UPON_INTAKE like 'Intact%'
and (animal_outs.SEX_UPON_OUTCOME like 'Neutered Male' or animal_outs.SEX_UPON_OUTCOME LIKE 'Spayed Female')
order by animal_ins.ANIMAL_ID;