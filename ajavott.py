#################################
#   Credit: Anette Mozessov     #
#################################
from datetime import date, datetime

def getStartingTime():
    return datetime.now()

def getSpentTime(algusaeg):
    loppaeg = datetime.now()
    return loppaeg - algusaeg

def writeToFile(kasutajanimi, aeg):
    with open("lahendamise_ajad.txt", "a") as file:
        tulemus = kasutajanimi + '|' +  str(aeg) + '|' + str(date.today()) + '\n'
        file.write(tulemus)