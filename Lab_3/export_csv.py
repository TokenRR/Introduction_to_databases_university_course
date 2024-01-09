import csv
import psycopg2

username = 'postgres'
password = 'postgres'
database = 'Lab2'


OUTPUT_FILE_T = 'Lab3_DB_{}.csv'

TABLES = [
    'car_new',
    'location_new',
    'pointssystem_new',
    'race_new',
    'racedriver_new',
    'season_new',
    'team_new',
    'teammember_new',
]

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])