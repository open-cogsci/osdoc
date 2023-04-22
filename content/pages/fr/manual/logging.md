title: Enregistrement et lecture de fichiers de données
hash: 6c081bb9571ecf270fcbd02104d88319bf6044245745b621d549cbc38c34e370
locale: fr
language: French

Vérifiez toujours trois fois si vos données ont été correctement enregistrées avant d'exécuter votre expérience !
{: .page-notification}

[TOC]


## Utilisation de l'élément LOGGER

OpenSesame ne consignera pas automatiquement les données. Vous devez plutôt insérer un élément LOGGER, généralement à la fin de votre séquence d'essai.

%--
figure:
 id: FigLogger
 source: logger.png
 caption: |
  L'élément LOGGER.
--%

La manière la plus simple d'utiliser LOGGER est de laisser l'option "Enregistrer automatiquement toutes les variables" activée. Ainsi, toutes les variables que OpenSesame connaît seront écrites dans le fichier journal, à l'exception de celles qui sont explicitement exclues (voir ci-dessous).

Vous pouvez explicitement *inclure* les variables que vous souhaitez consigner. La raison principale de le faire est lorsque certaines variables sont manquantes (parce que OpenSesame ne les a pas détectées automatiquement) ou si vous désactivez l'option "Enregistrer automatiquement toutes les variables".

Vous pouvez également explicitement exclure certaines variables du fichier journal. La raison principale de le faire est de garder les fichiers journaux propres en excluant les variables généralement non utiles.

En général, vous devez créer un seul élément LOGGER et réutiliser LOGGER à différents endroits de votre expérience si nécessaire (c'est-à-dire utiliser des copies liées du même élément LOGGER). Si vous créez plusieurs LOGGER (plutôt que d'utiliser un seul LOGGER plusieurs fois), ils écriront tous dans le même fichier journal, et le résultat sera un désordre!

## Utilisation de script Python inline

Vous pouvez écrire dans le fichier journal en utilisant l'objet `log` :

~~~ .python
log.write('Ceci sera écrit dans le fichier journal!')
~~~

Pour plus d'informations, voir :

- %link:log%

En règle générale, vous ne devez pas écrire directement dans le fichier journal et utiliser un élément LOGGER en même temps ; cela entraînera des fichiers journaux désordonnés.

## Format des fichiers de données

Si vous avez utilisé l'élément LOGGER standard, les fichiers de données sont au format suivant (simplement csv standard) :

- texte brut
- séparés par des virgules
- entre guillemets doubles (les guillemets doubles littéraux sont échappés avec des barres obliques inverses)
- fins de ligne de style Unix
- encodé en UTF-8
- noms de colonnes sur la première ligne

## Lecture et traitement des fichiers de données

### En Python avec pandas ou DataMatrix

En Python, vous pouvez utiliser [pandas](http://pandas.pydata.org/) pour lire les fichiers csv.

```python
import pandas
df = pandas.read_csv('sujet-1.csv')
print(df)
```

Ou [DataMatrix](https://datamatrix.cogsci.nl/):

```python
from datamatrix import io
dm = io.readtxt('sujet-1.csv')
print(dm)
```

### En R

En R, vous pouvez simplement utiliser la fonction `read.csv()` pour lire un fichier de données unique.

~~~ .R
df = read.csv('sujet-1.csv', encoding = 'UTF-8')
head(df)
~~~

De plus, vous pouvez utiliser la fonction `read_opensesame()` du package [readbulk](https://github.com/pascalkieslich/readbulk) pour facilement lire et fusionner plusieurs fichiers de données en un seul grand dataframe. Le package est disponible sur CRAN et peut être installé via `install.packages('readbulk')`.

~~~ .R
# Lire et fusionner tous les fichiers de données stockés dans le dossier 'raw_data'
library(readbulk)
df = read_opensesame('raw_data')
~~~

### Dans JASP

[JASP](http://jasp-stats.org/), un logiciel de statistiques open source, ouvre directement les fichiers csv.

### Dans LibreOffice Calc

Si vous ouvrez un fichier csv dans LibreOffice Calc, vous devez indiquer le format de données exact, comme indiqué dans %FigLibreOffice. (Les paramètres par défaut sont souvent corrects.)

%--
figure:
 source: libreoffice.png
 id: FigLibreOffice
--%

### Dans Microsoft Excel

Dans Microsoft Excel, vous devez utiliser l'Assistant d'importation de texte.

### Fusion de plusieurs fichiers de données en un seul grand fichier

Pour certaines utilisations, comme l'utilisation de tables croisées dynamiques, il peut être pratique de fusionner tous les fichiers de données en un seul grand fichier. Avec Python DataMatrix, vous pouvez le faire avec le script suivant :

```python
import os
from datamatrix import DataMatrix, io, operations as ops

# Changez ceci pour le dossier contenant les fichiers .csv
SRC_FOLDER = 'student_data'
# Changez ceci en une liste de noms de colonnes que vous souhaitez conserver
COLUMNS_TO_KEEP = [
    'RT_search',
    'load',
    'memory_resp'
]


dm = DataMatrix()
for basename in os.listdir(SRC_FOLDER):
    path = os.path.join(SRC_FOLDER, basename)
    print('Lecture de {}'.format(path))
    dm <<= ops.keep_only(io.readtxt(path), *COLUMNS_TO_KEEP)
io.writetxt(dm, 'donnees-fusionnees.csv')
```


## Enregistrement dans OSWeb

Lorsque vous exécutez une expérience dans un navigateur avec OSWeb, l'enregistrement fonctionne différemment de lorsque vous exécutez une expérience sur le bureau.

Plus précisément, lorsque vous lancez une expérience OSWeb directement à partir de OpenSesame, le fichier journal est téléchargé à la fin de l'expérience. Ce fichier journal est au format `.json`. Lorsque vous lancez une expérience OSWeb à partir de JATOS, il n'y a pas de fichier journal à proprement parler, mais plutôt toutes les données sont envoyées à JATOS à partir duquel elles peuvent être téléchargées.

Voir aussi :

- %link:manuel/osweb/workflow%



[libreoffice]: http://www.libreoffice.org/
[openoffice]: http://www.openoffice.org/
[gnumeric]: http://projects.gnome.org/gnumeric/
[log-func]: /python/inline-script/#inline_script.log
[codecs]: http://docs.python.org/2/library/codecs.html
[ppa]: https://launchpad.net/~smathot/+archive/cogscinl/