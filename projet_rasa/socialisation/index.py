import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

class SociabilityQuestion():
    
    def __init__(self):
        pass

    def univInfo(self):
        url = "https://univ-avignon.fr/universite/presentation/"
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        text=text[text.find("Une des plus anciennes universités de France"):text.find("Chiffres clés")]
        text=text.replace("FranceIl","France. Il").strip()
        return text

    def univHeureAcceuil(self):
        url = "https://univ-avignon.fr/s-orienter/"
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        text=text[text.find("Horaires d'accueil :"):text.find("Plan d'accès")].lower()
        for day in ["lundi","mardi","mercredi","jeudi","vendredi"]:
            text=text.replace(day, f', {day}')
        text=text.replace("horaires d'accueil :", "").strip()[2:]
        
        return f"Voici l'horaire d'acceuil de l'université:  {text}"

    def ServiceAccompagement(self):
        url = "https://univ-avignon.fr/s-orienter/"
        return f"L'addresse du service d'accompagnement est: 74 rue Louis Pasteur - Case 9 84029 Avignon cedex 1, Bâtiment Nord / Niveau 0 Bureaux 0E02 à 0E10"

if __name__ == '__main__':
    social= SociabilityQuestion()
    print(social.ServiceAccompagement())
    pass

