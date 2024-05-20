SELECT * FROM employee_tbl WHERE  (department_id, salary)
IN     (SELECT department_id, MAX(salary)
         FROM employee_tbl
         GROUP BY department_id);