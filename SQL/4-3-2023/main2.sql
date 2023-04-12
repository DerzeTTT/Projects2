CREATE OR ALTER TRIGGER trgNoweZamowienie ON Zamowienie AFTER INSERT AS
BEGIN
    DECLARE @IdZamowienia INT
    SELECT @IdZamowienia = Id FROM inserted
    PRINT 'Dodano zamówienie o Id: ' + CONVERT(VARCHAR(20), @IdZamowienia)
END

INSERT INTO Zamowienie
VALUES (27, 10, 1100.00, 'NOWE')
