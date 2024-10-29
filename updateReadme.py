from datetime import datetime

# Calcul des jours restants avant la nouvelle année
today = datetime.now()
new_year = datetime(today.year + 1, 1, 1)
days_left = (new_year - today).days

# Met à jour le README
with open("README.md", "r") as file:
    content = file.readlines()

# Change la ligne qui contient le compte à rebours
content[0] = f"{days_left} days before new year!\n"

with open("README.md", "w") as file:
    file.writelines(content)
