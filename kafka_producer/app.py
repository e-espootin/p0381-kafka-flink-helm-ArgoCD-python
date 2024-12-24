from time import sleep
from sensor.sensor import TemperatureSensor, HumiditySensor, GPSSensor, KVSensor
from iot_device.iot_device import Cobots, SCARA
from iot_device.stream_manager import StreamManager
from iot_device.kafka_stream_handler import StreamHandler

def main():
    pass

if __name__ == "__main__":
    try:
        # Initialize sensors
        temp_sensor = TemperatureSensor("temp-001", "temperature")
        temp_sensor_4 = TemperatureSensor("temp-004", "temperature")
        # humidity_sensor = HumiditySensor("hum-001", "humidity")
        # gps_sensor = GPSSensor("gps-001", "gps")
        # cobots = Cobots("cobots-001", "cobots")
        # scara = SCARA("scara-001", "scara")
        # kv = KVSensor("kv-001", "kv")

        # Create the stream manager
        stream_manager = StreamManager()
        stream_manager.add_sensor(temp_sensor)
        stream_manager.add_sensor(temp_sensor_4)
        # stream_manager.add_sensor(humidity_sensor)
        # stream_manager.add_sensor(gps_sensor)
        # stream_manager.add_sensor(cobots)
        # stream_manager.add_sensor(scara)
        # stream_manager.add_sensor(kv)   

        # Set up the stream handler
        stream_handler = StreamHandler()
        stream_manager.set_stream_handler(stream_handler)

        # Start streaming data
        stream_manager.start_streaming(interval=10.0)  # Stream every 10 seconds

    except KeyboardInterrupt as e:
        print("\n KeyboardInterrupt : Streaming stopped.")
        raise e
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise e
    