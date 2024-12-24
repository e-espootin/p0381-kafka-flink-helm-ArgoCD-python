import random
from abc import ABC, abstractmethod
from datetime import datetime

class ISensor(ABC):
    @abstractmethod
    def read_data(self) -> dict:
        pass

    @abstractmethod
    def get_id(self) -> str:
        pass

    @abstractmethod
    def get_topic(self) -> str:
        pass


class TemperatureSensor(ISensor):
    def __init__(self, sensor_id: str, topic_name: str):
        self.sensor_id = sensor_id
        self.topic = topic_name

    def read_data(self) -> dict:
        # Simulate reading temperature data
        return {"sensor_id": self.sensor_id, 
                "temperature": round(random.uniform(1.0, 40.0),1), 
                "reg_timestamp": int(datetime.utcnow().timestamp()), 
                "event_time": str(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
                }


    def get_id(self) -> str:
        return self.sensor_id
    
    def get_topic(self) -> str:
        return self.topic


class HumiditySensor(ISensor):
    def __init__(self, sensor_id: str, topic_name: str):
        self.sensor_id = sensor_id
        self.topic = topic_name

    def read_data(self) -> dict:
        # Simulate reading humidity data
        return {"sensor_id": self.sensor_id, 
                "humidity":random.uniform(40.0, 90.0), 
                "reg_timestamp": int(datetime.utcnow().timestamp()), 
                "event_time": str(datetime.utcnow())
                }

    def get_id(self) -> str:
        return self.sensor_id

    def get_topic(self) -> str:
        return self.topic
    
class KVSensor(ISensor):
    def __init__(self, sensor_id: str, topic_name: str):
        self.sensor_id = sensor_id
        self.topic = topic_name

    def read_data(self) -> dict:
        # Simulate reading humidity data
        return {"ckey": self.sensor_id, 
                "cvalue":round(random.uniform(40.0, 90.0),1),
                "ctimestamp": int(datetime.now().timestamp())
                }

    def get_id(self) -> str:
        return self.sensor_id

    def get_topic(self) -> str:
        return self.topic

class GPSSensor(ISensor):
    def __init__(self, sensor_id: str, topic_name: str):
        self.sensor_id = sensor_id
        self.topic = topic_name

    def read_data(self) -> dict:
        # Simulate reading GPS data
        return {
            "sensor_id": self.sensor_id,
            "type": "gps",
            "latitude": random.uniform(-90, 90),
            "longitude": random.uniform(-180, 180),
        }

    def get_id(self) -> str:
        return self.sensor_id
    
    def get_topic(self) -> str:
        return self.topic