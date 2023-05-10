-- 코드를 입력하세요
SELECT B.BOOK_ID, A.AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK AS B, AUTHOR AS A
WHERE B.AUTHOR_ID = A.AUTHOR_ID AND B.CATEGORY = '경제'
ORDER BY PUBLISHED_DATE
;