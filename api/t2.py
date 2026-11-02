#!/usr/bin/python3
"""Returns info about an employee's TODO list progress."""
import json
import sys
import urllib.request

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = urllib.request.urlopen(url)
    user = json.loads(response.read().decode("utf-8"))
    print(user.get("name")
