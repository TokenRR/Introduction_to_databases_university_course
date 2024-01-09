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