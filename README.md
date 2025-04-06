Dashboard Bitcoin - Projet Git & Linux

Ce projet consiste à créer un dashboard web interactif en Python (Dash) qui affiche le prix du Bitcoin (en EUR), scrapé automatiquement toutes les minutes grâce à un script Bash, avec un rapport quotidien généré à 20h. Le tout est hébergé sur une VM Linux et versionné sur GitHub.

---

## 📦 Structure du projet

projet_git/ ├── app.py # Dashboard Dash en Python ├── scraper.sh # Script Bash de scraping des données ├── data.csv # Données scrappées (timestamp, prix) ├── daily_report.sh # Script Bash de rapport journalier ├── rapport_YYYY-MM-DD.txt # Rapport généré chaque jour à 20h ├── README.md # Documentation du projet


---

## 🚀 Objectifs pédagogiques

- Utilisation conjointe de Bash, Python et Git
- Web scraping en ligne de commande
- Manipulation de données avec `pandas`
- Création de dashboard interactif avec `Dash`
- Automatisation via `cron`
- Déploiement sur une VM Linux

---

## ⚙️ Installation

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/tonuser/tonrepo.git
   cd tonrepo

    Installer les dépendances Python :

    pip3 install dash pandas plotly --break-system-packages

📈 Lancer le dashboard

Dans le terminal :

python3 app.py

Accéder à l'interface :

    Depuis la VM : http://127.0.0.1:8050

    Depuis l’hôte (si redirection NAT activée) : http://localhost:8050

🔁 Automatisation (cron)
1. Scraping toutes les minutes

Ouvrir crontab :

crontab -e

Ajouter :

* * * * * /bin/bash /home/frank/projet_git/scraper.sh

2. Rapport quotidien à 20h

Toujours dans crontab -e, ajouter :

0 20 * * * /bin/bash /home/frank/projet_git/daily_report.sh

🧾 Rapport quotidien

Chaque jour à 20h, un fichier rapport_YYYY-MM-DD.txt est généré avec :

    Moyenne du jour

    Min / Max

    Volatilité (écart-type)

👤 Auteurs

    Leslie NJOUKOUE

    Sami MEKKI
