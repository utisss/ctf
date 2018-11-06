DROP DATABASE IF EXISTS selena;
CREATE DATABASE selena;

DROP USER IF EXISTS 'selena_tester'@'localhost';
CREATE USER 'selena_tester'@'localhost' IDENTIFIED BY 'ctf2medtester';
GRANT SELECT ON selena.* TO 'selena_tester'@'localhost';

USE selena;

DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews 
( 
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128),
    review VARCHAR(4096),
    rating INT
);

INSERT INTO reviews (name, review, rating) VALUES ("Houston", "Selena is the GOAT", 5);
INSERT INTO reviews (name, review, rating) VALUES ("New York Times", "...Sensational", 5);
INSERT INTO reviews (name, review, rating) VALUES ("Kanye", "Imma let you finish, but Selena is the GOAT", 4);
INSERT INTO reviews (name, review, rating) VALUES ("Not a fake review", "Totes Awesome", 3);
INSERT INTO reviews (name, review, rating) VALUES ("J.Lo hater", "More like J.No", 2);
INSERT INTO reviews (name, review, rating) VALUES ("Yolanda", "I'm crazy", 1);
INSERT INTO reviews (name, review, rating) VALUES ("anonymous", "what if the flag is in another table", 6);

DROP TABLE IF EXISTS interesting;
CREATE TABLE interesting 
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    flag VARCHAR(64)
);

INSERT INTO interesting (flag) VALUES ("utflag{$ql_Pr0h1b1d0}");


