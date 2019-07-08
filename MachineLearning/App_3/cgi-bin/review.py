#!C:/Python37/python.exe
import cgi
from SentimentAnalysisLogistic import test
from storeReview import store, load

form = cgi.FieldStorage()
review = form.getvalue('msg')
pred = test(review)

store(review, pred)
data = load()

posCount = 0
negCount = 0
for i in range(len(data)):
    if data[i][1] == "Negative":
        negCount += 1
    else:
        posCount += 1

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">

      // Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

        // Create the data table.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Topping');
        data.addColumn('number', 'Slices');
        data.addRows([
          ['Positive', %s],
          ['Negative', %s],
        ]);

        // Set chart options
        var options = {'title':'Review Analysis',
                       'width':400,
                       'height':300};

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
</head>
<body>
    <h1>Prediction Analysis</h1>
    <div id="chart_div"></div>
"""%(posCount, negCount))

print("""<ul>""")
for i in range(len(data)):
    if data[i][1] == "Negative":
        color = "red"
    else:
        color = "green"
    print("""
        <li style='color:{};'>{}</li>
    """.format(color,data[i][0]))
print("</ul>")

print("""
</body>
</html>
""")