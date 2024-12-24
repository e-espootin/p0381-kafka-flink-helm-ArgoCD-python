import time
from sensor.sensor import ISensor

class StreamManager:
    def __init__(self):
        self.sensors = []
        self.stream_handler = None

    def add_sensor(self, sensor: ISensor):
        self.sensors.append(sensor)

    def set_stream_handler(self, handler):
        self.stream_handler = handler

    def start_streaming(self, interval: float = 1.0):
        """Continuously read data from sensors and send it."""
        if not self.stream_handler:
            raise ValueError("StreamHandler is not set.")
        
        print("Starting data streaming...")
        while True:
            for sensor in self.sensors:
                data = sensor.read_data()
                # print(f"Collected data: {data}")
                print(f"sensor topic: {sensor.topic}")
                self.stream_handler.send(topic=sensor.topic, data=data)
            time.sleep(interval)