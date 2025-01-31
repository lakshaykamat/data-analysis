import pandas as pd
import numpy as np
from faker import Faker

faker = Faker()

# Generating 'customers' table
customers = pd.DataFrame({
    'customer_id': range(1, 51),
    'customer_name': [faker.name() for _ in range(50)],
    'state': [faker.state() for _ in range(50)]
})

# Generating 'orders' table
order_ids = range(1, 101)
orders = pd.DataFrame({
    'order_id': order_ids,
    'customer_id': np.random.choice(customers['customer_id'], size=100, replace=True),
    'order_date': [faker.date_between(start_date='-2y', end_date='today') for _ in range(100)],
    'order_amount': np.random.randint(50, 1000, size=100),
    'product_id': np.random.randint(1, 21, size=100),
    'employee_id': np.random.randint(1, 11, size=100)
})

# Generating 'payments' table
payments = pd.DataFrame({
    'payment_id': range(1, 81),
    'order_id': np.random.choice(orders['order_id'], size=80, replace=False),
    'payment_date': [faker.date_between(start_date='-2y', end_date='today') for _ in range(80)],
    'payment_amount': [np.random.randint(50, 1000) for _ in range(80)]
})

# Generating 'products' table
products = pd.DataFrame({
    'product_id': range(1, 21),
    'product_name': [faker.word().capitalize() for _ in range(20)],
    'category_id': np.random.randint(1, 6, size=20),
    'price': np.random.randint(20, 200, size=20)
})

# Generating 'categories' table
categories = pd.DataFrame({
    'category_id': range(1, 6),
    'category_name': [faker.word().capitalize() for _ in range(5)]
})

# Generating 'employees' table
employees = pd.DataFrame({
    'employee_id': range(1, 11),
    'employee_name': [faker.name() for _ in range(10)]
})

# Generating 'regions' table
regions = pd.DataFrame({
    'region_id': range(1, 6),
    'region_name': [faker.city() for _ in range(5)]
})

# Generating 'refunds' table
refunds = pd.DataFrame({
    'refund_id': range(1, 21),
    'order_id': np.random.choice(orders['order_id'], size=20, replace=False),
    'refund_amount': [np.random.randint(20, 200) for _ in range(20)]
})

# Saving tables to CSV for SQL import
customers.to_csv('customers.csv', index=False)
orders.to_csv('orders.csv', index=False)
payments.to_csv('payments.csv', index=False)
products.to_csv('products.csv', index=False)
categories.to_csv('categories.csv', index=False)
employees.to_csv('employees.csv', index=False)
regions.to_csv('regions.csv', index=False)
refunds.to_csv('refunds.csv', index=False)
