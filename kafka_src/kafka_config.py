# kafka_config.py

CONFLUENT_CONFIG = {
    'bootstrap.servers': '192.168.0.108:9092',  # Confluent Kafka bootstrap server
    'client.id': 'iot-producer',
    'group.id': 'iot-consumer-group',
    'enable.auto.commit': False,
}

DEFAULT_TOPIC_CONFIG = {
    "num_partitions": 1,  # Default number of partitions
    "replication_factor": 1,  # Default replication factor
}

# Sensor-specific Kafka topics
KAFKA_TOPICS = {
    "temperature": "temperature_topic",
    "humidity": "humidity_topic",
    "gps": "gps_topic",
    "cobots": "cobots_topic",
    "scara": "scara_topic",
}