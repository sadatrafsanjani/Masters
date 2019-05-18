DECLARE
	v_a INTEGER := 0;
	v_b INTEGER;
	
BEGIN

	WHILE (v_a < 3)
	
	LOOP
		DBMS_OUTPUT.PUT_LINE('a: ' || v_a);
		v_b := 0;
		
		LOOP
			DBMS_OUTPUT.PUT_LINE('b: ' || v_b);
			v_b := v_b + 1;
			EXIT WHEN v_b >= 2;
		END LOOP;
		
		v_a := v_a + 1;

	END LOOP;
		
END;

/
