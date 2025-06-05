-- Retrieve all jokes from the database
SELECT * FROM jokes;
-- Find all jokes with a rating below 5
SELECT * FROM jokes WHERE rating < 5;
-- Remove all low-rated jokes (those with rating below 5)
DELETE FROM jokes WHERE rating < 5;
-- Remove ALL jokes from the database 
DELETE FROM jokes;