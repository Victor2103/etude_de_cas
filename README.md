# Un moteur de recherche des images avec des requêtes textuelles.

* Utilisation de [fiftyone](https://docs.voxel51.com/) pour afficher les données.
* Dataset intégré : [coco-2017](https://cocodataset.org/), [food-101](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/).
* Modèle utilisé : [CLIP](https://github.com/openai/CLIP).
* Mots clés : Classifiction zéro-shot, Moteur de recherche, Similarité.

*******

### Sommaire

- [Installation](#installation)
- [Example](#Example)

*******

## Installation

### Pré-requis 
[Python 3](https://www.python.org/), [pip](https://pip.pypa.io/en/stable/) et [Mongodb](https://www.mongodb.com/).

>recommandation : [Environnements virtuels](https://docs.python.org/3/library/venv.html)

1. Récupérer le repos
```
git clone https://github.com/Victor2103/etude_de_cas.git && cd etude_de_cas
```

2. Créer l'environnement virtuel (optionel)
```
python3 -m venv .env && source .env/bin/activate
```

3. Installer les librairies
```
pip install -r requirements.txt
```

4. lancer l'application
* COCO (plus léger et rapide) environ 15 min pour lancer l'app en CPU only.
```
python3 source/app_coco.py
```

* Food 101 (plus lourd et long) GPU fortement recommandé.
```
python3 source/app_food.py
```

5. Vous pouvez maintenant accéder à http://localhost:5151


## Example

1. Recherche wilds animals
![Search wild animals](docs/search%20wild%20animals.png)

2. Recheche furniture
![Search furniture](docs/search%20furniture.png)

