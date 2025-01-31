# SQL Subquery Problems
### **1. Top Customer by Spending**

**Problem**: Identify the customer with the highest total spending.  
**Hint**: Use a subquery to calculate total spending for each customer and find the maximum.

----------

### **2. Orders Greater Than Average**

**Problem**: List all orders where the order amount is greater than the average order amount.  
**Hint**: Use a subquery to calculate the average order amount.

----------

### **3. Products Sold in Multiple Categories**

**Problem**: Find products that belong to multiple categories.  
**Hint**: Use a subquery to count the number of categories per product.

----------

### **4. Customers Without Orders**

**Problem**: List all customers who have not placed any orders.  
**Hint**: Use a subquery with `NOT IN` or `NOT EXISTS` to filter customers who don't have orders in the `orders` table.

----------

### **5. Orders with Maximum Payment**

**Problem**: Identify orders that received the maximum payment.  
**Hint**: Use a subquery to find the maximum payment amount and filter orders with this value.

----------

### **6. Second Highest Order Amount**

**Problem**: Find the second highest order amount.  
**Hint**: Use a subquery to exclude the highest order amount and find the maximum of the remaining values.

----------

### **7. Customers Who Purchased a Specific Product**

**Problem**: List all customers who purchased 'Product A'.  
**Hint**: Use a subquery to filter customer IDs based on orders for 'Product A'.

----------

### **8. Employees Who Made No Sales**

**Problem**: Identify employees who have not made any sales.  
**Hint**: Use a subquery with `NOT EXISTS` or `NOT IN` to find employees without matching orders.

----------

### **9. Most Popular Product**

**Problem**: Identify the most frequently purchased product.  
**Hint**: Use a subquery to calculate the count of orders per product and find the maximum count.

----------

### **10. Products That Cost More Than the Average Price**

**Problem**: List all products whose price is higher than the average price of all products.  
**Hint**: Use a subquery to calculate the average price of products.


---

### Example Structure
1. `customers` (`customer_id`, `customer_name`)
2. `orders` (`order_id`, `customer_id`, `order_date`, `order_amount`, `product_id`)
3. `products` (`product_id`, `product_name`, `category_id`, `price`)
4. `categories` (`category_id`, `category_name`)
5. `employees` (`employee_id`, `employee_name`)
6. `payments` (`payment_id`, `order_id`, `payment_amount`)