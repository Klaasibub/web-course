import psycopg2
conn = psycopg2.connect(dbname='task_db', user='postgres',
                        password='1234', host='localhost')
cursor = conn.cursor()

cursor.execute('insert into users(age) values(22)')
cursor.execute('select * from users')

for row in cursor:
    print(row)

cursor.close()
conn.close()