import gzip
import csv
from decimal import getcontext, Decimal
#import MySQLdb

def main():
    print('Welcome to data tech interview 1')
    peliculas = loadBasicsFile('dataset/title.basics.tsv.gz', 'action')
    ratings = loadRatingsFile('dataset/title.ratings.tsv.gz')
    sum1 = dict()
    for r in ratings:
        anio = peliculas.get(r['tconst'], 3000)
        if anio != 3000:
            ratDesc = ""
            ratDesc = decodeRating(Decimal(r['averageRating']))
            prevCount = sum1.get((anio, ratDesc), 0)
            sum1.update({(anio, ratDesc): prevCount + 1})
    #print(sum1)

    ################ NO TESTEADO - DESDE ACA:
    #db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
    #cursor = db.cursor()
    #cursor.execute("DROP TABLE IF EXISTS data_tech_interview.`films_by_year`;")

    # Create table as per requirement
    #sql = """CREATE TABLE data_tech_interview.`films_by_year` (
    #`year` int(5) NOT NULL,
    #`rating` varchar(100) NOT NULL,
    #`count` varchar(100) DEFAULT NULL
    #) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

    #cursor.execute(sql)
    ################ NO TESTEADO - HASTA ACA.

    for (year, rate), value in sum1.items():
        print("year: " + year + ", rate: " + rate + ", cantidad: " + str(value))

        ################ NO TESTEADO - DESDE ACA:
        #valor = str(year) + ", '" + rate + "'," + str(value)

        #sql = """INSERT INTO data_tech_interview.`films_by_year`(year,
        #     rating, count)
        #     """ + " VALUES (" + valor + ")"
        #try:
        #   cursor.execute(sql)
        #   db.commit()
        #except:
        #   db.rollback()
        
    # disconnect from server
    #db.close()
    ################ NO TESTEADO - HASTA ACA.


def loadBasicsFile(archivo, genero):
    genre = genero.lower()
    peliculas = dict()
    with gzip.open(archivo, 'rb') as f:
        basics = csv.DictReader(f, dialect='excel-tab')
        for reg in basics:
            if (int(reg["startYear"].replace('\\N','0')) > 2013 and genre in reg["genres"].lower()):
                peliculas[reg['tconst']] = reg['startYear']
    f.close()
    return peliculas

def loadRatingsFile(archivo):
    with gzip.open(archivo, 'rb') as f:
        rats = csv.DictReader(f, dialect='excel-tab')
        ratings = []
        for reg in rats:
            ratings.append(reg)
    return ratings

def decodeRating(rint):
    if rint > 8:
        ratDesc = "excellent"
    elif rint > 7:
        ratDesc = "good"
    elif rint > 5:
        ratDesc = "acceptable"
    else:
        ratDesc = "regular"
    return ratDesc

if __name__ == "__main__":
    main()
