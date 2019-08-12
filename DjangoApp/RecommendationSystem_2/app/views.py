from django.shortcuts import render
from django.http import HttpResponse
import pymysql

connection = pymysql.connect(host='localhost',port=3306,
user='root',database='movie_db',autocommit=True)

cursor = connection.cursor()

query_1 = "select * from movies where m_category like '%action%'"
query_2 = "select * from movies where m_category like '%comedy%'"
query_3 = "select * from movies where m_category like '%horror%'"
query_4 = "select * from movies where m_category like '% adventure%'"
cursor.execute(query_1)
actionMovies = cursor.fetchall()

cursor.execute(query_2)
comedyMovies = cursor.fetchall()

cursor.execute(query_3)
horrorMovies = cursor.fetchall()

cursor.execute(query_4)
adventureMovies = cursor.fetchall()

# print("Horror Movies",horrorMovies)

query = "select * from movies inner join users on movies.m_id = users.m_id"
cursor.execute(query)
watchedMovies = cursor.fetchall()

query = "select * from movies"
cursor.execute(query)
all_movies = cursor.fetchall()

movie_1 = watchedMovies[0][4]
user_cat = movie_1.split(',')
for i in range(len(user_cat)):
		user_cat[i] = user_cat[i].strip()

x = {}
for i in range(len(all_movies)):
	m_name = all_movies[i][1]
	category = all_movies[i][4]
	cat_list = category.split(',')
	for i in range(len(cat_list)):
		cat_list[i] = cat_list[i].strip()
	x[m_name] = cat_list

sim = {}
for movieName in x:
    if watchedMovies[1][1] != movieName:
        numer = len(set(user_cat).intersection(set(x[movieName])))
        denom = len(set(user_cat).union(set(x[movieName])))
        dist = numer/denom
        if dist != 0.0:
            sim[movieName] = dist

rec = []
for i in range(len(all_movies)):
	for key in sim:
		if all_movies[i][1] == key:
			rec.append(all_movies[i])

def index(req):
    data = {"action":actionMovies,
    "comedy":comedyMovies,
    "horror":horrorMovies,"adventure":adventureMovies,"recent":watchedMovies,
    "rec":rec}
    return render(req,"index.html",context={"data":data})

def detail(req,pk):
    query = "select * from movies where m_id = %s"
    cursor.execute(query, (pk))
    data = cursor.fetchall()
    print(data)
    return render(req,'details.html',context={"data":data})
