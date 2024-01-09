SELECT * FROM Team

DO $$
    DECLARE
        id  Team.teamid%TYPE;

    BEGIN
        id := 0;
        FOR counter IN 1..5
            LOOP
                INSERT INTO Team(teamid)
                VALUES (id + counter);
            END LOOP;
    END;
$$
