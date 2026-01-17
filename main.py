from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

tasks = []
task_id_counter = 1

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskStatusUpdate(BaseModel):
    status: str

@app.get("/")
def root():
    return {"message": "Task Management API is running"}

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    global task_id_counter
    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "description": task.description,
        "status": "pending",
        "created_at": datetime.now().isoformat()
    }
    tasks.append(new_task)
    task_id_counter += 1
    return new_task

@app.get("/tasks")
def get_tasks(status: Optional[str] = None):
    if status:
        return [task for task in tasks if task["status"] == status]
    return tasks

@app.put("/tasks/{task_id}")
def update_task(task_id: int, update: TaskStatusUpdate):
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "completed":
                raise HTTPException(status_code=400, detail="Completed task cannot be updated")
            if update.status not in ["pending", "completed"]:
                raise HTTPException(status_code=400, detail="Invalid status")
            task["status"] = update.status
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return
    raise HTTPException(status_code=404, detail="Task not found")
