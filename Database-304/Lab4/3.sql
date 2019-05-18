CREATE OR REPLACE FUNCTION annual(salary IN NUMBER, cm IN NUMBER)
	RETURN NUMBER IS
BEGIN
	
	RETURN (salary + (nvl(cm, 0) * salary)) * 12;
	
END annual;

/

SELECT employee_id, last_name, annual(salary, COMMISSION_PCT)
FROM employees;