COLUMN Table_name FORMAT A12;
COLUMN Tablespace_name FORMAT A15;
SELECT Table_name, Tablespace_name 
    FROM User_tables
    WHERE Table_name IN ('EMPLOYEE'); 
