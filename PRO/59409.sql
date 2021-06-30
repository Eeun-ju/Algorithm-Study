-- 컬럼 값을 다른 변수로 바꾸기 : case when 경우 then 값 else 값 
SELECT animal_id, name, case when (sex_upon_intake like '%Neutered%') or (sex_upon_intake like '%Spayed%') then 'O' else 'X' end as '중성화'
from animal_ins
order by animal_id