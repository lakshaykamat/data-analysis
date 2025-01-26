# 90% of the companies ask the same SQL questions 

1. **Explain order of execution of SQL:**
   - The order of execution in SQL is:
     1. `FROM` clause
     2. `WHERE` clause
     3. `GROUP BY` clause
     4. `HAVING` clause
     5. `SELECT` clause
     6. `ORDER BY` clause

2. **What is the difference between `WHERE` and `HAVING`?**
   - `WHERE` clause filters rows before grouping, while `HAVING` clause filters groups after grouping.
   - `WHERE` is used with individual rows, `HAVING` is used with groups.

3. **What is the use of `GROUP BY`?**
   - The `GROUP BY` clause is used to group rows that have the same values into summary rows, like when you want to count the number of customers in each country.

4. **Explain all types of joins in SQL:**
   - `INNER JOIN`: Returns rows when there is a match in both tables.
   - `LEFT JOIN`: Returns all rows from the left table, and the matched rows from the right table.
   - `RIGHT JOIN`: Returns all rows from the right table, and the matched rows from the left table.
   - `FULL JOIN`: Returns all rows when there is a match in either left or right table.

5. **What are triggers in SQL?**
   - Triggers are special types of stored procedures that automatically run when an event occurs in the database, such as an insert, update, or delete.

6. **What is a stored procedure in SQL?**
   - A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.

7. **Explain all types of window functions:**
   - `RANK()`: Assigns a rank to each row within a partition.
   - `DENSE_RANK()`: Assigns a rank to each row within a partition, without gaps.
   - `ROW_NUMBER()`: Assigns a unique sequential number to each row within a partition.
   - `LEAD()`: Returns the value of a specified column from the next row in the partition.
   - `LAG()`: Returns the value of a specified column from the previous row in the partition.

8. **What is the difference between `DELETE` and `TRUNCATE`?**
   - `DELETE` removes specific rows from a table, while `TRUNCATE` removes all rows from a table.
   - `DELETE` is a DML (Data Manipulation Language) statement, `TRUNCATE` is a DDL (Data Definition Language) statement.

9. **What is the difference between DML, DDL, and DCL?**
   - DML (Data Manipulation Language): `SELECT`, `INSERT`, `UPDATE`, `DELETE`
   - DDL (Data Definition Language): `CREATE`, `ALTER`, `DROP`, `TRUNCATE`
   - DCL (Data Control Language): `GRANT`, `REVOKE`

10. **What are aggregate functions and when do we use them?**
    - Aggregate functions are used to perform calculations on multiple rows and return a single value.
    - Examples: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
    - Use cases: finding totals, averages, minimums, maximums, etc.

11. **Which is faster between CTE and Subquery?**
    - In general, CTEs are faster than correlated subqueries, but subqueries can be faster than uncorrelated CTEs.
    - The performance depends on the specific query and the database engine's optimization capabilities.

12. **What are constraints and types of constraints?**
    - Constraints are rules that the data must follow.
    - Types of constraints: `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`.

13. **Types of Keys:**
    - Primary Key: Uniquely identifies each row in a table.
    - Foreign Key: Links two tables by referencing the primary key of another table.
    - Composite Key: Combination of two or more columns that uniquely identifies each row.

14. **Different types of Operators:**
    - Arithmetic Operators: `+`, `-`, `*`, `/`, `%`
    - Comparison Operators: `=`, `<>`, `>`, `<`, `>=`, `<=`
    - Logical Operators: `AND`, `OR`, `NOT`

15. **Difference between `GROUP BY` and `WHERE`:**
    - `WHERE` clause filters rows before grouping, `GROUP BY` clause groups the resulting rows.
    - `WHERE` operates on individual rows, `GROUP BY` operates on groups of rows.

16. **What are Views?**
    - Views are virtual tables based on the result set of an SQL statement.
    - Views provide an abstraction layer, allowing users to query data without knowing the underlying table structure.

17. **What are different types of constraints?**
    - `NOT NULL`: Ensures that a column cannot have a NULL value.
    - `UNIQUE`: Ensures that all values in a column are different.
    - `PRIMARY KEY`: Uniquely identifies each row in a table.
    - `FOREIGN KEY`: Links two tables based on a relationship.
    - `CHECK`: Ensures that all values in a column satisfy a certain condition.

18. **What is the difference between `varchar` and `nvarchar`?**
    - `varchar` stores data in the default character set of the database, while `nvarchar` stores data in Unicode.
    - `nvarchar` can store a wider range of characters, including non-Latin scripts, but may require more storage space.

19. **Difference between `char` and `nchar`:**
    - `char` stores fixed-length character data, while `nchar` stores fixed-length Unicode character data.
    - `nchar` can store a wider range of characters, including non-Latin scripts, but may require more storage space.

20. **What are indexes and their types?**
    - Indexes are data structures that improve the speed of data retrieval operations on a table.
    - Types of indexes: `Clustered index`, `Non-clustered index`, `Composite index`, `Unique index`.

21. **What is an index? Explain its different types.**
    - An index is a data structure that improves the speed of data retrieval operations on a table.
    - Types of indexes:
      - Clustered index: Determines the physical order of data in the table.
      - Non-clustered index: Separate from the physical order of data in the table.
      - Composite index: Index on multiple columns.
      - Unique index: Ensures uniqueness of values in the indexed column(s).

22. **List the different types of relationships in SQL:**
    - One-to-One
    - One-to-Many
    - Many-to-Many

23. **Differentiate between `UNION` and `UNION ALL`:**
    - `UNION` combines the result sets of two or more `SELECT` statements and removes duplicate rows.
    - `UNION ALL` combines the result sets of two or more `SELECT` statements and retains all rows, including duplicates.

24. **How many types of clauses in SQL?**
    - The main clauses in SQL are:
      - `SELECT`
      - `FROM`
      - `WHERE`
      - `GROUP BY`
      - `HAVING`
      - `ORDER BY`

25. **What is the difference between `UNION` and `UNION ALL` in SQL?**
    - `UNION` removes duplicate rows from the combined result set.
    - `UNION ALL` retains all rows, including duplicates, from the combined result set.

26. **What are the various types of relationships in SQL?**
    - One-to-One
    - One-to-Many
    - Many-to-Many

27. **Difference between Primary Key and Secondary Key?**
    - Primary Key: Uniquely identifies each row in a table.
    - Secondary Key (or Index): Improves the speed of data retrieval operations, but does not uniquely identify rows.

28. **What is the difference between `WHERE` and `HAVING`?**
    - `WHERE` clause filters rows before grouping, `HAVING` clause filters groups after grouping.
    - `WHERE` is used with individual rows, `HAVING` is used with groups.

29. **Find the second highest salary of an employee?**
    ```sql
    SELECT MAX(Salary) AS SecondHighestSalary
    FROM Employees
    WHERE Salary < (SELECT MAX(Salary) FROM Employees);
    ```

30. **Write a retention query in SQL?**
    ```sql
    SELECT
        MONTH(registration_date) AS registration_month,
        YEAR(registration_date) AS registration_year,
        COUNT(*) AS new_registrations,
        COUNT(DISTINCT user_id) AS retained_users
    FROM user_activity
    WHERE registration_date >= DATE_SUB(CURRENT_DATE, INTERVAL 12 MONTH)
    GROUP BY registration_month, registration_year
    ORDER BY registration_year, registration_month;
    ```

31. **Write year-on-year growth in SQL?**
    ```sql
    SELECT
        YEAR(order_date) AS order_year,
        SUM(order_amount) AS total_orders,
        ROUND(
            (SUM(order_amount) - LAG(SUM(order_amount), 1) OVER (ORDER BY YEAR(order_date))) /
            LAG(SUM(order_amount), 1) OVER (ORDER BY YEAR(order_date)),
            2
        ) AS yoy_growth
    FROM orders
    GROUP BY order_year
    ORDER BY order_year;
    ```

32. **Write a query for cumulative sum in SQL?**
    ```sql
    SELECT
        order_date,
        order_amount,
        SUM(order_amount) OVER (ORDER BY order_date) AS cumulative_sum
    FROM orders;
    ```

33. **Difference between Function and Stored Procedure?**
    - Functions return a single value, stored procedures can return multiple result sets.
    - Functions are generally simpler and more focused, stored procedures can be more complex.
    - Functions can be used in queries, stored procedures are executed independently.

34. **Do we use variables in views?**
    - Yes, you can use variables in views. Variables in views can be used to make the view more dynamic and reusable.

35. **What are the limitations of views?**
    - Views are read-only by default, unless they are created with the `SCHEMABINDING` option.
    - Views cannot have `INSTEAD OF` triggers.
    - Views cannot have `ORDER BY` clauses, unless they are used in a nested query.
    - Views cannot contain certain types of statements, such as `COMPUTE` or `COMPUTE BY`.