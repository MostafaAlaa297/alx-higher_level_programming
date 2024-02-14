-- This updates the score
-- Execute cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- Then cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
UPDATE second_table
SET score = 10
WHERE name = "Bob";
