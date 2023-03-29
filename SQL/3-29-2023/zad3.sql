BEGIN TRANSACTION

DECLARE @balance INT

SELECT @balance = SUM(balance)
FROM Accounts AS Acc
LEFT JOIN dbo.Customers AS Cus ON Cus.customerID = acc.customerID
WHERE firstName = 'Robert' AND lastName = 'Lewandowski'

IF @balance > 0
 
BEGIN

    ROLLBACK TRANSACTION

    PRINT 'rolled back'

END

ELSE

BEGIN

    DELETE FROM customers
    WHERE firstName = 'Robert' AND lastName = 'Lewandowski'

    COMMIT TRANSACTION

    PRINT 'commited'
    
END;
