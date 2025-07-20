import pandas as pd
from appendSession import appendSession

#TODO add function to append Session
sessionDataSet ={
    "Fach" :["Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "Mehrrechner Datenbanken", "NOSQL", "NOSQL", "NOSQL"],
    "Aufgabe" :["SQL Tutorial", "SQL Tutorial", "SQL Tutorial", "Vorlesungsfolien", "Vorlesungsvideo", "Vorlesungsvideo ; SQL Tutorial", "SQL Tutorial", "SQL Tutorial", "Vorlesungsvideo", "Vorlesungsvideo", "Vorlesungsvideo", "Vorlesungsvideo", "SQL Tutorial", "Vorlesungsvideo", "Vorlesungsvideo", "Vorlesungsvideo", "Vorlesungsvideo", "Vorlesungsvideo", "Klausurvorbereitung mit Kommilitone", "Wiederholung Klausurvorbereitung", "Lots", "Lots", "Lots", "Wiederholung Klausurvorbereitung", "Vorlesungsvideo", "Vorlesungsvideo", "Vorlesungsvideo"],
    "Dauer" :[25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 120, 25, 25, 25, 25, 25, 25, 25, 25],
    "Datum" : ["11 Juli 2025","11 Juli 2025","11 Juli 2025", "12 Juli 2025", "14 Juli 2025", "14 Juli 2025", "14 Juli 2025", "15 Juli 2025", "15 Juli 2025", "15 Juli 2025", "15 Juli 2025", "15 Juli 2025", "16 Juli 2025", "16 Juli 2025", "16 Juli 2025", "17 Juli 2025", "17 Juli 2025", "17 Juli 2025", "17 Juli 2025", "17 Juli 2025", "18 Juli 2025", "18 Juli 2025", "18 Juli 2025", "18 Juli 2025", "20 Juli 2025", "20 Juli 2025", "20 Juli 2025"]}

sessionDataSet_var = pd.DataFrame(sessionDataSet)

print(sessionDataSet_var)

appendSession()
