-- (T-SQL (Microsoft SQL Server). Added the code in duckdb
CREATE TABLE youtube AS
SELECT * FROM read_csv_auto('data/social media influencers - youtube.csv');

