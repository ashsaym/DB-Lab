CREATE TABLE benutzer (
	bid SMALLINT NOT NULL GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(50) NOT NULL,
  	email VARCHAR(50) NOT NULL UNIQUE,
  	PRIMARY KEY (bid)
);