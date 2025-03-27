-- T-SQL . Added the code in duckdb
CREATE TABLE youtube AS
SELECT * FROM read_csv_auto('data/social media influencers - youtube.csv');

