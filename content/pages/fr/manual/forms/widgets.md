title: Widgets de formulaire et mots-clés
hash: a4f02ea6550b00af4807cff9e990f6b79be4e00837de3d2ed8f8c3d34f77a19e
locale: fr
language: French


[TOC]


## Capture d'écran

%--
figure :
 id : FigWidgets
 source : widgets.png
 légende : Liste des widgets FORM disponibles.
--%


## Widgets et mots-clés

Tous les mots-clés sont facultatifs, sauf indication contraire.

### Formulaire

Les mots-clés `cols` et `rows` peuvent être des valeurs simples `int`, auquel cas ils spécifient le nombre de colonnes et de rangées de taille égale, ou des listes d'`int`, auquel cas ils spécifient les tailles relatives de chaque colonne et rangée. Pour plus d'informations sur la géométrie des formulaires, consultez :

- %link:manuel/forms/custom%

Le mot-clé `validator` peut être utilisé pour valider les entrées du formulaire. Pour plus d'informations, consultez :

- %link:manuel/forms/validation%

(Dans le script OpenSesame, il n'est pas nécessaire de créer explicitement un formulaire.)

Script Python :

~~~ .python
formulaire = Formulaire(
    cols=2, rows=2, espacement=10, marges=(100, 100, 100, 100), thème='gris',
    délai=None, clics=False, validateur=None
)
bouton = Bouton(texte='Ok!')
formulaire.set_widget(bouton, (0, 0))
formulaire._exec()
~~~


### bouton / Bouton

Script OpenSesame :

~~~python
widget 0 0 1 1 bouton texte="Cliquez sur moi!" centre=oui cadre=oui var=réponse
~~~

Script Python:

~~~ .python
formulaire = Formulaire()
bouton = Bouton(texte="Cliquez sur moi!", cadre=True, centre=True, var='réponse')
formulaire.set_widget(bouton, (0, 0))
formulaire._exec()
~~~


### case à cocher / Case à cocher

Si un groupe est spécifié, cocher une case dans ce groupe décochera toutes les autres cases de ce groupe. Les cases à cocher faisant partie d'un groupe ne peuvent pas être décochées, sauf en cliquant sur une autre case à cocher de ce groupe.

Le mot-clé `groupe` influence également la manière dont les variables sont stockées, comme décrit ici :

- %link:manuel/forms/variables%

Script OpenSesame :

~~~python
widget 0 0 1 1 case à cocher groupe=groupe texte="Option 1"
widget 0 1 1 1 case à cocher groupe=groupe texte="Option 2"
~~~

Script Python :

~~~ .python
formulaire = Formulaire()
caseacocher1 = Case à cocher(texte='Option 1', groupe='groupe')
caseacocher2 = Case à cocher(texte='Option 2', groupe='groupe')
formulaire.set_widget(caseacocher1, (0, 0))
formulaire.set_widget(caseacocher2, (0, 1))
formulaire._exec()
~~~


### image / ImageWidget

L'objet Python est appelé `ImageWidget` pour le distinguer de l'élément de toile `Image`.

Script OpenSesame :

~~~python
# Seul le chemin est un mot-clé requis
widget 0 0 1 1 image chemin="mon_image.png" ajustement=oui cadre=non
~~~

Script Python :

~~~ .python
# Seul le chemin est un mot-clé requis
formulaire = Formulaire()
image = ImageWidget(chemin=pool['mon_image.png'], ajustement=True, cadre=False)
formulaire.set_widget(image, (0, 0))
formulaire._exec()
~~~


### bouton_image / Bouton image

Le mot-clé `image_id` est utilisé pour identifier le bouton image lorsqu'il est cliqué. Si aucun `image_id` n'est fourni, le chemin d'accès à l'image est utilisé comme identifiant.

Script OpenSesame :

~~~python
# Seul le chemin est un mot-clé requis
widget 0 0 1 1 bouton_image chemin="mon_image.png" ajustement=oui cadre=non image_id=mon_image var=réponse
~~~

Script Python :

~~~ .python
# Seul le chemin est un mot-clé requis
formulaire = Formulaire()
bouton_image = Bouton_image(
    chemin=pool['mon_image.png'], ajustement=oui, cadre=non,
    image_id='mon_image', var='réponse'
)
formulaire.set_widget(bouton_image, (0, 0))
formulaire._exec()
~~~


### étiquette / Étiquette

Script OpenSesame :

~~~python
widget 0 0 1 1 étiquette texte="Mon texte" cadre=non centre=oui
~~~

Script Python :

~~~ .python
formulaire = Formulaire()
étiquette = Étiquette(texte='Mon texte', cadre=False, centre=True)
formulaire.set_widget(étiquette, (0, 0))
formulaire._exec()
~~~


### échelle_d'évaluation / Échelle d'évaluation

Le mot-clé `noeuds` peut être un `int` ou une liste de libellés séparés par des points-virgules. Si `noeuds` est un `int`, il spécifie le nombre de nœuds (non étiquetés).

Le mot-clé `par défaut` indique quel numéro de nœud est sélectionné par défaut, où le premier nœud est 0.

Script OpenSesame :

~~~python
widget 0 1 1 1 échelle_d'évaluation var=réponse noeuds="D'accord;Ne sais pas;Désaccord" click_accepts=non orientation=horizontal var=réponse default=0
~~~

Script Python:

~~~ .python
form = Form()
rating_scale = RatingScale(
    nodes=['D'accord', u"Je ne sais pas", 'Pas d'accord'], click_accepts=False,
    orientation='horizontal', var='response', default=0
)
form.set_widget(rating_scale, (0, 0))
form._exec()
~~~


### text_input / TextInput

Le mot-clé `stub` indique du texte de remplissage qui est affiché lorsqu'aucun texte n'a été saisi. Le mot-clé `key_filter`, disponible uniquement en Python, spécifie une fonction pour filtrer les pressions de touches. Ceci est décrit plus en détail sous :

- %link:manual/forms/validation%

Script OpenSesame :

~~~python
widget 0 0 1 1 text_input text="Texte initial" frame=yes center=no stub="Tapez ici …" return_accepts=yes var=response
~~~

Script Python :

~~~ .python
form = Form()
text_input = TextInput(
    text='Texte initial', frame=True, center=False, stub='Tapez ici …',
    return_accepts=True, var='response', key_filter=my_filter_function
)
form.set_widget(text_input, (0, 0))
form._exec()
~~~