import psycopg2

username = 'postgres'
password = 'postgres'
database = 'Lab2'
host = 'localhost'
port = '5432'

q_1 = '''
SELECT TRIM(brand) AS brand, count(*) AS quantity
FROM car
GROUP BY brand
'''

q_2 = '''
SELECT TRIM(Team.Name) AS Team_Name, SUM(PointsScored) AS Points
FROM car 
JOIN RaceDriver ON car.CarID = RaceDriver.CarID
JOIN Team ON car.TeamID = Team.TeamID
GROUP by Team.Name
'''

q_3 = '''
SELECT Position, PointsScored AS Points
FROM RaceDriver
ORDER BY POSITION DESC;
'''
try:
    conn=psycopg2.connect(user=username, 
                          password=password,
                          dbname=database, 
                          host=host,
                          port = port)

    try:
        with conn:
            print(f'\nThe Database - {database} is connected and ready to go')
            cur = conn.cursor()

            print('\n\n1th query - Number of cars created by engineering teams')
            cur.execute(q_1)
            for row in cur:
                print(row)

            print('\n\n2th query - The amount of earned points per team')
            cur.execute(q_2)
            for row in cur:
                print(row)

            print('\n\n3th query - The number of points depends on the finishing position')
            cur.execute(q_3)
            for row in cur:
                print(row)
    except:
        print('Something wrong with your query / database / tables')
    
except:
    print('\
You made a mistake somewhere among these parameters: \n\
username, password, database, host, port.\n\
Please, change it')