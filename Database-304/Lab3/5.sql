DECLARE
	v_x NUMBER :=  &x;
	v_y NUMBER :=  &y;
	v_z NUMBER :=  &z;
	v_max NUMBER;
	
BEGIN
	
	IF v_x > v_y
	THEN
		v_max := v_x;
		
	ELSIF v_y > v_X
	THEN
		v_max := v_y;
		
	ELSIF v_x > v_z
	THEN
		v_max := v_x;
		
	ELSIF v_z > v_x
	THEN
		v_max := v_z;
	END IF;
	
	DBMS_OUTPUT.PUT_LINE(v_max);
			
END;

/
