drop table higher;
drop table lower;

CREATE TABLE higher
( employee_id varchar2(10) NOT NULL PRIMARY KEY,
  last_name varchar2(50) NOT NULL,
  salary NUMBER(38)
);

CREATE TABLE lowers
( employee_id varchar2(10) NOT NULL PRIMARY KEY,
  last_name varchar2(50) NOT NULL,
  salary NUMBER(38)
);
