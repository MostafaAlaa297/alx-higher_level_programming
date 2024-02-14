-- This lists all the privilages for a user
-- Execute cat 0-privileges.sql | mysql -hlocalhost -uroot -p
-- Then echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
-- Then cat 0-privileges.sql | mysql -hlocalhost -uroot -p 
SHOW GRANTS FOR "user_0d_1"@"localhost";
SHOW GRANTS FOR "user_0d_2"@"localhost";
