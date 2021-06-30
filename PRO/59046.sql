-- 이름 해당하는 값 가져오기 where in 사용
SELECT animal_id, name, SEX_UPON_INTAKE
from animal_ins
where name in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by animal_id; 