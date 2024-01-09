import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = 'postgres'
database = 'Lab2'
host = 'localhost'
port = '5432'


query_1 = '''
CREATE VIEW Cars_brand AS
SELECT TRIM(brand) AS brand, count(*) AS quantity
FROM car_new
GROUP BY brand
'''

query_2 = '''
CREATE VIEW Team_points AS
SELECT TRIM(Team_new.Name) AS Team_Name, SUM(PointsScored) AS Points
FROM car_new 
JOIN RaceDriver_new ON car_new.CarID = RaceDriver_new.CarID
JOIN Team_new ON car_new.TeamID = Team_new.TeamID
GROUP by Team_new.Name
'''

query_3 = '''
CREATE VIEW Points_for_finishing_position AS
SELECT Position, PointsScored
FROM RaceDriver_new
ORDER BY POSITION DESC;
'''


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:

    cur1 = conn.cursor()
    cur1.execute('DROP VIEW IF EXISTS Cars_brand')
    cur1.execute(query_1)
    cur1.execute('SELECT * FROM Cars_brand')
    brand = []
    quanitity = []

    for row in cur1:
        brand.append(row[0])
        quanitity.append(row[1])

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3, figsize=(12, 8))

    x_range = range(len(brand))
    bar = bar_ax.bar(x_range, quanitity, width=0.5)
    bar_ax.set_title('Кількість машин збудованих командою', size=15)
    bar_ax.set_xlabel('Команди')
    bar_ax.set_ylabel('Кількість, шт')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(brand)

    # --------------------------------------------------------------------

    cur2 = conn.cursor()
    cur2.execute('DROP VIEW IF EXISTS Team_points')
    cur2.execute(query_2)
    cur2.execute('SELECT * FROM Team_points')
    team = []
    points = []

    for row in cur2:
        team.append(row[0])
        points.append(row[1])

    pie_ax.pie(points, labels=team, autopct='%1.1f%%', textprops={'fontsize': 8}, rotatelabels=False)
    pie_ax.set_title('Розподіл балів між командами')

    # --------------------------------------------------------------------

    cur3 = conn.cursor()
    cur3.execute('DROP VIEW IF EXISTS Points_for_finishing_position')
    cur3.execute(query_3)
    cur3.execute('SELECT * FROM Points_for_finishing_position')
    positions = []
    points = []

    for row in cur3:
        positions.append(row[0])
        points.append(row[1])

    graph_ax.plot(positions, points, marker='o')
    graph_ax.set_xlabel('Зайняте місце')
    graph_ax.set_ylabel('Кількість балів')
    graph_ax.set_title('Кількість балів у залежності від фінішної позиції')

    for qnt, price in zip(positions, points):
        graph_ax.annotate(price, xy=(qnt, price), xytext=(7, 2), textcoords='offset points') 

mng = plt.get_current_fig_manager()
mng.resize(1500, 600)
figure.tight_layout()
plt.show()


'''
Те що команда Haas є на круговій діаграмі (розподіл балів),
але цієї команди немає на стовпчиковій гістограмі (к-сть збудованих машин)
означає, що ця команда приймала участь у змаганнях, але самостійно не
будувала машини, а купували екземляри в інших команд
'''