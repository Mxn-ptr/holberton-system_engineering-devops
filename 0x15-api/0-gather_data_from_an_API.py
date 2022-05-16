#!/usr/bin/python3
""" Script that use the REST API for a given employee ID
    Return information about his/her TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    UserId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(UserId))
    name = user.json().get("name")

    total_task = 0
    task_completed = []
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    for task in tasks.json():
        if task.get("userId") == int(UserId):
            total_task += 1
            if task.get("completed"):
                task_completed.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(task_completed), total_task))
    for task in task_completed:
        print("\t {}".format(task.get("title")))
