# move the code in juypter note book to here
import os
from sqlalchemy import create_engine
import pandas as pd
import logging


class DBConnect:
    @staticmethod
    def connect_to_db():
        # Fetch the database credentials from environment variables
        db_user = os.getenv("POSTGRES_USER")
        db_password = os.getenv("POSTGRES_PASSWORD")
        db_port = os.getenv("POSTGRES_PORT")
        db_name = os.getenv("POSTGRES_DB")

        # Create a connection to the PostgreSQL database
        engine = create_engine(
            f'postgresql://{db_user}:{db_password}@localhost:{db_port}/{db_name}')

        # Return the fetched rows
        return engine

    @staticmethod
    def execute_query(query):
        engine = DBConnect.connect_to_db()
        connection = engine.raw_connection()

        try:
            cursor = connection.cursor()
            print(f"Executing query: {query}")
            cursor.execute(query)
            result = cursor.fetchall()
            # Convert the result to a Pandas DataFrame
            columns = [desc[0] for desc in cursor.description]
            df = pd.DataFrame(result, columns=columns)

            return df

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

            # Dispose of the SQLAlchemy engine after use
            engine.dispose()
            print("Query execution complete")

    @staticmethod
    def save_to_postgres(data_frame, table_name):
        # Your database connection information
        engine = DBConnect.connect_to_db()

        try:
            # Save data to PostgreSQL table
            print(f"Saving data to PostgreSQL table '{table_name}'")
            data_frame.to_sql(table_name, con=engine,
                              if_exists="replace", index=False)

        finally:
            # Dispose of the SQLAlchemy engine after use
            engine.dispose()
            print("Save operation complete")
