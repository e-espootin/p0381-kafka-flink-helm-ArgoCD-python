

# Sensor-specific Kafka topics
Sensors = {
    "temperature": 
        {"topic": "temperature_topic",
        "table": "sensor_temp",
        "timestamp_column": "interval_event_time",
        "transformed_type": "transformed_silver"
        },
    "humidity": 
        {"topic": "humidity_topic",
        "table": "sensor_humidity",
        "timestamp_column": "interval_event_time",
        "transformed_type": "transformed_silver"
        },
    "cobots": 
        {"topic": "cobots_topic",
        "table": "sensor_cobots",
        "timestamp_column": "interval_event_time",
        "transformed_type": "transformed_silver"
        },
    "scara": 
        {"topic": "scara_topic",
        "table": "sensor_scara",
        "timestamp_column": "interval_event_time",
        "transformed_type": "transformed_silver"
        },
    "gps": 
        {"topic": "gps_topic",
        "table": "sensor_gps",
        "timestamp_column": "interval_event_time",
        "transformed_type": "transformed_silver"
        }
}