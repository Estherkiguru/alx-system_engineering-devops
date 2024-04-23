#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    # Extract the employee ID from command line argument
    userId = sys.argv[1]
    
    # Fetch user data using the provided user ID
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    # Extract the name of the user
    name = user.json().get('name')

    # Fetch all tasks
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    # Initialize variables to count total tasks and completed tasks
    totalTasks = 0
    completed = 0

    # Iterate through all tasks
    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    # Print the employee's progress summary
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    # Print the titles of completed tasks with proper indentation
    completed_tasks = [task.get('title') for task in todos.json()
                       if task.get('userId') == int(userId) and task.get('completed')]
    
    # Print each completed task with proper indentation
    for task in completed_tasks:
        print('\t', task)

