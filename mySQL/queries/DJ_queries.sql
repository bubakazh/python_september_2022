-- Query: Create 3 new dojos

INSERT INTO dojos (name) VALUES ('Manila'), ('Medellin'), ('Nagoya');

-- Query: Delete the 3 dojos you just created

SET FOREIGN_KEY_CHECKS=0;
DELETE FROM dojos WHERE id ORDER BY id DESC LIMIT 1;
DELETE FROM dojos WHERE id ORDER BY id DESC LIMIT 1;
DELETE FROM dojos WHERE id ORDER BY id DESC LIMIT 1;
SET FOREIGN_KEY_CHECKS=1; 

-- Query: Create 3 more dojos

INSERT INTO dojos (name) VALUES ('Tokyo'), ('Osaka'), ('Kyiv');

-- Query: Create 3 ninjas that belong to the first dojo

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Jason', 'Chang', 33, 1), ('Chase', 'Andrews', 38, 1), ('Vincent', 'Hagibis', 34, 1);

-- Query: Create 3 ninjas that belong to the second dojo

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('April', 'Cristal', 37, 2), ('Cherry', 'de Dios', 24, 2), ('Hannah', 'Martinho', 22, 2);

-- Query: Create 3 ninjas that belong to the third dojo

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('駿河', '神原', 18, 3), ('翼', '羽川', 18, 3), ('ひたぎ', '戦場ヶ原', 18, 3);

-- Query: Retrieve all the ninjas from the first dojo

SELECT * FROM ninjas WHERE dojo_id = 1;

-- Query: Retrieve all the ninjas from the last dojo

SELECT * FROM ninjas WHERE dojo_id = (SELECT id from dojos ORDER BY id DESC LIMIT 1);

-- Query: Retrieve the last ninja's dojo

SELECT * FROM dojos WHERE id = (SELECT dojo_id FROM ninjas ORDER BY id DESC LIMIT 1);
