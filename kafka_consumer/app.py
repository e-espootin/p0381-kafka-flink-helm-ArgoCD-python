import configparser
from consumers import base_consumer
#import argparse
import os
from utils.logger import setup_logger


def read_config(file_path):
    config = configparser.ConfigParser()
    # Read the configuration file
    config.read(file_path)
    return config

def consume_and_store_streams():
    #
    # logger = setup_logger()
    
    # input topic
    topic = os.getenv("KAFKA_TOPIC", "temperature_topic")

    # Access secrets from environment variables
    # aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    # aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    # Azure connection string
    azure_connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    #
    config = read_config('config.ini')
    # if not(args.broker):
    kafka_broker = config['kafka']['bootstrap_servers']
    kafka_topic = topic
    consumer_group = config['kafka']['consumer-group']
    interval_sec = int(config['recurring']['interval_sec'])
    messages_batch_size = int(config['recurring']['messages_batch_size'])
    
    try:
        kafka_manager = base_consumer.MyKafkaManager(
            bootstrap_servers=kafka_broker,
            topic_name=kafka_topic
        )
        kafka_manager.set_azure_blob_storage(connection_string=azure_connection_string, container_name=config['azure_blob_storage']['container_name'], 
                                             BLOB_NAME=config['azure_blob_storage']['blob_name'],
                                             transformed_type = config['azure_blob_storage']['transformed_type']
                                             )

        # logger.info(f"Starting consumer for topic: {topic}")
        print(f"Kafka bootstrap: {kafka_manager.bootstrap_servers}")
        print(f"Kafka topic: {kafka_manager.topic_name}")

        # create consumer
        kafka_manager.create_consumer(  # create consumer
            group_id=consumer_group
            , auto_offset_reset="earliest"
            , auto_commit_enable=True
        )
        kafka_manager.consume_messages_Commit_manually(messages_batch_size)
        
    except Exception as e:
        print(f"Failed to consume messages: {e}")   



if __name__ == "__main__":
    consume_and_store_streams()
