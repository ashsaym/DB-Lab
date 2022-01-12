CREATE TABLE schreiben (
  	benutzer SMALLINT NOT NULL,
  	fahrt SMALLINT NOT NULL,
  	bewertung SMALLINT NOT NULL,
  	PRIMARY KEY (benutzer, fahrt),
  	FOREIGN KEY (benutzer) REFERENCES benutzer(bid),
  	FOREIGN KEY (fahrt) REFERENCES fahrt(fid),
  	FOREIGN KEY (bewertung) REFERENCES bewertung(beid)
);