-- Zad. 3

CREATE OR ALTER PROC spPurchasePackage
@id INT,
@dayCount INT
AS
BEGIN
    IF NOT EXISTS (SELECT Userid FROM user WHERE @id = Userid)
        print 'Nie istnieje'
    IF NOT EXISTS (SELECT packageid FROM Package WHERE @dayCount = packageDurationInDays)
        PRINT 'Nie istnieje'
    ELSE
        BEGIN
    DECLARE @packageid INT
    SET @packageid = (SELECT TOP(1) packageId FROM Package 
    WHERE @dayCount = packageDurationInDays order by packagePrice asc)
    declare @datawygasniecia DATE
    set @datawygasniecia = (SELECT top(1) subscriptionExpirationDate 
    FROM Subscriptions where subscriptionUserId = @id 
    order by subscriptionExpirationDate desc)
    IF (@datawygasniecia IS NULL)
    SET @datawygasniecia = getdate()
    ELSE 
    SET @datawygasniecia = dateadd(day, 1, @datawygasniecia)
    INSERT INTO Subscriptions (subscriptionPackageId, subscriptionUserId, subscriptionStartDate, subscriptionExpirationDate, subscriptionPurchaseDate)
    VALUES (@packageid, @id, getdate(), 
    DATEADD(DAY, @dayCount, @datawygasniecia), @datawygasniecia)
END

END;

EXEC spPurchasePackage
@id = 2492,
@dayCount = 20

--Zad. 4

CREATE VIEW vwActiveUserAndIncomes