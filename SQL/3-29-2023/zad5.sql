CREATE PROC withdrawCash 
@accountNumber VARCHAR(50),
@amount DECIMAL(10,2)
AS BEGIN

    DECLARE @currentBalance DECIMAL
    SELECT @currentBalance = balance FROM accounts 
    WHERE accountNumber = @accountNumber

    IF (@currentBalance >= @amount)
    BEGIN

        BEGIN TRANSACTION;
        
        UPDATE accounts SET balance = balance - @amount WHERE accountNumber = @accountNumber;

        DECLARE @updatedBalance DECIMAL(10,2);
        SELECT @updatedBalance = balance FROM accounts WHERE accountNumber = @accountNumber;

        IF (@updatedBalance < 0)
        BEGIN

            ROLLBACK TRANSACTION;
            PRINT 'rolled back';
        
        END

        ELSE

        BEGIN

            COMMIT TRANSACTION;
            PRINT 'commited';

        END
    END

    ELSE

    BEGIN

        PRINT 'not enough cash';

    END
END

EXEC withdrawCash
@accountNumber = '1002',
@amount = 53.2