-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, SUM(F.TOTAL_ORDER) AS TOTAL_ORDER
FROM ICECREAM_INFO AS I
INNER JOIN FIRST_HALF AS F
ON SHIPMENT_ID
WHERE I.FLAVOR = F.FLAVOR
GROUP BY INGREDIENT_TYPE
ORDER BY TOTAL_ORDER
;