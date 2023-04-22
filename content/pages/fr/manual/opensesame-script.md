title: Script OpenSesame
reviewed: false
hash: 73e219615747fe9d3e0d6444db9859ce306004221b08c7ff0f63e555f160cfa2
locale: fr
language: French

[TOC]

## À propos du script OpenSesame

Le script OpenSesame est un langage définitionnel simple qui définit une expérience. Ce n'est pas un langage de programmation à part entière et ne comprend pas de fonctionnalités telles que les boucles `for`. Le script OpenSesame est interprété par un environnement d'exécution OpenSesame.

Le script OpenSesame est différent des scripts Python utilisés dans les éléments inline_script. Python est un véritable langage de programmation avec toute la flexibilité et les complexités que cela implique. En revanche, le script OpenSesame est utilisé pour définir des expériences de manière simple et lisible.

## Remarques générales

### Mots-clés

Certains éléments, tels que form_base et sketchpad, acceptent des mots-clés. Les mots-clés sont de la forme `mot-clé=valeur`. Les mots-clés sont facultatifs et doivent revenir à une valeur par défaut.

### Commentaires

Les chaînes précédées d'un dièse doivent être interprétées comme des commentaires.

*Exemple*

	# Ceci est un commentaire

### Citation

La citation n'est pas nécessaire, sauf autour des chaînes contenant des espaces ou d'autres formes de ponctuation. Ainsi, les lignes suivantes doivent être interprétées comme identiques :

	set my_var 'my_value'
	set my_var "my_value"
	set my_var my_value

Cependant, les lignes suivantes ne le sont pas. En fait, la première ligne n'est pas valide, car elle a un troisième paramètre inattendu.

	set my_var my value
	set my_var "my value"

### Types

Il n'y a pas de types. Aucune distinction n'est faite entre les chaînes, les entiers, etc.

### Syntaxe spécifique aux éléments

Certains éléments ont une syntaxe spécifique. Ceci est indiqué dans la section "S'applique à" pour chacun des mots-clés discutés ci-dessous.

### Résolution des noms de chemin

TODO

## Instruction *define*

Commence la définition d'un élément. Après une instruction define, toutes les lignes sont indentées par une seule tabulation. La fin de la définition de l'élément est la première chaîne qui n'est plus indentée. Les instructions define imbriquées ne sont pas autorisées.

*S'applique à*

Tous les éléments

*Format*

	define [nom de l'élément] [type d'élément]
		[définition de l'élément]

*Paramètres*

|`nom de l'élément`	| le nom de l'élément	|
|`type d'élément`	| le type de l'élément	|

*Exemple*

	define get_key keyboard_response
		set allowed_responses "a;x"
		set description "Collecte les réponses au clavier"
		set timeout "infini"
		set flush "oui"

## Instruction *draw*

Définit un élément visuel d'un élément sketchpad ou feedback.

*S'applique à*

sketchpad, feedback

*Format*

Le format dépend de l'élément.

	draw ellipse [gauche] [haut] [largeur] [hauteur] [mots-clés]
	draw circle [x] [y] [rayon] [mots-clés]
	draw line [gauche] [droite] [haut] [bas] [mots-clés]
	draw arrow [gauche] [droite] [haut] [bas] [mots-clés]
	draw textline [x] [y] [texte]
	draw image [x] [y] [chemin]
	draw gabor [x] [y]
	draw noise [x] [y]
	draw fixdot [x] [y]

*Paramètres*

|`gauche` 		|la coordonnée x la plus à gauche		|
|`droite`		|la coordonnée x la plus à droite	|
|`haut`			|la coordonnée y la plus haute			|
|`bas`			|la coordonnée y la plus basse			|
|`x` 			|la coordonnée x						|
|`y`			|la coordonnée y						|
|`texte` 		|chaîne de texte						|
|`chemin` 		|le chemin vers un fichier image		|

*Mots-clés*

TODO

*Exemple*

	draw fixdot 0 0

## Instruction *log*

Indique qu'une variable doit être écrite dans le fichier de journal.

*S'applique à*

logger

*Format*

	log [nom de la variable]

*Paramètres*

|`nom de la variable`		| le nom d'une variable	|

*Exemple*

	log response_time

## Instruction *run*

Indique qu'un élément doit être exécuté. Dans le cas de la séquence, l'ordre des instructions run détermine l'ordre dans lequel les éléments sont appelés. Dans le cas du plugin coroutines, tous les éléments sont appelés en même temps.

*S'applique à*

séquence

*Format*

	run [nom de l'élément] [optionnel : condition] [optionnel : désactivé]

*Paramètres*

|`nom de l'élément`			| le nom de l'élément à exécuter	|
|`condition` (facultatif)	| l'instruction conditionnelle, qui détermine si l'élément est effectivement appelé. Si aucune condition n'est fournie, l'élément est toujours appelé.|

*Exemple*

	run correct_feedback '[correct] = 1'

## Instruction *set*

Définit des variables monolignes.

*S'applique à*

Tous les éléments

*Format*

	set [nom de la variable] [valeur]

*Paramètres*

|`nom de variable`	|le nom de la variable	|
|`valeur`			|la valeur de la variable	|

*Exemple*

	définir le délai d'attente 1000

*Notes*

Les variables multilignes sont définies en utilisant la notation `__[nom de variable]__`. Ceci est principalement utile pour les éléments qui nécessitent de grands blocs de texte. Dans une définition d'élément, chaque ligne est précédée d'une seule tabulation, qui ne doit pas être interprétée comme faisant partie du texte. `__end__` indique la fin de la variable.

*Par exemple :*

	__ma_variable__
	Ceci est la première ligne.
	Ceci est la deuxième ligne.
	__end__

## *setcycle* instruction

Similaire à l'instruction "set" régulière, mais définit une variable uniquement pendant un cycle spécifique d'une boucle. Il s'agit de l'équivalent en script du tableau de boucle.

*S'applique à*

Boucle

*Format*

	setcycle [numéro de cycle] [nom de variable] [valeur de variable]

*Paramètres*

|`Numéro de cycle`|le numéro du cycle, où 0 est le premier	|
|`nom de variable` |le nom de la variable							|
|`valeur`			|la valeur de la variable							|

*Exemple*

	setcycle 0 repère valide

## *widget* instruction

Ajoute un widget (boutons, étiquettes, etc.) à un formulaire. Les mots-clés valides dépendent du type de widget. L'instruction widget ne fait pas strictement partie de la syntaxe de base d'OpenSesame, mais est utilisée par le plugin form_base.

*S'applique à*

form_base (plugin)

*Format*

	widget [colonne] [rangée] [étendue de colonne] [étendue de rangée] [type de widget] [mots-clés]

*Paramètres*

|`colonne`		|la position de la colonne du widget dans le formulaire, où 0 est le plus à gauche								|
|`rangée`		|la position de la rangée du widget dans le formulaire, où 0 est le sommet										|
|`étendue de colonne`|le nombre de colonnes occupées par le widget												|
|`étendue de rangée`	|le nombre de rangées occupées par le widget												|
|`type de widget`		|'button', 'checkbox', 'image', 'image_button', 'label', 'rating_scale', or 'text_input'	|

*Mots-clés*

TODO

*Exemple*

	widget 0 0 1 1 label text='Ceci est une étiquette'