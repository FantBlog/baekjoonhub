-- 코드를 입력하세요
SELECT COUNT(A.NAME) AS count
FROM (SELECT NAME
      FROM ANIMAL_INS
      GROUP BY NAME
      ) AS A
;