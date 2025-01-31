### 1. Create Tables with Primary Keys
```sql
-- Create Customers Table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name NVARCHAR(255) NOT NULL,
    state NVARCHAR(100)
);

-- Create Orders Table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    order_amount DECIMAL(10, 2),
    product_id INT,
    employee_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Create Payments Table
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    payment_date DATE,
    payment_amount DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

-- Create Products Table
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name NVARCHAR(255),
    category_id INT,
    price DECIMAL(10, 2)
);

-- Create Categories Table
CREATE TABLE Categories (
    category_id INT PRIMARY KEY,
    category_name NVARCHAR(255)
);

-- Create Employees Table
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_name NVARCHAR(255)
);

-- Create Regions Table
CREATE TABLE Regions (
    region_id INT PRIMARY KEY,
    region_name NVARCHAR(255)
);

-- Create Refunds Table
CREATE TABLE Refunds (
    refund_id INT PRIMARY KEY,
    order_id INT,
    refund_amount DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);
```

### 2. Add Foreign Key Relationships
Below are the foreign key constraints to establish relationships between the tables.
```sql
-- Add Foreign Key Between Orders and Customers
ALTER TABLE Orders
ADD CONSTRAINT FK_Orders_Customers
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id);

-- Add Foreign Key Between Orders and Products
ALTER TABLE Orders
ADD CONSTRAINT FK_Orders_Products
FOREIGN KEY (product_id) REFERENCES Products(product_id);

-- Add Foreign Key Between Orders and Employees
ALTER TABLE Orders
ADD CONSTRAINT FK_Orders_Employees
FOREIGN KEY (employee_id) REFERENCES Employees(employee_id);

-- Add Foreign Key Between Payments and Orders
ALTER TABLE Payments
ADD CONSTRAINT FK_Payments_Orders
FOREIGN KEY (order_id) REFERENCES Orders(order_id);

-- Add Foreign Key Between Products and Categories
ALTER TABLE Products
ADD CONSTRAINT FK_Products_Categories
FOREIGN KEY (category_id) REFERENCES Categories(category_id);

-- Add Foreign Key Between Refunds and Orders
ALTER TABLE Refunds
ADD CONSTRAINT FK_Refunds_Orders
FOREIGN KEY (order_id) REFERENCES Orders(order_id);
```