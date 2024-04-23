#!/usr/bin/python3
"""
returns information about employees TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()
    completed_tasks = [t.get("title")
                       for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
         user.get("username"), len(completed_tasks), len(todos)))

    for complete in completed_tasks:
        print("\t {}".format(complete))
