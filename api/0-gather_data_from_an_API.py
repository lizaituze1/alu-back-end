#!/usr/bin/python3
"""Returns info about an employee's TODO list progress."""
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

    done = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))
