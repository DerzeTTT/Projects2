CREATE OR ALTER TRIGGER trgPasswdSecurityCheck ON Users
AFTER INSERT
AS
BEGIN
  SET NOCOUNT ON;
  
  IF @@ROWCOUNT > 1
  BEGIN
    PRINT 'Tylko jeden uzytkownik moze byc insertowany'
    ROLLBACK TRANSACTION;
    RETURN;
  END;
  
  IF (SELECT COUNT(*) FROM Users WHERE Password = (SELECT Password FROM inserted)) > 2
  BEGIN
    PRINT 'Haslo juz jest uzywane przez wiecej niz 2 uzytkownikow'
    ROLLBACK TRANSACTION;
    RETURN;
  END;
END;
