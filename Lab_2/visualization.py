import psycopg2
import matplotlib.pyplot as plt

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

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:

    cur = conn.cursor()

    cur.execute(q_1)
    teams = []
    quantity = []

    for row in cur:
        teams.append(row[0])
        quantity.append(row[1])

    x_range = range(len(teams))
 
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    
    bar_ax.bar(x_range, quantity, label='Кількість')
    bar_ax.set_title('Кількість болідів створена інженерними командами')
    bar_ax.set_xlabel('Команди')
    bar_ax.set_ylabel('Кількість, шт')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(teams)


    cur.execute(q_2)

    teams = []
    points = []

    for row in cur:
        teams.append(row[0])
        points.append(row[1])

    pie_ax.pie(points, labels=teams, autopct='%1.1f%%')
    pie_ax.set_title('Кількість зароблених балів командою')

  
    cur.execute(q_3)
    positions = []
    points = []
  
    for row in cur:
        positions.append(row[0])
        points.append(row[1])

    graph_ax.plot(positions, points, marker='o')
    graph_ax.set_xlabel('Зайняте місце')
    # graph_ax.set_ylabel('Кількість балів')
    graph_ax.set_title('Графік кількості балів у залежності від фінішної позиції')

    for qnt, price in zip(positions, points):
        graph_ax.annotate(price, xy=(qnt, price), xytext=(7, 2), textcoords='offset points')    


mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()
