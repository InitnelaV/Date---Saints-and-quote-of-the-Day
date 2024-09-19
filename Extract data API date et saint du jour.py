import time
import requests

# Variables date - jour - heure - mois
t = time.localtime(time.time())
day_of_week = t.tm_wday
day = t.tm_mday
month = t.tm_mon

# Messages du jour 0: lundi => 6: dimanche
messages = {
    0: "Lundi: I hate Mondays - Garfield ",
    1: "Mardi: Un homme qui a épousé une flamme devient son mardi",
    2: "Mercredi: Fête hebdomadaire de la bascule à 12h pétantes! ",
    3: "Jeudi: #TittyTuesday!",
    4: "Vendredi: Dernière ligne droite ensuite c'est ravioli",
    5: "Samedi: Youhou !!!",
    6: "Dimanche: Damn, c'est déjà la fin du week-end!"
}

# URL de l'API pour récupérer le saint/prénom du jour
url = f"https://nominis.cef.fr/json/nominis.php?type=saintdujour&json&jour={day}&mois={month}"

try:
    # Effectuer la requête HTTP
    response = requests.get(url)
    response.raise_for_status()  # Vérifier si la requête a réussi

    # Extraire les données JSON
    data = response.json()

    '''# débogage Disabled par defaut
    print("Données JSON reçues : ", data)'''

    # Récupérer les prénoms dans 'prenoms' -> 'majeurs'
    if 'prenoms' in data['response'] and 'majeurs' in data['response']['prenoms']:
        prenoms = list(data['response']['prenoms']['majeurs'].keys())  # Liste des prénoms
        saint_du_jour = ', '.join(prenoms)  # Convertir en chaîne de caractères
    else:
        saint_du_jour = "Pas de prénoms trouvés pour aujourd'hui"

except requests.exceptions.RequestException as e:
    # En cas d'erreur de requête HTTP
    saint_du_jour = "Erreur lors de la récupération des prénoms"

# Formatage du message avec l'heure, le message du jour, et les prénoms du jour
localtime = time.asctime(t)
str = f"Heure actuelle : {localtime}\n{messages[day_of_week]}\nPrénoms du jour : {saint_du_jour}"

# Affichage du message
print(str)
