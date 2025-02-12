# FrenchOpenDataWebservices- merge_json.py

## Description

Le script `merge_json.py` fonctionne comme suit :

1. Il commence par définir un modèle JSON parent avec une structure spécifique. Ce modèle parent est initialisé avec les éléments suivants :
   - "title": Un titre qui inclut la date actuelle.
   - "ident": Une valeur d'identifiant unique.
   - "description": Une description (initialement vide).
   - "type": Un type ("folder").
   - "children": Une liste vide pour stocker les données JSON fusionnées.

2. Le script recueille ensuite tous les fichiers JSON d'entrée spécifiés. Ces fichiers JSON sont considérés comme les "enfants" qui seront fusionnés dans le modèle parent.

3. Pour chaque fichier JSON d'entrée, le script vérifie s'il existe. Si le fichier n'existe pas, il affiche un avertissement et passe au fichier suivant. Si le fichier existe, il le charge et ajoute son contenu à la liste des "enfants" dans le modèle parent.

4. Après avoir fusionné tous les fichiers JSON, le script écrit le modèle parent complet dans un fichier de sortie `config.json`.

5. Le fichier `config.json` résultant contient la fusion de tous les fichiers JSON d'entrée dans le format spécifié.

## Utilisation

```bash
python3 merge_to_json.py config.json *.yaml
```
