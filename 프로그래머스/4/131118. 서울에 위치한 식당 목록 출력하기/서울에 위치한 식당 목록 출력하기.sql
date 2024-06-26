-- 코드를 입력하세요
-- 식당아이디, 식당이름, 음식종류, 즐겨찾기수, 주소, 리뷰 평균 점수
SELECT a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS, ROUND(AVG(b.REVIEW_SCORE),2) as SCORE
FROM REST_INFO as a
INNER JOIN REST_REVIEW as b
ON a.REST_ID = b.REST_ID
GROUP BY b.REST_ID
HAVING SUBSTR(a.ADDRESS,1,2) = "서울"
ORDER BY SCORE DESC, a.FAVORITES DESC