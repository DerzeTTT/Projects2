-- CREATE OR ALTER PROC deleteAcc 
-- @firstName VARCHAR(35),
-- @lastName VARCHAR(50) AS BEGIN
-- BEGIN TRANSACTION

-- DECLARE @balance INT

-- SELECT @balance = SUM(balance)
-- FROM Accounts AS Acc
-- LEFT JOIN dbo.Customers AS Cus ON Cus.customerID = acc.customerID
-- WHERE firstName = @firstName AND lastName = @lastName

-- IF @balance > 0
 
-- BEGIN

--     ROLLBACK TRANSACTION

--     PRINT 'rolled back'

-- END

-- ELSE

-- BEGIN

--     DELETE FROM customers
--     WHERE firstName = @firstName AND lastName = @lastName

--     COMMIT TRANSACTION

--     PRINT 'commited'
    
-- END;
-- END;

-- CREATE OR ALTER PROC addToAccount
-- @accNumber VARCHAR(50),
-- @amount DECIMAL AS BEGIN
-- BEGIN TRANSACTION
--     UPDATE Accounts
--     SET balance = balance + @amount
--     WHERE accountNumber = @accNumber
-- COMMIT TRANSACTION
-- END;

CREATE OR ALTER PROC transferMoney
@acc1 VARCHAR(50),
@acc2 VARCHAR(50),
@amount DECIMAL
AS BEGIN
BEGIN TRANSACTION;

    DECLARE @prevBalance1 INT;
    DECLARE @prevBalance2 INT;

    SELECT @prevBalance1 = balance
    FROM accounts
    WHERE accountNumber = @acc1;

    SELECT @prevBalance2 = balance
    FROM accounts
    WHERE accountNumber = @acc2;

    UPDATE accounts
    SET balance = balance - 1000
    WHERE accountNumber = @acc1;

    UPDATE accounts
    SET balance = balance + 1000
    WHERE accountNumber = @acc2;

    IF @prevBalance1 - 1000 <> (SELECT balance FROM accounts
     WHERE accountNumber = @acc1)
     OR @prevBalance2 + 1000 <> (SELECT balance FROM accounts
      WHERE accountNumber = @acc2)

    BEGIN
        ROLLBACK TRANSACTION;
        PRINT 'rolled back'
    END

    ELSE
    
    BEGIN
        COMMIT TRANSACTION;
        PRINT 'Committed'
    END;
    
END;

EXEC transferMoney
@acc1 = '1002',
@acc2 = '2001',
@amount = 5000000