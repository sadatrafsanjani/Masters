ALTER SYSTEM SET db_cache_advice = OFF;

describe v$db_cache_advice;

SELECT name, block_size, advice_status FROM
v$db_cache_advice; 