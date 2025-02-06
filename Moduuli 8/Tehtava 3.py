import mysql.connector
from geopy import distance
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='testaaja',
    password="j33s",
    autocommit=True,
    collation='utf8mb3_general_ci'
)
def lentokentan_koordinaatit(ICAO_koodi1, ICAO_koodi2):
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{ICAO_koodi1}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            lat1 = rivi[0]
            long1 = rivi[1]
    else:
        print("Virheellinen ICAO-koodi")
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{ICAO_koodi2}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            lat2 = rivi[0]
            long2 = rivi[1]
    else:
        print("Virheellinen ICAO-koodi")
    eka = (lat1, long1)
    toka = (lat2, long2)
    etaisyys = distance.distance(eka, toka).km
    print(f"Lentokenttien välilnen etäisyys on {etaisyys:.2f} kilometriä")
    return

ekalentkent = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
tokalentkent = input("Anna toisen lentokentän ICAO-koodi: ")
lentokentan_koordinaatit(ekalentkent, tokalentkent)






