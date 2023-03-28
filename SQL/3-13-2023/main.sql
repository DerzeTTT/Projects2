DECLARE @lol INT = 0;

WHILE @lol < 10
BEGIN

    PRINT REPLICATE('-', @lol);

    IF @lol < 5
     SET @lol = @lol + 1;
    ELSE
     SET @lol = @lol - 1;

END;