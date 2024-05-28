SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `Inventory` DEFAULT CHARACTER SET utf8;
USE `Inventory`;

CREATE TABLE IF NOT EXISTS `Inventory`.`Item` (
  `ItemName` VARCHAR(50) NOT NULL,
  `ItemDescription` VARCHAR(100) NOT NULL,
  `ItemAmount` INT NOT NULL,
  PRIMARY KEY (`ItemName`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Inventory`.`Room` (
  `RoomName` VARCHAR(50) NOT NULL,
  `RoomDescription` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`RoomName`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Inventory`.`RoomItems` (
  `RoomName` VARCHAR(50) NOT NULL,
  `ItemName` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`RoomName`, `ItemName`),
  CONSTRAINT `RoomName`
    FOREIGN KEY (`RoomName`)
    REFERENCES `Inventory`.`Room` (`RoomName`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ItemName`
    FOREIGN KEY (`ItemName`)
    REFERENCES `Inventory`.`Item` (`ItemName`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Inventory`.`ItemCategory` (
  `ItemName` VARCHAR(50) NOT NULL,
  `Category` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`ItemName`, `Category`),
  CONSTRAINT `FK_ItemCategory_Item`
    FOREIGN KEY (`ItemName`)
    REFERENCES `Inventory`.`Item` (`ItemName`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- Populating our DB
INSERT INTO `Inventory`.`Item` (`ItemName`, `ItemDescription`, `ItemAmount`)
VALUES
    ('Keyboard', 'Mechanical gaming keyboard', 1),
    ('Monitor', 'PC Monitor', 2),
    ('Mouse', 'Wired mouse', 1),
    ('Mirror', 'An ornately framed mirror', 2),
    ('Towel', 'Towel', 4),
    ('Trash Can', 'A trash can', 1),
    ('Television', 'Flat Screen', 1),
    ('Laptop', 'Gaming laptop', 1);

INSERT INTO `Inventory`.`Room` (`RoomName`, `RoomDescription`)
VALUES
    ('Bedroom', 'A Bedroom on the ground floor'),
    ('Bathroom', 'A Bathroom on the ground floor'),
    ('Living Room', 'A Living Room on the ground floor');

INSERT INTO `Inventory`.`RoomItems` (`RoomName`, `ItemName`)
VALUES
    ('Bedroom', 'Keyboard'),
    ('Bedroom', 'Monitor'),
    ('Bedroom', 'Mouse'),
    ('Bathroom', 'Mirror'),
    ('Bathroom', 'Towel'),
    ('Bathroom', 'Trash Can'),
    ('Living Room', 'Laptop'),
    ('Living Room', 'Television');

INSERT INTO `Inventory`.`ItemCategory` (`ItemName`, `Category`)
VALUES
    ('Mirror', 'Decor'),
    ('Towel', 'Toiletries'),
    ('Trash Can', 'Utility'),
    ('Keyboard', 'Electronics'),
    ('Monitor', 'Electronics'),
    ('Mouse', 'Electronics'),
    ('Television', 'Electronics'),
    ('Laptop', 'Electronics');

-- WORKFLOW PROCEDURES

-- Adding an item to the DB
DELIMITER $$

CREATE PROCEDURE AddNewItem(
    IN itemName VARCHAR(50),
    IN itemDescription VARCHAR(100),
    IN itemAmount INT
)
BEGIN
    INSERT INTO Item (ItemName, ItemDescription, ItemAmount)
    VALUES (itemName, itemDescription, itemAmount);
END $$

DELIMITER ;

-- Moving items from one room to another
DELIMITER $$

CREATE PROCEDURE MoveItemsToRoom(
    IN itemName VARCHAR(50),
    IN fromRoom VARCHAR(50),
    IN toRoom VARCHAR(50),
    IN itemQuantity INT
)
BEGIN
    UPDATE RoomItems
    SET ItemQuantity = ItemQuantity - itemQuantity
    WHERE RoomName = fromRoom AND ItemName = itemName;

    INSERT INTO RoomItems (RoomName, ItemName, ItemQuantity)
    VALUES (toRoom, itemName, itemQuantity)
    ON DUPLICATE KEY UPDATE ItemQuantity = ItemQuantity + itemQuantity;
END $$

DELIMITER ;

-- Updating the total amount of an item
DELIMITER $$

CREATE PROCEDURE UpdateItemAmount(
    IN itemName VARCHAR(50),
    IN newAmount INT
)
BEGIN
    UPDATE Item
    SET ItemAmount = newAmount
    WHERE ItemName = itemName;
END $$

DELIMITER ;


