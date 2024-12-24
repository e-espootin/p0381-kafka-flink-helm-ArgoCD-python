import os
from azure.storage.blob import BlobServiceClient, BlobClient
import pandas as pd
import io
from io import StringIO

class AzureBlobStorageHandler:
    def __init__(self, *, transformed_type: str, topic_name: str, connection_string_env_var: str, blob_name: str, container_name: str):
   
        # Azure Blob Storage details
        self.CONNECTION_STRING = connection_string_env_var
        self.CONTAINER_NAME = container_name
        self.BLOB_NAME = blob_name
        self.transformed_type = transformed_type
        self.topic_name = topic_name

        

    def save_dataframe_to_blob(self, df: pd.DataFrame):
        try:

            # file name with date - time stamp
            filename = f'sensor_{self.topic_name}_{pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")}.csv'
            directory = f'{self.BLOB_NAME}/{self.transformed_type}/{self.topic_name}/{filename}'
            print(f"directory : {directory}")
            # Convert DataFrame to CSV in memory
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, index=False)
            csv_buffer.seek(0)

            # Initialize Azure Blob client
            blob_service_client = BlobServiceClient.from_connection_string(self.CONNECTION_STRING)
            blob_client = blob_service_client.get_blob_client(container=self.CONTAINER_NAME, blob=directory)

            # Upload CSV to Azure Blob
            blob_client.upload_blob(csv_buffer.getvalue(), overwrite=True)

            print(f"DataFrame successfully written to Azure Blob storage: {self.CONTAINER_NAME}/{directory}")

        except Exception as e:
            print(f"Failed to store messages in Azure Blob storage: {e}")

