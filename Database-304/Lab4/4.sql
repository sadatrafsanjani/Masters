CREATE OR REPLACE FUNCTION area(r IN NUMBER)
	RETURN NUMBER IS
BEGIN
	
	RETURN 3.1416 * r * r;
	
END area;

/

SELECT area(5.56)
FROM dual;