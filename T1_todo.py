import requests

def fetch_todos():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    
    if response.status_code == 200:
        todos = response.json()
        for i, todo in enumerate(todos[:10], start=1):
            print(f"{i}. ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    fetch_todos()
