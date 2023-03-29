BEGIN TRANSACTION;

    DECLARE @prevBalance1 INT;
    DECLARE @prevBalance2 INT;

    SELECT @prevBalance1 = balance
    FROM accounts
    WHERE accountNumber = '1002';

    SELECT @prevBalance2 = balance
    FROM accounts
    WHERE accountNumber = '2001';

    UPDATE accounts
    SET balance = balance - 1000
    WHERE accountNumber = '1002';

    UPDATE accounts
    SET balance = balance + 1000
    WHERE accountNumber = '2001';

    IF @prevBalance1 - 1000 <> (SELECT balance FROM accounts
     WHERE accountNumber = '1002')
     OR @prevBalance2 + 1000 <> (SELECT balance FROM accounts
      WHERE accountNumber = '2001')

    BEGIN
        ROLLBACK TRANSACTION;
        PRINT 'rolled back'
    END

    ELSE
    
    BEGIN
        COMMIT TRANSACTION;
        PRINT 'Committed'
    END;