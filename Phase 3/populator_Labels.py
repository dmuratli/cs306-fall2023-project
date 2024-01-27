# Taken from Recit 8; tailored to my DB

import mysql.connector
from faker import Faker
import random
from connect import create_connection

# Connect to your MySQL server
connection = create_connection()

# Create a cursor object
cursor = connection.cursor()

# Create a Faker instance
fake = Faker()

# Number of records to generate
num_records = 1000000

# Generate and insert data to Labels
last_lid = 9

for _ in range(num_records):
    lname = fake.company()
    website = fake.url()
    lcountry = fake.country()
    est_year = random.randint(1800, 2023)
    lid = last_lid + 1

    last_lid = lid

    cursor.execute(
        """
        INSERT INTO Labels (lid, lname, website, lcountry, est_year)
        VALUES (%s, %s, %s, %s, %s)
    """,
        (lid, lname, website, lcountry, est_year),
    )

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
