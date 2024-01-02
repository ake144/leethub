# Write your MySQL query statement below

SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM 
    Employee e
INNER JOIN 
    Department d ON e.departmentId = d.id
WHERE 
    (e.departmentId, e.salary) IN (
        SELECT 
            e2.departmentId,
            MAX(e2.salary) AS max_salary
        FROM 
            Employee e2
        WHERE 
            e2.departmentId = e.departmentId
        GROUP BY 
            e2.departmentId
    );



