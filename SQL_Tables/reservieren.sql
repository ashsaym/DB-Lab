CREATE TABLE reservieren (
  	kunde SMALLINT NOT NULL,
  	fahrt SMALLINT NOT NULL,
  	anzPlaetze SMALLINT NOT NULL CHECK (anzPlaetze BETWEEN 1 AND 2),
  	PRIMARY KEY (kunde, fahrt),
  	FOREIGN KEY (kunde) REFERENCES benutzer(bid),
  	FOREIGN KEY (fahrt) REFERENCES fahrt(fid)
);