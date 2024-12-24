from sensor.pydantic_data import *

class Cobots:
    def __init__(self, sensor_id: str, topic_name: str):
        self.sensor_id = sensor_id
        self.topic = topic_name

    def read_data(self) -> dict:
        return Cobots_Gen.generate_data(self.sensor_id)
    
    def get_id(self) -> str:
        return self.sensor_id
    
    def get_topic(self) -> str:
        return self.topic
    

class SCARA:
    def __init__(self, sensor_id: str, topic_name: str):
        self.sensor_id = sensor_id
        self.topic = topic_name
        
    def read_data(self) -> dict:
        return SCARA_Gen.generate_data(self.sensor_id)
    
    def get_id(self) -> str:
        return self.sensor_id
    
    def get_topic(self) -> str:
        return self.topic