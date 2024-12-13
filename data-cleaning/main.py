import pandas as pd
import random
from faker import Faker

# Initialize Faker for generating fake data
fake = Faker()

# Generate a sample dataset
data = {
    "customer_id": [i for i in range(1, 21)],
    "name": [fake.name() for _ in range(20)],
    "age": [random.choice([random.randint(18, 70), None]) for _ in range(20)],
    "email": [fake.email() if random.random() > 0.1 else None for _ in range(20)],
    "purchase_date": [fake.date_this_year() if random.random() > 0.2 else None for _ in range(20)],
    "purchase_amount": [round(random.uniform(10.5, 500.5), 2) if random.random() > 0.15 else None for _ in range(20)],
    "region": [random.choice(["North", "South", "East", "West", None]) for _ in range(20)],
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
file_path = "sample_dataset.csv"
df.to_csv(file_path, index=False)

