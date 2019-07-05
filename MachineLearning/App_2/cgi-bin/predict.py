import cgi
import numpy as np
from sklearn.preprocessing import StandardScaler

form = cgi.FieldStorage()
bedroom = form.getvalue('bedrooms')
bathroom = form.getvalue('bathrooms')
area = form.getvalue('area')
waterfront = form.getvalue('waterfront')

b = np.array([-1.94571236e-16, -1.20610776e-01,  5.16206330e-02,  7.03696660e-01,1.89915143e-01])
X = np.array([1,bedroom,bathroom,area,waterfront])

sc = StandardScaler()
X = sc.fit_transform(X.reshape(-1,1))
X = X.T
pred = np.dot(X,b)
final_pred = sc.inverse_transform(pred)
print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h2>No of Bedrooms : {}</h2>
    <h2>No of Bathrooms : {}</h2>
    <h2>Area : {}</h2>
    <h2>Waterfront : {}</h2>
    <h2>Prediction is : {}</h2>
</body>
</html>
""".format(bedroom, bathroom,area,waterfront,final_pred[0]))