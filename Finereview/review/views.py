from django.shortcuts import render
from . import plag,variables,functions,space,time,unique,loops,functions
import mysql.connector


# Create your views here.
def connection():
    
    con = mysql.connector.connect(user='root',password='4844',host='127.0.0.1',database='finecode')
    return con


def review(request):

    dir='D:/Hacathon/permisson less/finyash/Finereview/review/codes'
    variables.count_variables(dir)
    plag.main()
    time.main()
    functions.count_functions(dir)
    space.main()
    loops.main() 
    con=connection()
    cursor=con.cursor()

    querry1="select distinct code1,code2,percentage from plag"
    cursor.execute(querry1)
    myresult=cursor.fetchall()
    code1=[]
    code2=[]
    percentage=[]
    for x in myresult:
        code1.append(x[0])
        code2.append(x[1])
        percentage.append(x[2])
    zipped=zip(code1,code2,percentage)


    querry1="select * from time group by code"
    cursor.execute(querry1)
    myresult=cursor.fetchall()
    code_time=[]
    time1=[]
    for x in myresult:
        code_time.append(x[0])
        time1.append(int(x[1]*100))



        
    return render(request,'index.html',{'zipped':zipped,'code_time':code_time,'time1':time1})