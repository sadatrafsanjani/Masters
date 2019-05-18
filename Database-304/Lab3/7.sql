DECLARE
	v_counter NUMBER := 1;
	
BEGIN
	LOOP
	
		IF(MOD(v_counter, 2) == 0) THEN
			DBMS_OUTPUT.PUT_LINE('Number: ' || v_counter);
			v_counter := v_counter + 2;
		END IF;
		EXIT WHEN v_counter <= 100;
	END LOOP;
		
END;

/
