# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing tasks with FastAPI. Practice defining request and response models, creating HTTP endpoints, validating input, and returning appropriate status codes.

## 📝 Tasks

### 🛠️ Create and List Tasks

#### Description
Complete the starter code to create a FastAPI application that stores tasks in memory. A task has an integer ID, a title, and a completion status. Implement endpoints to list all tasks and create a task.

Run the application with `uvicorn starter-code:app --reload`, then open `http://127.0.0.1:8000/docs` to try the endpoints. Install the required packages first with `pip install fastapi uvicorn`.

#### Requirements
Completed program should:

- Define Pydantic models for task input and task responses
- Implement `GET /tasks` to return all tasks and `POST /tasks` to create a task
- Assign each new task a unique ID and return the created task with status code `201`
- Reject an empty task title through request validation


### 🛠️ Read, Update, and Delete Tasks

#### Description
Add endpoints to retrieve one task by its ID, change its completion status, and delete it. Use the interactive API documentation at `/docs` or an HTTP client to test the endpoints.

#### Requirements
Completed program should:

- Implement `GET /tasks/{task_id}` to return one task
- Implement `PATCH /tasks/{task_id}` to update a task's completion status
- Implement `DELETE /tasks/{task_id}` to delete a task and return status code `204`
- Return status code `404` when a requested task ID does not exist
- Keep task data in memory and explain that it resets when the server restarts