# SQL Frequently Asked Questions

## 1. What is SQL and what are its main features?

SQL (Structured Query Language) is a standard programming language used for accessing and manipulating databases. Its main features include:

- **Data Querying**: Retrieve specific data from databases using the `SELECT` statement.
- **Data Manipulation**: Insert, update, and delete data with `INSERT`, `UPDATE`, and `DELETE` statements.
- **Data Definition**: Define and modify database structures using `CREATE`, `ALTER`, and `DROP` statements.
- **Data Control**: Control access to data through `GRANT` and `REVOKE` statements.

## 2. What are some of the most common SQL commands?

- `CREATE TABLE`: Creates a new table in the database.
- `INSERT INTO`: Adds new records to a table.
- `UPDATE`: Modifies existing records in a table.
- `DELETE`: Removes records from a table.
- `SELECT`: Retrieves data from one or more tables.

## 3. Explain the different types of JOINs in SQL.

- **INNER JOIN**: Returns records that have matching values in both tables.
- **LEFT JOIN (LEFT OUTER JOIN)**: Returns all records from the left table and the matched records from the right table; returns `NULL` for unmatched rows from the right table.
- **RIGHT JOIN (RIGHT OUTER JOIN)**: Returns all records from the right table and the matched records from the left table; returns `NULL` for unmatched rows from the left table.
- **FULL JOIN (FULL OUTER JOIN)**: Returns all records when there is a match in either left or right table; returns `NULL` for unmatched rows from both tables.

## 4. What is the difference between `WHERE` and `HAVING` clauses?

- **`WHERE`**: Filters records before any groupings are made; it cannot be used with aggregate functions.
- **`HAVING`**: Filters records after groupings are made; it can be used with aggregate functions.

## 5. How would you retrieve the second highest salary from an `employees` table?

You can use the `LIMIT` clause with an offset:

```sql
SELECT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

Alternatively, using a subquery:

```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

## 6. What is a primary key and a foreign key?

- **Primary Key**: A field (or combination of fields) that uniquely identifies each record in a table. It must contain unique values and cannot contain `NULL` values.
- **Foreign Key**: A field (or combination of fields) in one table that uniquely identifies a row of another table. It establishes a link between the data in the two tables.

## 7. Write a SQL query to find the total number of orders placed by each customer.

Assuming a table `orders` with columns `order_id`, `customer_id`, and `order_date`:

```sql
SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id;
```

## 8. How can you delete duplicate records from a table?

One approach is to use a Common Table Expression (CTE) with the `ROW_NUMBER()` window function:

```sql
WITH CTE AS (
  SELECT *,
         ROW_NUMBER() OVER (PARTITION BY column1, column2 ORDER BY (SELECT 0)) AS rn
  FROM table_name
)
DELETE FROM CTE WHERE rn > 1;
```

Replace `column1`, `column2` with the columns that define duplicates.

## 9. Explain the ACID properties in a database.

- **Atomicity**: Ensures that all operations within a transaction are completed successfully; if not, the transaction is aborted.
- **Consistency**: Ensures that the database remains in a consistent state before and after the transaction.
- **Isolation**: Ensures that transactions are executed in isolation; intermediate transaction results are not visible to other transactions.
- **Durability**: Ensures that the results of a completed transaction are permanently stored in the database, even in the event of a system failure.

## 10. What is normalization? Explain its types.

Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. The types include:

- **First Normal Form (1NF)**: Ensures that the table has a primary key and that all columns contain atomic (indivisible) values.
- **Second Normal Form (2NF)**: Achieved when the table is in 1NF and all non-key columns are fully functional dependent on the primary key.
- **Third Normal Form (3NF)**: Achieved when the table is in 2NF and all the columns are not transitively dependent on the primary key.

## 11. What is the difference between `DELETE`, `TRUNCATE`, and `DROP` statements?

- **`DELETE`**: Removes specific rows from a table based on a condition specified in the `WHERE` clause. This operation can be rolled back and triggers any `DELETE` triggers on the table.
- **`TRUNCATE`**: Removes all rows from a table, resetting any auto-increment counters. It is a DDL (Data Definition Language) operation and cannot be rolled back in some databases. `TRUNCATE` is faster than `DELETE` because it doesn't generate individual row delete operations.
- **`DROP`**: Deletes the entire table structure from the database, including all its data, constraints, and indexes. This operation cannot be rolled back.

## 12. Explain the concept of indexing in SQL.

An **index** in SQL is a database object that improves the speed of data retrieval operations on a table at the cost of additional storage space and maintenance overhead. Indexes are created on columns that are frequently used in `WHERE` clauses, join conditions, or as sorting columns in `ORDER BY` clauses.

Types of indexes:

- **Clustered Index**: Alters the physical order of the table and searches based on the key values. A table can have only one clustered index.
- **Non-Clustered Index**: Creates a logical order that doesn't alter the physical order of the table. A table can have multiple non-clustered indexes.
- **Unique Index**: Ensures that all the values in the index key are unique.
- **Full-Text Index**: Used for full-text searches.

## 13. What are subqueries and correlated subqueries?

- **Subquery**: A query nested inside another query. It is executed once, and its result is used by the outer query.

  Example:
  ```sql
  SELECT employee_id, first_name, last_name
  FROM employees
  WHERE department_id = (SELECT department_id
                         FROM departments
                         WHERE department_name = 'Sales');
  ```

- **Correlated Subquery**: A subquery that references columns from the outer query. It is executed once for each row processed by the outer query.

  Example:
  ```sql
  SELECT e1.employee_id, e1.first_name, e1.last_name
  FROM employees e1
  WHERE e1.salary > (SELECT AVG(e2.salary)
                     FROM employees e2
                     WHERE e2.department_id = e1.department_id);
  ```

## 14. How can you improve the performance of a SQL query?

- **Use Indexes**: Create indexes on columns that are frequently used in `WHERE` clauses, join conditions, or sorting.
- **Avoid Using `SELECT *`**: Specify only the columns you need to reduce the amount of data transferred.
- **Use Joins Instead of Subqueries**: Joins are generally more efficient than subqueries.
- **Filter Early**: Use the `WHERE` clause to filter data as early as possible in the query.
- **Limit the Use of Wildcards**: Avoid leading wildcards in `LIKE` clauses, as they prevent the use of indexes.
- **Optimize Joins**: Ensure that join conditions are based on indexed columns and use the most restrictive joins first.

## 15. What is a Common Table Expression (CTE)?

A **Common Table Expression (CTE)** is a temporary result set defined within the execution scope of a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement. CTEs improve readability and maintainability of complex queries by breaking them into simpler, reusable components.

Example:

```sql
WITH Sales_CTE AS (
  SELECT salesperson_id, SUM(sales_amount) AS total_sales
  FROM sales
  GROUP BY salesperson_id
)
SELECT s.salesperson_id, s.total_sales, e.first_name, e.last_name
FROM Sales_CTE s
JOIN employees e ON s.salesperson_id = e.employee_id
WHERE s.total_sales > 100000;
```


## **16. Explain the difference between `UNION` and `UNION ALL`.**

- **`UNION`**: Combines the result sets of two or more `SELECT` statements into a single result set, removing duplicate rows.

- **`UNION ALL`**: Combines the result sets of two or more `SELECT` statements into a single result set, including all duplicate rows.

**17. How do you find the top `N` records in a table?**

To retrieve the top `N` records from a table, you can use the `LIMIT` clause (in MySQL, PostgreSQL) or the `TOP` keyword (in SQL Server).

- **MySQL/PostgreSQL**:

  ```sql
  SELECT *
  FROM employees
  ORDER BY salary DESC
  LIMIT 5;
  ```

- **SQL Server**:

  ```sql
  SELECT TOP 5 *
  FROM employees
  ORDER BY salary DESC;
  ```

## **18. What is the purpose of the `HAVING` clause?**

The `HAVING` clause is used to filter groups of rows after the `GROUP BY` clause has been applied. It allows you to specify conditions on aggregate functions, which cannot be done using the `WHERE` clause.

```sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 10;
```

## **19. Describe the different types of normalization forms.**

Normalization is the process of organizing data to reduce redundancy and improve data integrity. The normal forms include:

- **First Normal Form (1NF)**: Ensures that each column contains atomic (indivisible) values and each record is unique.

- **Second Normal Form (2NF)**: Achieved when the table is in 1NF and all non-key columns are fully functionally dependent on the primary key.

- **Third Normal Form (3NF)**: Achieved when the table is in 2NF and all the columns are not transitively dependent on the primary key.

- **Boyce-Codd Normal Form (BCNF)**: A stronger version of 3NF where every determinant is a candidate key.

## **20. What are window functions in SQL?**

Window functions perform calculations across a set of 


## **21. What is the difference between `UNION` and `UNION ALL`?**

- **`UNION`**: Combines the result sets of two or more `SELECT` statements into a single result set, removing duplicate rows.
- **`UNION ALL`**: Combines the result sets of two or more `SELECT` statements into a single result set, including all duplicate rows.

## **22. How can you retrieve the first 5 records from a table?**

To retrieve the first 5 records from a table, you can use the `LIMIT` clause (in MySQL, PostgreSQL) or the `TOP` keyword (in SQL Server).

- **MySQL/PostgreSQL**:

  ```sql
  SELECT *
  FROM table_name
  LIMIT 5;
  ```

- **SQL Server**:

  ```sql
  SELECT TOP 5 *
  FROM table_name;
  ```

## **23. Explain the use of the `HAVING` clause in SQL.**

The `HAVING` clause is used to filter groups of rows after the `GROUP BY` clause has been applied. It allows you to specify conditions on aggregate functions, which cannot be done using the `WHERE` clause.

```sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 10;
```

## **24. What is a subquery, and how is it used?**

A **subquery** is a query nested inside another query. It can be used in various parts of an SQL statement, such as the `SELECT`, `FROM`, `WHERE`, or `HAVING` clauses. Subqueries are useful for breaking down complex queries into simpler components.

Example:

```sql
SELECT employee_id, first_name, last_name
FROM employees
WHERE department_id = (SELECT department_id
                       FROM departments
                       WHERE department_name = 'Sales');
```

## **25. How do you find the maximum salary in each department?**

To find the maximum salary in each department, you can use the `GROUP BY` clause along with the `MAX` aggregate function:

```sql
SELECT department_id, MAX(salary) AS max_salary
FROM employees
GROUP BY department_id;
```

## **26. What is a self-join, and when would you use it?**

A **self-join** is a join in which a table is joined with itself. It is useful when you need to compare rows within the same table.

Example: Finding employees who have the same manager.

```sql
SELECT e1.employee_id AS Employee, e2.employee_id AS Manager
FROM employees e1
JOIN employees e2 ON e1.manager_id = e2.employee_id;
```

## **27. Explain the difference between `CHAR` and `VARCHAR` data types.**

- **`CHAR(n)`**: A fixed-length character data type. It always reserves space for `n` characters, padding with spaces if the input is shorter.
- **`VARCHAR(n)`**: A variable-length character data type. It stores only the characters you assign, plus a byte or two to record the length of the string, saving storage space.

## **28. How can you remove duplicate rows from a result set?**

To remove duplicate rows from a result set, you can use the `DISTINCT` keyword:

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

## **29. What is a stored procedure, and what are its benefits?**

A **stored procedure** is a set of SQL statements that can be stored in the database and executed repeatedly. Benefits include:

- **Modularity**: Encapsulates complex operations for reuse.
- **Performance**: Reduces client-server communication and can be optimized by the database server.
- **Security**: Restricts direct access to data and can encapsulate business logic.

## **30. How do you handle NULL values in SQL?**

NULL values represent missing or unknown data. To handle NULL values:

- Use the `IS NULL` or `IS NOT NULL` operators in `WHERE` clauses.
- Use functions like `COALESCE` or `IFNULL` to replace NULL with a default value.
- Be cautious with arithmetic operations, as they can result in NULL if any operand is NULL.

## 41. What is the purpose of the `GROUP BY` clause in SQL?

The `GROUP BY` clause in SQL is used to arrange identical data into groups. This is often used with aggregate functions like `COUNT`, `SUM`, `AVG`, `MAX`, or `MIN` to perform operations on each group of data.

**Example:**

```sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;
```

This query groups employees by their department and counts the number of employees in each department.

## 42. How do you find the second highest salary from a table?

To find the second highest salary, you can use a subquery that selects the maximum salary less than the highest salary.

**Example:**

```sql
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

This query first finds the highest salary and then selects the maximum salary that is less than this value, effectively giving the second highest salary.

## 43. What is the difference between `INNER JOIN` and `OUTER JOIN`?

- **`INNER JOIN`**: Returns records that have matching values in both tables.

- **`OUTER JOIN`**: Returns all records when there is a match in one of the tables. It can be further classified into:

  - **`LEFT OUTER JOIN`**: Returns all records from the left table and the matched records from the right table.

  - **`RIGHT OUTER JOIN`**: Returns all records from the right table and the matched records from the left table.

  - **`FULL OUTER JOIN`**: Returns all records when there is a match in either left or right table.

**Example:**

```sql
-- INNER JOIN
SELECT employees.first_name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id;

-- LEFT OUTER JOIN
SELECT employees.first_name, departments.department_name
FROM employees
LEFT OUTER JOIN departments ON employees.department_id = departments.department_id;
```

The first query returns employees with their corresponding department names where a match exists, while the second query returns all employees and their department names, including those without a matching department.

## 44. What is the purpose of the `DISTINCT` keyword in SQL?

The `DISTINCT` keyword is used to return only distinct (different) values in the result set. It eliminates duplicate records from the result set.

**Example:**

```sql
SELECT DISTINCT department_id
FROM employees;
```

This query returns a list of unique department IDs from the employees table.

## 45. How do you update data in a table?

To update data in a table, you use the `UPDATE` statement along with the `SET` clause to specify the columns to be updated and the `WHERE` clause to specify which records should be updated.

**Example:**

```sql
UPDATE employees
SET salary = 50000
WHERE employee_id = 101;
```

This query updates the salary of the employee with `employee_id` 101 to 50,000.

## 46. What is a `CASE` statement in SQL?

The `CASE` statement in SQL is used to create conditional logic within a query. It allows you to perform IF-THEN-ELSE operations in SQL.

**Example:**

```sql
SELECT first_name, last_name,
       CASE
           WHEN salary > 70000 THEN 'High'
           WHEN salary BETWEEN 50000 AND 70000 THEN 'Medium'
           ELSE 'Low'
       END AS salary_grade
FROM employees;
```

This query assigns a salary grade based on the salary of each employee.

## 47. How do you delete data from a table?

To delete data from a table, you use the `DELETE` statement along with the `WHERE` clause to specify which records should be deleted.

**Example:**

```sql
DELETE FROM employees
WHERE employee_id = 101;
```

This query deletes the record of the employee with `employee_id` 101.

## 48. What is the purpose of the `LIMIT` clause in SQL?

The `LIMIT` clause is used to specify the number of records to return in the result set. It is commonly used to retrieve a subset of records.

**Example:**

```sql
SELECT * FROM employees
LIMIT 10;
```

This query returns the first 10 records from the employees table.

## 49. What is a `JOIN` in SQL?

A `JOIN` in SQL is used to combine rows from two or more tables based on a related column between them.

**Example:**

```sql
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
JOIN departments ON employees.department_id = departments.department_id;
```

This query retrieves the first name, last name, and department name for each employee by joining the employees and departments tables on the `department_id` column.

## 50. How do you find the total number of records in a table?

To find the total number of records in a table, you can use the `COUNT` function.

**Example:**

```sql
SELECT COUNT(*) AS total_records
FROM employees;
```

This query returns the total number of records in the employees table.

## 51. What is the difference between `WHERE` and `HAVING` clauses?

- **`WHERE`**: Filters records before any groupings are made. It operates on individual rows.

- **`HAVING`**: Filters records after the `GROUP BY` clause has been applied. It operates on aggregated data.

**Example:**

```sql
-- Using WHERE
SELECT department_id, COUNT(*) AS employee_count
FROM employees
WHERE salary > 50000
GROUP BY department_id;

-- Using HAVING
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 10;
```

The first query filters employees with a salary greater than 50,000 before grouping, while the second filters departments having more than 10 employees after grouping.

## 52. How do you find the total number of records in a table?

To find the total number of records in a table, you can use the `COUNT` function.

**Example:**

```sql
SELECT COUNT(*) AS total_records
FROM employees;
```

This query returns the total number of records in the employees table.

## 53. What is a subquery, and how is it used?

A **subquery** is a query nested inside another query. It can be used in various parts of an SQL statement, such as the `SELECT`, `FROM`, `WHERE`, or `HAVING` clauses. Subqueries are useful for breaking down complex queries into simpler components.

**Example:**

```sql
SELECT employee_id, first_name, last_name
FROM employees
WHERE department_id = (SELECT department_id
                       FROM departments
                       WHERE department_name = 'Sales');
```

This query retrieves employees who work in the 'Sales' department by using a subquery to find the department ID.

## 54. What is a self-join, and when would you use it?

A **self-join** is a join in which a table is joined with itself. It is useful when you need to compare rows within the same table.

**Example:**

```sql
SELECT e1.employee_id AS Employee, e2.employee_id AS Manager
FROM employees e1
JOIN employees e2 ON e1.manager_id = e2.employee_id;
```

This query finds employees and their corresponding managers by joining the employees table with itself.

## 55. Explain the difference between `CHAR` and `VARCHAR` data types.

- **`CHAR(n)`**: A fixed-length character data type. It always reserves space for `n` characters, padding with spaces if the input is shorter.

- **`VARCHAR(n)`**: A variable-length character data type. It stores only the characters you assign, plus a byte or two to record the length of the string, saving storage space.

**Example:**

```sql
CREATE TABLE employees (
    employee_id INT,
    first_name CHAR(50),
    last_name VARCHAR(100)
);
```

In this table, `first_name` is a fixed-length field, while `last_name` is a variable-length field.

## 56. How can you remove duplicate rows from a result set?

To remove duplicate rows from a result set, you can use the `DISTINCT` keyword.

**Example:**

```sql
SELECT DISTINCT department_id
FROM employees;
```

This query returns a list of unique department IDs from the employees table.

## 57. What is a stored procedure, and what are its benefits?

A **stored procedure** is a set of SQL statements that can be stored in the database and executed repeatedly. Benefits include:

- **Modularity**: Encapsulates complex operations for reuse.

- **Performance**: Reduces client-server communication and can be optimized by the database server.

- **Security**: Restricts direct access to data and can encapsulate business logic.

**Example:**

```sql
CREATE PROCEDURE GetEmployeeDetails (IN emp_id INT)
BEGIN
    SELECT * FROM employees WHERE employee_id = emp_id;
END;
```

This stored procedure retrieves employee details based on the provided employee ID.

## 58. How do you handle NULL values in SQL?

NULL values represent missing or unknown data. To handle NULL values:

- Use the `IS NULL` or `IS NOT NULL` operators in `WHERE` clauses.

- Use the `COALESCE` function to replace NULL with a default value.

**Example:**

```sql
SELECT first_name, last_name, COALESCE(phone_number, 'N/A') AS phone_number
FROM employees;
```

This query replaces any NULL `phone_number` values with 'N/A'.

## 59. What is the purpose of the `GROUP BY` clause in SQL?

The `GROUP BY` clause in SQL is used to arrange identical data into groups. This is often used with aggregate functions like `COUNT`, `SUM`, `AVG`, `MAX`, or `MIN` to perform operations on each group of data.

**Example:**

```sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;
```

This query groups employees by their department and counts the number of employees in each department.

## 60. How do you find the second highest salary from a table?

To find the second highest salary, you can use a subquery that selects the maximum salary less than the highest salary.

**Example:**

```sql
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

This query first finds the highest salary and then selects the maximum salary that is less than 