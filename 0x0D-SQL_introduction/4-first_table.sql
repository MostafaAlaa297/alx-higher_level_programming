-- This creates a table passed in the command line
-- Execute cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- Then execute cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
CREATE TABLE IF NOT EXISTS first_table(
	id INT,
	name VARCHAR(256)
);
