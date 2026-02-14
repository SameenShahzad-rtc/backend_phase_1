from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app=FastAPI()




class Task(BaseModel):
    id:int
    task_name:str
    status:str

#welcome msg
@app.get('/')

def wel_msg():
    return {"Welcome to Mini PRoject"}

#return list of tasks
@app.get("/tasks",response_model=List[Task])
def li_task(t:Task):
    return t

#get single task
@app.get("/tasks/{task_id}")
def Single_t(task_id:int,task:Task):
    for t in task:
        if t["id"]==task_id:
            return t
    return {"message": "Task id is not found"}
#delete
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int,t:Task):
    for index, task in enumerate(t):
        if task["id"] == task_id:
            t.pop(index)
            return {"message": "Task deleted"}
    return {"message": "Task id is not found"}

#Add a task



@app.post("/tasks", response_model=Task)
def add_task(task: Task):

    new_task = {
        "id": task.id,
        "task_name": task.task_name,
        "status": task.status
    }

    task.append(new_task)
    return new_task