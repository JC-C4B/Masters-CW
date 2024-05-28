/* CSC6302 Database Principles
	Unit Three: Database System Design
    Juan Carlos Cabrera
    Homework responses can be found toward the end!
*/
    
/* This SQL script creates a new database, the MealPlanning database, and inserts some data into the database.
	This will be another example database we will be using in this course. */

-- First, lets add a database to work with, and let's use the MealPlanning set of relations. We can do this with the UI, using the "Add Schema" button, or we can write the SQL

-- Its good practice to check if the database exists before adding it, especially in a database script like this one. That way, you can run it multiple times!
DROP DATABASE IF EXISTS MealPlanning;

-- Create the database MealPlanning. Note this is the SQL Create Statement that is written for you when you use the UI to create a new schema
-- Also note that create schema is synonomous to create database in MySql. 
-- This is not true in Sql Server. It is a decision that the database engine creators decided to make.
CREATE DATABASE MealPlanning;

-- Because we are using a script, and because a script let's us execute against different databases, even in the same script, we have to tell it what database we want to use. If we want to use a different 
-- database later on, we would use another "Use" statement to indicate that. But we are going to stick to the Meal Planning Database.
USE  MealPlanning;

-- Now, we need to create the tables, which are how SQL internally stores a relation, and all the information about that relation. Notice that these create table SQL statements are very
-- similiar to our relation's schemas. Again, its a good practice to check if a table exists before creating it. We can drop tables if they currently exist. I'll show both ways in this script. The rest of the table definition should be familiar.
-- We see out relation/table name, its attributes in a comma seperated list, the domains of each attribute, and we define a primary key
--  The domain has more information then we've seen before: it talks about if an attribute can be null.

-- When I went to create the Cookbook relation, I noticed that our attribute Cookbook.Name was a poor choice, as Name is a MySql keyword.
-- Its good practice to not use keywords as attribute or table names. Also not that we are paying attention not only to our attribute domains, but if we allow nulls.
CREATE TABLE IF NOT EXISTS Cookbook (
CookbookName varchar(200)  not null,
IsBook bool not null,
Website varchar(200),
PRIMARY KEY ( CookbookName)
);

-- Let's see how we'd drop a table if its exists. I'll have to create it again, but since I know it doesn't exist at that point in the script, no need to check for existance before creating it. 
DROP TABLE IF EXISTS Cookbook;

CREATE TABLE Cookbook (
CookbookName varchar(200)  not null,
IsBook bool not null,
Website varchar(200),
PRIMARY KEY ( CookbookName)
);

-- We can also just drop the table althogther, because we know it exists. It would return an error if this was not true! And we'll have to create it one more time.
DROP TABLE Cookbook;

CREATE TABLE Cookbook (
CookbookName varchar(200)  not null,
IsBook bool not null,
Website varchar(200),
PRIMARY KEY ( CookbookName)
);

-- When i created the Recipe relation as a table, again I decided to rename some of my attrbutes. Name and Source are MySql keywords we want to avoid.
-- I also know that Cookbook.Name is referenced by Recipe.CookbookName, so let's make sure the domains/IngredientTypes match!
-- Also not that any attributes identified as a primary key or a foreign key when we designed the relations is not null! 
-- We haven't added any SQL to define those constraints, but when we do, these attributes/column must be not null!
CREATE TABLE IF NOT EXISTS Recipe (
RecipeName varchar(100) not null,
CookbookName varchar (200) not null,
TotalServings int,
PRIMARY KEY (RecipeName),
FOREIGN KEY (CookbookName) REFERENCES Cookbook (CookbookName) on update cascade on delete cascade
);

-- We had to rename some columns again, Name and IngredientType are SQL Keywords and we want to avoid that!
-- Also note the keyword auto_increment. This means that when we insert into the table, we dont have to give a value for Id, the database engine
-- will just do that for us, and our Ids will be in numerical order. This is a good practice for ensuring the values of a primary key column are unique. 
CREATE TABLE IF NOT EXISTS Ingredients (
Id int not null auto_increment,
IngredientName varchar(100) not null,
IngredientType varchar (100),
PRIMARY KEY (Id)
);

-- Two things of note here. I made sure that RecipeName had the same domain/IngredientType as Recipe.RecipeName, and our primary key can have multiple attrbutes, just like in relation algrebra
CREATE TABLE IF NOT EXISTS Meal (
RecipeName varchar(100) not null,
IngredientId int not null,
PRIMARY KEY (RecipeName, IngredientId),
FOREIGN KEY (RecipeName) REFERENCES Recipe (RecipeName) on update cascade on delete cascade,
FOREIGN KEY (IngredientId) REFERENCES Ingredients (Id) on update cascade on delete cascade
);

-- In order to query these tables, they need some data in them!

-- For our nullable columns, meaning the attributes whose domains allow nulls, we don't even need them in the insert staement, unless they have a value. The null is added for us by the database engine
INSERT INTO Cookbook (CookbookName, IsBook) VALUES ("Dude Diet", true);
INSERT INTO Cookbook (CookbookName, IsBook) VALUES ("Dude Diet Dinner", true);
INSERT INTO Cookbook (CookbookName, IsBook, Website) VALUES ("Domesticate Me", false, "http://domesticate-me.com");

INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Fajitas", "Dude Diet", 6);
INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Stir Fry", "Dude Diet Dinner", 3);
INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Stuffing", "Domesticate Me", 8);
INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Chicken Stew", "Dude Diet", 4);

INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Red Pepper", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Green Pepper", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Yellow Onion", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Chicken", "meat");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Enchillada Sauce", "pantry");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Shredded Cheese", "dairy");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Garlic", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Soy Sauce", "condiment");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Butter", "dairy");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Sausage", "meat");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Golden Delicious Apple", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Tyme", "spice");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Chicken broth", "pantry");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Stale bread crumbs", "pantry");

-- Because I am entering this data from our practive problem relation, I know the IngredientIds. If I didn't have those tables to work from, I'd just do a select on the Ingredient table, so I could
-- see the values addded by the database engine.
-- How would I do a select? Its the same concept as in relation alegrba, we use an operation on the relation to generate a relation instance. But the syntax is better for programmers to work with. Let's add one into the script! 
-- You can always highlight part of the script, and execute just that part, clicking the lighting bolt button.
SELECT * FROM INGREDIENTS;

INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 1);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 2);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 3);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 4);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 5);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 6);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 1);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 2);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 3);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 4);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 7);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 8);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 9);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing",3 );
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 10);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 11);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 12);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 13);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 14);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 1);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 4);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 14);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 13);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 3);

-- At this point, let's end with select statements, so we can see the current relation instances of all our four relations/tables:
-- Note that you will see the ingredient table twice, because we did a select earlier. You should get a tab opening for each table instance that looks similiar to the grids we've seen in class
SELECT * FROM Cookbook;
SELECT * FROM Recipe;
SELECT * FROM Ingredients;
SELECT * FROM Meal;

/*                                                                   START OF HOMEWORK QUESTIONS                                                                           */

-- 1(a) Number of ingredients needed for chicken stew, with the recipe name included -- JUAN
SELECT RecipeName, COUNT(*) AS Number_Of_Ingredients
FROM Meal
WHERE RecipeName= 'Chicken Stew';

-- 1(b) Ingredients needed for each recipe including the name of the recipe, the cookbook, the name of the ingredient, and the type of ingredient -- JUAN
SELECT Recipe.RecipeName, Recipe.CookbookName, Ingredients.IngredientName, Ingredients.IngredientType
FROM Recipe
JOIN Meal ON Recipe.RecipeName = Meal.RecipeName
JOIN Ingredients ON Meal.IngredientId = Ingredients.Id
ORDER BY Recipe.RecipeName, Ingredients.IngredientName;

-- 1(c) The recipe that uses the most ingredients, the amount of ingredients, and the recipe name. 
-- Utilizing 'HAVING' as seen in class to only show the recipe with the most ingredients              -- JUAN
SELECT Recipe.RecipeName, COUNT(*) AS NumberOfIngredients
FROM Recipe 
JOIN Meal  ON Recipe.RecipeName = Meal.RecipeName
GROUP BY Recipe.RecipeName
HAVING COUNT(*) = (
    SELECT MAX(IngredientCount)
    FROM (
        SELECT COUNT(*) AS IngredientCount
        FROM Recipe 
        JOIN Meal  ON Recipe.RecipeName = Meal.RecipeName
        GROUP BY Recipe.RecipeName
    ) AS IngredientCounts
);

-- 1(d) Finding the Recipes that do not use any type of pepper
SELECT Recipe.RecipeName, Recipe.CookBookName
FROM Recipe
WHERE Recipe.RecipeName NOT IN (
	SELECT DISTINCT Meal.RecipeName
    FROM Meal
    JOIN Ingredients ON Meal.IngredientId = Ingredients.Id
    WHERE Ingredients.IngredientType LIKE "%pepper%"
);

-- 1(e) List of ingredients, grouped by type, and then alphabetized by name
SELECT IngredientType, IngredientName
FROM Ingredients
ORDER BY IngredientType, IngredientName;

-- 2(a)(b) Inserting a recipe into the database and making sure it is in all tables necessary -- JUAN
INSERT INTO Cookbook (CookbookName, IsBook)
VALUES ("Magnolia Table", true);

INSERT INTO Recipe (RecipeName, CookbookName, TotalServings)
VALUES ("Shepard's Pie", "Magnolia Table", 8);

INSERT INTO Ingredients (IngredientName, IngredientType)
VALUES ("Potato", "produce");

INSERT INTO Ingredients (IngredientName, IngredientType)
VALUES ("Beef", "meat");

INSERT INTO Ingredients (IngredientName, IngredientType)
VALUES ("Corn", "produce");

INSERT INTO Meal (RecipeName, IngredientId)
VALUES ("Shepard's Pie", (SELECT Id FROM Ingredients WHERE IngredientName = 'Potato'));

INSERT INTO Meal (RecipeName, IngredientId)
VALUES ("Shepard's Pie", (SELECT Id FROM Ingredients WHERE IngredientName = 'Beef'));

INSERT INTO Meal (RecipeName, IngredientId)
VALUES ("Shepard's Pie", (SELECT Id FROM Ingredients WHERE IngredientName = 'Corn'));

-- 4 Creating a new script to incorporate food allergies -- JUAN

-- Regular database creation -- JUAN 
DROP DATABASE IF EXISTS MealPlanning;

CREATE DATABASE MealPlanning;

USE MealPlanning;

-- Same Cookbook table -- JUAN 
CREATE TABLE IF NOT EXISTS Cookbook (
  CookbookName varchar(200) not null,
  IsBook bool not null,
  Website varchar(200),
  PRIMARY KEY (CookbookName)
);

-- Adding an Allergn column to the Recipe table -- JUAN 
CREATE TABLE IF NOT EXISTS Recipe (
  RecipeName varchar(100) not null,
  CookbookName varchar(200) not null,
  TotalServings int,
  Allergens varchar(50), 
  PRIMARY KEY (RecipeName),
  FOREIGN KEY (CookbookName) REFERENCES Cookbook (CookbookName) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Same ingredient table
CREATE TABLE IF NOT EXISTS Ingredients (
  Id int not null auto_increment,
  IngredientName varchar(100) not null,
  IngredientType varchar (100),
  PRIMARY KEY (Id)
);

-- Adding allergen column to the Meal table and having it reference the allergens from the recipe table
CREATE TABLE IF NOT EXISTS Meal (
  RecipeName varchar(100) not null,
  IngredientId int not null,
  Allergens varchar(50), 
  PRIMARY KEY (RecipeName, IngredientId),
  FOREIGN KEY (RecipeName) REFERENCES Recipe (RecipeName) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (IngredientId) REFERENCES Ingredients (Id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Making a table to add the Allergens to, and to reference when necessary
CREATE TABLE IF NOT EXISTS Allergens (
  AllergenId int not null auto_increment,
  AllergenName varchar(50) not null,
  PRIMARY KEY (AllergenId),
  UNIQUE (AllergenName)
);

-- Making a table to keep track of ingredients that are allergens within recipes
CREATE TABLE IF NOT EXISTS RecipeAllergens (
  RecipeName varchar(100) not null,
  IngredientId int not null,
  AllergenId int not null,
  PRIMARY KEY (RecipeName, IngredientId, AllergenId),
  FOREIGN KEY (RecipeName) REFERENCES Recipe (RecipeName) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (IngredientId) REFERENCES Ingredients (Id) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (AllergenId) REFERENCES Allergens (AllergenId) ON UPDATE CASCADE ON DELETE CASCADE
);









