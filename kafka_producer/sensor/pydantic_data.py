from pydantic import BaseModel, Field
from faker import Faker
from random import uniform
from typing import Dict
from datetime import datetime

class Cobots_Gen(BaseModel):
    id: str
    temperature: float
    pressure: float
    humidity: float
    timestamp: str
    location: Dict = None
    city: str
    country: str

    @staticmethod
    def generate_data(sensor_id: str) -> Dict:
        fake = Faker()

        return Cobots_Gen(
            id=sensor_id,
            temperature=uniform(20.0, 30.0),
            pressure=uniform(1000, 2000),
            humidity=uniform(40.0, 60.0),
            timestamp=str(datetime.now().strftime('%Y-%m-%dT%H:%M:%S')),
            location={
                "latitude": uniform(-90, 90),
                "longitude": uniform(-180, 180)
            },
            city=fake.city(),
            country=fake.country()
        ).dict()
    
# Cartesian
# Articulated
# Scara
class SCARA_Gen(BaseModel):
    id: str
    temperature: float
    pressure: float
    humidity: float
    timestamp: str
    location: Dict = None
    city: str

    @staticmethod
    def generate_data(sensor_id: str) -> Dict:
        fake = Faker()

        return SCARA_Gen(
            id=sensor_id,
            temperature=uniform(20.0, 30.0),
            pressure=uniform(1000, 2000),
            humidity=uniform(40.0, 60.0),
            timestamp=str(datetime.now().strftime('%Y-%m-%dT%H:%M:%S')),
            location={
                "latitude": uniform(-90, 90),
                "longitude": uniform(-180, 180)
            },
            city=fake.city(),
        ).dict()