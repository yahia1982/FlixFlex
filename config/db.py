import sqlite3

db_name = 'data/FlixFlaxDB.db'

class DbHelper:
    def __init__(self):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            return True
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")
            return False

    def execute_query(self, query, params=None):
        try:
            if self.connect():
                cursor = self.conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor
            else:
                print("Database connection is not established.")
                return None
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None

    def fetch_all(self, query, params=None):
        cursor = self.execute_query(query, params)
        if cursor:
            return cursor.fetchall()

        return []

    def fetch_one(self, query, params=None):
        cursor = self.execute_query(query, params)
        if cursor:
            return cursor.fetchone()
        return None

    def commit(self):
        if self.conn:
            self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
