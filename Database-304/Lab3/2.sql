DECLARE
	v_student_id NUMBER :=  &sv_student_id;
	v_first_name VARCHAR2(20);
	v_last_name VARCHAR2(20);
	
BEGIN
	SELECT first_name, last_name
	INTO v_first_name, v_last_name 
	FROM employees
	WHERE EMPLOYEE_ID = v_student_id;
	DBMS_OUTPUT.PUT_LINE
	('Employee Name: ' || v_first_name || ' ' || v_last_name);

EXCEPTION
	WHEN NO_DATA_FOUND THEN
		DBMS_OUTPUT.PUT_LINE
			('There is no employee with employee id 123');
			
END;

/
