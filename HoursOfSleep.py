import csv 
import pandas as pd
import plotly.express as px
import numpy as np

def dataSource(data_path):
    cofeeInMl=[]
    hoursOfSleep=[]
    df = pd.read_csv(data_path)
    for i in df:
       
        cofeeInMl.append(float(i["Coffee in ml"]))
        hoursOfSleep.append(float(i["sleep in hours"]))

    return {"x":cofeeInMl,"y":hoursOfSleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("correlation between hours of sleeep and cofee in ml is:", correlation)

def setup():
    
    output =  dataSource("data.csv")
    findCorrelation(output)

setup()