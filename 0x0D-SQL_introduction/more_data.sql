-- a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

CREATE TABLE IF NOT EXISTS `second_table`(`id` INT,`name` VARCHAR(256),`score` INT);

INSERT INTO second_table (id, name, score) VALUES (1, "Jone", 10);
INSERT INTO second_table (id, name, score) VALUES (2, "Alix", 7);
INSERT INTO second_table (id, name, score) VALUES (3, "Boob", 10);
INSERT INTO second_table (id, name, score) VALUES (4,"Georgia", 18);
INSERT INTO second_table (id, name, score) VALUES (1, "Johne", 10);
INSERT INTO second_table (id, name, score) VALUES (2, "Aelex", 13);
INSERT INTO second_table (id, name, score) VALUES (3, "Bobie", 14);
INSERT INTO second_table (id, name, score) VALUES (4,"Georgena", 8);
INSERT INTO second_table (id, name, score) VALUES (1, "Joahn", 0);
INSERT INTO second_table (id, name, score) VALUES (2, "Alexa", 3);
INSERT INTO second_table (id, name, score) VALUES (3, "Boabe", 2);
INSERT INTO second_table (id, name, score) VALUES (4,"George", 8);
