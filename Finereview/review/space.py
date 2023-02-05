import os
import tracemalloc

import mysql.connector

def connection():
    con = mysql.connector.connect(user='root',password='4844',host='127.0.0.1',database='finecode')
    return con

def space_complexity(directory):
    con=connection()
    cursor=con.cursor()
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            with open(os.path.join(directory, filename), "r") as f:
                code = f.read()
                try:
                    exec(code, {'__file__': filename})
                    current, peak = tracemalloc.get_traced_memory()
                    print("Space complexity in {}: current={}MB peak={}MB".format(filename, current / 10**6, peak / 10**6))
                    query=("insert into space values(%s,%s)")
                    data=(filename,peak / 10**6)
                    cursor.execute(query,data)
                
                except Exception as e:
                    continue
    cursor.close()
    con.commit()
    con.close() 
def main():
    tracemalloc.start()
    space_complexity("D:/Hacathon/permisson less/finyash/Finereview/review/codes")
    tracemalloc.stop()
main()
