#!/usr/bin/python3
"""
returns information about employees TODO list progress
"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]
    
    user = requests.get(url + "users/{}".format(user_id)).json()
    
    username = user.get("username")

    params = {"userId": user_id}

    todos = requests.get(url + "todos", params).json()
    
    export_data = {user_id:[]}
    
    for t in todos:
        task_stats = {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
                }
        export_data[user_id].append(task_stats)

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(export_data, jsonfile, indent=4)
