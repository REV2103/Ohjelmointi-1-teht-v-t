from flask import Flask, Response
import json
app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        lukulista = [*range(2, 1000)]
        luku = float(luku)
        laskulista = []
        tilakoodi = 200
        for n in lukulista:
            if luku != n:
                lasku = (luku % n)
                laskulista.append(lasku)
        if 0 not in laskulista or luku == 1:
            isprime = True
        else:
            isprime = False
        vastaus = {
            "number": luku,
            "isprime": isprime,
            "status": tilakoodi,
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen luku"
        }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

