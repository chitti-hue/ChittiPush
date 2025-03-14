import pandas as pd
import sqlite3

# third time push test
# fileread = pd.read_excel('chitti_python.xlsx') print(fileread) #used to read the outer excel file
# dataframe=fileread.iloc[:,1:]#iloc is from pandas (used to print rows, column

conn = sqlite3.connect("chitti.db")  # used to create a connection to data base name
df = pd.read_excel('chitti_python.xlsx', engine='openpyxl')
print(df)


# dff=df.iloc[:,1:]
# pd.read_excel() reads an Excel file into a Pandas DataFrame.
# The engine="openpyxl" tells Pandas to use the OpenPyXL library to handle the .xlsx file.
def update_method(sql_conn, name, emp_id, age, salary, domain, location):
    temp_cursor = sql_conn.cursor()
    sql_query = f"INSERT INTO emp3(namee,emp_id,age,salary,domainn,location) VALUES('{name}','{emp_id}','{age}','{salary}','{domain}','{location}')"
    print(sql_query)
    temp_cursor.execute(sql_query)
    temp_cursor.close()


# pushing changes
for index, row in df.iterrows():
    if row["emp_id"] == 2251:
        update_method(sql_conn=conn, row["namee"], row["emp_id"], row["age"], row["salary"], row["domainn"], "hyd")
    else:
        update_method(conn, row["namee"], row["emp_id"], row["age"], row["salary"], row["domainn"], row["location"])

conn.commit()
conn.close()
"""
#Used to create new table in data base
conn.cursor().execute('''
    CREATE TABLE IF NOT EXISTS emp3 (
        namee  TEXT NOT NULL,
        emp_id INTEGER PRIMARY KEY,
        age INTEGER NOT NULL,
        salary NUMBER NOT NULL,
        domainn  TEXT NOT NULL,
        location TEXT
    )
''')

#Used to delete entaire table in data base
conn.cursor().execute("DROP TABLE emp3")

#Used to insert multiple data at a time
df.to_sql("emp3", conn, if_exists="append", index=False) #The to_sql() method simplifies bulk insertion
   #The to_sql() method in Pandas is used to write a DataFrame into a SQL database.Creates a table "employees" in the company.db database.
   #If the table exists, it will be replaced with new data (if_exists="replace").Does not include the DataFrame index (index=False).
   #A DataFrame is a two-dimensional table-like data structure in the Pandas library, similar to an Excel sheet or SQL table. It consists of rows and columns,
                           where each column can have different data types (integers, floats, strings, etc.).
conn.cursor().executemany("INSERT INTO emp3 (namee,emp_id, age,salary,domainn,location) VALUES (?,?,?,?,?)", df)

#Used to update value in existing table
conn.cursor().execute("UPDATE emp3 SET salary=salary+5000 WHERE age=26 ") 

#used to select individual rows 
val=conn.cursor()
val.execute("Select namee from emp3")
print(val.fetchall())

#used insert data row-by-row 
def update data (conn, update_id, update_value):
    temp_cursore=connection.cursor()#create a cursor object to execute Sql comands
    temp_cursore.execute(f"INSERT INTO TABLE(id, value) VALUES({update_id}{update_value})")
       #used to INSERT single rowl
    print(temp_cursore.rowcount)

conn=sqlite3.connect("chitti.db")#used to create a connection to data base name
for index, row in df.iterrows():
    if row["emp_id"] == 2251
        update data(conn, row["id"], 99999)
    else:
        update_data(conn, row["id"], row["value"])


 """