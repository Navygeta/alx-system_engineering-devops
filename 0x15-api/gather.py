#!/usr/bin/python3
"""
Fetches and displays completed tasks for a given employee ID.

Usage:
    python script.py <employee_id>
"""

import requests
import sys


def get_employee_info(employee_id):
    """
    Get employee information based on the provided ID.

    Args:
        employee_id (int): The employee ID.

    Returns:
        dict: Dictionary with information about the employee.
    """
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    return user


def get_completed_tasks(employee_id):
    """
    Get completed tasks for a given employee ID.

    Args:
        employee_id (int): The employee ID.

    Returns:
        list: List of titles of completed tasks.
    """
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()
    completed_tasks = [t.get("title") for t in todos if t.get("completed") is True]
    return completed_tasks


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_info = get_employee_info(employee_id)
    completed_tasks = get_completed_tasks(employee_id)

    print("Employee {} is done with tasks({}/{}):".format(
        user_info.get("name"), len(completed_tasks), len(todos)))

    [print("\t {}".format(task)) for task in completed_tasks]
