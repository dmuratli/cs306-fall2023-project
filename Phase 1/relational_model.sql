CREATE DATABASE RevolutionaryHarmony;

USE RevolutionaryHarmony;

CREATE TABLE Labels(
	lid INTEGER NOT NULL,
	lname VARCHAR(255),
	website VARCHAR(255),
	lcountry VARCHAR(255),
	est_year INTEGER,
	PRIMARY KEY (lid)
);

CREATE TABLE Artists(
	artid INTEGER NOT NULL,
	atype VARCHAR(10),
	aname VARCHAR(255),
	acountry VARCHAR(255),
	deb_year INTEGER,
	PRIMARY KEY (artid)
);

CREATE TABLE Albums(
	albid INTEGER NOT NULL,
	atitle VARCHAR(255),
	rel_year INTEGER,
	lid INTEGER NOT NULL,
	artid INTEGER NOT NULL,
	PRIMARY KEY (albid),
	FOREIGN KEY (lid) REFERENCES Labels ON DELETE NO ACTION,
	FOREIGN KEY (artid) REFERENCES Artists ON DELETE NO ACTION
);

CREATE TABLE Tracks(
	tid INTEGER NOT NULL,
	lang VARCHAR(255),
	trtitle VARCHAR(255),
	PRIMARY KEY (tid)
);

CREATE TABLE Part_Of(
	tid INTEGER NOT NULL,
	albid INTEGER NOT NULL,
	PRIMARY KEY (tid, albid),
	FOREIGN KEY (tid) REFERENCES Tracks ON DELETE NO ACTION,
	FOREIGN KEY (albid) REFERENCES Albums ON DELETE NO ACTION
);