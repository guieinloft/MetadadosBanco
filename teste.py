import mysql.connector

database = input('Digite o nome do banco: ')
con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database=database)
cur = con.cursor()

queryt = 'show tables'
tables = list()

queryc = 'describe %s'

cur.execute(queryt)
for table in cur:
    tables.append(table[0])

for table in tables:
    print(table + ": ")
    queryc = 'describe ' + table
    cur.execute(queryc)
    for column in cur:
        print(column)


con.close()
