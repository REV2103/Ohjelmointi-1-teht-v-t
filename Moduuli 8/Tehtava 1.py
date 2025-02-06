import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='testaaja',
    password='j33s',
    autocommit=True,
    collation='utf8mb3_general_ci'
)
def hae_lentokentta_ICAO_koodilla(ICAO_koodi):
    sql = f"SELECT name, municipality from airport where ident= '{ICAO_koodi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            print(f"Lentokentän nimi on {rivi[0]} ja sen sijaintikunta on {rivi[1]}")
    return
ICAO_koodi = input("Anna lentokentän ICAO-koodi: ")
hae_lentokentta_ICAO_koodilla(ICAO_koodi)

