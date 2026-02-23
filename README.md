# 🚴 Prédiction de la Disponibilité des Vélos en Libre-Service (Paris)

## 📌 Description du Projet
Ce projet de Data Science vise à prédire le taux de remplissage (`filling_rate`) des stations de vélos en libre-service à Paris. En utilisant des données géospatiales et temporelles, l'objectif est d'anticiper la disponibilité des vélos pour optimiser l'expérience utilisateur et la gestion de la flotte.

## 🗂️ Structure du Notebook
Le projet suit un pipeline Data Science complet, documenté étape par étape :

### 1. Contexte et Objectif
Définition de la problématique métier et mise en place du plan d'action (Pipeline).

### 2. Importation et Nettoyage des Données
- Traitement des valeurs manquantes et formatage des dates.
- Création de variables temporelles cycliques (sinus/cosinus des heures et jours).
- Ingénierie des caractéristiques : Création des "Lag Features" (Mémoire du réseau).

### 3. Analyse Exploratoire (EDA)
- **Matrice de Corrélation :** Compréhension des liens entre les variables.
- **Analyse et correction d'anomalies :** Nettoyage approfondi des valeurs aberrantes.
- **ACP (Analyse en Composantes Principales) :** Réduction de dimensionnalité et visualisation des clusters de stations.

### 4. Machine Learning (Modélisation)
L'entraînement des modèles a été divisé en deux approches distinctes pour comparer les performances avec et sans "fuite d'information temporelle" :
- **Approche 1 : Sans la variable `Filling_rate_H_minus_1`** (Véritable prédiction dans le futur).
  *Modèle gagnant : LightGBM optimisé par Cross-Validation (R² : ~68%).*
- **Approche 2 : Avec la variable `Filling_rate_H_minus_1`** (Prédiction à très court terme).

## 🚀 Améliorations en cours (Work in Progress)
Le projet est actuellement en phase d'évolution active. Voici les deux grands chantiers sur lesquels je travaille :

- [ ] 🌦️ **Intégration de la Météo :** Récupération et fusion de l'historique météorologique de Paris (précipitations, température) pour aider les modèles à comprendre les baisses soudaines d'utilisation.
- [ ] 🧠 **Deep Learning (PyTorch) :** Implémentation d'un réseau de neurones de type MLP (Multi-Layer Perceptron) avec le framework PyTorch pour challenger les performances de LightGBM.

## 🛠️ Technologies Utilisées
- **Langage :** Python
- **Manipulation de données :** Pandas, NumPy
- **Visualisation :** Matplotlib, Seaborn
- **Machine Learning :** Scikit-Learn, LightGBM, Random Forest, XGBoost
- **Deep Learning :** PyTorch (en cours)