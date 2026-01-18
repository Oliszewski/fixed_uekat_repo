from fastapi import FastAPI, BackgroundTasks
import requests
import os
from logic import count_people

app = FastAPI()

tasks = {}
task_id = 0 

def process_task(id, file_path):

    tasks[id] = "Processing"

    amount_of_people = count_people(file_path)

    if amount_of_people is not None:
        tasks[id] = f"Success: There are {amount_of_people} people on the image"
    else:
        tasks[id] = "[ERROR] Something went wrong"
    
    if os.path.exists(file_path):
        os.remove(file_path)

@app.get("/status/{id}")
def check_status(id: int):
    result = tasks.get(id, "There is no such a task")
    return {"status": result}

@app.get("/scan/url")
def scan_url(background_tasks: BackgroundTasks, url: str):
    global task_id
    task_id += 1
    
    file_name = f"url_{task_id}.jpg"
    
    try:
        response = requests.get(url)
        with open(file_name, "wb") as f:
            f.write(response.content)
            
        background_tasks.add_task(process_task, task_id, file_name)
        
        return {"message": "Task queued", "id": task_id}
        
    except:
        return {"error": "Could not download image"}

@app.get("/scan/local")
def scan_local(background_tasks: BackgroundTasks, path: str):
    global task_id
    task_id += 1
        
    background_tasks.add_task(process_task, task_id, path)
    return {"message": "Task queued", "id": task_id}