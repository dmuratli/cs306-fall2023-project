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

# Generate and insert data to Artists
last_artid = 10

for _ in range(num_records):
    atype = fake.random_element(elements = ["Band", "Person"])
    aname = fake.name()
    acountry = fake.country()
    deb_year = random.randint(1800, 2023)
    artid = last_artid + 1

    last_artid = artid

    cursor.execute(
        """
        INSERT INTO Artists (artid, atype, aname, acountry, deb_year)
        VALUES (%s, %s, %s, %s, %s)
    """,
        (artid, atype, aname, acountry, deb_year),
    )

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
