-- create Todo table
CREATE TABLE Todo
(
TodoID INTGER PRIMARY KEY,
CreateTime TEXT,
TotalAmount INT
SlashedAmount INT,
StandbyAmount INT,
LastEditTime TEXT
);

-- CREATE Todo Item table
CREATE TABLE Items
(
ItemID INTGER PRIMARY KEY,
TodoID INT,
ItemOrder INT,
ItemContent TEXT,
Slashed bool,
CreateTime TEXT,
SlashTime TEXT
);