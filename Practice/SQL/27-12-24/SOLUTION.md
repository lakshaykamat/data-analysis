## **Basic Queries**

### **1. Retrieve all users who have a Premium subscription.**

```sql
SELECT *
FROM demo_data.users
WHERE Subscription_Type = "Premium";

```

**Explanation:**

- This query retrieves all columns (``) from the `users` table where the `Subscription_Type` is "Premium".
- It assumes that the `users` table contains a column `Subscription_Type` that stores the subscription status of each user.

---

### **2. Find all users who signed up in the last two years.**

```sql
SELECT *
FROM demo_data.users
WHERE Signup_Date >= CURRENT_DATE - INTERVAL 2 YEAR;
```

**Explanation:**

- This query returns all users who signed up within the last two years.
- `CURRENT_DATE - INTERVAL 2 YEAR` calculates the date exactly two years ago, and the query filters users whose `Signup_Date` is greater than or equal to that date.

---

### **3. Get the top 5 countries by the number of users.**

```sql
SELECT Country, COUNT(*) AS user_count
FROM demo_data.users
GROUP BY Country
ORDER BY user_count DESC
LIMIT 5;

```

**Explanation:**

- This query calculates the number of users (`COUNT(*)`) for each `Country` and orders the countries in descending order by `user_count`.
- `LIMIT 5` restricts the results to the top 5 countries with the most users.

---

## **Aggregate Functions**

### **1. Calculate the average age of users for each subscription type.**

```sql
SELECT ROUND(AVG(age))
FROM users
WHERE Subscription_Type = "Premium";

```

```sql
SELECT ROUND(AVG(age))
FROM users
WHERE Subscription_Type = "Basic";

```

```sql
SELECT ROUND(AVG(age))
FROM users
WHERE Subscription_Type = "Free";

```

**Explanation:**

- These queries calculate the average age of users for each subscription type: "Premium", "Basic", and "Free".
- The `ROUND()` function is used to round the average age to the nearest integer.
- Replace `age` with the correct column representing users' ages if it's different in your database.

---

### **2. Find the total Lifetime Value of users from the United Kingdom.**

```sql
SELECT ROUND(SUM(Lifetime_Value))
FROM users
WHERE Country = "United Kingdom";

```

**Explanation:**

- This query sums the `Lifetime_Value` of all users from the United Kingdom (`Country = "United Kingdom"`) and returns the total.
- `ROUND()` ensures the result is a whole number, removing any decimal places.

---

## **Filtering and Sorting**

### **1. List the top 10 users with the highest Lifetime Value.**

```sql
SELECT *
FROM users
ORDER BY Lifetime_Value DESC
LIMIT 10;

```

**Explanation:**

- This query sorts all users by `Lifetime_Value` in descending order, ensuring the users with the highest Lifetime Value are listed first.
- `LIMIT 10` restricts the result to the top 10 users.

---

### **2. Identify users who made zero purchases but have a Basic or Premium subscription.**

```sql
SELECT *
FROM users
WHERE Total_Purchases = 0
AND Subscription_Type IN ("Basic", "Premium");

```

**Explanation:**

- This query filters users who have made zero purchases (`Total_Purchases = 0`) and have either a "Basic" or "Premium" subscription (`Subscription_Type IN ("Basic", "Premium")`).

---

## **Date Operations**

### **1. Find users whose last login was more than 6 months ago.**

```sql
SELECT *
FROM users
WHERE Last_Login <= CURRENT_DATE - INTERVAL 6 MONTH;

```

**Explanation:**

- This query identifies users whose `Last_Login` was more than 6 months ago by comparing it to the date 6 months before today (`CURRENT_DATE - INTERVAL 6 MONTH`).

---

### **2. Calculate the number of days between signup and last login for each user.**

```sql
SELECT Name, DATEDIFF(Last_Login, Signup_Date) AS date_between
FROM users;

```

**Explanation:**

- This query calculates the number of days between each user's `Signup_Date` and their `Last_Login` using the `DATEDIFF()` function.
- The result is aliased as `date_between`.

---

## **Advanced Analysis**

### **1. Group users by subscription type and find the total purchases for each group.**

```sql
SELECT Subscription_Type, COUNT(Total_Purchases)
FROM demo_data.users
GROUP BY Subscription_Type;

```

**Explanation:**

- This query groups users by `Subscription_Type` and counts the total number of purchases (`COUNT(Total_Purchases)`) for each subscription type.
- This helps to understand the purchase behavior across different subscription categories.

---

### **2. Find the youngest and oldest users in each subscription category.**

```sql
SELECT Subscription_Type,
       MIN(Signup_date) AS oldest,
       MAX(Signup_date) AS youngest
FROM users
GROUP BY Subscription_Type;

```

**Explanation:**

- This query groups users by `Subscription_Type` and finds the **oldest** (earliest `Signup_date`) and **youngest** (latest `Signup_date`) users in each subscription category.
- The `MIN()` function returns the oldest user, while `MAX()` returns the youngest.

---

### **3. Determine the retention rate by comparing the number of users who logged in within the last 30 days to the total users.**

```sql
SELECT
    (COUNT(DISTINCT CASE WHEN Last_Login >= CURRENT_DATE - INTERVAL 30 DAY THEN User_ID END) /
    COUNT(DISTINCT User_ID)) * 100 AS retention_rate
FROM users;

```

**Explanation:**

- This query calculates the retention rate by first counting the number of distinct users (`User_ID`) who have logged in within the last 30 days (`Last_Login >= CURRENT_DATE - INTERVAL 30 DAY`).
- It then divides this number by the total number of distinct users (`COUNT(DISTINCT User_ID)`) and multiplies by 100 to get the retention rate as a percentage.