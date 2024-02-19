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

    get_employee_todo_progress(employee_id: int) -> None:
        Fetch and display information about the employee's TODO list progress.

        Args:
            employee_id (int): The ID of the employee.

        Displays:
            Employee EMPLOYEE_NAME is done with tasks
            (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
                EMPLOYEE_NAME: name of the employee
                NUMBER_OF_DONE_TASKS: number of completed tasks
                TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the
                sum of completed and non-completed tasks
            Second and N next lines display the title of completed tasks:
                TASK_TITLE (with 1 tabulation & 1 space before the
                TASK_TITLE)

        Exports:
            CSV file named USER_ID.csv with format "USER_ID","USERNAME",
            "TASK_COMPLETED_STATUS","TASK_TITLE"
"""

import requests
import csv
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


def get_employee_todo_progress(employee_id):
    """
    Fetch and display information about the employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Displays:
        Employee EMPLOYEE_NAME is done with tasks
        (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            EMPLOYEE_NAME: name of the employee
            NUMBER_OF_DONE_TASKS: number of completed tasks
            TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the
            sum of completed and non-completed tasks
        Second and N next lines display the title of completed tasks:
            TASK_TITLE (with 1 tabulation and 1 space before the
            TASK_TITLE)

    Exports:
        CSV file named USER_ID.csv with format "USER_ID","USERNAME",
        "TASK_COMPLETED_STATUS","TASK_TITLE"
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{user_url}/todos"

    # Fetch user information and TODO list for the user
    user_data = make_request(user_url)
    todos_data = make_request(todos_url)

    # Extract relevant information
    employee_name = user_data.get('name', 'Unknown Employee')
    user_id = user_data.get('id', 'Unknown ID')

    # Display information in the specified format

    print(f"Employee {employee_name} is done with tasks "
          f"({len([task for task in todos_data if task['completed']])}/"
          f"{len(todos_data)}):")

    print(f"Employee {employee_name} is done with tasks "
          f"({len([task for task in todos_data if task['completed']])}/"
          f"{len(todos_data)}):")

    completed_tasks = [task['title'] for task in todos_data
                       if task['completed']]

    [print(f"\t\t{task_title}") for task_title in completed_tasks]

    # Export to CSV
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            csv_writer.writerow([user_id, employee_name,
                                 str(task['completed']), task['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
