DECLARE
	v_last_name VARCHAR2(20);
	v_salary NUMBER;
	
BEGIN
	SELECT last_name, ((salary + (nvl(COMMISSION_PCT, 0) * salary)) * 12)
	INTO v_last_name, v_salary 
	FROM employees ORDER BY v_salary ASC;
	
	DBMS_OUTPUT.PUT_LINE('Salary Greater Than 2000: ' || v_last_name || ' ' || v_salary);

EXCEPTION
	WHEN NO_DATA_FOUND THEN
		DBMS_OUTPUT.PUT_LINE('There is no employee');
END;

/
