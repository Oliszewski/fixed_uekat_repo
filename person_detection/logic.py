import os
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def count_people(source):
    if not os.path.exists(source):
        print("[ERROR] There is no such a file. ")
        return None 
    
    try:
        results = model(source,classes=0,verbose=False)
        return len(results[0].boxes)
    
    except:
        print("[ERROR] Something went wrong. Try again")
        return None 