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