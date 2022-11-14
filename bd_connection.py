import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_host, db_port):
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def insert_values(value_list):
    connection.autocommit = True
    cursor = connection.cursor()
    user_records = ", ".join(["%s"] * len(value_list))
    query = (
        f"INSERT INTO users(name, age, gender, nationality) VALUES {user_records}"
    )
    try:
        cursor.execute(query, value_list)
        print("Query inserted successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


''' ПОДКЛЮЧЕНИЕ К БД '''
connection = create_connection("postgres", "natalaantonenko", "localhost", "5432")


''' СОЗДАНИЕ ТАБЛИЦЫ '''
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL, 
  age INTEGER,
  gender TEXT,
  nationality TEXT
)"""
execute_query(connection, create_users_table)


''' ДОБАВЛЕНИЕ ЗАПИСИ В ТАБЛИЦУ '''
user = [
    ("Liza", 12, "female", "rus"),
    ("Misha", 17, "male", "rus")
]
insert_values(user)


''' УДАЛЕНИЕ ЗАПИСЕЙ ИЗ ТАБЛИЦЫ '''
delete_comment = "DELETE FROM users WHERE id = 2"
execute_query(connection, delete_comment)

select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)
for user in users:
    print(user)


''' УДАЛЕНИЕ ТАБЛИЦЫ '''
drop_table = "DROP TABLE users"
execute_query(connection, drop_table)