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

fake_copy = Faker()

# Number of records to generate
num_records = 1000000

# Generate and insert data to Albums
last_albid = 10
last_lid = 9
last_artid = 10

max_lid = 1000009
max_artid = 1000010

for _ in range(num_records):
    atitle = fake.word()
    rel_year = random.randint(1800, 2023)
    lid = last_lid + 1
    artid = last_artid + 1
    albid = last_albid + 1

    last_albid = albid
    last_lid = lid
    last_artid = artid

    if last_lid > max_lid:
        last_lid = 1
    else:
        pass

    if last_artid > max_artid: # It should never come to this tbh
        last_artid = 1
    else:
        pass

    cursor.execute(
        """
        INSERT INTO Albums (albid, atitle, rel_year, lid, artid)
        VALUES (%s, %s, %s, %s, %s)
    """,
        (albid, atitle, rel_year, lid, artid),
    )

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
