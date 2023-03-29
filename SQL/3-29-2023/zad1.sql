BEGIN TRANSACTION
    UPDATE Accounts
    SET balance = balance + 153
    WHERE accountNumber = '1001'
COMMIT TRANSACTION