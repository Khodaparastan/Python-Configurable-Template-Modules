```python
# Usage Example
db = MySQLDatabase(host='localhost', user='username', password='password', database='mydatabase')

# Fetching data using with statement
with db as cursor:
    cursor.execute("SELECT * FROM my_table")
    records = cursor.fetchall()
    for record in records:
        print(record)

# Executing a query without with statement
result = db.execute_query("UPDATE my_table SET column = %s WHERE id = %s", params=('value', 1))
print(f"{result} rows affected.")

#MULTIPLE CONNECTIONS
# Configuration for the first database
db1 = MySQLDatabase(host='localhost', user='user1', password='password1', database='database1')

# Configuration for the second database
db2 = MySQLDatabase(host='localhost', user='user2', password='password2', database='database2')

# You can now use db1 and db2 independently to interact with their respective databases.
```