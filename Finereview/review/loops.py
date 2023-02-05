import ast
import os

import mysql.connector

def connection():
    con = mysql.connector.connect(user='root',password='4844',host='127.0.0.1',database='finecode')
    return con

def count_loops(node):
    count = 0
    if isinstance(node, (ast.For, ast.While)):
        count += 1
    for child in ast.iter_child_nodes(node):
        count += count_loops(child)
    return count

def count_loops_in_file(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
        tree = ast.parse(code)
        return count_loops(tree)

def main():
    con=connection()
    cursor=con.cursor()
    directory = 'D:/Hacathon/permisson less/finyash/Finereview/review/codes'
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            file_path = os.path.join(directory, filename)
            loop_count = count_loops_in_file(file_path)
            print(f'{filename}: {loop_count} loops')
            query=("insert into looptable values(%s,%s)")
            data=(filename,loop_count)
            cursor.execute(query,data)
'''
if __name__ == '__main__':
   main()
   '''