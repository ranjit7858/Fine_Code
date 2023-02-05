import os
import timeit
import mysql.connector

def connection():
    con = mysql.connector.connect(user='root',password='4844',host='127.0.0.1',database='finecode')
    return con

def main():
    directory = 'D:/Hacathon/permisson less/finyash/Finereview/review/codes'
    con=connection()
    cursor=con.cursor()
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as f:
                code = f.read()
                elapsed_time = timeit.timeit(stmt=code, number=1)
                
                query=("insert into time values(%s,%s)")
                data=(filename,elapsed_time)
                cursor.execute(query,data)
                print(f'{filename}: {elapsed_time:.6f} seconds')
    cursor.close()
    con.commit()
    con.close()
