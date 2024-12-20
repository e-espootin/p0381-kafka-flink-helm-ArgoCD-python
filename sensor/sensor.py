import random
from abc import ABC, abstractmethod

class ISensor(ABC):
    @abstractmethod
    def read_data(self) -> dict:
        pass

    @abstractmethod
    def get_id(self) -> str:
        pass


class TemperatureSensor(ISensor):
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id

    def read_data(self) -> dict:
        # Simulate reading temperature data
        return {"id": self.sensor_id, "type": "temperature", "value": random.uniform(20.0, 30.0)}

    def get_id(self) -> str:
        return self.sensor_id


class HumiditySensor(ISensor):
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id

    def read_data(self) -> dict:
        # Simulate reading humidity data
        return {"id": self.sensor_id, "type": "humidity", "value": random.uniform(40.0, 60.0)}

    def get_id(self) -> str:
        return self.sensor_id


class GPSSensor(ISensor):
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id

    def read_data(self) -> dict:
        # Simulate reading GPS data
        return {
            "id": self.sensor_id,
            "type": "gps",
            "latitude": random.uniform(-90, 90),
            "longitude": random.uniform(-180, 180),
        }

    def get_id(self) -> str:
        return self.sensor_id