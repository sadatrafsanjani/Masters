DECLARE
	v_employee_id NUMBER :=  &sv_employee_id;
	v_last_name VARCHAR2(20);
	v_salary NUMBER;
	
BEGIN
	SELECT last_name, (salary + (nvl(COMMISSION_PCT, 0) * salary)) * 12
	INTO v_last_name, v_salary 
	FROM employees
	WHERE EMPLOYEE_ID = v_employee_id;
	DBMS_OUTPUT.PUT_LINE
	('Employee Name: ' || v_last_name || ' ' || v_salary);

EXCEPTION
	WHEN NO_DATA_FOUND THEN
		DBMS_OUTPUT.PUT_LINE
			('There is no employee with employee id 123');
			
END;

/
