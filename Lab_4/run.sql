-------------------------------------------------
--                  Функція                    --
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

-------------------------------------
-- Запит для перевірки результату  --
-------------------------------------

SELECT TRIM(Team_new.Name) AS Team_Name, SUM(PointsScored) AS Points
FROM car_new 
JOIN RaceDriver_new ON car_new.CarID = RaceDriver_new.CarID
JOIN Team_new ON car_new.TeamID = Team_new.TeamID
GROUP by Team_new.Name

SELECT team_points('McLaren')

SELECT team_points('Haas')
--------------------------------------------------------------------------

-------------------------------------------------
--                 Процедура                   --
-------------------------------------------------
--     Додавання нової команди в таблицю       --
-------------------------------------------------

CREATE OR REPLACE PROCEDURE add_new_team(t_name char(50))

LANGUAGE'plpgsql'
AS $$
   DECLARE 
      team_id team.teamid%type;

   BEGIN
      SELECT (teamid+1) INTO team_id FROM team ORDER BY teamid DESC LIMIT 1;
      INSERT INTO team(teamid, name)
      VALUES(team_id, t_name);
   END;
$$

CALL add_new_team('KM01')

-- -- DROP PROCEDURE add_new_team

SELECT * FROM team
--------------------------------------------------------------------------

----------------------------------------------------
--                    Тригер                      --
----------------------------------------------------
-- Додавання дати при додаванні команди в таблицю --
----------------------------------------------------

DROP TRIGGER IF EXISTS added_new_team ON team;
DROP FUNCTION IF EXISTS set_data;

CREATE FUNCTION set_data() RETURNS TRIGGER
LANGUAGE 'plpgsql'
AS
$$
   BEGIN 
      UPDATE Team
      SET
		   team_date = now()
      WHERE 
         team.teamid = NEW.teamid;
      RETURN NULL;
   END;
$$;

CREATE TRIGGER added_new_team
AFTER INSERT ON Team
FOR EACH ROW EXECUTE FUNCTION set_data();


CALL add_new_team('Romanetskiy')

SELECT * FROM team