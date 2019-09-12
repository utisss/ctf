DROP DATABASE IF EXISTS sec_day_medium;
CREATE DATABASE sec_day_medium;

DROP USER IF EXISTS 'med_tester'@'localhost';
CREATE USER 'med_tester'@'localhost' IDENTIFIED BY 'ctf2medtester';
GRANT SELECT ON sec_day_medium.* TO 'med_tester'@'localhost';

USE sec_day_medium;

DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews 
( 
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128),
    review VARCHAR(4096),
    rating INT
);

INSERT INTO reviews (name, review, rating) VALUES ("Joe", "I got a hamster from here and its awesome", 5);
INSERT INTO reviews (name, review, rating) VALUES ("Joe", "Nvm, it ran away. 2Fast4Me", 1);
INSERT INTO reviews (name, review, rating) VALUES ("Not a fake review", "Totes Awesome", 5);
INSERT INTO reviews (name, review, rating) VALUES ("Cat", "What do you call a pile of kittens? A meowtain", 2);
INSERT INTO reviews (name, review, rating) VALUES ("toilet", "RIP fish", 3);
INSERT INTO reviews (name, review, rating) VALUES ("anonymous", "what if the flag is in another table", 6);

DROP TABLE IF EXISTS flags;
CREATE TABLE flags
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    flag VARCHAR(64)
);

INSERT INTO flags (flag) VALUES ("utflag{Un10n_$chmun10n}");


