DROP TABLE IF EXISTS hemnet;

-- Creates the hemnet table from the CSV file
CREATE TABLE hemnet AS
SELECT * FROM read_csv_auto('D:/hemnet_data_clean.csv');

-- Shows the table structure
desc;

-- Select all to view the data
SELECT * FROM hemnet;

-- Find out number of rows
SELECT COUNT(*) AS total_rows
FROM hemnet;

-- Show the 5 most expensive properties
SELECT * FROM hemnet
ORDER BY final_price DESC
LIMIT 5;

-- Show the 5 least expensive properties
SELECT * FROM hemnet
ORDER BY final_price ASC
LIMIT 5;

-- Summary statistics from this dataset (prices)
SELECT
	MIN (final_price) AS min_price,
	MAX(final_price) AS max_price,
	AVG (final_price) AS AVG_price,
	MEDIAN(final_price) AS median_price
FROM
	hemnet;

-- Summary statistics from this dataset (price per square meter)
SELECT
	MIN (price_per_area) AS min_price,
	MAX(price_per_area) AS max_price,
	AVG (price_per_area) AS AVG_price,
	MEDIAN(price_per_area) AS median_price
FROM
	hemnet;

-- Find number of unique values for commune column
SELECT COUNT (DISTINCT commune)
FROM hemnet;

-- Find number of unique municipalities
SELECT COUNT(DISTINCT trim(split_part(commune, ',', 2))) AS nr_kommun
FROM hemnet;

-- Calculate percentage of houses sold over 10 million SEK
	-- Number of total houses
	-- Number of expensive houses
	-- Using the calculated numbers to calculate a percentage
-- ref for CTE: hhtps://www.geeksforgeeks.ord/cte-in-sql
WITH all_houses AS (SELECT COUNT(*) AS total_count FROM hemnet), 
	expensive_houses AS (SELECT COUNT(*) AS expensive_count FROM hemnet WHERE final_price > 10000000) 
SELECT (eh.expensive_count*100/ah.total_count) AS percentage_expensive_houses 
FROM all_houses ah , expensive_houses eh;

-- Count number of expensive properties (above 10 million SEK)
SELECT COUNT (*) AS expensive_count FROM hemnet WHERE final_price > 10000000;
-- Count number of less expensive properties (below 10 million SEK)
SELECT COUNT (*) AS expensive_count FROM hemnet WHERE final_price < 10000000;


