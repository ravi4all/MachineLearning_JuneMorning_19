database = {
    "action" : ["baahubali","kgf","hulk","batman","superman","thor","avengers",
                "spiderman","aquaman","antman","baahubali 2"],
    "comedy" : ["zero","dhamaal","hera pheri","stree"],
    "horror" : ["annabelle","conjuring","the ring","stree","sixth sense"],
    "biopic" : ["ms dhoni","sanju","mary kom"],
    "thriller" : ["annabelle","conjuring","sixth sense","seven"]
    }

user_1 = {"baahubali","zero","kgf","hulk","avengers","dhamaal","ms dhoni",
        "annabelle","conjuring","sanju","sixth sense","stree"}

user_2 = {"avengers","dhamaal","ms dhoni","annabelle","conjuring","stree",
          "superman","mary kom","thor"}

sim = user_1.intersection(user_2)
score = {}
for key in database:
    j = len(sim.intersection(database[key])) / len(sim.union(database[key]))
    score[key] = round(j*100,2)
print(score)
d = user_1 - user_2
print(d)
cat = max(score.items(), key=lambda i : i[1])[0]
for movie in database[cat]:
    if movie in d:
        print("Recommended",movie)
