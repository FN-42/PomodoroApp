import pandas as pd
from appendSession import appendSession

#TODO add function to append Session
sessionDataSet ={
    "Fach" :["Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken"],
    "Aufgabe" :["SQL Tutorial", "SQL Tutorial", "SQL Tutorial", "Vorlesungsfolien"],
    "Dauer" :[25, 25, 25, 25],
    "Datum" : ["11 Juli 2025","11 Juli 2025","11 Juli 2025", "12 Juli 2025"]}

sessionDataSet_var = pd.DataFrame(sessionDataSet)

print(sessionDataSet_var)

appendSession()
