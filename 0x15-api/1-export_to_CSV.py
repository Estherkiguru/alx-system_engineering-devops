#!/usr/bin/python3

"""Exports to-do list information for a given employee ID to CSV format."""


import csv
import requests
import sys

def get_user_tasks(user_id):
    # Make API request to fetch tasks for the specified user
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')

    # Check if request was successful
    if response.status_code == 200:
        tasks = response.json()
        return tasks
    else:
        print("Failed to fetch tasks")
        return None

def export_to_csv(user_id, tasks):
    if tasks:
        # Define CSV file name
        filename = f"{user_id}.csv"

        # Write data to CSV file
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for task in tasks:
                writer.writerow({
                    'USER_ID': user_id,
                    'USERNAME': task['username'],  # Assuming username is available
                    'TASK_COMPLETED_STATUS': str(task['completed']),
                    'TASK_TITLE': task['title']
                })
        print(f"Tasks exported to {filename}")
    else:
        print("No tasks found for the specified user")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]
    tasks = get_user_tasks(user_id)
    export_to_csv(user_id, tasks)

