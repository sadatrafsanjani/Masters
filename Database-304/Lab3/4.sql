DECLARE
	v_x NUMBER :=  &x;
	v_y NUMBER :=  &y;
	v_z NUMBER :=  &z;
	v_max NUMBER;
	
BEGIN
	
	IF v_x > v_y
	THEN
		v_max := v_x;
	END IF;

	IF v_y > v_max
	THEN
		v_max := v_y;
	END IF;
	
	IF v_z > v_max
	THEN
		v_max := v_z;
	END IF;
	
	DBMS_OUTPUT.PUT_LINE(v_max);
			
END;

/
