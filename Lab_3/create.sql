CREATE TABLE Race(
	RaceID 					INT 	 			NOT NULL,
	LocationID 				INT 	 			NOT NULL,
	SeasonID 				INT 	 			NOT NULL,
	Name					CHAR(50) 			NOT NULL,
	Date 					DATE 	 			NOT NULL
	);

CREATE TABLE Season(
	SeasonID 				INT 	 			NOT NULL,
	PointsSystemID 			INT 	 			NOT NULL,
	Name 					CHAR(50)			NOT NULL,
	StartDate 				DATE 	 			NOT NULL,
	EndDate 				DATE 				NOT NULL
	);

CREATE TABLE Location(
	LocationID 				INT 	  			NOT NULL,
	LocationName 			CHAR(150) 			NOT NULL
	);

CREATE TABLE RaceDriver(
	RaceID 					INT 				NOT NULL,
	TeamMemberID 			INT 				NOT NULL,
	CarID 					INT 				NOT NULL,
	Position 				INT					NOT NULL,
	PointsScored 			INT 				NOT NULL
	);

CREATE TABLE TeamMember(
	TeamMemberID 			INT 	  			NOT NULL,
	TeamID 					INT 	  			NOT NULL,
	Name					CHAR(150) 			NOT NULL,
	JobFunction 			CHAR(150) 			NOT NULL,
	StartDate 				DATE 	  			NOT NULL,
	EndDate 				DATE 	  			NOT NULL
	);

CREATE TABLE PointsSystem(
	PointsSystemID 			INT 	  			NOT NULL,
	Name 					CHAR(50)   			NOT NULL
	);

CREATE TABLE Team(
	TeamID 					INT 	 			NOT NULL,
	Name 					CHAR(50) 			NOT NULL
	);

CREATE TABLE Car(
	CarID 					INT 	 			NOT NULL,
	TeamID 					INT 	 			NOT NULL,
	Name 					CHAR(50) 			NOT NULL,
	Brand 					CHAR(50) 			NOT NULL,
	Number 					INT 	 			NOT NULL
	);
	

-------------------------
-- Define primary keys --
-------------------------
ALTER TABLE Race ADD 			PRIMARY KEY (RaceID);
ALTER TABLE Season ADD 			PRIMARY KEY (SeasonID);
ALTER TABLE Location ADD 		PRIMARY KEY (LocationID);
ALTER TABLE TeamMember ADD 		PRIMARY KEY (TeamMemberID);
ALTER TABLE PointsSystem ADD 	PRIMARY KEY (PointsSystemID);
ALTER TABLE Team ADD 			PRIMARY KEY (TeamID);
ALTER TABLE Car ADD 			PRIMARY KEY (CarID);


-------------------------
-- Define foreign keys --
-------------------------
ALTER TABLE RaceDriver ADD CONSTRAINT FK_racedriver_race
FOREIGN KEY (RaceID) REFERENCES Race (RaceID);

ALTER TABLE RaceDriver ADD CONSTRAINT FK_racedriver_teammember
FOREIGN KEY (TeamMemberID) REFERENCES TeamMember (TeamMemberID);

ALTER TABLE RaceDriver ADD CONSTRAINT FK_racedriver_car
FOREIGN KEY (CarID) REFERENCES Car (CarID);

ALTER TABLE Race ADD CONSTRAINT FK_race_season
FOREIGN KEY (SeasonID) REFERENCES Season (SeasonID);

ALTER TABLE Race ADD CONSTRAINT FK_race_location
FOREIGN KEY (LocationID) REFERENCES Location (LocationID);

ALTER TABLE Season ADD CONSTRAINT FK_season_pointssystem
FOREIGN KEY (PointsSystemID) REFERENCES PointsSystem (PointsSystemID);

ALTER TABLE TeamMember ADD CONSTRAINT FK_teammember_team
FOREIGN KEY (TeamID) REFERENCES Team (TeamID);
