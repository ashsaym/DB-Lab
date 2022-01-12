CREATE TABLE fahrt (
  	fid SMALLINT NOT NULL GENERATED ALWAYS AS IDENTITY,
  	startort VARCHAR(100) NOT NULL,
  	zielort VARCHAR(100) NOT NULL,
  	fahrtdatumzeit timestamp NOT NULL,
	maxPlaetze SMALLINT NOT NULL CHECK (maxPlaetze BETWEEN 1 AND 10),
	fahrtkosten DECIMAL(10,2) NOT NULL,
	status VARCHAR(11) NOT NULL CHECK (status IN ('offen', 'geschlossen')) DEFAULT 'offen',
  	anbieter SMALLINT NOT NULL,
  	transportmittel SMALLINT NOT NULL,
  	beschreibung CLOB (1M),
  	PRIMARY KEY (fid),
  	FOREIGN KEY (anbieter) REFERENCES benutzer(bid),
  	FOREIGN KEY (transportmittel) REFERENCES transportmittel(tid)
);