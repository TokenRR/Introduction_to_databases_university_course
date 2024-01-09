-------------------------------------------------
-- Знаходження кількості балів однієї команди  --
-------------------------------------------------

DROP FUNCTION IF EXISTS team_points;

CREATE OR REPLACE FUNCTION team_points(team_name character(50))
RETURNS INTEGER
LANGUAGE 'plpgsql'

AS $$
   BEGIN
      RETURN (SELECT SUM(PointsScored) AS Points
              FROM car_new 
              JOIN RaceDriver_new ON car_new.CarID = RaceDriver_new.CarID
              JOIN Team_new ON car_new.TeamID = Team_new.TeamID
              Where Team_new.Name = team_name
              GROUP by Team_new.Name);
   END;
$$


SELECT team_points('McLaren')

SELECT team_points('Haas')
