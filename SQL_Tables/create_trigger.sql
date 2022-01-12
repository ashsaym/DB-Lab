-- Datenbanken Praktikum WS 2021/22
-- Musterlösung - Trigger
-- Importieren mit: db2 -td@ -v -f create_trigger.sql
CREATE TRIGGER statusupdate
AFTER INSERT ON reservieren
REFERENCING NEW AS neu
FOR EACH ROW MODE DB2SQL
BEGIN ATOMIC
	DECLARE maxPlaetze SMALLINT;
	DECLARE bisherReserviertePlaetze SMALLINT;
	SET maxPlaetze = (select maxPlaetze from fahrt f where f.fid = neu.fahrt);
	SET bisherReserviertePlaetze = (select sum(anzPlaetze) from reservieren r where r.fahrt = neu.fahrt);
	IF bisherReserviertePlaetze = maxPlaetze THEN
		UPDATE fahrt SET status = 'geschlossen' where fid = neu.fahrt;
	END IF;
END@


