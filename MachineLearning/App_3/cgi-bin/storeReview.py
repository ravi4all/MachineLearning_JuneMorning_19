import csv

def store(review,pred):
    data = {"review":review,"prediction":pred}
    with open('reviews.csv','a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.values())

def load():
    data = []
    with open('reviews.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    
    return data
