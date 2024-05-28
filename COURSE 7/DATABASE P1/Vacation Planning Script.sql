/* CSC6302 Database Principles
	Unit One: Database System Design
   @Juan Carlos Cabrera
*/

-- Dropping the database if it already exists

DROP DATABASE IF EXISTS VacationPlanning;

-- Creating the Database

CREATE DATABASE VacationPlanning;

-- Using the database to create tables within it

USE VacationPlanning;

-- Creating 'Trip' relation / table if it does not exist
-- Implementing 'Location' and 'Days' attributes
-- Setting primary key to Location

CREATE TABLE IF NOT EXISTS Trip(
Location VARCHAR(100) not null,
Days int not null,
PRIMARY KEY (Location)
);

-- Creating 'Items' table if it does not exist
-- Implementing "I_Name' and 'Amount' Attributes
-- Setting Primary key to I_Name

CREATE TABLE IF NOT EXISTS Items(
I_Name VARCHAR(100) not null,
Amount int not null,
PRIMARY KEY (I_Name)
);

-- Creating "Check_List" table if it does not exist
-- Implementing foreign keys 'Location' and 'I_Name' from the 'Trip' and 'Items' tables respectively
-- Implementing 'Packed attribuite'
-- Setting Primary Key to Location, I_Name

CREATE TABLE IF NOT EXISTS Check_List(
Location VARCHAR(100) not null,
I_Name VARCHAR(100) not null,
Packed TINYINT(1) not null,
PRIMARY KEY (Location, I_Name),
FOREIGN KEY (Location) REFERENCES Trip (Location) on update cascade on delete cascade,
FOREIGN KEY (I_Name) REFERENCES Items (I_Name) on update cascade on delete cascade
);

-- Inserting values into 'Trip' table

INSERT INTO Trip (Location, Days) VALUES ("Florida", 7);
INSERT INTO Trip (Location, Days) VALUES ("Dominican Republic", 7);
INSERT INTO Trip (Location, Days) VALUES ("California", 7);

-- Inserting values into 'Items' table

INSERT INTO Items (I_Name, Amount) VALUES ("Sunscreen", 2);
INSERT INTO Items (I_Name, Amount) VALUES ("Towels", 4);
INSERT INTO Items (I_Name, Amount) VALUES ("Beach ball", 1);

-- Inserting values into 'Check_List' table

INSERT INTO Check_List (Location, I_Name, Packed) VALUES ("Florida", "Sunscreen", 1);
INSERT INTO Check_List (Location, I_Name, Packed) VALUES ("Florida", "Towels", 1);
INSERT INTO Check_List (Location, I_Name, Packed) VALUES ("Florida", "Beach ball", 0);

INSERT INTO Check_List (Location, I_Name, Packed) VALUES ("Dominican Republic", "Sunscreen", 1);
INSERT INTO Check_List (Location, I_Name, Packed) VALUES ("Dominican Republic", "Towels", 1);
INSERT INTO Check_List (Location, I_Name, Packed) VALUES ("Dominican Republic", "Beach ball", 0);

INSERT INTO Check_List (Location, I_Name, Packed) VALUES ("California", "Sunscreen", 1);
INSERT INTO Check_List (Location, I_Name, Packed) VALUES ("California", "Towels", 1);
INSERT INTO Check_List (Location, I_Name, Packed) VALUES ("California", "Beach ball", 0);

-- Checking Table relations and inserts!

SELECT * FROM Trip;
SELECT * FROM Items;
SELECT * FROM Check_List;
