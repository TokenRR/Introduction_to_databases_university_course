-- Number of cars created by engineering teams (Bar chart)
SELECT TRIM(brand) AS brand, count(*) AS quantity
FROM car
GROUP BY brand

-- The amount of earned points per team (Pie chart)
SELECT TRIM(Team.Name) AS Team_Name, SUM(PointsScored) AS Points
FROM car 
JOIN RaceDriver ON car.CarID = RaceDriver.CarID
JOIN Team ON car.TeamID = Team.TeamID
GROUP by Team.Name

-- The number of points depends on the finishing position (dependence graph)
SELECT Position, PointsScored AS Points
FROM RaceDriver
ORDER BY POSITION DESC;