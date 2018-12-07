import pymysql
import random
connection = pymysql.connect("hostname","DB user name", "DB password","DB name")
table_name=str(input("Enter the Table name:"))
action = connection.cursor()
rows=int(input("How many rows want to add:"))
sql="""desc """+table_name
action.execute(sql)
result=action.fetchall()
aa=int(action.execute(sql))
sql="""insert into """+table_name+" values"
for i in range(1,rows+1):
    count = 1
    sql = sql + "("
    print("ROW: ", i)
    for j in result:
        print("Enter",j[0],end='')
        value=input()
        sql=sql+"'"+value+"'"
        if(count<aa):
            sql=sql+","
        count=count+1
    sql=sql+")"
    if (i < rows):
        sql = sql + ","
try:
    action.execute(sql)
    connection.commit()
    print('Row created successfully !!!')
    connection.close()
except:
    print("Row creation failed !!!")


