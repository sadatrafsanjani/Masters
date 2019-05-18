CREATE TABLE customer
( customer_name varchar2(10) NOT NULL PRIMARY KEY,
  customer_street varchar2(50) NOT NULL,
  customer_city varchar2(50)
);

CREATE TABLE branch
( branch_name varchar2(10) NOT NULL PRIMARY KEY,
  branch_city varchar2(50) NOT NULL,
  assets number(38)
);

CREATE TABLE account
( account_number varchar2(10) NOT NULL PRIMARY KEY,
  branch_name varchar2(50) NOT NULL,
  balance number(38),
  CONSTRAINT branch_name_fk
  FOREIGN KEY (branch_name)
  REFERENCES branch(branch_name)
);

CREATE TABLE loan
( loan_number varchar2(10) NOT NULL PRIMARY KEY,
  branch_name varchar2(50) NOT NULL,
  amount number(38),
  CONSTRAINT loan_branch_name_fk FOREIGN KEY (branch_name) REFERENCES branch(branch_name)
);

CREATE TABLE depositor
( customer_name varchar2(10) NOT NULL,
  account_number varchar2(10) NOT NULL,
  CONSTRAINT depositor_customer_name_fk FOREIGN KEY (customer_name) REFERENCES customer(customer_name),
  CONSTRAINT depositor_account_number_fk FOREIGN KEY (account_number) REFERENCES account(account_number)
);


CREATE TABLE borrower
( customer_name varchar2(10) NOT NULL,
  loan_number varchar2(10) NOT NULL,
  CONSTRAINT borrower_customer_name_fk FOREIGN KEY (customer_name) REFERENCES customer(customer_name),
  CONSTRAINT borower_loan_number_fk FOREIGN KEY (loan_number) REFERENCES loan(loan_number)
);