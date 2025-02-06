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
def hae_lentokenttien_lukumaara(maakoodi):
    sql = f"select airport.type, count(*) from airport, country where airport.iso_country = country.iso_country and airport.iso_country= '{maakoodi}' group by type order by type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Valitsemassasi maassa on {rivi[1]} kpl {rivi[0]}")
    else:
        print("Virhellinen maakoodi")
    return
maakoodi = input("Anna kaksikirjaiminen maakoodi: ")
hae_lentokenttien_lukumaara(maakoodi)
