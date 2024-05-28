/* CSC6302 Database Principles
	Unit Four: Database System Design
    Juan Carlos Cabrera
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


/* START OF HOMEWORK RESPONSES */

-- 1) Function that determines if an ingredient is in the Ingedients table
-- Returns False if not in table and True if it is in the table -- JUAN
DROP FUNCTION IF EXISTS IngredientExists;
DELIMITER $$
CREATE FUNCTION IngredientExists(ingredient_name varchar(100)) RETURNS BOOL DETERMINISTIC
BEGIN
    DECLARE ingredient_id INT;
    SET ingredient_id = (SELECT Id FROM Ingredients WHERE IngredientName = ingredient_name);
    IF ingredient_id IS NULL THEN
        RETURN false;
    ELSE
        RETURN True; 
    END IF;
END $$
DELIMITER ;

-- 2)
/*                            Class procedure below                                */
DELIMITER $$
DROP FUNCTION IF EXISTS doesCookbookExist;$$
CREATE FUNCTION doesCookbookExist(myCookBookName VARCHAR(200))
RETURNS BOOLEAN DETERMINISTIC
BEGIN
-- Let's try another way to see if a cookbook exists,
DECLARE doesExist bool;
SET doesExist = EXISTS
(SELECT CookbookName
FROM Cookbook
WHERE CookbookName = myCookBookName);
RETURN doesExist;
END;$$
DELIMITER ;

DELIMITER $$
DROP FUNCTION IF EXISTS doesRecipeExist;$$
CREATE FUNCTION doesRecipeExist(myRecipeName VARCHAR(200))
RETURNS BOOLEAN DETERMINISTIC
BEGIN
-- And yet another to way to use variables and null checks
declare result varchar(200);
SET result = (SELECT RecipeName FROM Recipe WHERE RecipeName = myRecipeName);
RETURN (result IS NOT NULL);
END;$$
DELIMITER ;

DROP PROCEDURE IF EXISTS InsertNewRecipe;
delimiter $$
CREATE PROCEDURE InsertNewRecipe (
myRecipeName varchar(100), -- Note the size I chose for the parameter matches the Recipe tables column size!
myCookBookName varchar(200), -- Also note my parameters have names that are distinct!
myTotalServings int,
myIsBook bool,
myWebsite varchar(200))
BEGIN
-- Call my function!
if (select doesCookbookExist(myCookBookName) = false ) then
insert into Cookbook (cookbookName, isBook, Website) values (myCookBookName,
myIsBook, myWebsite);
end if;
-- More of the same
if (select doesRecipeExist(myRecipeName) = false) then
insert into Recipe (RecipeName, CookbookName, TotalServings) values (myRecipeName,
myCookBookName, myTotalServings);
end if;
END $$
delimiter ;

/*                            End of Class procedure                            */

-- 2(a) Inserting our favorite recipe into the database -- JUAN
CALL InsertNewRecipe("Shepard's Pie", 'Magnolia Table', 8, true, "https://magnolia.com/visit/eat/magnolia-table/");

-- 2(b) Writing a stored procedure to insert all needed ingredients for our favorite recipe with no duplicates
-- Making sure the Meal table is properly updated and that we are using our previous functions.
-- This took quite a while so hopefully it's okay! -- JUAN

-- Covering our bases -- JUAN
DROP PROCEDURE IF EXISTS InsertRecipeIngredients;

DELIMITER $$
-- Creating our procedure -- JUAN
CREATE PROCEDURE InsertRecipeIngredients (
    IN NewRecipeName varchar(100),
    IN NewCookbookName varchar(200),
    IN NewTotalServings int,
    IN NewIsBook bool,
    IN NewWebsite varchar(200),
    IN NewIngredientList TEXT
)
BEGIN
    -- Declaring our variable -- JUAN
    DECLARE ingredient_exists INT;

    -- Calling and inserting into the Cookbook and Recipe tables -- JUAN
    CALL InsertNewRecipe(NewRecipeName, NewCookbookName, NewTotalServings, NewIsBook, NewWebsite);

        -- Getting the ingredients ready to insert them one by one -- JUAN
    WHILE LENGTH(NewIngredientList) > 0 DO
    
        -- Getting the current ingredient from the -- JUAN
        SET @current_ingredient = TRIM(SUBSTRING_INDEX(NewIngredientList, ',', 1));

        -- Checking if the ingredient already exists in the table with our function from question 1 -- JUAN
        SET ingredient_exists = IngredientExists(@current_ingredient);

        -- Adding it to the Ingredient table if it doesn't exist already -- JUAN
        IF ingredient_exists = FALSE THEN
            INSERT INTO Ingredients (IngredientName) VALUES (@current_ingredient);
            SET ingredient_exists = LAST_INSERT_ID();
        END IF;

        -- Putting the ingredient into the Meal table and mapping it to the recipe -- JUAN
        INSERT INTO Meal (RecipeName, IngredientId) VALUES (NewRecipeName, ingredient_exists);

        -- Removing the current ingredient from the list so we don't add it again by accident -- JUAN
        SET NewIngredientList = TRIM(SUBSTRING(NewIngredientList, LENGTH(@current_ingredient) + 1));
        IF LEFT(NewIngredientList, 1) = ',' THEN
            SET NewIngredientList = TRIM(SUBSTRING(NewIngredientList, 2));
        END IF;
    END WHILE;
END $$
DELIMITER ;

-- Testing our procedure -- JUAN
CALL InsertRecipeIngredients(
"Pork Katsu",
"Magnolia Table",
4,
True,
"https://magnolia.com/visit/eat/magnolia-table/",
"Pork, Panko, Flour, Oil, Rice"
);


-- 3) Stored procedure that takes a recipe name and returns all ingredients in alphabetical order -- JUAN
DROP PROCEDURE IF EXISTS GetIngredientsFromRecipe;

DELIMITER $$
CREATE PROCEDURE GetIngredientsFromRecipe (
    IN RecipeName varchar(100)
)
BEGIN
    -- Getting all ingredients for the input recipe and returning in alphabetical order -- JUAN
    SELECT Ingredients.IngredientName
    FROM Ingredients 
    INNER JOIN Meal ON Ingredients.Id = Meal.IngredientId
    WHERE Meal.RecipeName = RecipeName
    ORDER BY Ingredients.IngredientName;
END $$

DELIMITER ;

-- Testing procedure just to make sure everything works -- JUAN 
CALL GetIngredientsFromRecipe("Pork Katsu");


-- 4) Creating a view that displays all recipes, their cookbooks, and their ingredients;
-- ordered by by cookbook name, recipe name, and ingredient name  -- JUAN
DROP VIEW IF EXISTS RecipeInformation;

CREATE VIEW RecipeInformation AS
SELECT CookBook.CookbookName, Recipe.RecipeName, Ingredients.IngredientName
FROM Cookbook
INNER JOIN Recipe ON Cookbook.CookbookName = Recipe.CookbookName
INNER JOIN Meal ON Recipe.RecipeName = Meal.RecipeName
INNER JOIN Ingredients ON Meal.IngredientId = Ingredients.Id
ORDER BY Cookbook.CookbookName, Recipe.RecipeName, Ingredients.IngredientName;

-- Checking our view -- JUAN
SELECT * fROM RecipeInformation;


-- 5) Query that returns the number of ingredient in each recipe, ordered the number of ingredients in descending order -- JUAN

SELECT Recipe.RecipeName, COUNT(Meal.IngredientId) AS NumIngredients
FROM Recipe
-- Using a left join to get all recipes, even the ones with no ingredients (like our shepard's pie from earlier) -- JUAN
LEFT JOIN Meal ON Recipe.RecipeName = Meal.RecipeName
GROUP BY Recipe.RecipeName
ORDER BY NumIngredients DESC;


-- 6) Query for the ingredients that are not in our favorite recipe, returned in alphabetical order
-- (Used the pork Katsu because it has ingredients mapped to our database) -- JUAN

SELECT Ingredients.IngredientName
FROM Ingredients
WHERE Ingredients.Id NOT IN (
    SELECT IngredientId
    FROM Meal
    WHERE RecipeName = 'Pork Katsu'
)
ORDER BY Ingredients.IngredientName;







