-- Zad. 1

-- CREATE OR ALTER TRIGGER trgNowyKlient ON Klient AFTER INSERT AS
-- PRINT 'Dodano nowego klienta'

-- INSERT INTO Klient (Imie, Nazwisko, Id)
-- VALUES ('ok', 'test', 52432)

-- Zad. 2

-- ALTER TRIGGER trgNowyKlient ON Klient AFTER INSERT AS
-- BEGIN
--     DECLARE @Imie VARCHAR(50)
--     SELECT @Imie = Imie FROM inserted
--     PRINT 'Dodano nowego klienta o imieniu: ' + @Imie
-- END

-- INSERT INTO Klient (Imie, Nazwisko, Id)
-- VALUES ('haha', 'test', 32132)

-- Zad. 3

-- ALTER TRIGGER trgNowyKlient ON Klient AFTER INSERT AS
-- BEGIN
--     DECLARE @ClientCount INT
--     SELECT @ClientCount = COUNT(*) FROM Klient
--     PRINT 'Liczba klientów w tabeli Klient: ' + CONVERT(VARCHAR(35), @ClientCount)
-- END

-- INSERT INTO Klient (Imie, Nazwisko, Id)
-- VALUES ('hhhhaha', 'test', 3242342)

-- Zad. 4

-- ALTER TRIGGER trgNowyKlient ON Klient INSTEAD OF INSERT AS
-- BEGIN

--     DECLARE @ClientCount INT
--     SELECT @ClientCount = COUNT(*) FROM Klient

--     IF @ClientCount < 10

--     INSERT INTO Klient SELECT * FROM inserted

--     ELSE

--     PRINT 'Too many clients'

-- END

-- INSERT INTO Klient (Imie, Nazwisko, Id)
-- VALUES ('hhhhaha', 'test', 321213)

-- Zad. 5

-- CREATE TRIGGER trgNoweZamowienie ON Zamowienie AFTER INSERT AS
-- BEGIN
--     DECLARE @IdZamowienia INT
--     SELECT @IdZamowienia = Id FROM inserted
--     PRINT 'Dodano zamówienie o Id: ' + CONVERT(VARCHAR(20), @IdZamowienia)
-- END

-- INSERT INTO Zamowienie
-- VALUES (23, 10, 1000.00, 'NOWE')

-- Zad. 6

-- CREATE OR ALTER TRIGGER trgNoweZamowienie ON Zamowienie INSTEAD OF INSERT AS
-- BEGIN

--     DECLARE @SumaZamowien MONEY
--     SELECT @SumaZamowien = SUM(Wartosc) FROM Zamowienie WHERE Status != 'Zakonczone'

--     IF (@SumaZamowien + (SELECT SUM(Wartosc) FROM inserted)) <= 2000

--         INSERT INTO Zamowienie SELECT * FROM inserted

--     ELSE
    
--         PRINT 'Amount of value from unfinished orders is too high'
    
-- END

-- INSERT INTO Zamowienie
-- VALUES (38, 10, 1500.00, 'NOWE')

-- Zad. 7

-- CREATE OR ALTER TRIGGER trgNowyPracownik ON Pracownik AFTER INSERT AS
-- BEGIN

--     UPDATE Pracownik SET Imie = UPPER(Imie) WHERE Id IN (SELECT Id FROM inserted)

-- END

-- INSERT INTO Pracownik
-- VALUES (138, 'Ok', 1, 1300.00)

-- SELECT * FROM Pracownik

-- Zad. 8

-- CREATE OR ALTER TRIGGER trgPodwyzka ON Pracownik AFTER UPDATE AS
-- BEGIN

--   IF UPDATE(Zarobki)

--   BEGIN
  
--     IF EXISTS (

--       SELECT * FROM inserted AS ins
--       INNER JOIN deleted AS del ON ins.Id = del.Id
--       WHERE ins.Zarobki > del.Zarobki * 1.3

--     ) BEGIN

--       PRINT 'Raise was too high'
--       ROLLBACK TRANSACTION

--     END

--   END

-- END

-- UPDATE Pracownik
-- SET Zarobki = Zarobki * 1.1

-- Zad. 9

-- CREATE OR ALTER TRIGGER trgWynagrodzenie ON Pracownik AFTER INSERT AS
-- BEGIN

--   UPDATE Pracownik

--   SET Zarobki =

--     CASE 

--       WHEN Pracownik.StazPracy < 2 THEN 2000
--       WHEN Pracownik.StazPracy >= 2 AND Pracownik.StazPracy < 5 THEN 3000

--       ELSE 5000

--     END

--   FROM inserted AS ins
  
--   WHERE Pracownik.Id = ins.Id
  
-- END

-- INSERT INTO Pracownik
-- VALUES (123, 'Jan', 9, 23)

-- Zad. 10

-- CREATE OR ALTER TRIGGER trgZmianaZamowienia ON Zamowienie AFTER UPDATE AS
-- BEGIN

--   IF UPDATE(Status)

--   BEGIN

--     INSERT INTO HistoriaZamowienia (ZamowienieId, DataZmiany, StatusPrzed, StatusPo)
--     SELECT ins.ZamowienieId, GETDATE(), del.Status, ins.Status
--     FROM inserted AS ins
--     INNER JOIN deleted AS del ON ins.ZamowienieId = del.ZamowienieId

--   END

-- END


-- INSERT INTO

-- Zad. 12

-- CREATE OR ALTER TRIGGER trgBlockNegativeOrder ON Zamowienie FOR INSERT AS
-- BEGIN

--   IF EXISTS (SELECT * FROM inserted WHERE Wartosc < 0)
--   BEGIN

--     PRINT 'Order value was negative'
--     ROLLBACK TRANSACTION

--   END

-- END

-- INSERT INTO Zamowienie 
-- VALUES (55, 10, -500.00, 'NOWE')

-- Zad. 13

-- CREATE OR ALTER TRIGGER trgAdditionalDiscount ON Zamowienie FOR INSERT AS
-- BEGIN

--   IF (SELECT SUM(Wartosc) FROM inserted) > 1000

--   BEGIN

--     UPDATE Zamowienie
--     SET Wartosc = Wartosc * 0.9

--     WHERE Id IN (SELECT Id FROM inserted)

--   END

-- END

-- INSERT INTO Zamowienie
-- VALUES (58, 10, 1001, 'NOWE')

-- Zad. 14

-- CREATE OR ALTER PROC testProc
--   @OrderId INT,
--   @ClientId INT
-- AS
-- BEGIN

--   BEGIN TRANSACTION

--   DECLARE @Status NVARCHAR(50)

--   SELECT @Status = Status FROM Zamowienie WHERE Id = @OrderId

--   IF @Status = 'NOWE' AND EXISTS (SELECT * FROM Klient WHERE Id = @ClientId)

--   BEGIN

--     UPDATE Zamowienie
--     SET Status = 'WYSLANE'
--     WHERE Id = @OrderId

--     INSERT INTO HistoriaZamowienia (ZamowienieId, DataZmiany, StatusPo)
--     VALUES (@OrderId, GETDATE(), 'WYSLANE')

--     COMMIT TRANSACTION

--   END

--   ELSE

--   BEGIN

--     ROLLBACK TRANSACTION
--     PRINT 'Invalid input'

--   END

-- END

-- EXEC testProc
-- @OrderId = 58,
-- @ClientId = 10

-- Zad. 15

-- BEGIN TRANSACTION

-- DECLARE @ClientId INT
-- SET @ClientId = 10

-- IF NOT EXISTS (SELECT * FROM Zamowienie WHERE KlientId = @ClientId)
-- BEGIN

--   DELETE FROM Klient WHERE Id = @ClientId
--   COMMIT TRANSACTION

-- END

-- ELSE

-- BEGIN

--   PRINT 'Klient ma zamowienia'
--   ROLLBACK TRANSACTION

-- END

-- Zad. 16

BEGIN TRANSACTION

UPDATE Zamowienie
SET Wartosc = Wartosc * 1.1
WHERE Wartosc < 1000 AND Status = 'ZAKONCZONE'

COMMIT TRANSACTION