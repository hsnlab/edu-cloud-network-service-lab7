import os

# API params
PATH_LAST_PROCESSED = "./data/last_processed.json"
MAX_LIMIT = 100
MAX_OFFSET = 10000

# We have three parameters in the URL:
# 1. MAX_LIMIT: the maximum number of records to be returned by the API
# 2. date_publication: the date from which we want to get the data
# 3. offset: the index of the first result
URL_API = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/rappelconso-v2-gtin-espaces/records?limit={}&where=date_publication%20%3E%20'{}'&order_by=date_publication%20ASC&offset={}"
URL_API = URL_API.format(MAX_LIMIT, "{}", "{}")

# POSTGRES PARAMS
user_name = os.getenv("POSTGRES_DOCKER_USER", "localhost")
POSTGRES_URL = f"jdbc:postgresql://{user_name}:5432/postgres"
POSTGRES_PROPERTIES = {
    "user": "postgres",
    "password": os.getenv("POSTGRES_PASSWORD"),
    "driver": "org.postgresql.Driver",
}

NEW_COLUMNS = [
    "risques_pour_le_consommateur",
    "recommandations_sante",
    # "date_debut_commercialisation",
    # "date_fin_commercialisation",
    "informations_complementaires",
]

COLUMNS_TO_NORMALIZE = [
    "categorie_produit",
    "sous_categorie_produit",
    "marque_produit",
    "modeles_ou_references",
    # "identification_produits",
    "conditionnements",
    "temperature_conservation",
    "zone_geographique_de_vente",
    "distributeurs",
    "motif_rappel",
    "numero_contact",
    "modalites_de_compensation",
]

COLUMNS_TO_KEEP = [
    "numero_fiche",
    "liens_vers_les_images",
    "lien_vers_la_liste_des_produits",
    "lien_vers_la_liste_des_distributeurs",
    "lien_vers_affichette_pdf",
    "lien_vers_la_fiche_rappel",
    "date_publication",
    "date_debut_commercialisation",
    "date_date_fin_commercialisation",
    "date_de_fin_de_la_procedure_de_rappel",
]
DB_FIELDS = COLUMNS_TO_KEEP + COLUMNS_TO_NORMALIZE + NEW_COLUMNS
