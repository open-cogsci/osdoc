title: Tutoriel intermédiaire (Python) recherche visuelle
uptodate: false
hash: 2b4f7f8ee08b18e413216b18d817c3513539a9befce4a79f157785b8dedbf837
locale: fr
language: French

[TOC]

## À propos d'OpenSesame

OpenSesame est un programme convivial pour le développement d'expériences comportementales en psychologie, neurosciences et économie expérimentale. Pour les débutants, OpenSesame dispose d'une interface graphique complète, basée sur des actions point et clic. Pour les utilisateurs avancés, OpenSesame prend en charge Python (bureau uniquement) et JavaScript (bureau et navigateur).

OpenSesame est disponible gratuitement sous la [Licence publique générale v3][gpl].

## À propos de ce tutoriel

Ce tutoriel montre comment créer une expérience de recherche visuelle de base en utilisant OpenSesame [(Mathôt, Schreij, & Theeuwes, 2012)][references]. Nous utiliserons à la fois l'interface graphique et les scripts Python. Une certaine expérience avec OpenSesame et Python est recommandée. Ce tutoriel dure environ une heure.

Une version JavaScript de ce tutoriel est également disponible. Si vous souhaitez exécuter vos expériences en ligne (avec OSWeb), alors le tutoriel JavaScript est ce dont vous avez besoin :

- %link:tutorials/intermediate-javascript%

## Ressources

- __Téléchargement__ — Ce tutoriel suppose que vous utilisez la version 3.2.0 d'OpenSesame ou ultérieure. Vous pouvez télécharger la version la plus récente d'OpenSesame à partir de :
	- %link:download%
- __Documentation__ — Un site web de documentation dédié se trouve à l'adresse :
	- <http://osdoc.cogsci.nl/>
- __Forum__ — Un forum de support est disponible à l'adresse :
	- <http://forum.cogsci.nl/>

## L'expérience

Dans ce tutoriel, vous créerez une expérience de recherche visuelle de base. L'expérience ressemble aux études classiques de recherche visuelle de [Treisman et Gelade (1980)][references], mais elle n'est pas identique.

Dans cette expérience, les participants recherchent un objet cible, qui peut être un carré jaune, un cercle jaune, un carré bleu ou un cercle bleu ; l'identité de la cible varie entre les blocs d'essais. Les participants indiquent si la cible est présente ou non en appuyant sur la flèche droite (présente) ou gauche (absente).

En plus de la cible, zéro ou plusieurs objets distracteurs sont montrés. Il y a trois conditions, et la condition détermine quel type de distracteurs il y a :

- Dans la condition *Conjonction*, les distracteurs peuvent avoir n'importe quelle forme et couleur, avec pour seule restriction que les distracteurs ne peuvent pas être identiques à la cible. Ainsi, par exemple, si la cible est un carré jaune, les distracteurs sont des cercles jaunes, des cercles bleus et des carrés bleus.
- Dans la condition *Attribut de forme*, les distracteurs ont une forme différente de la cible, mais peuvent avoir n'importe quelle couleur. Ainsi, par exemple, si la cible est un carré jaune, les distracteurs sont des cercles jaunes et des cercles bleus.
- Dans la condition *Attribut de couleur*, les distracteurs peuvent avoir n'importe quelle forme, mais ont une couleur différente de la cible. Ainsi, par exemple, si la cible est un carré jaune, les distracteurs sont des carrés bleus et des cercles bleus.

Un retour d'information immédiat est présenté après chaque essai : un point vert après une réponse correcte et un point rouge après une réponse incorrecte. Des informations détaillées sur les temps de réponse moyens et la précision sont présentées après chaque bloc d'essais.

%--
figure :
 id: FigVisualSearch
 source: visual-search.svg
 caption: |
  L'expérience de recherche visuelle que vous allez mettre en œuvre dans ce tutoriel.
--%

Les expériences comme celle-ci montrent deux résultats typiques :

- Il faut plus de temps pour trouver la cible dans la condition Conjonction que dans les deux conditions Attribut.
- Dans la condition Conjonction, les temps de réponse augmentent à mesure que le nombre de distracteurs augmente. Cela suggère que les gens recherchent la cible un élément à la fois ; c'est ce qu'on appelle la *recherche série*.
- Dans les conditions Attribut (forme et couleur), les temps de réponse n'augmentent pas, ou très peu, à mesure que le nombre de distracteurs augmente. Cela suggère que les gens traitent l'ensemble de l'affichage en même temps ; c'est ce qu'on appelle la *recherche parallèle*.

Selon la théorie de l'intégration des caractéristiques de Treisman et Gelade, ces résultats montrent que la condition Conjonction exige que vous combiniez, ou *liez*, la couleur et la forme de chaque objet. Cette liaison nécessite de l'attention, et vous devez donc déplacer votre attention d'un objet à l'autre ; cela est lent et explique pourquoi les temps de réponse dépendent du nombre d'objets présents. En revanche, dans les conditions des caractéristiques, la couleur et la forme n'ont pas besoin d'être liées, et l'ensemble du dispositif peut donc être traité en une seule fois sans que l'attention soit dirigée vers chaque objet.

## Plan expérimental

Ce plan :

- Est *intra-sujet*, car tous les participants font toutes les conditions
- Est *entièrement croisé* (ou factoriel complet), car toutes les combinaisons de conditions se produisent
- A trois conditions (ou facteurs) :
	- Variées au sein des blocs :
		- `set_size` avec trois niveaux (1, 5, 15), ou SS<sub>3</sub>
		- `condition` avec trois niveaux (conjonction, feature_shape, feature_color), ou CN<sub>3</sub>
		- `target_present` avec deux niveaux (présent, absent), ou TP<sub>2</sub>
	- Variées entre les blocs :
		- `target_shape` avec deux niveaux (carré, cercle), ou TS<sub>2</sub>
		- `target_color` avec deux niveaux (jaune, bleu), ou TC<sub>2</sub>
- A N sujets, ou <u>S</u><sub>N</sub>

Vous pouvez écrire ce plan comme <u>S</u><sub>N</sub>×SS<sub>3</sub>×CN<sub>3</sub>×TP<sub>2</sub>×TS<sub>2</sub>×TC<sub>2</sub>

Pour plus d'informations sur cette notation pour la conception expérimentale, consultez :

- %link:experimentaldesign%

## Étape 1 : Créez la structure de base de l'expérience

Ouvrez OpenSesame et, dans l'onglet 'Démarrer !', sélectionnez le modèle étendu. Ce modèle fournit la structure de base qui est commune à de nombreuses expériences de psychologie cognitive, comme celle que nous allons créer ici.

Le modèle étendu contient quelques éléments dont nous n'avons pas besoin. Supprimez les éléments suivants :

- *about_this_template*
- *practice_loop*
- *end_of_practice*

Lorsque vous avez supprimé ces éléments, ils sont encore visibles dans la corbeille 'Unused items'. Pour supprimer définitivement ces éléments, cliquez sur la corbeille 'Unused items' puis sur le bouton 'Supprimer définitivement les éléments inutilisés'.

Enfin, donnez un bon titre à l'expérience, comme 'Recherche visuelle'. Pour ce faire, ouvrez l'onglet des propriétés générales (en cliquant sur 'Extended template' dans la zone de vue d'ensemble) et cliquez sur le nom de l'expérience pour le modifier.

La zone de vue d'ensemble doit maintenant ressembler à %FigStep1 :

%--
figure :
 id: FigStep1
 source: step1.png
 caption: |
  La zone de vue d'ensemble à la fin de l'étape 1.
--%

## Étape 2 : Définir les variables expérimentales qui varient entre les blocs

Comme décrit ci-dessus, deux variables varient entre les blocs dans notre expérience : `target_shape` et `target_color`. Nous devons donc définir ces variables dans la *experimental_loop*. Pour comprendre pourquoi, considérez la structure montrée dans %FigStep1, en commençant par le bas (c'est-à-dire le niveau le plus indenté).

- *trial_sequence* correspond à un essai unique
- *block_loop* correspond à un bloc d'essais
	- Par conséquent, les variables définies ici varient pour chaque exécution de *trial_sequence* ; en d'autres termes, les variables définies dans *block_loop* varient __au sein des blocs__.
- *block_sequence* correspond à un bloc d'essais, précédé par la réinitialisation des variables de feedback et suivi par des commentaires aux participants
- *experimental_loop* correspond à plusieurs blocs d'essais
	- Par conséquent, les variables définies ici varient pour chaque exécution de *block_sequence* ; en d'autres termes, les variables définies dans *experimental_loop* varient __entre les blocs__.
- *experiment* correspond à l'ensemble de l'expérience, qui est un écran d'instruction, suivi de plusieurs blocs d'essais, puis d'un écran de fin d'expérience

Cliquez sur experimental loop et définissez :

- `target_shape`, qui peut être 'square' ou 'circle'; et
- `target_color`, qui peut être 'yellow' ou 'blue'.

Nous avons un plan factoriel complet, ce qui signifie que toutes les combinaisons 2 × 2 = 4 doivent se produire. Le tableau de *experimental_loop* devrait maintenant ressembler à %FigStep2 :

%--
figure :
 id: FigStep2
 source: step2.png
 caption: |
  Le tableau de *experimental_loop* à la fin de l'étape 2.
--%

## Étape 3 : Donner des instructions au début de chaque bloc

Pour l'instant, l'expérience commence par un seul écran d'instructions. Dans notre cas, nous voulons donner des instructions avant chaque bloc d'essais, pour indiquer au participant quelle cible rechercher (car l'identité de la cible varie entre les blocs).

__Déplacez les instructions dans block_sequence__

Pour cela, saisissez l'élément *instructions* et faites-le glisser sur *block_sequence*. Une fenêtre contextuelle apparaîtra, vous demandant si vous voulez :

- Insérer l'élément dans *block_sequence*, auquel cas *instructions* deviendrait le premier élément de *block_sequence* ; ou
- Insérer l'élément après *block_sequence*, auquel cas *instructions* serait déplacé à une position après *block_sequence*.

Sélectionnez la première option ('Insérer dans'). Maintenant, *block_sequence* commence par un écran d'instructions, ce que nous voulons.

__Ajoutez un texte d'instruction__

Cliquez sur *instructions* pour l'ouvrir et ajoutez un bon texte d'instruction, tel que :

```text
INSTRUCTIONS

Cherchez le [target_color] [target_shape]

Appuyez sur la touche flèche droite si vous le trouvez
Appuyez sur la touche flèche gauche si vous ne le trouvez pas

Appuyez sur n'importe quelle touche pour commencer
```

Les crochets autour de '[target_color]' et '[target_shape]' indiquent qu'il ne s'agit pas de textes littéraux, mais qu'ils se réfèrent aux variables que nous avons définies dans *experimental_loop*. Lorsque l'expérience est en cours, les valeurs de ces variables apparaîtront ici, et le participant verra (par exemple) "Cherchez le cercle jaune".

__Donnez un aperçu visuel de la cible__

Il est également bon de montrer au participant le stimulus réel qu'il doit trouver. Pour ce faire :

- Dessinez un cercle rempli au centre de l'affichage (assurez-vous qu'il ne se superpose pas au texte) ;
- Changez la couleur du cercle en '[target_color]'. Cela signifie que la couleur du cercle dépend de la valeur de la variable `target_color` ; et
- Changez l'instruction show-if en '[target_shape] = circle'.

En d'autres termes, nous avons dessiné un cercle dont la couleur est déterminée par `target_color` ; de plus, ce cercle n'est montré que lorsque la variable `target_shape` a la valeur 'circle'. Pour plus d'informations sur les variables et les instructions show-if, voir :

- %link:manual/variables%

Nous utilisons la même astuce pour dessiner un carré :

- Dessinez un carré rempli au centre de l'affichage ;
- Changez la couleur du carré en '[target_color]' ; et
- Changez l'instruction show-if en '[target_shape] = square'

L'écran *instructions* devrait maintenant ressembler à %FigStep3 :

%--
figure :
 id: FigStep3
 source: step3.png
 caption: |
  L'écran *instructions* à la fin de l'étape 3.
--%

## Étape 4 : Définir les variables expérimentales qui varient à l'intérieur des blocs

Trois variables varient à l'intérieur des blocs dans notre expérience : `condition`, `set_size` et `target_present`. Comme décrit à l'étape 2, nous devons définir ces variables dans le *block_loop* afin qu'elles varient pour chaque exécution de *trial_sequence*.

Les trois variables font un total de 3 × 3 × 2 = 18 combinaisons différentes. Nous pouvons les saisir manuellement dans le tableau, mais, comme nous avons un plan factoriel complet, nous pouvons également utiliser l'assistant de plan factoriel complet. Pour ce faire, ouvrez d'abord *block_loop* et cliquez sur le bouton 'Plan factoriel complet'.

Dans le tableau qui apparaît, mettez les noms de variables sur la première ligne et les valeurs sur les lignes ci-dessous, comme indiqué dans %FigFullFactorial.

%--
figure :
 id: FigFullFactorial
 source: fullfactorial.png
 caption: |
  L'écran *instructions* à la fin de l'étape 3.
--%

Cliquez maintenant sur 'Ok' pour générer la conception complète. Le tableau de *block_loop* devrait maintenant ressembler à %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  Le tableau de *block_loop* à la fin de l'étape 4.
--%

## Étape 5 : Créer la séquence d'essai

Nous voulons que notre séquence d'essai ressemble à ceci :

- Un point de fixation, pour lequel nous utiliserons un SKETCHPAD.
- Un affichage de recherche, que nous créerons en Python avec un INLINE_SCRIPT personnalisé.
- La collecte des réponses, pour laquelle nous utiliserons un KEYBOARD_RESPONSE.
- L'enregistrement des données, pour lequel nous utiliserons un LOGGER.
- (Nous voulons également avoir un retour d'information immédiat après chaque essai, mais nous y reviendrons plus tard.)

Il ne manque donc qu'un INLINE_SCRIPT.

- Insérez un nouveau INLINE_SCRIPT après *sketchpad* et renommez-le en *search_display_script*.
- Renommez *sketchpad* en *fixation_dot*, afin que sa fonction soit claire ; et
- Changez la durée de *fixation_dot* en 500, de sorte que le point de fixation soit affiché pendant 500 ms. (Il devrait déjà y avoir un point de fixation dessiné ; sinon, dessinez-en un au centre de *fixation_dot*.)

La zone d'aperçu devrait maintenant ressembler à %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  La zone d'aperçu à la fin de l'étape 5.
--%

## Étape 6 : Générer l'affichage de recherche

__Programmation descendante et défensive__

Maintenant, les choses vont devenir intéressantes : nous commencerons à programmer en Python. Nous utiliserons deux principes directeurs : la programmation *descendante* et *défensive*.

- La *programmation descendante* signifie que nous commençons par la logique la plus abstraite, sans nous soucier de la façon dont cette logique est mise en œuvre. Une fois la logique la plus abstraite en place, nous passerons à une logique légèrement moins abstraite, et ainsi de suite, jusqu'à ce que nous arrivions aux détails de l'implémentation. Cette technique aide à garder le code structuré.
- La *programmation défensive* signifie que nous supposons que nous faisons des erreurs. Par conséquent, pour nous protéger de nous-mêmes, nous intégrons des vérifications de cohérence dans le code.

*Note :* L'explication ci-dessous suppose que vous êtes un peu familiarisé avec le code Python. Si des concepts comme `list`, `tuple`, et les fonctions ne vous disent rien, il est préférable de suivre d'abord un didacticiel Python d'introduction. Vous pouvez trouver des liens vers des tutoriels Python ici :

- %link:manual/python/about%

La logique du code est présentée dans %FigHierarchy. Les chiffres indiquent l'ordre dans lequel nous mettrons en œuvre la fonctionnalité, en commençant par le niveau abstrait.

%--
figure:
 id: FigHierarchy
 source: hierarchy.svg
 caption: |
  La logique du code pour dessiner un affichage de recherche visuelle.
--%

__Les phases de préparation et d'exécution__

Ouvrez *search_display_script* et passez à l'onglet Prepare (Préparer). OpenSesame distingue deux phases d'exécution :

- Pendant la phase de préparation, chaque élément a la possibilité de se préparer ; ce que cela signifie dépend de l'élément : Pour un SKETCHPAD, cela signifie dessiner un canevas (mais ne pas l'afficher) ; pour un SAMPLER, cela signifie charger un fichier son (mais ne pas le lire) ; etc.
- Pendant la phase d'exécution, chaque élément est effectivement exécuté ; là encore, cela dépend de l'élément : Pour un SKETCHPAD, cela signifie afficher le canevas préparé précédemment ; pour un SAMPLER, cela signifie lire un fichier son précédemment chargé.

Pour un INLINE_SCRIPT, vous devez décider vous-même ce qu'il faut mettre dans la phase de préparation et ce qu'il faut mettre dans la phase d'exécution. La distinction est généralement assez claire : dans notre cas, nous mettons le code pour dessiner le canevas dans la phase de préparation et le code pour afficher le canevas (qui est petit) dans la phase d'exécution.

Voir aussi :

- %link:prepare-run%

__Mettre en œuvre le niveau abstrait__

Nous commençons par le niveau le plus abstrait : définir une fonction qui dessine un affichage de recherche visuelle. Nous ne précisons pas *comment* cela est fait ; nous supposons simplement qu'il existe une fonction qui le fait, et nous nous occuperons des détails plus tard - c'est de la programmation descendante.

Dans l'onglet Prepare, saisissez le code suivant :

~~~ .python
c = draw_canvas()
~~~

Que se passe-t-il ici ? Nous …

- Appelez `draw_canvas()`, qui renvoie un objet `Canvas` que nous stockons sous le nom de `c` ; en d'autres termes, `c` est un objet `Canvas` qui correspond à l'affichage de recherche. Cela suppose qu'il existe une fonction `draw_canvas()`, même si nous ne l'avons pas encore définie.

Un objet `Canvas` est un seul affichage ; c'est en quelque sorte l'équivalent Python d'un SKETCHPAD. Voir aussi :

- %link:manual/python/canvas%

Nous définissons maintenant `draw_canvas()` (au-dessus du reste du script) :

~~~ .python
def draw_canvas():

	"""
	Dessine le canevas de recherche.

	Retour :
	Un Canvas.
	"""

	c = Canvas()
	xy_list = xy_random(n=var.set_size, width=500, height=500, min_dist=75)
	if var.target_present == 'present':
		x, y = xy_list.pop()
		draw_target(c, x, y)
	elif var.target_present != 'absent':
		raise Exception(
			'Valeur invalide pour target_present %s' % var.target_present)		
	for x, y in xy_list:
		draw_distractor(c, x, y)
	return c
~~~

Que se passe-t-il ici ? Nous…

- Créons un canevas vide, `c`, en utilisant la fonction usine `Canvas()`.
- Générons une liste de coordonnées aléatoires `x, y`, appelée `xy_list`, en utilisant une autre fonction courante, `xy_random()`. Cette liste détermine où les stimuli sont affichés.
- Vérifiez si la variable expérimentale `target_present` a la valeur 'present' ; si c'est le cas, `pop()` un tuple `x, y` de `xy_list`, et dessinez la cible à cet endroit. Cela suppose qu'il existe une fonction `draw_target()`, même si nous ne l'avons pas encore définie.
- Si `target_present` n'est ni 'present' ni 'absent', nous levons une `Exception` ; c'est de la programmation défensive, et cela nous protège des erreurs de frappe (par exemple, si nous avions accidentellement saisi 'presenr' au lieu de 'present').
- Parcourez tous les tuples `x, y` restants et dessinez un distracteur à chaque position. Cela suppose qu'il y a une fonction `draw_distractor()`, même si nous ne l'avons pas encore définie.
- Retourne `c`, qui a maintenant l'affichage de recherche dessiné dessus.

Il existe plusieurs fonctions courantes, telles que `Canvas()` et `xy_random()`, qui sont toujours disponibles. Voir :

- %link:manual/python/common%

Les variables expérimentales sont stockées en tant que propriétés de l'objet `var`. C'est pourquoi vous écrivez `var.set_size` et non directement `set_size`. Voir :

- %link:var%

__Mettre en œuvre le niveau intermédiaire__

Nous allons maintenant définir `draw_target` (au-dessus du reste du script) :

~~~ .python
def draw_target(c, x, y):

	"""
	Dessine la cible.

	arguments :
	c : Un Canvas.
	x : Une coordonnée x.
	y : Une coordonnée y.
	"""

	draw_shape(c, x, y, color=var.target_color, shape=var.target_shape)
~~~

Que se passe-t-il ici ? Nous…

- Appelons une autre fonction, `draw_shape()`, et spécifions la couleur et la forme à dessiner. Cela suppose qu'il existe une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

Nous définissons également `draw_distractor` (au-dessus du reste du script) :

~~~ .python
def draw_distractor(c, x, y):

	"""
	Dessine un seul distracteur.

	Arguments :
	c : Un Canvas.
	x : Une coordonnée x.
	y : Une coordonnée y.
	"""

	if var.condition == 'conjunction':
		draw_conjunction_distractor(c, x, y)
	elif var.condition == 'feature_shape':
		draw_feature_shape_distractor(c, x, y)
	elif var.condition == 'feature_color':
		draw_feature_color_distractor(c, x, y)
	else:
		raise Exception('Condition invalide : %s' % var.condition)
~~~

Que se passe-t-il ici ? Nous…

- Appelons une autre fonction pour dessiner un distracteur plus spécifique en fonction de la condition.
- Vérifiez si `var.condition` a l'une des valeurs attendues. Sinon, nous levons une `Exception`. C'est de la programmation défensive ! Sans cette vérification, si nous avions fait une erreur de frappe quelque part, le distracteur pourrait simplement ne pas être affiché sans provoquer de message d'erreur.

Maintenant, nous définissons la fonction qui dessine les distracteurs dans la condition Conjonction (au-dessus du reste du script) :

~~~ .python
import random


def draw_conjunction_distractor(c, x, y):

	"""
	Dessine un seul distracteur dans la condition de conjonction : un objet qui
	peut avoir n'importe quelle forme et couleur, mais ne peut pas être identique à la cible.

	arguments :
	c : Un Canvas.
	x : Une coordonnée x.
	y : Une coordonnée y.
	"""

	conjonctions = [
		('jaune', 'cercle'),
		('bleu', 'cercle'),
		('jaune', 'carré'),
		('bleu', 'carré'),
		]
	conjonctions.remove((var.target_color, var.target_shape))
	couleur, forme = random.choice(conjonctions)
	draw_shape(c, x, y, color=couleur, shape=forme)
~~~

Que se passe-t-il ici ? Nous ...

- Définissons une liste, `conjonctions`, de toutes les combinaisons possibles de couleurs et de formes.
- Supprimons la cible de cette liste ; cela est nécessaire, car le distracteur ne peut pas être identique à la cible.
- Sélectionnons aléatoirement l'une des combinaisons de couleurs et de formes de `conjonctions`.
- Appelons une autre fonction, `draw_shape()`, et spécifions la couleur et la forme du distracteur à dessiner. Cela suppose qu'il existe une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

De plus, nous …

- Ajoutons la ligne `import random` en haut du script. Ceci est nécessaire pour que nous puissions utiliser des fonctions qui font partie du module `random`, telles que `random.choice()`.

Maintenant, nous définissons la fonction qui dessine les distracteurs dans la condition "Shape Feature" (juste en dessous de l'instruction `import`) :

~~~ .python
def draw_feature_shape_distractor(c, x, y):

	"""
	Dessine un seul distracter dans la condition "shape-feature" : un objet qui
	a une forme différente de celle de la cible, mais peut avoir n'importe quelle couleur.

	Arguments:
	c : Un Canvas.
	x : Une coordonnée x.
	y : Une coordonnée y.
	"""

	couleurs = ['jaune', 'bleu']
	couleur = random.choice(couleurs)
	if var.target_shape == 'cercle':
		forme = 'carré'
	elif var.target_shape == 'carré':
		forme = 'cercle'
	else :
		raise Exception('Invalid target_shape: %s' % var.target_shape)
	draw_shape(c, x, y, color=couleur, shape=forme)
~~~

Que se passe-t-il ici ? Nous …

- Sélectionnons aléatoirement une couleur.
- Choisissons une forme carrée si la cible est un cercle, et une forme circulaire si la cible est un carré.
- Si `target_shape` n'est ni 'cercle' ni 'carré', levons une `Exception` - plus de programmation défensive !
- Appelons une autre fonction, `draw_shape()`, et spécifions la couleur et la forme du distracteur à dessiner. Cela suppose qu'il existe une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

Maintenant, nous définissons la fonction qui dessine les distracteurs dans la condition "Color Feature" (juste en dessous de l'instruction `import`) :

~~~ .python
def draw_feature_color_distractor(c, x, y):

	"""
	Dessine un seul distracter dans la condition "feature-color" : un objet qui
	a une couleur différente de celle de la cible, mais peut avoir n'importe quelle forme.

	Arguments:
	c : Un Canvas.
	x : Une coordonnée x.
	y : Une coordonnée y.
	"""

	formes = ['cercle', 'carré']
	forme = random.choice(formes)
	if var.target_color == 'jaune':
		couleur = 'bleu'
	elif var.target_color == 'bleu':
		couleur = 'jaune'
	else :
		raise Exception('Invalid target_color: %s' % var.target_color)
	draw_shape(c, x, y, color=couleur, shape=forme)
~~~

Que se passe-t-il ici ? Nous …

- Sélectionnons aléatoirement une forme.
- Choisissons une couleur bleue si la cible est jaune, et une couleur jaune si la cible est bleue.
- Si `target_color` n'est ni 'jaune' ni 'bleu', levons une `Exception` - plus de programmation défensive !
- Appelons une autre fonction, `draw_shape()`, et spécifions la couleur et la forme du distracteur à dessiner. Cela suppose qu'il existe une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

__Mettre en œuvre le niveau détaillé__

Maintenant, nous descendons jusqu'aux détails en définissant la fonction qui dessine réellement une forme sur le canevas (juste en dessous de l'instruction `import`) :

~~~ .python
def draw_shape(c, x, y, color, shape):

	"""
	Dessine une seule forme.

	Arguments :
	c :		Un Canvas.
	x :		Une coordonnée x.
	y :		Une coordonnée y.
	color :	Une couleur (jaune ou bleu)
	shape :	Une forme (carré ou cercle)
	"""

	si shape == 'carré':
		c += Rect(x=x-25, y=y-25, w=50, h=50, color= couleur, fill=True)
	elif shape == 'cercle':
		c += Circle(x=x, y=y, r=25, color= couleur, fill=True)
	else:
		raise Exception('Forme invalide : %s' % shape)
	if color not in ['jaune', 'bleu']:
		raise Exception('Couleur invalide : %s' % couleur)
~~~

Que se passe-t-il ici ? Nous …

- Vérifions quelle forme doit être dessinée. Pour les carrés, nous ajoutons un élément `Rect()` au canevas. Pour les cercles, nous ajoutons un élément `Circle()`.
- Vérifions si la forme est un carré ou un cercle, et si ce n'est pas le cas, nous levons une `Exception`. C'est un autre exemple de programmation défensive! Nous nous assurons que nous n'avons pas accidentellement spécifié une forme invalide.
- Vérifions si la couleur n'est ni jaune ni bleue, et si ce n'est pas le cas, nous levons une `Exception`.

__Mettez en œuvre la phase Run__

Parce que nous avons fait tout le travail difficile dans la phase Prepare, la phase Run est juste:

~~~ .python
c.show()
~~~

C'est tout! Maintenant, vous avez dessiné un affichage complet de recherche visuelle. Et, surtout, vous avez fait cela d'une manière facile à comprendre, grâce à la programmation descendante, et sûre, grâce à la programmation défensive.


## Étape 7: Définir la réponse correcte

Pour savoir si le participant répond correctement, nous devons connaître la réponse correcte. Vous pouvez la définir explicitement dans le *block_loop* (comme cela a été fait dans le didacticiel pour débutants); mais ici, nous allons utiliser un simple script Python qui vérifie si la cible est présente ou non et définit la réponse correcte en conséquence.

Pour ce faire, insérez un nouveau INLINE_SCRIPT au début de *trial_sequence* et renommez-le en *correct_response_script*. Dans la phase Prepare, saisissez le code suivant:

~~~ .python
if var.target_present == 'présent':
	var.correct_response = 'droite'
elif var.target_present == 'absent':
	var.correct_response = 'gauche'
else:
	raise Exception("target_present doit être absent ou présent, pas %s" % var.target)
~~~

Que se passe-t-il ici ? Nous …

- Vérifions si la cible est présente ou non. Si la cible est présente, la réponse correcte est 'droite' (la touche flèche droite); si la cible est absente, la réponse correcte est 'gauche' (la touche flèche gauche). La variable expérimentale `var.correct_response` est automatiquement utilisée par OpenSesame; par conséquent, nous n'avons pas besoin d'indiquer explicitement que cette variable contient la réponse correcte.
- Vérifions si la cible est présente ou absente, et si ce n'est pas le cas, nous levons une `Exception` : un autre exemple de programmation défensive.

## Étape 8: Donner des commentaires par essai

Des commentaires après chaque essai peuvent motiver les participants; cependant, les commentaires par essai ne doivent pas interférer avec le déroulement de l'expérience. Une bonne façon de donner des commentaires par essai est de montrer brièvement un point de fixation vert après une réponse correcte et un point de fixation rouge après une réponse incorrecte.

Pour ce faire:

- Insérez deux nouveaux SKETCHPADs dans *trial_sequence*, juste après *keyboard_response*.
- Renommez un SKETCHPAD en *green_dot*, dessinez un point de fixation vert central dessus et changez sa durée à 500.
- Renommez l'autre SKETCHPAD en *red_dot*, dessinez un point de fixation rouge central dessus et changez sa durée à 500.

Bien sûr, un seul des deux points doit être montré à chaque essai. Pour ce faire, nous spécifierons des instructions run-if dans *trial_sequence* :

- Changez l'instruction run-if pour *green_dot* en '[correct] = 1', indiquant qu'il doit être montré seulement après une réponse correcte.
- Changez l'instruction run-if pour *red_dot* en '[correct] = 0', indiquant qu'il doit être montré seulement après une réponse incorrecte.

La variable `correct` est automatiquement créée si la variable `correct_response` est disponible; c'est pourquoi nous avons défini `correct_response` à l'étape 7. Pour plus d'informations sur les variables et les instructions run-if, voir :

- %link:manuel/variables%

Le *trial_sequence* doit maintenant ressembler à %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  Le *trial_sequence* à la fin de l'étape 8.
--%

## Terminé!

Félicitations, l'expérience est terminée ! Vous pouvez la tester en appuyant sur le bouton double-flèche bleu (raccourci : `Ctrl+W`).

Si l'expérience ne fonctionne pas du premier coup : Ne vous inquiétez pas et cherchez calmement d'où vient l'erreur. Les crashs font partie du processus de développement normal. Mais vous pouvez vous épargner beaucoup de temps et de maux de tête en travaillant de manière structurée, comme nous l'avons fait dans ce tutoriel.

## Références

<div class='reference' markdown='1'>

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, 12(1), 97–136. doi:10.1016/0010-0285(80)90005-5

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
