import pandas as pd

sessionDataSet ={
    "Fach" :["Mehrrechner Datenbanken"],
    "Aufgabe" :["SQL Tutorial"],
    "Dauer" :[25],
    "Datum" : ["11 Juli 2025"]}

sessionDataSet_var = pd.DataFrame(sessionDataSet)

print(sessionDataSet_var)