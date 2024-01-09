import psycopg2


username = 'postgres'
password = 'postgres'
database = 'Lab2'
host = 'localhost'
port = '5432'


query_Car = '''
CREATE TABLE car_new
(
	CarID 	INT 	 NOT NULL,
	TeamID 	INT 	 NOT NULL,
	Name 	CHAR(50) NOT NULL,
	Brand 	CHAR(50) NOT NULL,
	Number 	INT 	 NOT NULL,
    CONSTRAINT pk_car_new PRIMARY KEY (CarID)
);
'''

query_Location = '''
CREATE TABLE location_new
(
	LocationID 		INT 	  NOT NULL,
	LocationName 	CHAR(150) NOT NULL,
    CONSTRAINT pk_location_new PRIMARY KEY (LocationID)
);
'''

query_Pointssystem = '''
CREATE TABLE pointssystem_new
(
	PointsSystemID 	INT 	   NOT NULL,
	Name 			CHAR(50)   NOT NULL,
    CONSTRAINT pk_pointssystem_new PRIMARY KEY (PointsSystemID)
);
'''

query_Race = '''
CREATE TABLE race_new
(
	RaceID 		INT 	 NOT NULL,
	LocationID 	INT 	 NOT NULL,
	SeasonID 	INT 	 NOT NULL,
	Name		CHAR(50) NOT NULL,
	Date 		DATE 	 NOT NULL,
    CONSTRAINT pk_race_new PRIMARY KEY (RaceID)
);
'''

query_Racedriver = '''
CREATE TABLE racedriver_new
(
	RaceID 			INT 	NOT NULL,
	TeamMemberID 	INT 	NOT NULL,
	CarID 			INT 	NOT NULL,
	Position 		INT		NOT NULL,
	PointsScored 	INT 	NOT NULL
);
'''

query_Season = '''
CREATE TABLE season_new
(
	SeasonID 		INT 	 NOT NULL,
	PointsSystemID 	INT 	 NOT NULL,
	Name 			CHAR(50) NOT NULL,
	StartDate 		DATE 	 NOT NULL,
	EndDate 		DATE 	 NOT NULL,
    CONSTRAINT pk_season_new PRIMARY KEY (SeasonID)
);
'''

query_team = '''
CREATE TABLE team_new
(
	TeamID 	INT 	 NOT NULL,
	Name 	CHAR(50) NOT NULL,
    CONSTRAINT pk_team_new PRIMARY KEY (TeamID)
);
'''

query_teammember = '''
CREATE TABLE teammember_new
(
	TeamMemberID 	INT 	  NOT NULL,
	TeamID 			INT 	  NOT NULL,
	Name			CHAR(150) NOT NULL,
	JobFunction 	CHAR(150) NOT NULL,
	StartDate 		DATE 	  NOT NULL,
	EndDate 		DATE 	  NOT NULL,
    CONSTRAINT pk_teammember_new PRIMARY KEY (TeamMemberID)
);
'''


conn = psycopg2.connect(user=username, password=password, dbname=database)

cur = conn.cursor()

with open('D:\KPI\Databases\Labs\Lab_3\car_new.csv', 'r') as f0:
    cur.execute('DROP TABLE car_new')
    cur.execute(query_Car)
    next(f0)
    cur.copy_from(f0, 'car_new', sep=',')
conn.commit()

with open('D:\KPI\Databases\Labs\Lab_3\location_new.csv', 'r') as f1:
    cur.execute('DROP TABLE location_new')
    cur.execute(query_Location)
    next(f1)
    cur.copy_from(f1, 'location_new', sep=',')
conn.commit()

with open('D:\KPI\Databases\Labs\Lab_3\pointssystem_new.csv', 'r') as f2:
    cur.execute('DROP TABLE pointssystem_new')
    cur.execute(query_Pointssystem)
    next(f2)
    cur.copy_from(f2, 'pointssystem_new', sep=',')
conn.commit()

with open('D:\KPI\Databases\Labs\Lab_3\\race_new.csv', 'r') as f3:
    cur.execute('DROP TABLE race_new')
    cur.execute(query_Race)
    next(f3)
    cur.copy_from(f3, 'race_new', sep=',')
conn.commit()

with open('D:\KPI\Databases\Labs\Lab_3\\racedriver_new.csv', 'r') as f4:
    cur.execute('DROP TABLE racedriver_new')
    cur.execute(query_Racedriver)
    next(f4)
    cur.copy_from(f4, 'racedriver_new', sep=',')
conn.commit()

with open('D:\KPI\Databases\Labs\Lab_3\season_new.csv', 'r') as f5:
    cur.execute('DROP TABLE season_new')
    cur.execute(query_Season)
    next(f5)
    cur.copy_from(f5, 'season_new', sep=',')
conn.commit()

with open('D:\KPI\Databases\Labs\Lab_3\\team_new.csv', 'r') as f6:
    cur.execute('DROP TABLE team_new')
    cur.execute(query_team)
    next(f6)
    cur.copy_from(f6, 'team_new', sep=',')
conn.commit()

with open('D:\KPI\Databases\Labs\Lab_3\\teammember_new.csv', 'r') as f7:
    cur.execute('DROP TABLE teammember_new')
    cur.execute(query_teammember)
    next(f7)
    cur.copy_from(f7, 'teammember_new', sep=',')
conn.commit()
