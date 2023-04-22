title: Création de formulaires personnalisés
hash: a87d6a87fa567e6e8d52bfd533cc60fb77b7e646afa3b49d05009bbe198d852f
locale: fr
language: French

## À propos des formulaires, des géométries et des widgets

Un formulaire est un ensemble de widgets (boutons, étiquettes, champs de saisie de texte, etc.) disposés dans une grille avec une géométrie particulière. Dans l'image ci-dessous, vous voyez un exemple d'un formulaire 2 (colonnes) × 3 (lignes). La géométrie d'un formulaire est simple et comprend les propriétés suivantes :

- *les marges* garantissent que les widgets ne touchent pas le bord de l'affichage. Vous pouvez avoir des marges différentes pour le haut, la droite, le bas et la gauche.
- *les espacements* garantissent que les widgets ne se touchent pas les uns les autres. L'espacement horizontal et vertical est le même.
- Il y a une ou plusieurs *lignes*, éventuellement de différentes tailles.
- Il y a une ou plusieurs *colonnes*, éventuellement de différentes tailles.

%--
figure:
 id: FigGeometry
 source: geometry.png
 caption: Un schéma des géométries de FORMULAIRE.
--%

Bien sûr, un formulaire vide n'est pas amusant. Ajoutons donc les widgets suivants pour créer un formulaire de question simple :

- Une `étiquette` qui s'étend sur les deux colonnes de la rangée supérieure. Nous utilisons cette étiquette pour donner un titre au formulaire.
- Une autre `étiquette` qui s'étend sur les deux colonnes de la rangée du milieu. Cette étiquette contient la question réelle.
- Un `bouton` dans la zone de widget en bas à droite. Ce bouton permet à l'utilisateur de donner la réponse de 0,05 $.
- Un autre `bouton` dans la zone de widget en bas à gauche. Ce bouton permet à l'utilisateur de donner la réponse de 0,10 $.

%--
figure:
 id: FigSchematicExample1
 source: schematic-example1.png
 caption: Un exemple schématique de FORMULAIRE.
--%

Les images ci-dessus sont des exemples schématiques. À quoi ressemble réellement ce formulaire dans OpenSesame dépend de vos paramètres (notamment votre police et vos couleurs), mais cela peut ressembler à ceci :

%--
figure:
 id: FigExample1
 source: example1.png
 caption: Un exemple de FORMULAIRE.
--%

## Créer des formulaires personnalisés

Il y a deux façons de créer des formulaires personnalisés. Vous pouvez :

- Utiliser l'élément FORM_BASE et spécifier votre formulaire à l'aide du script OpenSesame.
- Utiliser Python dans un élément INLINE_SCRIPT. La méthode Python est légèrement plus flexible, mais pour la plupart des objectifs, les deux méthodes peuvent être utilisées.

### Créer des formulaires en utilisant le script OpenSesame

Nous allons créer le formulaire décrit ci-dessus en utilisant le script OpenSesame. Tout d'abord, faites glisser le plugin FORM_BASE dans votre expérience. Cliquez sur l'élément créé pour ouvrir son onglet. Ensuite, cliquez sur le bouton "Modifier le script" (avec l'icône du terminal), en haut à droite de la zone des onglets. Cela ouvrira l'éditeur de script. Entrez le script suivant pour générer le formulaire décrit ci-dessus (voir les commentaires pour les explications).

~~~
# Les marges sont définies comme "haut;droite;bas;gauche". Chaque valeur correspond à une
# marge en pixels.
set margins "50;100;50;100"
# L'espacement est simplement une valeur en pixels.
set spacing "25"
# Les tailles des lignes sont relatives. "1;2;1" signifie qu'il y a trois lignes,
# où la ligne du milieu est deux fois plus grande que les lignes du bas et du haut. Donc, "1;2;1"
# signifie exactement la même chose que "3;6;3". Veuillez noter que "3" ne signifie pas
# qu'il y a trois lignes de même taille (mais "1;1;1" le fait).
set rows "1;2;1"
# Les colonnes sont définies de la même manière. "1;1" signifie simplement qu'il y
# a deux colonnes de même taille.
set cols "1;1"
# Les widgets sont définis comme suit :
# widget [colonne] [ligne] [largeur de colonne] [hauteur de ligne] [type de widget] [mots-clés]
#
# Les colonnes et les lignes commencent à compter à 0. Si vous ne voulez pas que votre widget
# s'étende sur plusieurs colonnes et lignes, il vous suffit de définir la largeur et la hauteur de la ligne à 1.
widget 0 0 2 1 label text="Question"
widget 0 1 2 1 label center="no" text="Une batte et une balle de baseball coûtent ensemble 1,10 $. La batte coûte un dollar de plus que la balle. Combien coûte la balle ?"
widget 0 2 1 1 button text="0,10 $"
widget 1 2 1 1 button text="0,05 $"
~~~

### Créer des formulaires en utilisant un script Python en ligne

Le même formulaire peut être créé à l'aide d'un INLINE_SCRIPT et un peu de code Python. Vous remarquerez que le code Python ressemble un peu au script OpenSesame présenté ci-dessus. Ce n'est pas étonnant : le plugin FORM_BASE traduit essentiellement le script OpenSesame en code Python.

Tout d'abord, faites glisser un INLINE_SCRIPT dans votre expérience. Sélectionnez l'élément nouvellement créé pour ouvrir son onglet et ajoutez le script suivant dans la phase d'exécution de l'élément INLINE_SCRIPT (voir les commentaires pour les explications).

~~~ .python
# Créer un formulaire
form = Form(
    cols=[1,1], rows=[1,2,1],
    margins=(50,100,50,100), spacing=25
)
# Créer quatre widgets
labelTitle = Label(text='Question')
labelQuestion = Label(
    text='Une chauve-souris et une balle de baseball coûtent ensemble 1,10 $. La chauve-souris coûte un dollar de plus que la balle. Combien coûte la balle ?',
    center=False
)
button5cts = Button(text='0,05 $')
button10cts = Button(text='0,10 $')
# Ajouter les widgets au formulaire. La position dans le formulaire est indiquée sous la forme
# d'un tuple (colonne, ligne).
form.set_widget(labelTitle, (0,0), colspan=2)
form.set_widget(labelQuestion, (0,1), colspan=2)
form.set_widget(button5cts, (0,2))
form.set_widget(button10cts, (1,2))
# Exécuter le formulaire! Dans ce cas, le formulaire renverra le texte du bouton
# qui a été cliqué. C'est une façon d'obtenir une valeur de retour du formulaire. Une autre façon
# est d'utiliser le mot-clé 'var', pris en charge par certains des widgets.
button_clicked = form._exec()
~~~

Si vous voulez qu'un widget spécifique reçoive le focus lorsque le formulaire est exécuté, vous pouvez utiliser le mot-clé `focus_wiget` :

~~~ .python
button_clicked = form._exec(focus_widget=button5cts)
~~~

### Formulaires non interactifs

Habituellement, un formulaire aura un champ de saisie, un bouton ou un autre élément interactif. Cependant, vous pouvez également utiliser des formulaires sans avoir d'élément interactif. Pour ce faire dans un script OpenSesame, définissez `only_render` sur "yes" :

```python
set only_render yes
```

Pour ce faire dans un script Python INLINE_SCRIPT, vous appelez `form.render()`, au lieu de `form._exec()`.

### Thèmes

Les formulaires prennent en charge le thème. Actuellement, deux thèmes sont disponibles: 'gray' et 'plain'. Le thème 'gray' est celui par défaut. Bien que le thème 'gray' soit déjà assez clair, le thème 'plain' est encore plus basique. Vous pouvez choisir un thème comme celui-ci dans OpenSesame script:

```python
set theme plain
```

Et en utilisant le mot-clé `theme` dans un script Python en ligne:

~~~ .python
form = Form(theme='plain')
~~~

### Widgets et mots-clés disponibles

Pour une liste des widgets et mots-clés disponibles, consultez:

- %link:manual/forms/widgets%

### Valider la saisie

Pour voir comment vous pouvez valider la saisie d'un formulaire, consultez:

- %link:manual/forms/validation%

## Autre exemple

Le script OpenSesame suivant (dans un plugin FORM_BASE) produira un questionnaire de trois échelles d'évaluation plus un bouton suivant:

```python
set rows "1;1;1;1;1"
set cols "1;1"
widget 0 0 2 1 label text="Indiquez dans quelle mesure vous êtes d'accord avec les affirmations suivantes"
widget 0 1 1 1 label center="no" text="Les formulaires sont faciles"
widget 1 1 1 1 rating_scale var="question1" nodes="D'accord;Ne sais pas;Pas d'accord"
widget 0 2 1 1 label center="no" text="J'aime les données"
widget 1 2 1 1 rating_scale var="question2" nodes="D'accord;Ne sais pas;Pas d'accord"
widget 0 3 1 1 label center="no" text="J'aime les questionnaires"
widget 1 3 1 1 rating_scale var="question3" nodes="D'accord;Ne sais pas;Pas d'accord"
widget 0 4 2 1 button text="Suivant"
```

Le script Python en ligne suivant produira le même questionnaire.

~~~ .python
form = Form(cols=[1,1], rows=[1,1,1,1,1])
title = Label(
    text="Indiquez dans quelle mesure vous êtes d'accord avec l'affirmation suivante"
)
question1 = Label(text='Les formulaires sont faciles', center=False)
question2 = Label(text="J'aime les données", center=False)
question3 = Label(text="J'aime les questionnaires", center=False)
ratingScale1 = RatingScale(
    var='question1',
    nodes=['D\'accord', "Ne sais pas", 'Pas d\'accord']
)
ratingScale2 = RatingScale(
    var='question2',
    nodes=['D\'accord', "Ne sais pas", 'Pas d\'accord']
)
ratingScale3 = RatingScale(var='question3',
    nodes=['D\'accord', "Ne sais pas", 'Pas d\'accord']
)
nextButton = Button(text='Suivant')
form.set_widget(title, (0, 0), colspan=2)
form.set_widget(question1, (0, 1))
form.set_widget(question2, (0, 2))
form.set_widget(question3, (0, 3))
form.set_widget(ratingScale1, (1, 1))
form.set_widget(ratingScale2, (1, 2))
form.set_widget(ratingScale3, (1, 3))
form.set_widget(nextButton, (0, 4), colspan=2)
form._exec()
~~~

Le formulaire résultant ressemble à ceci. (L'apparence exacte dépend de votre police, couleurs, etc.)

%--
figure :
 id: FigExample2
 source: example2.png
 caption: Un autre exemple de FORMULAIRE.
--%