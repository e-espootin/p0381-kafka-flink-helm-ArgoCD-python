import os
import pandas as pd
import clickhouse_connect
from datetime import datetime

class ClickHouseDataRetriever:
    def __init__(self, host, port, database, table, timestamp_column, last_datetime_file='last_retrieve_datetime.txt'):
        """
        Initialize the ClickHouseDataRetriever class.
        """
        self.host = host
        self.port = port
        self.database = database
        self.table = table
        self.timestamp_column = timestamp_column
        self.last_datetime_file = last_datetime_file
        self.client = clickhouse_connect.get_client(host=self.host, port=self.port)

    def _get_last_retrieve_datetime(self):
        """
        Retrieve the last datetime from the file or return a default value.
        """
        if os.path.exists(self.last_datetime_file):
            with open(self.last_datetime_file, 'r') as file:
                return datetime.fromisoformat(file.read().strip())
        # Default to a very old date if the file doesn't exist
        return datetime(1970, 1, 1)

    def _save_last_retrieve_datetime(self, dt):
        """
        Save the last retrieved datetime to the file.
        """
        with open(self.last_datetime_file, 'w') as file:
            file.write(dt.isoformat())

    def fetch_data(self):
        """
        Fetch data from ClickHouse and return it as a Pandas DataFrame.
        Updates the last retrieve datetime.
        """
        # Get the last retrieval datetime
        last_datetime = self._get_last_retrieve_datetime()

        # Query to fetch data
        query = f"""
        SELECT 
            st.sensor_id,
            toStartOfInterval(event_time, INTERVAL 2 minute) AS interval_event_time,
            COUNT(*) AS event_count,
            AVG(temperature) AS avg_value
        FROM {self.database}.{self.table} as st
        where interval_event_time < subtractMinutes(now(), 2) -- ignore current record, it changes constantly
            and {self.timestamp_column} > '{last_datetime.isoformat()}'
        GROUP BY sensor_id, interval_event_time
        ORDER BY interval_event_time desc
        """
        
        print(f"Query: {query}")
        # Execute the query
        result = self.client.query(query)

        # Convert to Pandas DataFrame
        df = pd.DataFrame(result.result_rows, columns=result.column_names)

        # Update the last retrieve datetime if data exists
        if not df.empty:
            new_last_datetime = df[self.timestamp_column].max()
            self._save_last_retrieve_datetime(new_last_datetime)

        return df

    def close_connection(self):
        """
        Close the connection to the ClickHouse server.
        """
        self.client.close()