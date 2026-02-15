from psycopg2 import connect, sql
from psycopg2.extras import RealDictCursor

class Database:
    def __init__(self):
        self.connection = connect(
            dbname='ecommerce_db',
            user='postgres',
            password='2008',
            host='localhost',
            port=5432
        )
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id VARCHAR(50) NOT NULL UNIQUE,
            ism VARCHAR(100) NOT NULL,
            fam VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL,
            tel VARCHAR(15) NOT NULL
        );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def execute_update(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def add_user(self, user_id, ism, fam, age, tel):
        insert_query = """
        INSERT INTO users (user_id, ism, fam, age, tel)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (user_id) DO NOTHING;
        """
        self.execute_update(insert_query, (user_id, ism, fam, age, tel))

    def check_user(self, user_id):
        select_query = "SELECT * FROM users WHERE user_id = %s;"
        result = self.execute_query(select_query, (str(user_id),))
        return result[0] if result else None

