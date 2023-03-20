Select OrderId, DateOrdered, DateShipped, C.Country, C.RegionId into #z ad7 FROM Orders
JOIN Customer AS C ON C.CustomerId = C.CustomerId
WHERE COUNTRY = 'Japan'

SELECT DATEDIFF(DAY, DateOrdered, DateShipped) AS Diff, OrderId FROM #Zad7

SELECT AVG(diff), RegionName FROM zad7_CTE AS C
LEFT JOIN Region AS R ON R.RegionId = C.RegionId