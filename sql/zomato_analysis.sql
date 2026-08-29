-- Zomato Bengaluru Restaurant Analysis
-- Dataset: compact public sample
-- Purpose: demonstrate SQL analysis for restaurant/business insights

-- 1. Restaurant count by location
SELECT location, COUNT(*) AS restaurant_count
FROM zomato_sample
WHERE location IS NOT NULL AND TRIM(location) <> ''
GROUP BY location
ORDER BY restaurant_count DESC;

-- 2. Average rating and votes by restaurant type
SELECT
    rest_type,
    COUNT(*) AS restaurant_count,
    ROUND(AVG(rate), 2) AS avg_rating,
    SUM(votes) AS total_votes
FROM zomato_sample
WHERE rest_type IS NOT NULL
GROUP BY rest_type
ORDER BY avg_rating DESC;

-- 3. Online-order availability
SELECT
    online_order,
    COUNT(*) AS restaurant_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentage
FROM zomato_sample
GROUP BY online_order
ORDER BY restaurant_count DESC;

-- 4. Book-table availability
SELECT
    book_table,
    COUNT(*) AS restaurant_count
FROM zomato_sample
GROUP BY book_table
ORDER BY restaurant_count DESC;

-- 5. Top restaurants by votes
SELECT name, location, rate, votes, cuisines
FROM zomato_sample
WHERE votes IS NOT NULL
ORDER BY votes DESC
LIMIT 10;

-- 6. Most common cuisines
-- If cuisines contains comma-separated values, this query can be adapted
-- using the string-splitting function supported by your SQL database.
SELECT cuisines, COUNT(*) AS restaurant_count
FROM zomato_sample
WHERE cuisines IS NOT NULL AND TRIM(cuisines) <> ''
GROUP BY cuisines
ORDER BY restaurant_count DESC
LIMIT 10;

-- 7. High-rated restaurants with strong review volume
SELECT name, location, rate, votes, cuisines
FROM zomato_sample
WHERE rate >= 4.0
  AND votes >= 1000
ORDER BY rate DESC, votes DESC;

-- 8. Restaurant types with the largest footprint
SELECT rest_type, COUNT(*) AS restaurant_count
FROM zomato_sample
WHERE rest_type IS NOT NULL
GROUP BY rest_type
ORDER BY restaurant_count DESC
LIMIT 10;
