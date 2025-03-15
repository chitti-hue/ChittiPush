import pandas as pd
import sqlite3
excel_file="C:/Users/HP/Desktop/hike_file.xlsx"
df=pd.read_excel(excel_file,sheet_name="Sheet2",engine='openpyxl')
#print(df)
conn_method=sqlite3.connect('database.db')
cursor_method=conn_method.cursor()
#cursor_method.execute('''DROP table salary_increment3''')

"""cursor_method.execute('''CREATE TABLE IF NOT EXISTS salary_increment4(namee text,
                                                                     emp_id primary key not null, 
                                                                     salary integer not null,
                                                                     hike_per integer,
                                                                     dept text,
                                                                     dept_max integer 
                                                                      ) ''')"""
def insert_data(name, emp_id,salary,hike_per,dept_text,dept_max):
    cursor_method1=conn_method.cursor()
    sql_query=f"INSERT INTO salary_increment4(namee,emp_id,salary,hike_per,dept,dept_max) VALUES ('{name}','{emp_id}','{salary}','{hike_per}','{dept_text}','{dept_max}')"
    cursor_method1.execute(sql_query)

for index, row in df.iterrows():
    department=row['dept']#dep1
    # #print(department)
    #print(df["dept"])
    filtered_df = df[df["dept"] == department]#dep1 == dep1  # used to fileter values & create new df based on condition
    #print(filtered_df)
    current_total_salary = filtered_df["salary"].sum()  # used to sum the column values in df
    #print((current_total_salary))
    hike_value =(row['salary'] * row['hike_per'])/100
    # salary + salary * hike /100  = 1 + hike/100 * salary
    #print(hike_value)
    if current_total_salary +hike_value <= row['dept_max']:
        after_hiked_salary=row['salary']+hike_value
        #row['salary'] = row['salary'] + hike_value
        df.loc[df["emp_id"] == row['emp_id'], "salary"] = after_hiked_salary #If you want to update values only for specific rows, use loc[]:
        #print(df)
        insert_data(row['namee'],row['emp_id'],after_hiked_salary,row['hike_per'],row['dept'],row['dept_max'])
    else:
        #print("___________")
        insert_data(row['namee'], row['emp_id'],row['salary'], row['hike_per'], row['dept'], row['dept_max'])

conn_method.commit()
cursor_method.close()
conn_method.close()
