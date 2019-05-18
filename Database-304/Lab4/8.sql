DECLARE
	CURSOR c_zip IS
	SELECT *
	FROM employees;
	vr_zip c_zip%ROWTYPE;
	
BEGIN
	OPEN c_zip;
		
	FETCH c_zip INTO vr_zip;
	WHILE c_zip%FOUND LOOP
		IF (vr_zip.salary + (nvl(vr_zip.commission_pct, 0) * vr_zip.salary)) * 12 > 100000 THEN
			INSERT INTO higher VALUES (vr_zip.employee_id, vr_zip.last_name, 
			(vr_zip.salary + (nvl(vr_zip.commission_pct, 0) * vr_zip.salary)) * 12);
			DBMS_OUTPUT.PUT_LINE('High');
		ELSE
			INSERT INTO lowers VALUES (vr_zip.employee_id, vr_zip.last_name, 
			(vr_zip.salary + (nvl(vr_zip.commission_pct, 0) * vr_zip.salary)) * 12);
			DBMS_OUTPUT.PUT_LINE('Low');
		END IF;
	FETCH c_zip INTO vr_zip;
	
	END LOOP;

END;

/