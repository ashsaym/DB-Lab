CREATE TABLE fahrerlaubnis (
  	fahrer SMALLINT NOT NULL,
  	nummer SMALLINT NOT NULL GENERATED BY DEFAULT AS IDENTITY,
  	ablaufdatum timestamp NOT NULL,
  	PRIMARY KEY (fahrer, nummer),
  	FOREIGN KEY (fahrer) REFERENCES benutzer(bid)
);