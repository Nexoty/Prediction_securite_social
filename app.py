import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Optimisation de l’analyse et du nettoyage des données
"""
#Extraction des donnees du
extraction_donnee =pd.read_csv('donnees_securite_sociale.csv')

#Nettoyage
#Suppression des doublons et des valeurs manquantes

#Eliminer les doublons
extraction_donnee.drop_duplicates(inplace=True)
#Eliminer les valeurs manquantes
extraction_donnee.fillna(method="ffill",inplace=True)

#Standartisation de l'heure et date
extraction_donnee['date_payment']=pd.to_datetime(extraction_donnee['date_payment'],errors='coerce')
donnee_matricielle=np.array(extraction_donnee)

tableau_frame = pd.DataFrame(extraction_donnee)

print(tableau_frame)

def pipeline_traitement(df):
    df=df.drop_duplicates()
    df=df.fillna(df.mean(numeric_only=True))
    return df

calcul_moyenne =pipeline_traitement(extraction_donnee)

#Graphique avec matplotlib

plt.figure(figsize=(10,5))
plt.plot(extraction_donnee['date_payment'],extraction_donnee['montant_declared'])
plt.title("Évolution du coût des prestations de sécurité sociale")
plt.xlabel("Date")
plt.ylabel("Cout")
plt.show()


