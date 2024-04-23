#!/usr/bin/python3
"""
returns information about employees TODO list progress
"""
import requests
import sys
import csv


import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]

    # Fetch user data
    user_response = requests.get(url + "users/{}".format(user_id))
    if user_response.status_code != 200:
        print("Failed to fetch user data")
        sys.exit(1)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch todos for the user
    todos_response = requests.get(url + "todos", params={"userId": user_id})
    if todos_response.status_code != 200:
        print("Failed to fetch TODO list")
        sys.exit(1)
    todos = todos_response.json()

    # Write data to CSV
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for t in todos:
            writer.writerow([user_id, username, t.get("completed"), t.get("title")])

    print("Tasks exported to {}.csv".format(user_id))

