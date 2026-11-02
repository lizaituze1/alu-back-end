#!/usr/bin/python3
"""Exports an employee's TODO list data to a CSV file."""
import csv
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
    file_name = "{}.csv".format(employee_id)

    with open(file_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")])
