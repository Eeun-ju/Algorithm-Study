-- 코드를 입력하세요
SET @hour := -1;
SELECT (@hour := @hour +1) as 'HOUR', (SELECT COUNT(*) FROM ANIMAL_OUTS where hour(datetime) = @hour) as 'COUNT'
from
animal_outs
where 
@hour<23
