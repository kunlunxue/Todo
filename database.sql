-- create Todo table
CREATE TABLE Todo
(
TodoID INT,
CreateTime TEXT,
TotalAmount INT
SlashedAmount INT,
StandbyAmount INT,
LastEditTime TEXT
)

-- CREATE Todo Item table
CREATE TABLE Items
(
TodoID INT,
ItemID INT,
ItemContent TEXT,
Slashed bool,
CreateTime TEXT,
SlashTime TEXT
)