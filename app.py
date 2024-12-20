from time import sleep
from sensor.sensor import TemperatureSensor, HumiditySensor, GPSSensor
from iot_device.iot_device import Cobots, SCARA
from iot_device.stream_manager import StreamManager
from iot_device.kafka_stream_handler import StreamHandler

if __name__ == "__main__":
    # Initialize sensors
    temp_sensor = TemperatureSensor("temp-001")
    humidity_sensor = HumiditySensor("hum-001")
    gps_sensor = GPSSensor("gps-001")
    cobots = Cobots("cobots-001")
    scara = SCARA("scara-001")

    # Create the stream manager
    stream_manager = StreamManager()
    stream_manager.add_sensor(temp_sensor)
    stream_manager.add_sensor(humidity_sensor)
    stream_manager.add_sensor(gps_sensor)
    stream_manager.add_sensor(cobots)
    stream_manager.add_sensor(scara)

    # Set up the stream handler
    stream_handler = StreamHandler()
    stream_manager.set_stream_handler(stream_handler)

    # Start streaming data
    try:
        stream_manager.start_streaming(interval=2.0)  # Stream every 2 seconds
    except KeyboardInterrupt:
        print("\nStreaming stopped.")