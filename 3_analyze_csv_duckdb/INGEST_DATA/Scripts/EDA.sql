
-- Retrieves all columns and all rows from the youtube table
SELECT * FROM youtube;

-- Retrieves a list of unique categories from the youtube table
SELECT DISTINCT category FROM youtube;

-- ctrl + shift + f (shortcut for formatting SQL in many editors)
-- Show numbers of category 

SELECT
	count(category) AS number_of_science
FROM
	youtube
WHERE
	category = 'Science & Technology';

-- Display names of all Science & Technology YouTubers
SELECT
	"youtuber name" category
FROM
	youtube
WHERE
	category = 'Science & Technology';


-- Show all columns EXCEPT "youtuber name" and "avg views"
SELECT
	* EXCLUDE ("youtuber name", "avg views")
FROM
	youtube
WHERE
	category = 'Science & Technology'
	OR category = 'Education';