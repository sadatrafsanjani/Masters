DECLARE
	v_counter NUMBER := 1;
	
BEGIN

	WHILE (v_counter < 100)
	
	LOOP
	
		IF (MOD(v_counter, 2) == 1) THEN
			DBMS_OUTPUT.PUT_LINE('Number: ' || v_counter);			
		END IF;
		
		v_counter := v_counter + 1;

	END LOOP;
		
END;

/
