title: Contrebalancement
hash: f746c6dcc8ded61b700e84340fafff7a9ab6a1c217365d1ff9b97ab344438cd2
locale: fr
language: French

La contrebalancement est une méthode pour éliminer les facteurs de confusion d'une expérience en proposant des tâches légèrement différentes pour différents groupes de participants. Cela semble abstrait, alors examinons deux exemples.

[TOC]

### Exemple 1 : Contrebalancement de la règle de réponse

Prenons une expérience de décision lexicale dans laquelle les participants classent les mots en verbes en appuyant sur 'z' avec leur main gauche, ou en noms en appuyant sur 'm' avec leur main droite. Ce plan a un problème : si vous constatez que les participants répondent plus rapidement aux noms qu'aux verbes, cela pourrait être parce que les noms sont traités plus rapidement que les verbes, ou parce que les participants répondent plus rapidement avec leur main droite qu'avec leur main gauche. Vous pouvez résoudre ce problème en contrebalançant la règle de réponse.

Pour un nombre pair de participants :

- verbe → z
- nom → m

Pour un nombre impair de participants :

- verbe → m
- nom → z

### Exemple 2 : Rotation des conditions de stimulus

Prenons une expérience d'amorçage masqué dans laquelle les participants lisent à haute voix des mots cibles. À chaque essai, le mot cible est précédé par l'un des trois types de mots d'amorçage :

- Un amorce non liée, par exemple amorcer avec 'baie' pour la cible 'maison'.
- Une amorce orthographiquement liée, par exemple amorcer avec 'souris' pour la cible 'maison'.
- Une amorce sémantiquement liée, par exemple amorcer avec 'jardin' pour la cible 'maison'.

Pour éviter les effets de répétition, vous ne voulez montrer les mots cibles qu'une seule fois par participant. Par conséquent, vous créez trois ensembles différents de mots cibles, un pour chaque type d'amorce. Il s'agit d'un plan entre mots, qui a moins de puissance statistique qu'un plan intra-mots, dans lequel chaque mot cible se produit dans chaque condition. (Pour la même raison que les plans entre-sujets sont moins puissants que les plans intra-sujets.)

Vous pouvez utiliser le contrebalancement pour transformer cette expérience en un plan intra-mots en faisant « tourner » la condition dans laquelle chaque mot apparaît entre les participants. Nous avons trois conditions et donc trois groupes de participants :

- Participants 1, 4, 7, etc.
    - Mot A en condition 1
    - Mot B en condition 2
    - Mot C en condition 3
- Participants 2, 5, 8, etc.
    - Mot A en condition 2
    - Mot B en condition 3
    - Mot C en condition 1
- Participants 3, 6, 9, etc.
    - Mot A en condition 3
    - Mot B en condition 1
    - Mot C en condition 2

## Mise en œuvre du contrebalancement

### En utilisant le numéro de sujet

Lorsque vous exécutez une expérience dans OpenSesame sur le bureau, on vous demande un numéro de sujet. Lorsque vous exécutez une expérience en ligne, un numéro de sujet est sélectionné au hasard dans la liste des numéros de sujet possibles que vous avez spécifiés dans l'[extension OSWeb](%url:osweb). (Cela signifie que pour les expériences en ligne, vous ne pouvez pas garantir que le nombre de participants est exactement égal pour les différentes conditions que vous souhaitez contrebalancer, du moins pas si vous comptez sur le numéro de sujet.)

Ce numéro de sujet est disponible sous la forme de la variable expérimentale `subject_nr`. De plus, la variable expérimentale `subject_parity` a la valeur "impair" ou "pair", selon que le numéro de sujet est impair ou pair. Maintenant, disons que vous voulez contrebalancer la règle de réponse comme dans l'exemple 1, vous pouvez ajouter le SCRIPT_EN_LIGNE suivant au début de l'expérience.

```python
if subject_parity == 'odd':
    verb_response = 'z'
    noun_response = 'm'
else:
    verb_response = 'm'
    noun_response = 'z'
```

Ou, lors de la création d'une expérience OSWeb, ajoutez le INLINE_JAVASCRIPT suivant au début de l'expérience :

```javascript
if (subject_parity === 'odd') {
    verb_response = 'z'
    noun_response = 'm'
} else {
    verb_response = 'm'
    noun_response = 'z'
}
```

Maintenant, dans votre *block_loop*, au lieu de définir `correct_response` sur une valeur fixe, vous le définissez sur une variable : `{verb_response}` ou `{noun_response}`. Vous pouvez jeter un coup d'œil à l'exemple de *tâche de décision lexicale* pour voir comment cela fonctionne (Menu -> Outils -> Expériences d'exemple).


### En utilisant les données de session Batch (JATOS et OSWeb uniquement)

Lors de l'exécution d'une expérience OSWeb hébergée sur JATOS, vous pouvez utiliser les [Données de Session de Lot](https://www.jatos.org/jatos.js-Reference.html#functions-to-access-the-batch-session). Il s'agit de données partagées entre toutes les sessions expérimentales faisant partie du même lot de travailleurs. Vous pouvez donc utiliser ces données pour définir une liste de conditions à répartir entre les participants. Au début de chaque session expérimentale, une condition est retirée de cette liste et utilisée pour la session en cours. Il s'agit de la manière la plus sophistiquée de mettre en œuvre le contrebalancement pour les expériences OSWeb hébergées sur JATOS.

Vous pouvez télécharger un modèle d'expérience ici :

- %static:attachments/counterbalancing-osweb-jatos.osexp%

Lors de l'exécution sur JATOS, l'expérience récupère une seule condition à partir des Données de Session de Lot (voir ci-dessous) et l'enregistre en tant que variable expérimentale `condition`. Lors d'un test, `condition` est définie sur une valeur par défaut spécifiée à la fin de *init_condition*.

L'expérience elle-même doit être mise en œuvre dans la SEQUENCE *experiment*, qui dans le modèle ne contient que l'élément SKETCHPAD *show_condition* (voir %FigCounterbalancingOSWebJATOS).

%--
figure:
    source: counterbalancing-osweb-jatos.png
    id: FigCounterbalancingOSWebJATOS
    caption: |
        La zone d'aperçu du modèle d'expérience pour mettre en œuvre le contrebalancement avec JATOS Batch Session Data.
--%

Lors de l'importation de l'expérience dans JATOS, toutes les conditions doivent être spécifiées dans les Données de Session de Lot sous forme de liste `pending` (sous Worker & Batch Manager; voir %FigBatchSessionData). Chaque condition de `pending` correspond à une seule session expérimentale ; ainsi, si la condition `a` doit être utilisée pour deux sessions expérimentales, alors `a` doit apparaître deux fois dans la liste `pending`. Les conditions sont utilisées dans l'ordre dans lequel elles sont définies.

%--
figure:
    source: batch-session-data.png
    id: FigBatchSessionData
    caption: |
        Les conditions doivent être spécifiées dans les Données de Session de Lot dans JATOS.
--%

Au début d'une session expérimentale, une seule condition est déplacée de `pending` à `started`. (Lorsque la liste `pending` est vide, le participant est informé qu'il ne peut plus participer à l'expérience.) À la fin de la session expérimentale, la condition est ajoutée à la liste `finished`.

Pour rendre cela plus concret, disons que vous avez défini les Données de Session de Lot comme indiqué dans %FigBatchSessionData. Ensuite, quatre sessions expérimentales sont lancées, mais la deuxième session expérimentale, avec la condition `a`, ne se termine jamais, par exemple parce que le participant ferme le navigateur à mi-parcours de l'expérience. Les Données de Session de Lot ressembleront alors à celles de %FigBatchSessionAfter :

%--
figure:
    source: batch-session-data-after.png
    id: FigBatchSessionAfter
    caption: |
        Les Données de Session de Lot après que toutes les conditions ont été consommées. Une session, avec la condition `a`, n'a jamais été terminée.
--%

Vous pouvez constater à partir des Données de Session de Lot qu'une session expérimentale a commencé avec la condition `a` mais ne s'est jamais terminée. Pour néanmoins recueillir une session expérimentale avec cette condition, vous devez ajouter manuellement un nouveau `a` à la liste `pending` et collecter une nouvelle session.