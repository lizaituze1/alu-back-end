#!/usr/bin/python3
"""Exports the TODO list data of all employees to a JSON file."""
import json
import urllib.request

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_response = urllib.request.urlopen("{}/users".format(base_url))
    users = json.loads(users_response.read().decode("utf-8"))

    todos_response = urllib.request.urlopen("{}/todos".format(base_url))
    todos = json.loads(todos_response.read().decode("utf-8"))

    all_employees = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        all_employees[str(user_id)] = [
            {"username": username,
             "task": task.get("title"),
             "completed": task.get("completed")}
            for task in todos if task.get("userId") == user_id]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees, json_file)
