database = {
    "action" : ["baahubali","kgf","hulk","batman","superman","thor","avengers",
                "spiderman","aquaman","antman","baahubali 2"],
    "comedy" : ["zero","dhamaal","hera pheri","stree"],
    "horror" : ["annabelle","conjuring","the ring","stree"],
    "biopic" : ["ms dhoni","sanju","mary kom"],
    "thriller" : ["annabelle","conjuring","sixth sense","seven"]
    }

user = {"baahubali","zero","kgf","hulk","avengers","dhamaal","ms dhoni",
        "annabelle","conjuring","sanju","sixth sense","stree","batman"}

#score = {"action":0,"comedy":0,"horror":0,"biopic":0,"thriller":0}
score = {}
'''
for key in database:
    s = len(user.intersection(database[key]))
    score[key] = s
'''

for key in database:
    j = len(user.intersection(database[key])) / len(user.union(database[key]))
    score[key] = round(j*100,2)
print(score)

cat = max(score.items(), key=lambda i : i[1])[0]
for movie in database[cat]:
    if movie not in user:
        print("Recommended :",movie)

