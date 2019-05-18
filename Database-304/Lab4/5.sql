DECLARE
	vr_emp employees%ROWTYPE;
	
BEGIN
	SELECT *
	INTO vr_emp
	FROM employees
	WHERE employee_id = 156;
	
	DBMS_OUTPUT.PUT_LINE(vr_emp.first_name || ' ' || vr_emp.salary || ' ' || (vr_emp.salary + (nvl(vr_emp.COMMISSION_PCT, 0) * vr_emp.salary)) * 12);

EXCEPTION
	WHEN no_data_found
	THEN
	RAISE_APPLICATION_ERROR(-2001, 'The Employee not in the database');
END;

/