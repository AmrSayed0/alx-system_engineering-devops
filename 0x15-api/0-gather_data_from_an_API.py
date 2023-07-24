#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch user data
        response_user = requests.get(user_url)
        response_user.raise_for_status()
        user_data = response_user.json()
        employee_name = user_data['name']

        # Fetch TODO list data
        response_todos = requests.get(todos_url)
        response_todos.raise_for_status()
        todos_data = response_todos.json()

        # Calculate the progress
        total_tasks = len(todos_data)
        done_tasks = sum(1 for todo in todos_data if todo['completed'])

        # Display progress
        print(f'Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):')
        for todo in todos_data:
            if todo['completed']:
                print(f'\t{todo["title"]}')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)