## 💻알고리즘 해결한 문제들💻  
### **[백준](https://www.acmicpc.net/)**

| Level       | Problem number                                                                                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 😃튼튼 기본기😃 | [1292](BOJ/1292.py)<br>[1978](BOJ/1978.py) [2309](BOJ/2309.py) [2460](BOJ/2460.py) [2501](BOJ/2501.py) [2581](BOJ/2581.py) [2609](BOJ/2609.py) [2693](BOJ/2693.py) [3460](BOJ/3460.py) [10818](BOJ/10818.py) [10870](BOJ/10870.py)  [DFS와BFS(1260)](BOJ/1260.py)<br>[평균은 넘겠지(4344)](BOJ/4344.py) <br>[RGB거리(1149)](BOJ/1149.py)<br>[국영수(10825)](https://www.acmicpc.net/problem/10825) lambda함수<br>[상근이의 여행(9372)](BOJ/9372.py) BFS                                                |
| 👍약점 체크👍 | [가르침(1062)](BOJ/1062.py)<br> [인구이동(16234)](BOJ/16234.py) BFS 이용한 문제 풀이<br> [이차원 배열과 연산(17140)](BOJ/17140.py) Collections-Counter <br> [운동(1956)](BOJ/1956.py) 플로이드워셜   |

[참고 자료](https://covenant.tistory.com/224)

### **[프로그래머스](https://programmers.co.kr/)**

| Level       | Problem number                                                                                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 😃코딩테스트 연습😃 | [크레인 인형 뽑기](PRO/64061.py)                     |
| 👍SQL👍 | LEVEL1 <br>[59034](PRO/59034.sql)<br>[59035](PRO/59035.sql)<br>[59036](PRO/59036.sql)<br>[59037](PRO/59037.sql)<br>[59039](PRO/59039.sql)<br>[59403](PRO/59403.sql)<br>[59404](PRO/59404.sql)<br>[59405](PRO/59405.sql)<br>[59407](PRO/59407.sql)<br>[59415](PRO/59415.sql)<br>[59038](PRO/59038.sql)<br> LEVEL2 <br>|



### **[구름](https://level.goorm.io/)**

| Level       | Problem number                                                                                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 코딩테스트연습 | [길찾기(다이아몬드)](GOORM/43145.py)                     |


### mysql (MariaDB 쿼리 문법 정리)
+ DATE_FORMAT(날짜,형식) : 날짜를 지정한 형식으로 출력 <br> 형식은 '%Y %m %d' 사용 <br> hour(시간데이터)로 시간 접근 가능
+ SET @변수이름 := 초기값;
+ NULL 처리하기 <br> NULL값 채우기 IFNULL(변수,'대체 값') <br> 변수 IS NULL (or 변수 IS NOT NULL)
+ 출력 개수는 limit로 제한 ex) order by 변수 limit 개수 <br> 3번째 row부터 11번째 row까지 조회 Limit 2,10;
+ 데이터 개수, 카운트(COUNT) ex) count(*) 전체 개수, COUNT(컬럼) 특정 컬럼의 개수
+ 글자 비교는 like ex) 변수 like 'happy%' -- 앞글자가 happy로 시작하는 단어 <br> '%happy' 끝부분이 happy인 경우, '%happy%' happy가 들어간느 모든 값
+ 특정 컬럼을 그룹화 하는 GROUP BY, 특정 컬럼을 그룹화한 결과에 조건을 거는 HAVING <br> WHERE은 그룹화 하기 전, HAVING은 그룹 후 조건

#### [프로그래머스-입양 시각 구하기1](PRO/59412.sql)

 
    SELECT DATE_FORMAT(DATETIME,'%H') AS H, COUNT(DATETIME)
    FROM ANIMAL_OUTS
    GROUP BY H
    HAVING H BETWEEN 9 AND 19
    ORDER BY H

#### [프로그래머스-입양 시각 구하기2](PRO/59413.sql)

    SET @TIME := -1;
    SELECT (@TIME := @TIME + 1), (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @TIME)
    FROM ANIMAL_OUTS
    WHERE @TIME <23
    
#### [프로그래머스-오랜 기간 보호 동물1](PRO/59044.sql)

    SET ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.DATETIME
    FROM ANIMAL_INS
    WHERE ANIMAL_INS.ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS)
    ORDER BY ANIMAL_INS.DATETIME
    LIMIT 3;

#### LIKE 
    
    SELECT *
    FROM STUDENT
    WHERE STUDENT_ID like 'a%'
    
    LIKE 'a%' a로 시작하는 모든 값
    LIKE 'a_%_%' a로 시작되고 최소 3이상 길이를 가진 값
    LIKE '_a%' 두번쨰 자리가 a인 모든 값
    
#### Between
  where 절 내 검색 조건으로 범위를 지정하고자 할 때
  
    select *
    from products
    wher price between 10 and 20
    
    select *
    from products
    where price not between 10 and 20

#### 중복 제거 (DISTINCT, GROUP BY)

    SELECT COUNT(DISTINCT NAME) AS NAME_COUNT 
    FROM ANIMAL_INS 
    WHERE NAME IS NOT NULL
    
    SELECT COUNT(NAME) 
    FROM ANIMAL_INS
    WHERE NAME IS NOT NULL
    GROUP BY NAME;

#### JOIN 구문
  
  ##### 1. INNER JOIN 구문
  tabel1, table2의 일치되는 same_feature 내용을 가져온다
  
    select table1.name, tabel2.date
    from table1
    inner join table2
    on tabel1.same_feature = tabel2.same_feature
    oreder by tabel1.name;
    
      
 ##### 2. LEFT JOIN 구문(LEFT를 포함한 교집합)
 tabel1을 기준으로 table2의 일치되는 same_feature 내용을 table1 뒤에 붙이고 불일치 데이터는 NULL 채움
  
    select *
    from table1
    left join table2
    on tabel1.same_feature = tabel2.same_feature
    
  ##### 3. RIGHT JOIN 구문(RIGHT를 포함한 교집합)
 tabel2을 기준으로 table1의 일치되는 same_feature 내용을 table1 뒤에 붙이고 불일치 데이터는 NULL 채움<br>
 right join table => talbe을 중심으로 
  
    select *
    from table1
    right join table2
    on tabel1.same_feature = tabel2.same_feature
    
#### CASE WHEN 구문  

    select col1, col2, case when 조건1 then 값1 when 조건2 then 값2 else 값3 end as 새로운 컬럼 이름
    from table1
    
    -- 조건에 포함되지 않는 경우만 다른 when으로 내려감! 
    select *,(
      case
         when size < 10 then 'small'
         when size < 30 then 'medium'
         when size < 50 then 'large'
         else 'extra'
      end) as '크기'
    from datatable
   
   
   

