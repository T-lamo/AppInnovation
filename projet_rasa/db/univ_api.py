import requests
import json

class API:
    def __init__(self):

        self.salle_disponible = json.loads(requests.get('https://edt-api.univ-avignon.fr/app.php/api/salles/disponibilite').text)['results']

    def getSalle(self):
        print(self.salle_disponible)

    def getSalleDispoParHeure(self, site="CERI",duree=3,debut="10.30", date="2022-11-17"):
        return json.loads(requests.get(f'https://edt-api.univ-avignon.fr/app.php/api/salles/disponibilite?site={site}&duree={duree}&debut={debut}&date={date}').text)['results']



if __name__ == "__main__":
    print(API().getSalleDispoParHeure())
    