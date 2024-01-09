INSERT INTO Location(LocationID, LocationName)
VALUES
('1', 'USA'),
('2', 'France'),
('3', 'Ukraine'),
('4', 'Canada'),
('5', 'Japan');

INSERT INTO Team(TeamID, Name, team_date) 
VALUES
('1', 'McLaren',      NULL),
('2', 'Mercedes AMG', NULL),
('3', 'Ferrari',      NULL),
('4', 'Haas',         NULL),
('5', 'Aston Martin', NULL);

INSERT INTO PointsSystem(PointsSystemID, Name) 
VALUES
('1', '1980'),
('2', '1981-1990'),
('3', '1991-2002'),
('4', '2003-2009'),
('5', '2010-2018');

INSERT INTO Season(SeasonID, PointsSystemID, Name, StartDate, EndDate) 
VALUES
('1', '3', '2014 Formula One World Championship', '2014-03-28', '2014-11-25'),
('2', '3', '2015 Formula One World Championship', '2015-03-19', '2015-11-24'),
('3', '3', '2016 Formula One World Championship', '2016-03-20', '2016-11-27'),
('4', '3', '2017 Formula One World Championship', '2017-03-26', '2017-11-26'),
('5', '3', '2018 Formula One World Championship', '2018-03-25', '2018-11-25');

INSERT INTO TeamMember(TeamMemberID, TeamID, Name, JobFunction, StartDate, EndDate) 
VALUES
('1', '1', 'Lando Norris',     'Driver',  '2015-05-20', '2020-10-27'),
('2', '1', 'Daniel Ricciardo', 'Driver',  '2015-07-28', '2020-03-10'),
('3', '2', 'Lewis Hamilton',   'Driver',  '2015-05-16', '2020-10-01'),
('4', '2', 'Valtteri Bottas',  'Driver',  '2015-07-06', '2020-07-10'),
('5', '3', 'Sebastian Vettel', 'Driver',  '2015-12-15', '2020-03-08');

INSERT INTO Race(RaceID, LocationID, SeasonID, Name, Date) 
VALUES
('1', '1', '5', 'The Circuit of the Americas',  '2018-06-15'),
('2', '2', '5', 'Le Castellet',                 '2018-07-10'),
('3', '3', '5', 'Chaika Motorsports Complex',   '2018-08-20'),
('4', '4', '5', 'Circuit de Gilles-Villeneuve', '2018-09-12'),
('5', '5', '5', 'Suzuka',                       '2018-10-01');

INSERT INTO Car(CarID, TeamID, Name, Brand, Number) 
VALUES
('1', '1', 'MCL34',                         'McLaren',      '34'),
('2', '1', 'MCL35',                         'McLaren',      '35'),
('3', '2', 'Mercedes AMG F1 W09 EQ Power+', 'Mercedes-AMG', '09'),
('4', '2', 'Mercedes AMG F1 W10 EQ Power+', 'Mercedes-AMG', '10'),
('5', '3', 'Ferrari SF71H',                 'McLaren',      '71');

INSERT INTO RaceDriver(RaceID, TeamMemberID, CarID, Position, PointsScored) 
VALUES
('5', '1', '1', '1', '25'),
('5', '2', '1', '7', '6'),
('5', '3', '3', '2', '18'),
('5', '4', '3', '4', '12'),
('5', '5', '5', '9', '2');
