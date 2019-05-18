drop table if exists employee; 

CREATE TABLE employee
(
	employee_id number(38) NOT NULL PRIMARY KEY, 
	employee_name varchar2(10) NOT NULL
)
PCTFREE 5 PCTUSED 60
TABLESPACE inventory;


INSERT INTO employee VALUES (101, 'Adams');
INSERT INTO employee VALUES (102, 'Brooks');
INSERT INTO employee VALUES (103, 'Curry');
INSERT INTO employee VALUES (104, 'Glenn');
INSERT INTO employee VALUES (105, 'Green');