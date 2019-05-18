COLUMN Table_Name FORMAT A14;

COLUMN inventory FORMAT A15;

SELECT Table_Name, Tablespace_Name
FROM Tabs
WHERE Table_Name = 'EMPLOYEE';