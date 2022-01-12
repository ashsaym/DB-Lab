CREATE TABLE bewertung (
  	beid SMALLINT NOT NULL GENERATED BY DEFAULT AS IDENTITY,
  	textnachricht CLOB(1M) NOT NULL,
  	erstellungsdatum timestamp NOT NULL DEFAULT CURRENT TIMESTAMP,
  	rating SMALLINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
  	PRIMARY KEY (beid)
);