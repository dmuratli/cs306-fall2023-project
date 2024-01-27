from connect import connectDB
from pymongo import errors
from bson.objectid import ObjectId
import textwrap

def input_to_dict(input_data, user_id): # New
    lines = input_data.strip().split(",")
    
    output_dict = {"user_id": user_id}

    for line in lines:
        line = line.strip().split(":")
        field = line[0]
        value = line[1]

        if value.isdigit() == True:
            value = int(value)
        else:
            pass

        if field not in output_dict:
            output_dict[field] = value
        else:
            pass
    
    return output_dict

def createCollection(db, collection_name): # Untouched
    try:
        # If the collection doesn't exist, create it
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Collection '{collection_name}' created.")
        elif collection_name in db.list_collection_names():
            print("Collection already exists")
    except Exception as e:
        print("An error occured: ", e)

def insert_into_collection(db, collection_name, input_data, user_id): # Modified
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Insert the input into the collection
        data = input_to_dict(input_data, user_id)

        result = collection.insert_one(data)

        # Print the inserted document ID
        print("Insertion successfully completed")
        print(f"Inserted document ID: {result.inserted_id}")

    except Exception as e:
        print(f"An error occurred: {e}")

def read_all_data(db, collection_name): # Untouched
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Use the find method to retrieve all documents
        result = collection.find()

        # Iterate through the documents and print them
        for document in result:
            print(document)

    except Exception as e:
        print(f"An error occurred: {e}")

def find_documents_containing_value(db, collection_name, field, value): # Modified
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Define the query to find orders containing the specified item
        query = {field: value}

        # Use the find method to retrieve matching documents
        cursor = collection.find(query)

        # Convert your cursor to a list to freely operate over it
        result = list(cursor)

        # Print the matching documents
        for document in result:
            print(document)

        # Return the whole result list
        return result

    except Exception as e:
        print(f"An error occurred: {e}")

def delete_record_by_id(db, collection_name, record_id): # Untouched
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Define the query to find the document by its ID
        query = {"_id": ObjectId(record_id)}

        # Use the delete_one method to delete the document
        result = collection.delete_one(query)

        # Check if the deletion was successful
        if result.deleted_count == 1:
            print(f"Successfully deleted record with ID {record_id}")
        else:
            print(f"No record found with ID {record_id}")

    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

def update_record_by_id(db, collection_name, record_id, field, value): # Modified
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Define the query to find the document by its ID
        query = {"_id": ObjectId(record_id)}

        # Use the update_one method to update the specific field
        result = collection.update_one(query, {"$set": {field: value}})

        # Check if the update was successful
        if result.matched_count == 1:
            print(f"Successfully updated {field} for record with ID {record_id}")
        else:
            print(f"No record found with ID {record_id}")

    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

def delete_record_by_user_id(db, collection_name, user_id): # Modified
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Define the query to find the document by its ID
        query = {"user_id": user_id}

        # Use the delete_one method to delete the document
        result = collection.delete_many(query)

        # Check if the deletion was successful
        if result.deleted_count >= 1:
            print(
                f"Successfully deleted {result.deleted_count} record that contains {user_id}"
            )
        else:
            print(f"No record found with {user_id}")

    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

def option_handler(db, option, user_id):
    if option == 1:
        collection_name = input("Enter the name of the collection you want to create: ")

        createCollection(db, collection_name)
    elif option == 2:
        collection_name = input("Enter the name of the collection you want to read all the input of: ")

        read_all_data(db, collection_name)
    elif option == 3:
        collection_name = input("Enter the name of the collection you want to search the value in: ")
        field = input("Enter the name of the field to be checked: ")
        value = input("Enter the value you want to search for: ")

        if value.isdigit():
            value = int(value)
        else:
            pass

        find_documents_containing_value(db, collection_name, field, value)
    elif option == 4:
        collection_name = input("Enter the name of the collection you want to insert input to: ")
        
        input_data = input("Enter the input you want to insert (in the format \"field:value\", where the field-value pairs are separated by commas):\n")
        
        insert_into_collection(db, collection_name, input_data, user_id)
    elif option == 5:
        collection_name = input("Enter the name of the collection you want to delete input from: ")
        
        prompt_text = textwrap.dedent("""\
        Do you want to delete by record ID or user ID?
        1) Record ID
        2) User ID
        Selected option: """)
        
        next_option = int(input(prompt_text))
        
        if next_option == 1:
            record_id = input("Enter the ID of the record you want to delete: ")

            delete_record_by_id(db, collection_name, record_id)
        elif next_option == 2:
            user_id = int(input("Enter the ID of the user whose entries you want to delete: "))

            delete_record_by_user_id(db, collection_name, user_id)
        else:
            print("Incorrect option!")
    elif option == 6:
        collection_name = input("Enter the name of the collection that contains the record you want to update: ")
        record_id = input("Enter the ID of the record you want to update: ")
        field = input("Enter the name of the field to be updated: ")
        value = input("Enter the value you want to replace the old value with: ")

        update_record_by_id(db, collection_name, record_id, field, value)
    else:
        print("Incorrect input!")

if __name__ == "__main__":
    db = connectDB()

    print("Welcome to Leftist Music Portal!")

    user_id = int(input("Please enter your user ID: \n"))

    prompt_text = textwrap.dedent("""\
    Please pick the option you want to proceed with:
    1) Create a collection
    2) Read all input in a collection
    3) Read some part of the input while filtering
    4) Insert input
    5) Delete input
    6) Update input

    Selected option: """)

    option = int(input(prompt_text))

    option_handler(db, option, user_id)

    while True:
        prompt_text = textwrap.dedent("""\
        What would you like to do next?
        1) Create a collection
        2) Read all input in a collection
        3) Read some part of the input while filtering
        4) Insert input
        5) Delete input
        6) Update input

        Selected option: """)

        option = int(input(prompt_text))
        
        option_handler(db, option, user_id)