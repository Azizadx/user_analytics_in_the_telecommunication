# move the code in juypter note book to here
import os
from sqlalchemy import create_engine


class DBConnect:
    @staticmethod
    def connect_to_db():
        # Fetch the database credentials from environment variables
        db_user = os.getenv("POSTGRES_USER")
        db_password = os.getenv("POSTGRES_PASSWORD")
        db_port = '5435'
        db_name = os.getenv("POSTGRES_DB")

        # Create a connection to the PostgreSQL database
        engine = create_engine(
            f'postgresql://{db_user}:{db_password}@localhost:{db_port}/{db_name}')

        # Return the fetched rows
        return engine
