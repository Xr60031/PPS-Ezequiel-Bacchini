import json
import base64

def serialize_data(data):
    if isinstance(data, bytes):
        return base64.b64encode(data).decode('utf-8')  # Convertir bytes a string base64
    if isinstance(data, dict):
        return {key: serialize_data(value) for key, value in data.items()}
    if isinstance(data, list):
        return [serialize_data(item) for item in data]
    return data

class Facade_Json():
    def __init__(self):
        self

    def dump(self, session_data, file, default):
        return json.dump(serialize_data(session_data), file, default=default)
    
    def load(self, file):
        return json.load(file)