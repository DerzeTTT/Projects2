BEGIN TRANSACTION;

IF EXISTS (SELECT * FROM Konto WHERE saldo > 0 AND klient_id IN (SELECT id FROM Klient WHERE imie = 'Jan' AND nazwisko = 'Kowalski'))
BEGIN
    ROLLBACK;
    PRINT 'Nie można usunąć konta klienta, który ma saldo większe niż 0';
END
ELSE IF EXISTS (SELECT * FROM Konto WHERE klient_id IN (SELECT id FROM Klient WHERE imie = 'Jan' AND nazwisko = 'Kowalski'))
BEGIN
    DELETE FROM Konto WHERE klient_id IN (SELECT id FROM Klient WHERE imie = 'Jan' AND nazwisko = 'Kowalski');
    DELETE FROM Klient WHERE imie = 'Jan' AND nazwisko = 'Kowalski';
    PRINT 'Usunięto klienta i jego konta.';
END
ELSE
BEGIN
    ROLLBACK;
    PRINT 'Nie znaleziono klienta o podanych danych.';
END

COMMIT;
