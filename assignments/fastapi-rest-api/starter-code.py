from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)


class TaskUpdate(BaseModel):
    completed: bool


class Task(TaskCreate):
    id: int
    completed: bool = False


tasks: list[Task] = []
next_task_id = 1


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    return tasks


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate) -> Task:
    # TODO: Assign an ID, store the task, and return it.
    raise NotImplementedError


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    # TODO: Find the task or raise HTTPException with status code 404.
    raise NotImplementedError


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate) -> Task:
    # TODO: Find the task, update its completion status, and return it.
    raise NotImplementedError


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    # TODO: Find and remove the task or raise HTTPException with status code 404.
    return Response(status_code=status.HTTP_204_NO_CONTENT)