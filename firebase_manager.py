import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 
import firebase_manager

from datetime import datetime 

class FirebaseManager:

    ref = None
    cred = None

    def __init__(self, cred_path, db_url, db_name):
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred, {"databaseURL": db_url})
        self.ref = db.reference(f'/{db_name}')

    def push(self, data) -> bool:
        if not isinstance(data, int):
            print("Data is not a integer")
            return False

        current_datetime = datetime.now()
        year = current_datetime.strftime("%Y")
        month = current_datetime.strftime("%m")
        day = current_datetime.strftime("%d")
        time = current_datetime.strftime("%H:%M:%S")

        object_data = {
            "time": f"{year}-{month}-{day} {time}",
            "value": data
        }
        
        self.ref.push(object_data)
        return True

    def get(self, latest: int = 10):
        data = self.ref.get()
        return data