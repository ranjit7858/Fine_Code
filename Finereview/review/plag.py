import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import mysql.connector 

# Reading all ".py" files and to load all the path ".py" files on project directory.
files = [doc for doc in os.listdir('D:/Hacathon/permisson less/finyash/Finereview/review/codes') if doc.endswith('.py')]
fileStore = [open(os.path.join('D:/Hacathon/permisson less/finyash/Finereview/review/codes',_file)).read()
                 for _file in files]

# Compute similarity between them.
def vectorize(Data): return TfidfVectorizer().fit_transform(Data).toarray()
def similarity(code_1, code_2): return cosine_similarity([code_1, code_2])

# Vectorize the data.
vectors = vectorize(fileStore)
s_vectors = list(zip(files, vectors))
plagiarismResults = set()

# Creating function to Compute similarity.
def PlagiarismChecker():
    global s_vectors
    for file_1, file_vector_1 in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((file_1, file_vector_1))
        del new_vectors[current_index]
        for file_2, file_vector_2 in new_vectors:
            sim_score = similarity(file_vector_1, file_vector_2)[0][1]
            file_pair = sorted((file_1, file_2))
            score = (file_pair[0], file_pair[1], sim_score)
            plagiarismResults.add(score)
    return plagiarismResults

  
def connection():
    
    con = mysql.connector.connect(user='root',password='4844',host='127.0.0.1',database='finecode')
    return con
def main():
    dict={}
    con=connection()
    cursor=con.cursor()
    for data in PlagiarismChecker():
        dict[data[0]]=data[2]
        query=("insert into plag values(%s,%s,%s)")
        data1=(data[0],data[1],data[2])
        cursor.execute(query,data1)
    cursor.close()
    con.commit()
    con.close()  
main()  