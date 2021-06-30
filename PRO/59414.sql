-- date_format을 이용한 날짜 변경
SELECT animal_id, name, date_format(datetime,'%Y-%m-%d') as '날짜'
from animal_ins
order by animal_id;