#!/usr/bin/python3
"""
Module: gather_data_from_an_API

This module defines functions for gathering and displaying information about
an employee's TODO list progress using a REST API.

Functions:
    make_request(url: str) -> dict:
        Make an HTTP GET request to the given URL and return the JSON response.

        Args:
            url (str): The URL to make the request to.

        Returns:
            dict: JSON response from the HTTP GET request.

        Raises:
            requests.exceptions.RequestException: If an error occurs during
            the request.

    export_to_json(data, file_name) -> None:
        Export the data to a JSON file.

        Args:
            data: Data to be exported (dictionary).
            file_name (str): Name of the output JSON file.

        Writes:
            Creates a JSON file with the specified data and file name.

    get_all_employees_todo_progress() -> None:
        Fetch and display information about TODO list progress for all employees.

        Displays:
            Employee EMPLOYEE_NAME is done with tasks
            (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
                EMPLOYEE_NAME: name of the employee
                NUMBER_OF_DONE_TASKS: number of completed tasks
                TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum
                of completed and non-completed tasks
            Second and N next lines display the title of completed tasks:
                TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

Main Execution:
    If the module is executed directly, it calls get_all_employees_todo_progress
    function to fetch and display TODO list progress for all employees.
"""

import requests
import json
import sys


def make_request(url):
    """
    Make an HTTP GET request to the given URL and return the JSON response.

    Args:
        url (str): The URL to make the request to.

    Returns:
        dict: JSON response from the HTTP GET request.

    Raises:
        requests.exceptions.RequestException: If an error occurs during
        the request.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        sys.exit(1)


def export_to_json(data, file_name):
    """
    Export the data to a JSON file.

    Args:
        data: Data to be exported (dictionary).
        file_name (str): Name of the output JSON file.

    Writes:
        Creates a JSON file with the specified data and file name.
    """
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=2)
    print(f"Data exported to {file_name}")


def get_all_employees_todo_progress():
    """
    Fetch and display information about TODO list progress for all employees.

    Displays:
        Employee EMPLOYEE_NAME is done with tasks
        (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            EMPLOYEE_NAME: name of the employee
            NUMBER_OF_DONE_TASKS: number of completed tasks
            TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of
            completed and non-completed tasks
        Second and N next lines display the title of completed tasks:
            TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    users_data = make_request(base_url)

    all_employees_data = {}

    for user in users_data:
        user_id = user['id']
        user_name = user['name']
        user_todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        user_todos_data = make_request(user_todos_url)

        completed_tasks = [task for task in user_todos_data if task['completed']]
        number_of_done_tasks, total_number_of_tasks = len(completed_tasks), len(user_todos_data)

        # Display information in the specified format
        print(f"Employee {user_name} is done with tasks "
              f"({number_of_done_tasks}/{total_number_of_tasks}):")
        print(f"\t{user_name}: {number_of_done_tasks}/{total_number_of_tasks}")

        tasks_data = [{"username": user_name, "task": task['title'], "completed": task['completed']} for task in completed_tasks]

        # Add tasks data to the dictionary
        all_employees_data[user_id] = tasks_data

        for task_title in completed_tasks:
            print(f"\t\t{task_title['title']}")

    # Export data to JSON file
    export_to_json(all_employees_data, "todo_all_employees.json")


if __name__ == "__main__":
    get_all_employees_todo_progress()
