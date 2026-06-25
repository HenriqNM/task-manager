from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from engine import TaskManager

app = FastAPI()
manager = TaskManager()

class TaskInput(BaseModel):
    title: str
    notes: str

@app.post("/lists/{list_name}")
def create_list(list_name: str) -> dict:
    manager.create_list_task(list_name)
    return {"message": f"List '{list_name}' created successfully."}

@app.get("/lists/{list_name}/tasks")
def get_tasks(list_name: str) -> dict:
    tasks = manager.get_tasks(list_name)
    if tasks is None:
        raise HTTPException(status_code=404, detail="List not found")
    return {"tasks": tasks}

@app.post("/lists/{list_name}/tasks")
def add_task(list_name: str, task_data: TaskInput) -> dict:
    success = manager.add_task(list_name, task_data.title, task_data.notes)
    if not success:
        raise HTTPException(status_code=404, detail="List not found")
    return {"message": "Task added successfully"}

@app.patch("/lists/{list_name}/tasks/{task_id}")
def complete_task(list_name: str, task_id: int) -> dict:
    success = manager.complete_task(list_name, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="List or Task ID not found")
    return {"message": f"Task {task_id} marked as completed"}

@app.delete("/lists/{list_name}/tasks/{task_id}")
def delete_task(list_name: str, task_id: int) -> dict:
    success = manager.delete_task(list_name, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="List or Task ID not found")
    return {"message": f"Task {task_id} deleted."}

@app.delete("/lists/{list_name}")
def delete_list(list_name: str) -> dict:
    success = manager.delete_task(list_name)
    if not success:
        raise HTTPException(status_code=404, detail="List not found")
    return {"message": f"List '{list_name}' deleted."}