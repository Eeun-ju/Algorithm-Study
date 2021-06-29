-- 오랜 기간 보호한 동물 : 입양을 가지 못한 동물이 3마리 이상인 경우 출력

SELECT animal_ins.name, animal_ins.datetime
from animal_ins
where animal_ins.ANIMAL_ID NOT IN ( SELECT animal_outs.ANIMAL_ID FROM ANIMAL_OUTS)
order by animal_ins.datetime limit 3;