-- 이름에 el이 들어가는 동물 찾기 : name like '%el%'
SELECT animal_id, name
from animal_ins
where animal_type = 'Dog'
and name like '%el%'
order by name;