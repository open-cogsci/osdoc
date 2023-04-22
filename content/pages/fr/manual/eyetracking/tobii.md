title: Tobii
hash: 91075c11d390d9162057a382ddc27a006029b42c7c7c79882ad81ff5e90f4430
locale: fr
language: French

PyGaze offre un support *expérimental* pour les eye-trackers Tobii. Le paquet `tobii-research` peut être installé via `pip`, mais au moment de l'écriture, il nécessite une version spécifique de Python—et *quelle* version de Python il requiert varie d'une version à l'autre. Par conséquent, la première étape consiste à déterminer quelle version de Python vous avez besoin. Vous pouvez le faire en visitant `tobii-research` sur PyPi et en cliquant sur "Download files":

- <https://pypi.org/project/tobii-research/#files>

À partir des noms de fichiers, vous pouvez déterminer quelle version de Python vous avez besoin; par exemple, le `cp310` dans le nom
`tobii_research-1.10.2-cp310-cp310-win_amd64.whl` signifie que vous avez besoin de Python 3.10 (`cp` signifie C-Python).

Ensuite, installez OpenSesame dans un environnement Python de la version correcte (donc Python 3.10 pour la version 1.10.2 de `tobii-research` comme indiqué ci-dessus). Ceci est plus facilement réalisé en utilisant Anaconda, comme décrit [ici](%url:download%). Enfin, installez le paquet `tobii-research` dans cet environnement Python.

```
!pip install tobii-research
```


Pour plus d'informations, voir :

- %link:pygaze%
- <https://rapunzel.cogsci.nl/manual/environment/>
- <http://www.tobii.com/en/eye-tracking-research/global/>