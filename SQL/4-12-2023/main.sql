-- CREATE TABLE PasswordUpdatesHistory (

--     Id INT IDENTITY(1,1) PRIMARY KEY,
--     UserId INT,
--     PassChangeDate DATE,
--     OldPass VARCHAR(55),
--     NewPass VARCHAR(55),

-- )

-- CREATE OR ALTER TRIGGER trgPasswordChanges ON [User] AFTER UPDATE AS BEGIN

--     INSERT INTO PasswordUpdatesHistory (UserId, PassChangeDate, OldPass, NewPass)
--     SELECT inserted.userId, GETDATE(), deleted.userPassword, inserted.userPassword
--     FROM inserted
--     LEFT JOIN deleted ON inserted.userId = deleted.userId
--     WHERE inserted.userPassword != deleted.userPassword

--     PRINT 'Changed ' + CAST(@@ROWCOUNT, VARCHAR(50))

-- END;

-- UPDATE [User]
-- SET userPassword = 'wdadadwaddsa'
-- WHERE userId = 1 OR userId = 3

-- SELECT * FROM PasswordUpdatesHistory

-- Zad. 1

-- CREATE OR ALTER TRIGGER trgPasswdSecurityCheck ON [User] AFTER INSERT AS
-- BEGIN

--   DECLARE @password VARCHAR(50)
--   DECLARE @count INT

--   SET @password = (SELECT userPassword FROM inserted)
--   SET @count = (SELECT COUNT(*) FROM [User] WHERE userPassword = @password)

--   IF (@count > 2)
--   BEGIN

--     PRINT 'password user by more than 1 user'
--     ROLLBACK TRANSACTION

--   END

--   IF ((SELECT COUNT(*) FROM inserted) > 1)
--   BEGIN

--     PRINT 'can only insert 1 user'
--     ROLLBACK TRANSACTION

--   END

-- END

-- Zad. 2

-- CREATE TABLE RentalStats
-- (
--   userId INT PRIMARY KEY,
--   avgRental FLOAT,
--   maxRental FLOAT,
--   minRental FLOAT
-- )

-- CREATE OR ALTER TRIGGER trgUpdateRentalStats ON [Rentals] AFTER UPDATE AS
-- BEGIN

--   IF UPDATE(rentalEndDate)
--   BEGIN

--     UPDATE RentalStats
--     SET avgRental = (SELECT AVG(productPricePerDay) FROM Rentals LEFT JOIN Product ON Product.productId = Rentals.rentalProductId WHERE rentalUserId = inserted.rentalUserId),
--         maxRental = (SELECT MAX(productPricePerDay) FROM Rentals LEFT JOIN Product ON Product.productId = Rentals.rentalProductId WHERE rentalUserId = inserted.rentalUserId),
--         minRental = (SELECT MIN(productPricePerDay) FROM Rentals LEFT JOIN Product ON Product.productId = Rentals.rentalProductId WHERE rentalUserId = inserted.rentalUserId)
--     FROM RentalStats
--     INNER JOIN inserted ON RentalStats.userId = inserted.rentalUserId

--   END

-- END

-- Zad. 3

-- CREATE OR ALTER TRIGGER trgChargeForRental ON Rentals AFTER UPDATE AS
-- BEGIN

--   IF UPDATE(rentalEndDate)
--   BEGIN

--     DECLARE @userid INT
--     DECLARE @balance FLOAT
--     DECLARE @rentalval FLOAT

--     SELECT @userid = inserted.rentalUserId,
--            @balance = Account.accountBalance,
--            @rentalval = (SELECT product.productPricePerDay FROM product WHERE product.productId = inserted.rentalProductId)
--     FROM inserted
--     INNER JOIN [user] ON inserted.rentalUserId = [User].userId
--     LEFT JOIN Account ON Account.accountUserId = [User].userId

--     IF (@rentalval IS NOT NULL AND @rentalval > 0)
--     BEGIN

--       BEGIN TRANSACTION
--       UPDATE [Account]
--       SET Account.accountBalance = Account.accountbalance - @rentalval
--       WHERE accountUserId = @userid

--       INSERT INTO TransactionHistory (transactionSourceAccountId, transactionAmount)
--       VALUES ((SELECT accountUserId FROM Account LEFT JOIN [User] ON accountUserId = [User].userId), @rentalval)

--       COMMIT TRANSACTION

--     END
--   END

-- END

-- Zad. 4

CREATE OR ALTER TRIGGER trgCheckRentalDates AFTER 