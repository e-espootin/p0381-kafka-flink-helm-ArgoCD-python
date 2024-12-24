from consumers.clickhouse import ClickHouseDataRetriever
from consumers.azureblob import AzureBlobStorageHandler
from config.sensors_config import Sensors
import pandas as pd
import os

def main():
    # get env variables
    var_sensor = os.getenv('SENSOR', 'temperature')
    var_topic = os.getenv('', Sensors[var_sensor]['topic'])
    var_table = os.getenv('', Sensors[var_sensor]['table'])
    var_timestamp_column = Sensors[var_sensor]['timestamp_column']

    # fetch data from ClickHouse
    retriever = ClickHouseDataRetriever(host='localhost'
                                        , port=18123
                                        , database='sensorDB'
                                        , table=var_table
                                        , timestamp_column=var_timestamp_column)
    data = retriever.fetch_data()
    print(data.head())
    retriever.close_connection()

    # save into Azure Blob
    azure_conn_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    var_transformed_type = Sensors[var_sensor]['transformed_type']
    var_container = "crp038xdev001"
    var_blob_name = "loaded_files"
    azure_blob = AzureBlobStorageHandler(transformed_type=var_transformed_type
                                         , topic_name=var_topic
                                         , connection_string_env_var=azure_conn_string
                                         , blob_name=var_blob_name
                                         , container_name=var_container)
    azure_blob.save_dataframe_to_blob(data)


if __name__ == "__main__":
    main()