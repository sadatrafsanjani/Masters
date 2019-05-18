DECLARE
	CURSOR c_zip IS
	SELECT *
	FROM employees INNER JOIN departments ON employees.department_id = departments.department_id ;
	vr_zip c_zip%ROWTYPE;
	
BEGIN
	OPEN c_zip;
	LOOP
	FETCH c_zip INTO vr_zip;
	EXIT WHEN c_zip%NOTFOUND;
	
DBMS_OUTPUT.PUT_LINE(vr_zip.last_name || ' ' || vr_zip.department_name);
	
	END LOOP;

END;

/