## ๐ป์๊ณ ๋ฆฌ์ฆ ํด๊ฒฐํ ๋ฌธ์ ๋ค๐ป  
### **[๋ฐฑ์ค](https://www.acmicpc.net/)**

| Level       | Problem number                                                                                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ๐ํผํผ ๊ธฐ๋ณธ๊ธฐ๐ | [1292](BOJ/1292.py)<br>[1978](BOJ/1978.py) [2309](BOJ/2309.py) [2460](BOJ/2460.py) [2501](BOJ/2501.py) [2581](BOJ/2581.py) [2609](BOJ/2609.py) [2693](BOJ/2693.py) [3460](BOJ/3460.py) [10818](BOJ/10818.py) [10870](BOJ/10870.py)  [DFS์BFS(1260)](BOJ/1260.py)<br>[ํ๊ท ์ ๋๊ฒ ์ง(4344)](BOJ/4344.py) <br>[RGB๊ฑฐ๋ฆฌ(1149)](BOJ/1149.py)<br>[๊ตญ์์(10825)](https://www.acmicpc.net/problem/10825) lambdaํจ์<br>[์๊ทผ์ด์ ์ฌํ(9372)](BOJ/9372.py) BFS                                                |
| ๐์ฝ์  ์ฒดํฌ๐ | [๊ฐ๋ฅด์นจ(1062)](BOJ/1062.py)<br> [์ธ๊ตฌ์ด๋(16234)](BOJ/16234.py) BFS ์ด์ฉํ ๋ฌธ์  ํ์ด<br> [์ด์ฐจ์ ๋ฐฐ์ด๊ณผ ์ฐ์ฐ(17140)](BOJ/17140.py) Collections-Counter <br> [์ด๋(1956)](BOJ/1956.py) ํ๋ก์ด๋์์   |

[์ฐธ๊ณ  ์๋ฃ](https://covenant.tistory.com/224)

### **[ํ๋ก๊ทธ๋๋จธ์ค](https://programmers.co.kr/)**

| Level       | Problem number                                                                                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ๐์ฝ๋ฉํ์คํธ ์ฐ์ต๐ | [ํฌ๋ ์ธ ์ธํ ๋ฝ๊ธฐ](PRO/64061.py)<br>[43165](PRO/43165.py)<br>[42746](PRO/42746.py)  <br>[42748](PRO/42748.py)<br>[42897](PRO/42897.py)<br>[42898](PRO/42898.py) <br>[42626](PRO/42626.py) <br>[42577](PRO/42577.py)<br>[42578](PRO/42578.py)                        |
| ๐Weekly Challenge๐ | [1์ฃผ์ฐจ](PRO/WeeklyChallenge/1์ฃผ์ฐจ.py)                    |
| ๐SQL๐ | LEVEL1 <br>[59034](PRO/59034.sql)<br>[59035](PRO/59035.sql)<br>[59036](PRO/59036.sql)<br>[59037](PRO/59037.sql)<br>[59039](PRO/59039.sql)<br>[59403](PRO/59403.sql)<br>[59404](PRO/59404.sql)<br>[59405](PRO/59405.sql)<br>[59407](PRO/59407.sql)<br>[59415](PRO/59415.sql)<br>[59038](PRO/59038.sql)<br> LEVEL2 <br> |



### **[๊ตฌ๋ฆ](https://level.goorm.io/)**

| Level       | Problem number                                                                                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ์ฝ๋ฉํ์คํธ์ฐ์ต | [๊ธธ์ฐพ๊ธฐ(๋ค์ด์๋ชฌ๋)](GOORM/43145.py)<br> [์ฝ์๊ฐ์์ธ๊ธฐ](GOORM/์ฝ์๊ฐ์์ธ๊ธฐ.py)<br> [์์ ์](GOORM/์์ ์.py)<br> [์ซ์๋ค์ง๊ธฐ](GOORM/.py)                    |


### mysql (MariaDB ์ฟผ๋ฆฌ ๋ฌธ๋ฒ ์ ๋ฆฌ)
+ DATE_FORMAT(๋ ์ง,ํ์) : ๋ ์ง๋ฅผ ์ง์ ํ ํ์์ผ๋ก ์ถ๋ ฅ <br> ํ์์ '%Y %m %d' ์ฌ์ฉ <br> hour(์๊ฐ๋ฐ์ดํฐ)๋ก ์๊ฐ ์ ๊ทผ ๊ฐ๋ฅ
+ SET @๋ณ์์ด๋ฆ := ์ด๊ธฐ๊ฐ;
+ NULL ์ฒ๋ฆฌํ๊ธฐ <br> NULL๊ฐ ์ฑ์ฐ๊ธฐ IFNULL(๋ณ์,'๋์ฒด ๊ฐ') <br> ๋ณ์ IS NULL (or ๋ณ์ IS NOT NULL)
+ ์ถ๋ ฅ ๊ฐ์๋ limit๋ก ์ ํ ex) order by ๋ณ์ limit ๊ฐ์ <br> 3๋ฒ์งธ row๋ถํฐ 11๋ฒ์งธ row๊น์ง ์กฐํ Limit 2,10;
+ ๋ฐ์ดํฐ ๊ฐ์, ์นด์ดํธ(COUNT) ex) count(*) ์ ์ฒด ๊ฐ์, COUNT(์ปฌ๋ผ) ํน์  ์ปฌ๋ผ์ ๊ฐ์
+ ๊ธ์ ๋น๊ต๋ like ex) ๋ณ์ like 'happy%' -- ์๊ธ์๊ฐ happy๋ก ์์ํ๋ ๋จ์ด <br> '%happy' ๋๋ถ๋ถ์ด happy์ธ ๊ฒฝ์ฐ, '%happy%' happy๊ฐ ๋ค์ด๊ฐ๋ ๋ชจ๋  ๊ฐ
+ ํน์  ์ปฌ๋ผ์ ๊ทธ๋ฃนํ ํ๋ GROUP BY, ํน์  ์ปฌ๋ผ์ ๊ทธ๋ฃนํํ ๊ฒฐ๊ณผ์ ์กฐ๊ฑด์ ๊ฑฐ๋ HAVING <br> WHERE์ ๊ทธ๋ฃนํ ํ๊ธฐ ์ , HAVING์ ๊ทธ๋ฃน ํ ์กฐ๊ฑด

#### [ํ๋ก๊ทธ๋๋จธ์ค-์์ ์๊ฐ ๊ตฌํ๊ธฐ1](PRO/59412.sql)

 
    SELECT DATE_FORMAT(DATETIME,'%H') AS H, COUNT(DATETIME)
    FROM ANIMAL_OUTS
    GROUP BY H
    HAVING H BETWEEN 9 AND 19
    ORDER BY H

#### [ํ๋ก๊ทธ๋๋จธ์ค-์์ ์๊ฐ ๊ตฌํ๊ธฐ2](PRO/59413.sql)

    SET @TIME := -1;
    SELECT (@TIME := @TIME + 1), (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @TIME)
    FROM ANIMAL_OUTS
    WHERE @TIME <23
    
#### [ํ๋ก๊ทธ๋๋จธ์ค-์ค๋ ๊ธฐ๊ฐ ๋ณดํธ ๋๋ฌผ1](PRO/59044.sql)

    SET ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.DATETIME
    FROM ANIMAL_INS
    WHERE ANIMAL_INS.ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS)
    ORDER BY ANIMAL_INS.DATETIME
    LIMIT 3;

#### LIKE 
    
    SELECT *
    FROM STUDENT
    WHERE STUDENT_ID like 'a%'
    
    LIKE 'a%' a๋ก ์์ํ๋ ๋ชจ๋  ๊ฐ
    LIKE 'a_%_%' a๋ก ์์๋๊ณ  ์ต์ 3์ด์ ๊ธธ์ด๋ฅผ ๊ฐ์ง ๊ฐ
    LIKE '_a%' ๋๋ฒ์จฐ ์๋ฆฌ๊ฐ a์ธ ๋ชจ๋  ๊ฐ
    
#### Between
  where ์  ๋ด ๊ฒ์ ์กฐ๊ฑด์ผ๋ก ๋ฒ์๋ฅผ ์ง์ ํ๊ณ ์ ํ  ๋
  
    select *
    from products
    wher price between 10 and 20
    
    select *
    from products
    where price not between 10 and 20

#### ์ค๋ณต ์ ๊ฑฐ (DISTINCT, GROUP BY)

    SELECT COUNT(DISTINCT NAME) AS NAME_COUNT 
    FROM ANIMAL_INS 
    WHERE NAME IS NOT NULL
    
    SELECT COUNT(NAME) 
    FROM ANIMAL_INS
    WHERE NAME IS NOT NULL
    GROUP BY NAME;

#### JOIN ๊ตฌ๋ฌธ
  
  ##### 1. INNER JOIN ๊ตฌ๋ฌธ
  tabel1, table2์ ์ผ์น๋๋ same_feature ๋ด์ฉ์ ๊ฐ์ ธ์จ๋ค
  
    select table1.name, tabel2.date
    from table1
    inner join table2
    on tabel1.same_feature = tabel2.same_feature
    oreder by tabel1.name;
    
      
 ##### 2. LEFT JOIN ๊ตฌ๋ฌธ(LEFT๋ฅผ ํฌํจํ ๊ต์งํฉ)
 tabel1์ ๊ธฐ์ค์ผ๋ก table2์ ์ผ์น๋๋ same_feature ๋ด์ฉ์ table1 ๋ค์ ๋ถ์ด๊ณ  ๋ถ์ผ์น ๋ฐ์ดํฐ๋ NULL ์ฑ์
  
    select *
    from table1
    left join table2
    on tabel1.same_feature = tabel2.same_feature
    
  ##### 3. RIGHT JOIN ๊ตฌ๋ฌธ(RIGHT๋ฅผ ํฌํจํ ๊ต์งํฉ)
 tabel2์ ๊ธฐ์ค์ผ๋ก table1์ ์ผ์น๋๋ same_feature ๋ด์ฉ์ table1 ๋ค์ ๋ถ์ด๊ณ  ๋ถ์ผ์น ๋ฐ์ดํฐ๋ NULL ์ฑ์<br>
 right join table => talbe์ ์ค์ฌ์ผ๋ก 
  
    select *
    from table1
    right join table2
    on tabel1.same_feature = tabel2.same_feature
    
#### CASE WHEN ๊ตฌ๋ฌธ  

    select col1, col2, case when ์กฐ๊ฑด1 then ๊ฐ1 when ์กฐ๊ฑด2 then ๊ฐ2 else ๊ฐ3 end as ์๋ก์ด ์ปฌ๋ผ ์ด๋ฆ
    from table1
    
    -- ์กฐ๊ฑด์ ํฌํจ๋์ง ์๋ ๊ฒฝ์ฐ๋ง ๋ค๋ฅธ when์ผ๋ก ๋ด๋ ค๊ฐ! 
    select *,(
      case
         when size < 10 then 'small'
         when size < 30 then 'medium'
         when size < 50 then 'large'
         else 'extra'
      end) as 'ํฌ๊ธฐ'
    from datatable
   
   
   

