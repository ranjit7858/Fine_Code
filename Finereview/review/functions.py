import os
import ast
import mysql.connector

def connection():
    con = mysql.connector.connect(user='root',password='4844',host='127.0.0.1',database='finecode')
    return con


def count_functions(directory):
    con=connection()
    cursor=con.cursor()
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            with open(os.path.join(directory, filename), "r") as f:
                code = f.read()
                try:
                    tree = ast.parse(code)
                    count = len([node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)])
                    print("Number of functions in {}: {}".format(filename, count))


                    query=("insert into functions values(%s,%s)")
                    data=(filename,count)
                    cursor.execute(query,data)
                except SyntaxError:
                    continue
    cursor.close()
    con.commit()
    con.close() 

count_functions("D:/Hacathon/permisson less/finyash/Finereview/review/codes")