#!/usr/bin/python3
"""Exports an employee's TODO list data to a JSON file."""
import json
import sys
import urllib.request

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = urllib.request.urlopen(user_url)
    user = json.loads(user_response.read().decode("utf-8"))

    todos_url = "{}/users/{}/todos".format(base_url, employee_id)
    todos_response = urllib.request.urlopen(todos_url)
    todos = json.loads(todos_response.read().decode("utf-8"))

    username = user.get("username")
    file_name = "{}.json".format(employee_id)

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username})

    with open(file_name, "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)
