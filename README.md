# Kwyk Solver

Kwyk Solver est un solveur d'exercices pour le [site web Kwyk](https://www.kwyk.fr/).

Celui-ci est écrit en Python 3.8 et nécessite les modules complémentaires `numpy` et `requests`.

## Installation

### Téléchargement du programme

Rendez-vous dans l'onglet 'Releases' de cette page de projet et téléchargez la version la plus récente.

Celle-ci se présentera sous la forme d'un dossier compressé d'extension `.zip`.

Une fois téléchargé, pensez à décompresser le dossier ZIP.

### Installation de Python

Assurez-vous d'avoir installé au préalable Python 3.8 ou ultérieur. Si ce n'est pas encore le cas, rendez-vous sur le [site web officiel de Python](https://www.python.org/downloads/) et téléchargez la version la plus récente correspondant à votre système d'exploitation.

Lors de l'installation sur Windows, assuez-vous de cocher la case "Add Python 3.8 to PATH" sur la première page de l'installeur.

Une fois cette première terminée, ouvrez l'invite de commandes Windows (`cmd.exe`) ou le PowerShell. Sur macOS, ouvrez l'application Terminal.

Tapez la commande suivante : `python --version`

Si celle-ci vous retourne un numéro de version, comme par exemple `Python 3.8.3`, Python s'est installé avec succès et vous pouvez continuer la procédure. Si vous obtenez une erreur ou un autre message, n'hésitez pas à demander de l'aide en vous rendant dans l'onglet 'Issues' de cette page de projet.

### Installation des modules requis au fonctionnement du programme

#### Méthode 1

Si vous êtes sur macOS, passez à la deuxième méthode.

Sur Windows, rendez-vous dans le dossier contenant les fichiers du programme et exécutez le fichier nommé `Installation_Windows.cmd`.

Si celui-ci vous indique que les modules requis se sont correctement installés ou étaient déjà installés, vous pouvez continuer la suite de la procédure. Autrement, essayez la méthode 2.

#### Méthode 2

Sur Windows, ouvrez l'invite de commandes (`cmd.exe`) ou le PowerShell.

Sur macOS, ouvrez l'application Terminal.

Tapez les commandes suivantes :

- `python -m pip install numpy`
- `python -m pip install requests`

Si vous n'arrivez toujours pas à installer les modules requis au fonctionnement du programme, demandez de l'aide dans l'onglet 'Issues' de cette page de projet.

## Lancement du programme

Sur Windows, exécutez le fichier nommé `Kwyk_Solver_Windows.cmd`.

Sur macOS, ouvrez le fichier `main.py` avec l'application PythonLauncher.

## Utilisation du programme

Le programme vous propose une liste d'exercices pour lesquels des solveurs ont été écrits.

Tapez simplement le numéro de l'exercice que vous souhaitez résoudre et suivez les instructions à l'écran.

## Mises à jour du programme

Lorsqu'une mise à jour est disponible, le programme vous en avertira et vous proposera de la télécharger et de l'installer. Vous pouvez refuser la procédure en appuyant sur la touche `Entrée` ou l'accepter en appuyant sur la touche `o` puis `Entrée`.

## Rapports de bugs ou demandes d'aide

Pour tout rapport d'erreur ou demande d'aide, veuillez vous rendre dans l'onglet 'Issues' de cette page de projet.

## Collaborer au projet

Vous avez la possibilité de collaborer au projet en effectuant un *fork* du *repo* puis en proposant vos modifications grâce à une *pull request*.

### Ajouter le support d'un exercice

Pour ajouter le support d'un exercice, veillez à :

- Ajoutez le numéro de l'exercice en question à la liste `supported_ex` située dans le fichier `main.py` (toujours en restant dans les parenthèses !),
- Ajouter un fichier dans le dossier `solvers` nommé `solver_`(le numéro de l'exercice va ici)`.py`,
- Dans ce fichier, importez les modules nécessaires à sa conception (veuillez néanmoins à éviter de rajouter de nouvelles dépendances au programme),
- Dans ce fichier, à la suite de ces importations, créez une fonction `solve()`. Celle-ci contient toute la logique du solveur en passant de la récupération de données avec `input()` au traitement des données pour au final afficher les résultats de l'exercice avec `print()`.




Merci d'avoir lu ce petit pacé 😁
