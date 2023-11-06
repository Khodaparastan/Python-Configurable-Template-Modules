import mysql.connector
from mysql.connector import pooling
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MySQLDatabase:
    def __init__(self, host, user, password, database, port=3306, ssl_ca=None, pool_name='mypool', pool_size=5, **kwargs):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port,
        }
        
        if ssl_ca:
            self.config['ssl_ca'] = ssl_ca
        
        # Merge additional keyword arguments
        self.config.update(kwargs)

        # Initialize connection pool
        self.pool = mysql.connector.pooling.MySQLConnectionPool(pool_name=pool_name, pool_size=pool_size, **self.config)

    def execute_query(self, query, params=None):
        try:
            connection = self.pool.get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                records = cursor.fetchall()
                return records
            else:
                connection.commit()
                return cursor.rowcount
        except mysql.connector.Error as e:
            logger.error(f"Error executing query: {e}")
            raise
        finally:
            cursor.close()
            connection.close()

    # Context manager for connection management
    def __enter__(self):
        self.conn = self.pool.get_connection()
        self.cursor = self.conn.cursor(dictionary=True)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is not None:
            logger.error(f"Error: {exc_type}, {exc_val}")


