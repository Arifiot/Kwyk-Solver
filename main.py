import updater
from functions import int_input


version = "1.1"
print(f"\tKwyk Solver version {version}")

# Recherche d'une nouvelle mise à jour.
check_for_updates = True
if check_for_updates:
    update_info_url = "https://yougi3.github.io/Kwyk-Solver/update_info.json"
    update_info = updater.get_update_info(update_info_url)
    if update_info is not None:
        update_version = update_info["version"]
        if (update_version.strip() != version.strip()):
            print(f"\n! Une nouvelle mise à jour est disponible (version {update_version}).")
            if input("Souhaitez-vous la télécharger et l'installer ? (o/N) : ").strip().lower() == "o":
                updater.download_and_install(update_info["url"])
            else:
                print("Mise à jour ignorée.")

supported_ex = (260, 20110, 20116, 20118, 20119, 20124, 20128, 20129, 28036, 28037)

while True:
    print(f"\nExercices supportés : {str(supported_ex)[1:-1]}")
    ex = int_input("Entrez le numéro de l'exercice : ")
    if ex in supported_ex:
        print()
        exec(f"from solvers import solver_{ex}")
        exec(f"solver_{ex}.solve()")
    else:
        print("Exercice non supporté par le solveur.")
