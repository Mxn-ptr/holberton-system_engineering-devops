#!/usr/bin/python3
""" Export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = tasks.json()
    t = {}

    for user in users:
        list_task = []
        for task in tasks:
            if task.get("userId") == user.get("id"):
                dict_task = {"username": user.get("username"),
                             "task": task.get("title"),
                             "completed": task.get("completed")}
                list_task.append(dict_task)
        t[user.get("id")] = list_task

    with open("todo_all_employees.json", 'w') as f:
        json.dump(t, f)
