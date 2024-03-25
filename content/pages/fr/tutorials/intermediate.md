title: Tutoriel intermédiaire (Python) recherche visuelle
hash: 2db5f6aa8a0276e362c99516e42c8d94a078dd3c52b5eacb7f4686da10b768df
locale: fr
language: French

[TOC]

## À propos d'OpenSesame

OpenSesame est un programme convivial pour le développement d'expériences comportementales en psychologie, neurosciences, et économie expérimentale. Pour les débutants, OpenSesame dispose d'une interface graphique complète et intuitive de pointage et de clic. Pour les utilisateurs avancés, OpenSesame prend en charge Python (uniquement sur le bureau) et JavaScript (sur le bureau et le navigateur).

OpenSesame est librement disponible sous la [General Public License v3][gpl].

## À propos de ce tutoriel

Ce tutoriel montre comment créer une expérience de recherche visuelle simple en utilisant OpenSesame [(Mathôt, Schreij, & Theeuwes, 2012)][references]. Nous utiliserons à la fois l'interface graphique et la programmation Python pour développer une expérience que vous pouvez exécuter sur le bureau dans un environnement de laboratoire traditionnel. Une certaine expérience avec OpenSesame et Python est recommandée. Ce tutoriel prend environ une heure.

Une version JavaScript de ce tutoriel est également disponible. Si vous souhaitez exécuter vos expériences en ligne dans un navigateur (avec OSWeb), alors le tutoriel JavaScript est ce dont vous avez besoin :

- %link:tutorials/intermediate-javascript%

## Ressources

- __Téléchargement__ — Ce tutoriel suppose que vous utilisez la version 4.0.0 ou ultérieure d'OpenSesame. Vous pouvez télécharger la version la plus récente d'OpenSesame à partir de :
	- %link:download%
- __Documentation__ — Un site web dédié à la documentation se trouve à :
	- <http://osdoc.cogsci.nl/>
- __Forum__ — Un forum de support est disponible à l'adresse :
	- <http://forum.cogsci.nl/>
- __Sigmund__ -- SigmundAI est un assistant IA doté d'une connaissance experte d'OpenSesame et est disponible à l'adresse :
	- <https://sigmundai.eu/>

## L'expérience

Dans ce tutoriel, vous allez créer une expérience de recherche visuelle de base. L'expérience ressemble aux études classiques de recherche visuelle de [Treisman et Gelade (1980)][references], mais n'est pas identique.

Dans cette expérience, les participants recherchent un objet cible, qui peut être un carré jaune, un cercle jaune, un carré bleu ou un cercle bleu ; l'identité de la cible varie entre les blocs d'essais. Les participants indiquent si la cible est présente ou non en appuyant sur la flèche de droite (présent) ou de gauche (absent).

En plus de la cible, zéro ou plusieurs objets distracteurs sont montrés. Il y a trois conditions, et la condition détermine quel type de distracteurs il y a :

- Dans la condition *Conjonction*, les distracteurs peuvent avoir n'importe quelle forme et couleur, avec la seule restriction que les distracteurs ne peuvent pas être identiques à la cible. Donc, par exemple, si la cible est un carré jaune, alors les distracteurs sont des cercles jaunes, des cercles bleus et des carrés bleus.
- Dans la condition *Caractéristique de Forme*, les distracteurs ont une forme différente de celle de la cible, mais peuvent avoir n'importe quelle couleur. Donc, par exemple, si la cible est un carré jaune, alors les distracteurs sont des cercles jaunes et des cercles bleus.
- Dans la condition *Caractéristique de Couleur*, les distracteurs peuvent avoir n'importe quelle forme, mais ont une couleur différente de celle de la cible. Donc, par exemple, si la cible est un carré jaune, alors les distracteurs sont des carrés bleus et des cercles bleus.

Un feedback immédiat est présenté après chaque essai : un point vert après une réponse correcte et un point rouge après une réponse incorrecte. Un feedback détaillé sur les temps de réponse moyens et la précision est montré après chaque bloc d'essais.

%--
figure:
 id: FigVisualSearch
 source: visual-search.svg
 caption: |
  L'expérience de recherche visuelle que vous allez implémenter dans ce tutoriel.
--%

Les expériences comme celle-ci montrent deux résultats typiques :

- Il faut plus de temps pour trouver la cible dans la condition Conjonction que dans les deux conditions Caractéristique.
- Dans la condition Conjonction, les temps de réponse augmentent à mesure que le nombre de distracteurs augmente. Cela suggère que les gens cherchent la cible un élément à la fois ; ceci est appelé *recherche sérielle*.
- Dans les conditions Caractéristique (forme et couleur), les temps de réponse n'augmentent pas, ou augmentent à peine, à mesure que le nombre de distracteurs augmente. Cela suggère que les gens traitent toute la scène en une seule fois ; ceci est appelé *recherche parallèle*.

Selon la théorie de l'intégration des caractéristiques de Treisman et Gelade, ces résultats montrent que la condition de Conjonction nécessite de combiner, ou *lier*, la couleur et la forme de chaque objet. Ce processus requiert de l'attention, et vous devez donc déplacer votre attention d'un objet à l'autre; ceci est lent, et explique pourquoi les temps de réaction dépendent du nombre d'objets. En revanche, dans les conditions de Caractéristique, la couleur et la forme n'ont pas besoin d'être liées, et donc l'ensemble du tableau peut être traité en un seul balayage sans que l'attention ne soit dirigée sur chaque objet.

## Conception expérimentale

Cette conception :

- Est *intra-sujet*, car tous les participants passent par toutes les conditions
- Est *entièrement croisée* (ou factorielle complète), car toutes les combinaisons de conditions se produisent
- A trois conditions (ou facteurs) :
	- Variées à l'intérieur des blocs :
		- `set_size` avec trois niveaux (1, 5, 15), ou SS<sub>3</sub>
		- `condition` avec trois niveaux (conjonction, feature_shape, feature_color), ou CN<sub>3</sub>
		- `target_present` avec deux niveaux (présent, absent), ou TP<sub>2</sub>
	- Variées entre les blocs :
		- `target_shape` avec deux niveaux (carré, cercle), ou TS<sub>2</sub>
		- `target_color` avec deux niveaux (jaune, bleu), ou TC<sub>2</sub>
- A N sujets, ou <u>S</u><sub>N</sub>

Vous pouvez écrire cette conception sous la forme <u>S</u><sub>N</sub>×SS<sub>3</sub>×CN<sub>3</sub>×TP<sub>2</sub>×TS<sub>2</sub>×TC<sub>2</sub>

Pour plus d'informations sur cette notation pour la conception expérimentale, voir:

- %link:experimentaldesign%

## Étape 1 : Créer la structure de base de l'expérience

Ouvrez OpenSesame et, dans l'onglet 'Get started!', sélectionnez le modèle Étendu. Ce modèle fournit la structure de base qui est courante dans de nombreuses expériences de psychologie cognitive, comme celle que nous allons créer ici.

Le modèle Étendu contient quelques éléments dont nous n'avons pas besoin. Supprimez les éléments suivants :

- *about_this_template*
- *practice_loop*
- *end_of_practice*

Lorsque vous avez supprimé ces éléments, ils sont toujours visibles dans la corbeille 'Unused items'. Pour supprimer définitivement ces éléments, cliquez sur la corbeille 'Unused items', puis cliquez sur le bouton 'Permanently delete unused items'.

Enfin, donnez un bon titre à l'expérience, comme 'Recherche visuelle'. Pour ce faire, ouvrez l'onglet des propriétés générales (en cliquant sur 'Extended template' dans la zone de présentation) et cliquez sur le nom de l'expérience pour le modifier.

La zone de présentation doit maintenant ressembler à la %FigStep1:

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  La zone de présentation à la fin de l'étape 1.
--%

## Étape 2 : Définir les variables expérimentales qui varient entre les blocs

Comme décrit ci-dessus, deux variables varient entre les blocs dans notre expérience : `target_shape` et `target_color`. Nous devons donc définir ces variables dans la *experimental_loop*. Pour comprendre pourquoi, considérez la structure montrée dans %FigStep1, en commençant par le bas (c'est-à-dire le niveau le plus indenté).

- *trial_sequence* correspond à un seul essai
- *block_loop* correspond à un bloc d'essais
	- Par conséquent, les variables définies ici varient pour chaque exécution de *trial_sequence* ; en d'autres termes, les variables définies dans *block_loop* varient __à l'intérieur des blocs__.
- *block_sequence* correspond à un bloc d'essais, précédé de la réinitialisation des variables de feedback, et suivi par le feedback des participants
- *experimental_loop* correspond à plusieurs blocs d'essais
	- Par conséquent, les variables définies ici varient pour chaque exécution de *block_sequence* ; en d'autres termes, les variables définies dans *experimental_loop* varient __entre les blocs__.
- *experiment* correspond à l'ensemble de l'expérience, qui est un écran d'instruction, suivi de plusieurs blocs d'essais, puis d'un écran de fin d'expérience

Cliquez sur experimental loop, et définissez :

- `target_shape`, qui peut être 'carré' ou 'cercle'; et
- `target_color`, qui peut être 'jaune' ou 'bleu'.

Nous avons un plan factoriel complet, ce qui signifie que toutes les 4 combinaisons de 2 × 2 doivent se produire. Le tableau de *experimental_loop* doit maintenant ressembler à %FigStep2 :

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  Le tableau de *experimental_loop* à la fin de l'étape 2.
--%

## Étape 3 : Donner des instructions au début de chaque bloc

En ce moment, l'expérience commence avec un seul écran *instructions*. Dans notre cas, nous voulons donner des instructions avant chaque bloc d'essais, pour indiquer au participant quelle cible rechercher (car l'identité de la cible varie entre les blocs).

__Déplacez les instructions dans block_sequence__

Alors, prenez l'élément *instructions* et faites-le glisser sur *block_sequence*. Une fenêtre contextuelle apparaîtra, vous demandant si vous voulez :

- Insérer l'élément dans *block_sequence*, dans ce cas *instructions* deviendrait le premier élément de *block_sequence* ; ou
- Insérer l'élément après *block_sequence*, dans ce cas *instructions* se déplacerait à une position après *block_sequence*.

Sélectionnez la première option ("Insérer dans"). Maintenant, *block_sequence* commence avec un écran d'instructions, ce que nous voulons.

__Ajouter un texte d'instruction__

Cliquez sur *instructions* pour l'ouvrir et ajoutez un bon texte d'instructions, tel que :

```text
INSTRUCTIONS

Cherchez le {target_color} {target_shape}

Appuyez sur la touche flèche droite si vous le trouvez
Appuyez sur la touche flèche gauche si vous ne le trouvez pas

Appuyez sur n'importe quelle touche pour commencer
```

Les accolades autour de '{target_color}' et '{target_shape}' indiquent qu'il ne s'agit pas de texte littéral, mais qu'elles font référence aux variables que nous avons définies dans *experimental_loop*. Lorsque l'expérience se déroule, les valeurs de ces variables apparaîtront ici et le participant verra (par exemple) "Cherchez le cercle jaune".

__Donnez un aperçu visuel de la cible__

Il est également bon de montrer au participant le stimulus réel qu'elle doit trouver. Pour ce faire :

- Dessinez un cercle rempli au centre de l'écran (assurez-vous qu'il ne chevauche pas le texte) ;
- Changez la couleur du cercle en '{target_color}'. Cela signifie que la couleur du cercle dépend de la valeur de la variable `target_color` ; et
- Changez l'expression show-if pour `target_shape == 'circle'`. Il s'agit d'une expression Python qui vérifie si la variable `target_shape` a la valeur 'circle'.

En d'autres termes, nous avons dessiné un cercle dont la couleur est déterminée par `target_color` ; en outre, ce cercle n'est montré que lorsque la variable `target_shape` a la valeur 'circle'. Pour plus d'informations sur les variables et les instructions show-if, voir :

- %link:manual/variables%

Nous utilisons la même astuce pour dessiner un carré :

- Dessinez un carré rempli au centre de l'écran ;
- Changez la couleur du carré en '{target_color}' ; et
- Changez l'instruction show-if pour `target_shape == 'square'`

L'écran *instructions* devrait maintenant ressembler à %FigStep3 :

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  L'écran *instructions* à la fin de l'étape 3.
--%

## Étape 4 : Définir les variables expérimentales qui varient au sein des blocs

Trois variables varient au sein des blocs dans notre expérience : `condition`, `set_size` et `target_present`. Comme décrit à l'étape 2, nous devons définir ces variables dans le *block_loop* de manière à ce qu'elles varient pour chaque exécution de *trial_sequence*.

Les trois variables produisent un total de 3 × 3 × 2 = 18 combinaisons différentes. Nous pouvons les saisir manuellement dans le tableau, mais, comme nous avons un plan factoriel complet, nous pouvons également utiliser l'assistant de plan factoriel complet. Pour ce faire, ouvrez d'abord *block_loop* et cliquez sur le bouton "Plan factoriel complet".

Dans le tableau qui apparaît, placez les noms des variables sur la première ligne et les valeurs sur les lignes ci-dessous, comme le montre %FigFullFactorial.

%--
figure:
 id: FigFullFactorial
 source: fullfactorial.png
 caption: |
  L'écran *instructions* à la fin de l'étape 3.
--%

Cliquez maintenant sur "Ok" pour générer le plan complet. Le tableau de *block_loop* devrait maintenant ressembler à %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  Le tableau de *block_loop* à la fin de l'étape 4.
--%

## Étape 5 : Créer la séquence d'essais

Nous voulons que notre séquence d'essais se déroule comme suit :

- Un point de fixation, pour lequel nous utiliserons un SKETCHPAD.
- Un affichage de recherche, que nous créerons en Python avec un INLINE_SCRIPT personnalisé.
- La collecte des réponses, pour laquelle nous utiliserons un KEYBOARD_RESPONSE.
- La journalisation des données, pour laquelle nous utiliserons un LOGGER.
- (Nous voulons également avoir des retours immédiats après chaque essai, mais nous y reviendrons plus tard.)

La seule chose qui manque est un INLINE_SCRIPT.

- Insérez un nouvel INLINE_SCRIPT après *sketchpad* et renommez-le *search_display_script*.
- Renommez *sketchpad* en *fixation_dot*, afin que sa fonction soit claire ; et
- Modifiez la durée de *fixation_dot* à 500, afin que le point de fixation soit affiché pendant 500 ms. (Il devrait déjà y avoir un point de fixation dessiné ; sinon, dessinez-en un au centre de *fixation_dot*.)

La zone d'aperçu doit maintenant ressembler à %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  La zone d'aperçu à la fin de l'étape 5.
--%

## Étape 6 : Générer l'affichage de recherche

__Programmation descendante et défensive__

Maintenant, les choses vont devenir intéressantes : nous allons commencer à programmer en Python. Nous utiliserons deux principes directeurs : la programmation *descendante* et *défensive*.

- La *programmation descendante* signifie que nous commençons avec la logique la plus abstraite, sans nous soucier de la façon dont cette logique est mise en œuvre. Une fois que la logique la plus abstraite est en place, nous descendons à un niveau de logique légèrement moins abstrait, et ainsi de suite, jusqu'à atteindre les détails de l'implémentation. Cette technique permet de garder le code structuré.
- La *programmation défensive* signifie que nous supposons que nous faisons des erreurs. Par conséquent, pour nous protéger de nous-mêmes, nous intégrons des vérifications de cohérence dans le code.

*Remarque :* L'explication ci-dessous suppose que vous êtes un peu familiarisé avec le code Python. Si des concepts comme `list`, `tuple` et fonctions ne vous disent rien, alors il est préférable de suivre d'abord un tutoriel Python d'introduction, comme celui-ci :

- <https://pythontutorials.eu/>

La logique du code est représentée dans %FigHierarchy. Les chiffres indiquent l'ordre dans lequel nous mettrons en œuvre la fonctionnalité, en commençant par le niveau abstrait.

%--
figure:
 id: FigHierarchy
 source: hierarchy.svg
 caption: |
  La logique du code pour dessiner un affichage de recherche visuelle.
--%

__Les phases Préparer et Exécuter__

Ouvrez *search_display_script* et passez à l'onglet Préparer. OpenSesame distingue deux phases d'exécution :

- Pendant la phase Préparer, chaque élément a l'occasion de se préparer ; cela dépend de l'élément : pour un SKETCHPAD, cela signifie dessiner un canevas (mais ne pas l'afficher) ; pour un SAMPLER, cela signifie charger un fichier son (mais ne pas le jouer) ; etc.
- Pendant la phase Exécuter, chaque élément est réellement exécuté ; là encore, cela dépend de l'élément : pour un SKETCHPAD, cela signifie afficher le canevas préparé précédemment ; pour un SAMPLER, cela signifie jouer un fichier son chargé précédemment.

Pour un INLINE_SCRIPT, vous devez décider vous-même ce qu'il faut mettre dans la phase Préparer et ce qu'il faut mettre dans la phase Exécuter. La distinction est généralement assez claire : dans notre cas, nous mettons le code pour dessiner le canevas dans la phase Préparer et le code pour afficher le canevas (qui est petit) dans la phase Exécuter.

Voir aussi :

- %link:prepare-run%

__Mettre en œuvre le niveau abstrait__

Nous commençons par le niveau le plus abstrait : définir une fonction qui dessine un affichage de recherche visuelle. Nous ne spécifions pas *comment* cela se fait ; nous supposons simplement qu'il y a une fonction qui le fait, et nous nous préoccuperons des détails plus tard - c'est la programmation descendante.

Dans l'onglet Préparer, entrez le code suivant :

~~~ .python
c = draw_canvas()
~~~

Que se passe-t-il ici ? Nous …

- Appelez `draw_canvas()`, qui renvoie un objet `Canvas` que nous stockons sous forme de `c`; en d'autres termes, `c` est un objet `Canvas` qui correspond à l'affichage de recherche. Ceci suppose qu'il y a une fonction `draw_canvas()`, même si nous ne l'avons pas encore définie.

Un objet `Canvas` est un écran unique; il est, en un sens, l'équivalent Python d'un SKETCHPAD. Voir également:

- %link:manual/python/canvas%

Nous définissons maintenant `draw_canvas()` (au-dessus du reste du script jusqu'à présent):

~~~ .python
def draw_canvas():
    """Dessine le canevas de recherche.

    Returns
    -------
    Canvas
    """
    c = Canvas()
    xy_list = xy_random(n=set_size, width=500, height=500, min_dist=75)
    if target_present == 'present':
        x, y = xy_list.pop()
        draw_target(c, x, y)
    elif target_present != 'absent':
        raise Exception(f'Valeur non valide pour target_present: {target_present}')
    for x, y in xy_list:
        draw_distractor(c, x, y)
    return c
~~~

Que se passe-t-il ici ? Nous …

- Créons un canevas vide, `c`, à l'aide de la fonction de fabrication `Canvas()`.
- Générons une liste de coordonnées `x, y` aléatoires, appelée `xy_list`, en utilisant une autre fonction courante, `xy_random()`. Cette liste détermine où les stimuli sont montrés.
- Vérifiez si la variable expérimentale `target_present` a la valeur 'present'; si c'est le cas, `pop()` un tuple `x, y` de `xy_list`, et dessinez la cible à cet endroit. Ceci suppose qu'il y a une fonction `draw_target()`, même si nous ne l'avons pas encore définie.
- Si `target_present` n'est ni 'present' ni 'absent', on soulève une `Exception`; c'est de la programmation défensive, et cela nous protège des fautes de frappe (par exemple, si nous avions accidentellement entré 'presenr' au lieu de 'present').
- Bouclez à travers tous les autres tuples `x, y` et dessinez un distractor à chaque position. Ceci suppose qu'il y a une fonction `draw_distractor()`, même si nous ne l'avons pas encore définie.
- Retourne `c`, qui a maintenant l'affichage de recherche dessiné dessus.

Il y a plusieurs fonctions communes, telles que `Canvas()` et `xy_random()`, qui sont toujours disponibles. Voir:

- %link:manual/python/common%

Les variables expérimentales sont des variables globales. C'est pourquoi vous pouvez vous référer à `set_size`, qui est défini dans *block_loop*, même si la variable `set_size` n'est jamais explicitement définie dans le script. La même chose est vraie pour `target_shape`, `target_color`, `condition`, etc. Voir:

- %link:var%

__Mettre en oeuvre le niveau intermédiaire__

Nous descendons encore d'un cran en définissant `draw_target` (au-dessus du reste du script jusqu'à présent):

~~~ .python
def draw_target(c, x, y):
    """Dessine la cible.

    Paramètres
    ----------
    c: Canvas
    x: int
    y: int
    """
    draw_shape(c, x, y, color=target_color, shape=target_shape)
~~~

Que se passe-t-il ici ? Nous …

- Appelons une autre fonction, `draw_shape()`, et spécifions la couleur et la forme à dessiner. Ceci suppose qu'il y a une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

Nous définissons également `draw_distractor` (au-dessus du reste du script jusqu'à présent):

~~~ .python
def draw_distractor(c, x, y):
    """Dessine un seul distractor.

    Paramètres
    ----------
    c: Canvas
    x: int
    y: int
    """
    if condition == 'conjunction':
        draw_conjunction_distractor(c, x, y)
    elif condition == 'feature_shape':
        draw_feature_shape_distractor(c, x, y)
    elif condition == 'feature_color':
        draw_feature_color_distractor(c, x, y)
    else:
        raise Exception(f'Condition invalide: {condition}')
~~~

Que se passe-t-il ici ? Nous …

- Appelons une autre fonction pour dessiner un distractor plus spécifique selon la Condition.
- Vérifiez si `condition` a l'une des valeurs attendues. Si ce n'est pas le cas, soulevez une `Exception`. C'est de la programmation défensive ! Sans cette vérification, si nous faisions une erreur de frappe quelque part, le distracteur pourrait simplement ne pas être montré sans provoquer de message d'erreur.

Maintenant, nous définissons la fonction qui dessine les distracteurs dans la condition Conjunction (au-dessus du reste du script jusqu'à présent):

~~~ .python
import random

def draw_conjunction_distractor(c, x, y):
    """Dessine un seul distracteur dans la condition de conjonction : un objet qui
    peut avoir n'importe quelle forme et couleur, mais ne peut pas être identique à la cible.

    Paramètres
    ----------
    c: Canvas
    x: int
    y: int
    """
    conjunctions = [('jaune', 'cercle'),
                    ('bleu',   'cercle'),
                    ('jaune', 'carré'),
                    ('bleu',   'carré')]
    conjunctions.remove((target_color, target_shape))
    color, shape = random.choice(conjunctions)
    draw_shape(c, x, y, color=color, shape=shape)
~~~

Que se passe-t-il ici ? Nous …

- Définissons une liste, `conjunctions`, de toutes les combinaisons possibles de couleur et de forme.
- Retirons la cible de cette liste ; cela est nécessaire car le distracteur ne peut pas être identique à la cible.
- Sélectionnons aléatoirement une des combinaisons de couleur et de forme de `conjunctions`.
- Appelons une autre fonction, `draw_shape()`, et spécifions la couleur et la forme du distracteur à dessiner. Ceci suppose qu'il existe une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

De plus, nous …

- Ajoutons la ligne `import random` en haut du script. Ceci est nécessaire pour pouvoir utiliser des fonctions qui font partie du module `random`, telles que `random.choice()`.

Maintenant, nous définissons la fonction qui dessine les distracteurs dans la condition de caractéristique de forme (juste en dessous de l'instruction `import`) :

~~~ .python
def draw_feature_shape_distractor(c, x, y):
    """Dessine un seul distracteur dans la condition de caractéristique de forme : un objet qui
    a une forme différente de la cible, mais peut avoir n'importe quelle couleur.

    Paramètres
    ----------
    c: Canvas
    x: int
    y: int
    """
    colors = ['jaune', 'bleu']
    color = random.choice(colors)
    if target_shape == 'cercle':
        shape = 'carré'
    elif target_shape == 'carré':
        shape = 'cercle'
    else:
        raise Exception(f'Invalid target_shape: {target_shape}')
    draw_shape(c, x, y, color=color, shape=shape)
~~~

Que se passe-t-il ici ? Nous …

- Sélectionnons aléatoirement une couleur.
- Choisissons une forme carrée si la cible est un cercle, et une forme circulaire si la cible est carrée.
- If `target_shape` is neither 'cercle' nor 'carré', raise an `Exception`—more defensive programming!
- Appelons une autre fonction, `draw_shape()`, et spécifions la couleur et la forme du distracteur à dessiner. Ceci suppose qu'il existe une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

Maintenant, nous définissons la fonction qui dessine les distracteurs dans la condition de caractéristique de couleur (juste en dessous de l'instruction `import`) :

~~~ .python
def draw_feature_color_distractor(c, x, y):
    """Dessine un seul distracteur dans la condition de caractéristique de couleur : un objet qui
    a une couleur différente de la cible, mais peut avoir n'importe quelle forme.

    Paramètres
    ----------
    c: Canvas
    x: int
    y: int
    """
    shapes = ['cercle', 'carré']
    shape = random.choice(shapes)
    if target_color == 'jaune':
        color = 'bleu'
    elif target_color == 'bleu':
        color = 'jaune'
    else:
        raise Exception(f'Invalid target_color: {target_color}')
    draw_shape(c, x, y, color=color, shape=shape)
~~~

Que se passe-t-il ici ? Nous …

- Sélectionnons aléatoirement une forme.
- Choisissons une couleur bleue si la cible est jaune, et une couleur jaune si la cible est bleue.
- If `target_color` is neither 'jaune' nor 'bleu', raise an `Exception`—more defensive programming!
- Appelons une autre fonction, `draw_shape()`, et spécifions la couleur et la forme du distracteur à dessiner. Ceci suppose qu'il existe une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

__Mettre en œuvre le niveau de détail__

Maintenant, nous allons jusqu'au bout des détails en définissant la fonction qui dessine réellement une forme sur le canevas (juste en dessous de l'instruction `import`) :

~~~ .python
def draw_shape(c, x, y, color, shape):
    """Dessine une seule forme.

Paramètres
----------
c: Canvas
x: int
y: int
color: str
shape: str
"""
if shape == 'carré':
    c += Rect(x=x-25, y=y-25, w=50, h=50, color=color, fill=True)
elif shape == 'cercle':
    c += Circle(x=x, y=y, r=25, color=color, fill=True)
else:
    raise Exception(f'Forme invalide: {shape}')
if color not in ['jaune', 'bleu']:
    raise Exception(f'Couleur invalide: {color}')
~~~

Que se passe-t-il ici ? Nous...

- Vérifions quelle forme doit être dessinée. Pour les carrés, nous ajoutons un élément `Rect()` au canevas. Pour les cercles, nous ajoutons un élément `Circle()`.
- Vérifions si la forme est un carré ou un cercle, et si ce n'est pas le cas, génère une `Exception`. C'est un autre exemple de programmation défensive ! Nous nous assurons que nous n'avons pas accidentellement spécifié une forme invalide.
- Vérifions si la couleur n'est ni jaune ni bleu, et si ce n'est pas le cas, génère une `Exception`.

__Mettre en œuvre la phase Run__

Comme nous avons fait tout le travail difficile dans la phase de préparation, la phase Run est simplement :

~~~ .python
c.show()
~~~

C'est tout ! Maintenant, vous avez dessiné un affichage complet de recherche visuelle. Et, surtout, vous l'avez fait de manière à être facile à comprendre, grâce à la programmation top-down, et sûre, grâce à la programmation défensive.

## Étape 7 : Définir la réponse correcte

Pour savoir si le participant répond correctement, nous devons connaître la réponse correcte. Vous pouvez définir cela explicitement dans le *bloc_loop* (comme dans le tutoriel débutant) ; mais ici, nous allons utiliser un simple script Python qui vérifie si la cible est présente ou non, et définit la réponse correcte en conséquence.

Pour ce faire, insérez un nouveau SCRIPT_EN_LIGNE au début de *trial_sequence*, et renommez-le en *correct_response_script*. Dans la phase de préparation (pas la phase Run !), entrez le code suivant :

~~~ .python
if target_present == 'présent':
    correct_response = 'droite'
elif target_present == 'absent':
    correct_response = 'gauche'
else:
    raise Exception(f'target_present doit être absent ou présent, pas {target}')
~~~

Que se passe-t-il ici ? Nous...

- Vérifions si la cible est présente ou non. Si la cible est présente, la réponse correcte est 'droite' (la touche flèche droite) ; si la cible est absente, la réponse correcte est 'gauche' (la touche flèche gauche). La variable expérimentale (globale) `correct_response` est automatiquement reconnue par *keyboard_response* ; par conséquent, nous n'avons pas besoin d'indiquer explicitement que cette variable contient la réponse correcte.
- Vérifions si la cible est présente ou absente, et si ce n'est pas le cas, génère une `Exception` - un autre exemple de programmation défensive.

## Étape 8 : Donner un retour d'information par essai

Un retour d'information après chaque essai peut motiver les participants ; cependant, un retour d'information par essai ne doit pas interférer avec le déroulement de l'expérience. Un bon moyen de donner un retour d'information par essai est de montrer brièvement un point de fixation vert après une réponse correcte et un point de fixation rouge après une réponse incorrecte.

Pour ce faire :

- Insérez deux nouvelles ZONES DE DESSIN dans *trial_sequence*, juste après *keyboard_response*.
- Renommez une ZONE DE DESSIN en *green_dot*, dessinez un point de fixation vert central dessus, et changez sa durée à 500.
- Renommez l'autre ZONE DE DESSIN en *red_dot*, dessinez un point de fixation rouge central dessus, et changez sa durée à 500.

Bien sûr, un seul des deux points doit être affiché à chaque essai. Pour réaliser cela, nous allons spécifier des expressions run-if dans *trial_sequence* :

- Modifiez l'expression run-if pour *green_dot* en 'correct == 1', indiquant qu'il ne doit être affiché qu'après une réponse correcte.
- Modifiez l'expression run-if pour *red_dot* en 'correct == 0', indiquant qu'il ne doit être affiché qu'après une réponse incorrecte.

La variable `correct` est automatiquement créée si la variable `correct_response` est disponible ; c'est pourquoi nous avons défini `correct_response` à l'étape 7. Pour plus d'informations sur les variables et les instructions run-if, voir :

- %lien:manuel/variables%

Le *trial_sequence* devrait maintenant ressembler à %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  Le *trial_sequence* à la fin de l'étape 8.
--%

## Fini !

Félicitations, l'expérience est terminée ! Vous pouvez la tester en appuyant sur le bouton des doubles flèches bleues (raccourci : `Ctrl+W`).

Si l'expérience ne fonctionne pas du premier coup : Ne vous inquiétez pas et calmement cherchez d'où l'erreur provient. Les plantages sont une partie normale du processus de développement. Mais vous pouvez vous épargner beaucoup de temps et de maux de tête en travaillant de manière structurée, comme nous l'avons fait dans ce tutoriel.

## Références

<div class='reference' markdown='1'>

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame : Un créateur d'expériences graphique open-source pour les sciences sociales. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Treisman, A. M., & Gelade, G. (1980). Une théorie de l'intégration des caractéristiques de l'attention. *Cognitive Psychology*, 12(1), 97–136. doi:10.1016/0010-0285(80)90005-5

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html