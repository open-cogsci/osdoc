title: Création de formulaires personnalisés
hash: a7ba48cceefdfccdc42df16e4cfeb5980dcbd13a9a5b8516a328456704b5b400
locale: fr
language: French


## À propos des formulaires, des géométries et des widgets

Un formulaire est un ensemble de widgets (boutons, étiquettes, champs de saisie de texte, etc.) arrangés en grille avec une géométrie particulière. Dans l'image ci-dessous, vous voyez un exemple de formulaire de 2 (colonnes) × 3 (rangées). La géométrie d'un formulaire est simple et comprend les propriétés suivantes :

- Les *marges* assurent que les widgets ne touchent pas le bord de l'affichage. Vous pouvez avoir des marges différentes pour le haut, la droite, le bas et la gauche.
- L'*espacement* assure que les widgets ne se touchent pas entre eux. L'espacement horizontal et vertical est le même.
- Il y a une ou plusieurs *rangées*, éventuellement de tailles différentes.
- Il y a une ou plusieurs *colonnes*, éventuellement de tailles différentes.

figure:
 id: FigGeometry
 source: geometry.png
 caption: Schéma des géométries de FORMULAIRE.

Bien sûr, un formulaire vide n'est pas très amusant. Ajoutons donc les widgets suivants pour créer un formulaire de question simple :

- Une `label` qui s'étend sur les deux colonnes de la rangée supérieure. Nous utilisons cette étiquette pour donner un titre au formulaire.
- Une autre `label` qui s'étend sur les deux colonnes de la rangée du milieu. Cette étiquette contient la question proprement dite.
- Un `button` dans la zone de widget en bas à droite. Ce bouton permet à l'utilisateur de donner la réponse de $0.05.
- Un autre `button` dans la zone de widget en bas à gauche. Ce bouton permet à l'utilisateur de donner la réponse de $0.10.

figure:
 id: FigSchematicExample1
 source: schematic-example1.png
 caption: Exemple schématique de FORMULAIRE.

Les images ci-dessus sont des exemples schématiques. L'apparence réelle de ce formulaire dans OpenSesame dépendra de vos paramètres (notamment votre police et vos couleurs), mais il pourrait ressembler à ceci :

figure:
 id: FigExample1
 source: example1.png
 caption: Exemple de FORMULAIRE.

## Créer des formulaires personnalisés

Il y a deux manières de créer des formulaires personnalisés. Vous pouvez :

- Utiliser l'élément FORM_BASE et spécifier votre formulaire en utilisant le script OpenSesame.
- Utiliser du Python dans un élément INLINE_SCRIPT. La méthode Python est légèrement plus flexible, mais pour la plupart des utilisations, les deux méthodes peuvent être employées.

### Créer des formulaires en utilisant le script OpenSesame

Nous allons créer le formulaire décrit ci-dessus en utilisant le script OpenSesame. D'abord, faites glisser le plugin FORM_BASE dans votre expérience. Cliquez sur l'élément nouvellement créé pour ouvrir son onglet. Ensuite, cliquez sur le bouton 'Modifier le script' (avec l'icône du terminal), dans le coin supérieur droit de la zone des onglets. Cela ouvrira l'éditeur de script. Entrez le script suivant pour générer le formulaire décrit ci-dessus (voir les commentaires pour des explications).

~~~
# Les marges sont définies comme "haut;droite;bas;gauche". Chaque valeur correspond à une
# marge en pixels.
set margins "50;100;50;100"
# L'espacement est simplement une valeur en pixels.
set spacing "25"
# La taille des rangées est relative. "1;2;1" signifie qu'il y a trois rangées,
# où celle du milieu est deux fois plus grande que celles du haut et du bas. Ainsi, "1;2;1"
# signifie exactement la même chose que "3;6;3". Veuillez noter que "3" ne signifie pas
# qu'il y a trois rangées de la même taille (mais "1;1;1" le fait).
set rows "1;2;1"
# Les colonnes sont définies de la même manière. "1;1" signifie simplement qu'il y a
# deux colonnes de la même taille.
set cols "1;1"
# Les widgets sont définis comme suit :
# widget [colonne] [rangée] [étendue de la colonne] [étendue de la rangée] [type de widget] [mots-clés]
#
# Les colonnes et les rangées commencent à compter à partir de 0. Si vous ne souhaitez pas que votre widget
# s'étende sur plusieurs colonnes et rangées, vous définissez simplement l'étendue de la colonne et de la rangée à 1.
widget 0 0 2 1 label text="Question"
widget 0 1 2 1 label center="no" text="Une chauve-souris et une balle de baseball coûtent ensemble $1.10. La chauve-souris coûte un dollar de plus que la balle. Combien coûte la balle ?"
widget 0 2 1 1 button text="$0.10"
widget 1 2 1 1 button text="$0.05"
~~~

Si vous souhaitez qu'un widget spécifique reçoive le focus lorsque le formulaire est exécuté, vous pouvez appliquer le mot-clé `focus=yes` à l'un des widgets :

```
widget 0 0 1 1 text_input text="Texte initial" frame=yes center=no stub="Tapez ici …" return_accepts=yes var=response focus=yes
```


### Créer des formulaires en utilisant le script Python inline

Le même formulaire peut être créé en utilisant un INLINE_SCRIPT et un peu de code Python. Vous remarquerez que le code Python ressemble quelque peu au script OpenSesame présenté ci-dessus. Ce n'est pas surprenant : le plugin FORM_BASE traduit essentiellement le script OpenSesame en code Python.

Tout d'abord, glissez un INLINE_SCRIPT dans votre expérience. Sélectionnez l'élément nouvellement créé pour ouvrir son onglet, et ajoutez le script suivant à la phase Run de l'élément INLINE_SCRIPT (voir les commentaires pour les explications).

~~~ .python
# Créer un formulaire
form = Form(
    cols=[1,1], rows=[1,2,1],
    marges=(50,100,50,100), espacement=25
)
# Créer quatre widgets
labelTitre = Label(texte='Question')
labelQuestion = Label(
    texte='Une chauve-souris et une balle coûtent ensemble $1.10. La chauve-souris coûte un dollar de plus que la balle. Combien coûte la balle ?',
    centrer=False
)
bouton5cts = Button(texte='$0.05')
bouton10cts = Button(texte='$0.10')
# Ajouter les widgets au formulaire. La position dans le formulaire est indiquée sous forme de
# tuple (colonne, rangée).
form.set_widget(labelTitre, (0,0), colspan=2)
form.set_widget(labelQuestion, (0,1), colspan=2)
form.set_widget(bouton5cts, (0,2))
form.set_widget(bouton10cts, (1,2))
# Exécuter le formulaire ! Dans ce cas, le formulaire retournera le texte du bouton qui
# a été cliqué. C'est une façon d'obtenir une valeur de retour du formulaire. Une autre manière
# est d'utiliser le mot-clé 'var', pris en charge par certains widgets.
bouton_clique = form._exec()
~~~

Si vous souhaitez qu'un widget spécifique reçoive le focus lorsque le formulaire est exécuté, vous pouvez utiliser le mot-clé `focus_widget` :

~~~ .python
bouton_clique = form._exec(focus_widget=bouton5cts)
~~~

### Formulaires non interactifs

Habituellement, un formulaire aura un champ de saisie, un bouton ou un autre élément interactif. Cependant, vous pouvez également utiliser des formulaires sans aucun élément interactif. Pour faire cela en OpenSesame script, vous définissez `only_render` sur "yes" :

```python
set only_render yes
```

Pour faire cela dans un Python INLINE_SCRIPT, vous appelez `form.render()`, au lieu de `form._exec()`.

### Thèmes

Les formulaires supportent l'utilisation de thèmes. Actuellement, deux thèmes sont disponibles : 'gray' et 'plain'. Le thème 'gray' est celui par défaut. Bien que le thème 'gray' soit déjà assez simple, le thème 'plain' est encore plus basique. Vous pouvez choisir un thème de cette façon en OpenSesame script :

```python
set theme plain
```

Et en utilisant le mot-clé `theme` dans un script Python inline :

~~~ .python
form = Form(theme='plain')
~~~

### Widgets et mots-clés disponibles

Pour une liste des widgets et mots-clés disponibles, voir :

- %link:manual/forms/widgets%

### Validation des entrées

Pour voir comment vous pouvez valider les entrées d'un formulaire, voir :

- %link:manual/forms/validation%

## Un autre exemple

Le script OpenSesame suivant (dans un plugin FORM_BASE) produira un questionnaire de trois échelles de notation plus un bouton suivant :

```python
set rows "1;1;1;1;1"
set cols "1;1"
widget 0 0 2 1 label texte="Indiquez dans quelle mesure vous êtes d'accord avec les affirmations suivantes"
widget 0 1 1 1 label centre="no" texte="Les formulaires sont faciles"
widget 1 1 1 1 rating_scale var="question1" nodes="D'accord;Ne sais pas;Pas d'accord"
widget 0 2 1 1 label centre="no" texte="J'aime les données"
widget 1 2 1 1 rating_scale var="question2" nodes="D'accord;Ne sais pas;Pas d'accord"
widget 0 3 1 1 label centre="no" texte="J'aime les questionnaires"
widget 1 3 1 1 rating_scale var="question3" nodes="D'accord;Ne sais pas;Pas d'accord"
widget 0 4 2 1 bouton texte="Suivant"
```

Le script Python inline_script suivant produira le même questionnaire.

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