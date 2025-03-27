-- (T-SQL (Microsoft SQL Server).
CREATE TABLE youtube AS
SELECT * FROM read_csv_auto('data/social media influencers - youtube.csv');

