-- 코드를 입력하세요
SELECT USED_GOODS_BOARD.TITLE, USED_GOODS_BOARD.BOARD_ID, USED_GOODS_REPLY.REPLY_ID, USED_GOODS_REPLY.WRITER_ID, USED_GOODS_REPLY.CONTENTS, date_format(USED_GOODS_REPLY.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD
INNER JOIN USED_GOODS_REPLY
ON USED_GOODS_BOARD.BOARD_ID = USED_GOODS_REPLY.BOARD_ID
WHERE USED_GOODS_BOARD.created_date LIKE '2022-10-%'
ORDER BY USED_GOODS_REPLY.CREATED_DATE, TITLE;