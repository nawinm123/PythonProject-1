import db_connection
import requests


from db_connection import fetch_records_from_db

records = fetch_records_from_db()

if records:
    print("Fetched Records:")
    for record in records:
        print(record)
else:
    print("No records fetched or an error occurred.")



BASE_URL = "http://127.0.0.1:5000/employees"

"""Fetch all employee records."""
response = requests.get(BASE_URL)
if response.status_code == 200:
    print("Employees List:")
    print(response.json())
else:
    print("Failed to fetch employees:", response.status_code, response.text)

