from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

dataUrl = "https://raw.githubusercontent.com/bookworm6/Data-Science-Final-Project/refs/heads/main/renderFiles/demographicsBySubject.csv"
demographicsBySubject = pd.read_csv(dataUrl)

averageDifferences = demographicsBySubject[demographicsBySubject["Race/Ethnicity"]=="all"].groupby(["Subject","Gender"])["percentDifference"].mean().reset_index()


#adding y values to divide scatter plot into 3 number lines
genderY = {"F":1,"M":0,"U":-1}
averageDifferences["y"] = averageDifferences['Gender'].apply(lambda x: genderY[x])

#plotting
#https://plotly.com/python-api-reference/generated/plotly.express.scatter
averageDiffNumberline = px.scatter(averageDifferences,"percentDifference","y",opacity=0.3,hover_name="Subject",color="Gender",hover_data={"y":False,"Gender":False,"percentDifference":False},title="Average Over/Under Representation of the Sexes across Subjects",labels={"Gender":"Sex","percentDifference":"percent under represented                          percent over represnted"}) #credit to AI overview
averageDiffNumberline.update_yaxes(visible=False) #credit to AI overview


app = Dash(__name__)
server = app.server
#setting layout. including the numberline graph above and a blank graph to be filled
app.layout = html.Div([
    dcc.Graph( id = "numberline",figure = averageDiffNumberline),
    dcc.Graph(id = "zoomin")
])

#creating callback
@app.callback(
    Output("zoomin","figure"),
    Input("numberline","clickData")
)
def update(clickData):
  if clickData is None:
    return px.line(title = "please click a point")
  subject = clickData["points"][0]["hovertext"]
  subjectDemographics = demographicsBySubject[demographicsBySubject["Subject"]==subject]
  graph = px.line(subjectDemographics, x="Term",y="percentDifference",color = "Gender", line_dash="Race/Ethnicity",title = f"Representation of the Sexes in {subject} over time",labels={"percentDifference":"percent under/over represented","Gender":"Sex"})
  for trace in graph.data: #credit to gemmini for helping me hide traces
    if "all" not in trace.name:
      trace.update(visible="legendonly")
  return graph