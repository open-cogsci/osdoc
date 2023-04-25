title: Tutoriel intermédiaire (JavaScript) : recherche visuelle
uptodate: false
hash: 358819a2bc08c033a30633e8e900731a0deb61f115286351f3291d6f433aba7f
locale: fr
language: French

[TOC]

## À propos d'OpenSesame

OpenSesame est un programme convivial pour le développement d'expériences comportementales en psychologie, neurosciences et économie expérimentale. Pour les débutants, OpenSesame propose une interface graphique complète en mode point-and-click. Pour les utilisateurs avancés, OpenSesame prend en charge Python (seulement sur ordinateur) et JavaScript (pour ordinateur et navigateur).

OpenSesame est disponible gratuitement sous la [General Public License v3][gpl].

## À propos de ce tutoriel

Ce tutoriel montre comment créer une expérience de recherche visuelle de base à l'aide d'OpenSesame [(Mathôt, Schreij, & Theeuwes, 2012)][references]. Nous utiliserons à la fois l'interface graphique et JavaScript. Une certaine expérience avec OpenSesame et JavaScript est recommandée. Ce tutoriel dure environ une heure.

Une version Python de ce tutoriel est également disponible. Si vous n'avez pas besoin d'exécuter vos expériences en ligne, le tutoriel Python est probablement ce dont vous avez besoin :

- %link:tutorials/intermediate%


## Ressources

- __Téléchargement__ — Ce tutoriel suppose que vous utilisez la version 3.3.10 d'OpenSesame ou ultérieure et OSWeb 1.4 ou ultérieure. Vous pouvez télécharger la version la plus récente d'OpenSesame à partir de :
	- %link:download%
- __Documentation__ — Un site web dédié à la documentation se trouve à :
	- < http://osdoc.cogsci.nl/ >
- __Forum__ — Un forum d'assistance se trouve à :
	- < http://forum.cogsci.nl/ >


## L'expérience

Dans ce tutoriel, vous créerez une expérience de recherche visuelle de base. L'expérience ressemble aux études classiques de recherche visuelle de [Treisman et Gelade (1980)][references], mais elle n'est pas identique.

Avant de commencer à *construire* l'expérience par vous-même, vous pouvez déjà *participer* à celle-ci. Cela vous donnera une bonne idée de ce que vous allez réaliser dans ce tutoriel.

<a role="button" class="btn btn-success btn-align-left" href="https://jatos.mindprobe.eu/publix/1938/start?batchId=2191&generalMultiple">Participez à l'expérience !</a>

Dans cette expérience, les participants recherchent un objet cible, qui peut être un carré jaune, un cercle jaune, un carré bleu ou un cercle bleu ; l'identité de la cible varie entre les blocs d'essais. Les participants indiquent si la cible est présente ou non en appuyant sur la flèche droite (présente) ou gauche (absente) du clavier.

En plus de la cible, zéro ou plusieurs objets distracteurs sont affichés. Il y a trois conditions, et la condition détermine le type de distracteurs :

- Dans la condition *Conjonction*, les distracteurs peuvent avoir n'importe quelle forme et couleur, à condition qu'ils ne soient pas identiques à la cible. Par exemple, si la cible est un carré jaune, les distracteurs sont des cercles jaunes, des cercles bleus et des carrés bleus.
- Dans la condition *Caractéristique de forme*, les distracteurs ont une forme différente de la cible, mais peuvent avoir n'importe quelle couleur. Par exemple, si la cible est un carré jaune, les distracteurs sont des cercles jaunes et des cercles bleus.
- Dans la condition *Caractéristique de couleur*, les distracteurs peuvent avoir n'importe quelle forme, mais ont une couleur différente de la cible. Par exemple, si la cible est un carré jaune, les distracteurs sont des carrés bleus et des cercles bleus.

Un retour d'information immédiat est affiché après chaque essai : un point vert après une réponse correcte et un point rouge après une réponse incorrecte. Un retour d'information détaillé sur les temps de réponse moyens et la précision est affiché après chaque bloc d'essais.

%--
figure:
 id: FigVisualSearch
 source: visual-search.svg
 caption: | 
  L'expérience de recherche visuelle que vous allez implémenter dans ce tutoriel.
--%

Des expériences comme celle-ci montrent deux résultats typiques :

- Il faut plus de temps pour trouver la cible dans la condition de Conjonction que dans les deux conditions de Caractéristique.
- Dans la condition de Conjonction, les temps de réponse augmentent à mesure que le nombre de distracteurs augmente. Cela suggère que les personnes recherchent la cible un élément à la fois ; cela s'appelle une *recherche sérielle*.
- Dans les conditions de Caractéristique (forme et couleur), les temps de réponse n'augmentent pas, ou très peu, à mesure que le nombre de distracteurs augmente. Cela suggère que les personnes traitent l'ensemble de l'affichage en une seule fois ; cela s'appelle une *recherche parallèle*.

Selon la théorie de l'intégration des caractéristiques de Treisman et Gelade, ces résultats reflètent que la condition de Conjonction nécessite de combiner, ou *lier*, la couleur et la forme de chaque objet. Cette liaison nécessite de l'attention, et vous devez donc déplacer votre attention d'un objet à l'autre ; cela est lent, et explique pourquoi les temps de réponse dépendent du nombre d'objets présents. En revanche, dans les conditions de Caractéristique, la couleur et la forme n'ont pas besoin d'être liées, et donc l'ensemble de l'affichage peut être traité en un seul balayage sans que l'attention ne soit dirigée vers chaque objet individuellement.

## Conception expérimentale

Cette conception :

- Est *intrasujet*, car tous les participants effectuent toutes les conditions
- Est *entièrement croisée* (ou factorielle complète), car toutes les combinaisons de conditions se produisent
- Comporte trois conditions (ou facteurs) :
	- Variées au sein des blocs :
		- `set_size` avec trois niveaux (1, 5, 15), soit SS<sub>3</sub>
		- `condition` avec trois niveaux (conjonction, caractéristique_forme, caractéristique_couleur), soit CN<sub>3</sub>
		- `target_present` avec deux niveaux (présent, absent), soit TP<sub>2</sub>
	- Variées entre les blocs :
		- `target_shape` avec deux niveaux (carré, cercle), soit TS<sub>2</sub>
		- `target_color` avec deux niveaux (jaune, bleu), soit TC<sub>2</sub>
- Comporte N sujets, soit <u>S</u><sub>N</sub>

Vous pouvez écrire cette conception sous la forme <u>S</u><sub>N</sub>×SS<sub>3</sub>×CN<sub>3</sub>×TP<sub>2</sub>×TS<sub>2</sub>×TC<sub>2</sub>

Pour plus d'informations sur cette notation pour la conception expérimentale, consultez :

- %link:experimentaldesign%

## Étape 1 : Créer la structure de base de l'expérience

Lancez OpenSesame et, dans l'onglet 'Commencer !', sélectionnez le modèle Extended. Ce modèle fournit la structure de base commune à de nombreuses expériences de psychologie cognitive, comme celle que nous allons créer ici.

Le modèle Extended contient quelques éléments dont nous n'avons pas besoin. Supprimez les éléments suivants :

- *about_this_template*
- *practice_loop*
- *end_of_practice*

Lorsque vous avez supprimé ces éléments, ils sont toujours visibles dans la corbeille "Unused items". Pour supprimer définitivement ces éléments, cliquez sur la corbeille "Unused items", puis sur le bouton "Supprimer définitivement les éléments inutilisés".

Enfin, donnez à l'expérience un bon titre, comme "Recherche visuelle". Pour ce faire, ouvrez l'onglet des propriétés générales (en cliquant sur "Extended template" dans la zone de vue d'ensemble) et cliquez sur le nom de l'expérience pour le modifier.

La zone de vue d'ensemble devrait maintenant ressembler à %FigStep1 :

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  La zone de vue d'ensemble à la fin de l'étape 1.
--%

## Étape 2 : Définir les variables expérimentales qui varient entre les blocs

Comme décrit ci-dessus, deux variables varient entre les blocs dans notre expérience : `target_shape` et `target_color`. Nous devons donc définir ces variables dans la *experimental_loop*. Pour comprendre pourquoi, considérez la structure montrée dans %FigStep1, en commençant par le bas (c.-à-d. le niveau le plus indenté).

- *trial_sequence* correspond à un essai unique
- *block_loop* correspond à un bloc d'essais
	- Par conséquent, les variables définies ici varient pour chaque exécution de *trial_sequence* ; en d'autres termes, les variables définies dans *block_loop* varient __au sein des blocs__.
- *block_sequence* correspond à un bloc d'essais, précédé par la réinitialisation des variables de feedback, et suivi par un feedback du participant
- *experimental_loop* correspond à plusieurs blocs d'essais
	- Par conséquent, les variables définies ici varient pour chaque exécution de *block_sequence* ; en d'autres termes, les variables définies dans *experimental_loop* varient __entre les blocs__.
- *experiment* correspond à l'ensemble de l'expérience, qui est un écran d'instruction, suivi de plusieurs blocs d'essais, suivi d'un écran de fin d'expérience

Cliquez sur experimental loop, et définissez :

- `target_shape`, qui peut être 'carré' ou 'cercle' ; et
- `target_color`, qui peut être 'jaune' ou 'bleu'.

Nous avons un plan factoriel complet, ce qui signifie que les 4 combinaisons 2 × 2 doivent se produire. La table de *experimental_loop* doit maintenant ressembler à %FigStep2:

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  La table de *experimental_loop* à la fin de l'étape 2.
--%

## Étape 3 : Donner des instructions au début de chaque bloc

Pour l'instant, l'expérience commence par un écran unique d'*instructions*. Dans notre cas, nous voulons donner des instructions avant chaque bloc d'essais, pour indiquer au participant quelle cible rechercher (car l'identité de la cible varie entre les blocs).

__Déplacer les instructions dans block_sequence__

Pour cela, prenez l'élément *instructions* et faites-le glisser sur *block_sequence*. Une fenêtre contextuelle apparaîtra, vous demandant si vous souhaitez :

- Insérer l'élément dans *block_sequence*, auquel cas *instructions* deviendrait le premier élément de *block_sequence* ; ou
- Insérer l'élément après *block_sequence*, auquel cas *instructions* passerait à une position après *block_sequence*.

Sélectionnez la première option ('Insérer dans'). *block_sequence* commence maintenant par un écran d'instructions, ce que nous voulons.

__Ajouter du texte d'instruction__

Cliquez sur *instructions* pour l'ouvrir et ajoutez un bon texte d'instruction, tel que :

```text
INSTRUCTIONS

Recherchez le [target_shape] [target_color]

Appuyez sur la touche flèche droite si vous le trouvez
Appuyez sur la touche flèche gauche si vous ne le trouvez pas

Appuyez sur n'importe quelle touche pour commencer
```

Les crochets autour de '[target_color]' et '[target_shape]' indiquent qu'il ne s'agit pas de texte littéral, mais qu'ils font référence aux variables que nous avons définies dans *experimental_loop*. Lorsque l'expérience se déroule, les valeurs de ces variables apparaîtront ici et le participant verra (par exemple) 'Recherchez le cercle jaune'.

__Donner un aperçu visuel de la cible__

Il est également bon de montrer au participant le stimulus qu'elle doit trouver. Pour ce faire :

- Dessinez un cercle rempli au centre de l'affichage (assurez-vous qu'il ne chevauche pas le texte) ;
- Changez la couleur du cercle en '[target_color]'. Cela signifie que la couleur du cercle dépend de la valeur de la variable `target_color` ; et
- Changez la déclaration show-if en '[target_shape] = cercle'.

En d'autres termes, nous avons dessiné un cercle dont la couleur est déterminée par `target_color` ; en outre, ce cercle n'est affiché que lorsque la variable `target_shape` a la valeur 'cercle'. Pour plus d'informations sur les variables et les déclarations show-if, voir :

- %link:manuel/variables%

Nous utilisons la même astuce pour dessiner un carré :

- Dessinez un carré rempli au centre de l'affichage ;
- Changez la couleur du carré en '[target_color]'; et
- Changez la déclaration show-if en '[target_shape] = carré'

L'écran *instructions* doit maintenant ressembler à %FigStep3:

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  L'écran *instructions* à la fin de l'étape 3.
--%

## Étape 4 : Définir les variables expérimentales qui varient au sein des blocs

Trois variables varient à l'intérieur des blocs de notre expérience : `condition`, `set_size` et `target_present`. Comme décrit à l'étape 2, nous devons définir ces variables dans la *block_loop* afin qu'elles varient à chaque exécution de *trial_sequence*.

Les trois variables représentent un total de 3 × 3 × 2 = 18 combinaisons différentes. Nous pouvons les saisir manuellement dans le tableau, mais, comme nous avons un plan factoriel complet, nous pouvons également utiliser l'assistant de plan factoriel complet. Pour ce faire, ouvrez d'abord *block_loop* et cliquez sur le bouton «Full-factorial design».

Dans le tableau qui apparaît, mettez les noms des variables sur la première ligne et les valeurs sur les lignes ci-dessous, comme indiqué dans %FigFullFactorial.

%--
figure:
 id: FigFullFactorial
 source: fullfactorial.png
 caption: |
  L'écran *instructions* à la fin de l'étape 3.
--%

Cliquez maintenant sur «Ok» pour générer le plan complet. Le tableau de *block_loop* devrait maintenant ressembler à %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  Le tableau de *block_loop* à la fin de l'étape 4.
--%

## Étape 5: Créer la séquence de test

Nous voulons que notre séquence de test soit:

- Un point de fixation, pour lequel nous utiliserons un SKETCHPAD.
- Un écran de recherche, que nous créerons en JavaScript avec un custom INLINE_JAVASCRIPT.
- La collecte des réponses, pour laquelle nous utiliserons un KEYBOARD_RESPONSE.
- L'enregistrement des données, pour lequel nous utiliserons un LOGGER.
- (Nous souhaitons également avoir des commentaires immédiats après chaque essai, mais nous y reviendrons plus tard.)

La seule chose qui manque est un INLINE_JAVASCRIPT.

- Insérez un nouvel INLINE_JAVASCRIPT après *sketchpad* et renommez-le en *search_display_script*.
- Renommez *sketchpad* en *fixation_dot*, afin que sa fonction soit claire;
- Changez la durée de *fixation_dot* à 500, pour que le point de fixation soit affiché pendant 500 ms. (Un point de fixation devrait déjà être dessiné ; sinon, en dessinez un au centre de *fixation_dot*.)

La zone d'aperçu devrait maintenant ressembler à %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  La zone d'aperçu à la fin de l'étape 5.
--%

## Étape 6: Générer l'affichage de recherche

__Programmation ascendante et défensive__

Les choses vont devenir intéressantes : Nous allons commencer à programmer en JavaScript. Nous utiliserons deux principes directeurs : la programmation *ascendante* et *défensive*.

- La *programmation ascendante* signifie que nous commençons par la logique la plus abstraite, sans nous soucier de la manière dont cette logique est mise en œuvre. Une fois que la logique la plus abstraite est en place, nous passons à un niveau de logique légèrement moins abstrait et ainsi de suite, jusqu'à ce que nous arrivions aux détails de la mise en œuvre. Cette technique contribue à garder le code structuré.
- La *programmation défensive* signifie que nous supposons que nous faisons des erreurs. Par conséquent, pour nous protéger de nous-mêmes, nous intégrons des vérifications de cohérence dans le code.

*Remarque:* L'explication ci-dessous suppose que vous êtes un peu familiarisé avec JavaScript. Si des concepts tels que `Array`, `for` loop et les fonctions ne signifient rien pour vous, il est préférable de suivre d'abord un tutoriel JavaScript d'introduction. Vous pouvez trouver des liens vers des tutoriels JavaScript ici:

- %link:manual/javascript/about%

La logique du code est illustrée dans %FigHierarchy. Les chiffres indiquent dans quel ordre nous mettrons en œuvre les fonctionnalités, en commençant par le niveau abstrait.

%--
figure:
 id: FigHierarchy
 source: hierarchy.svg
 caption: |
  La logique du code pour dessiner un affichage de recherche visuelle.
--%

__Les phases de préparation et d'exécution__

Ouvrez *search_display_script* et passez à l'onglet Préparer. OpenSesame distingue deux phases d'exécution:

- Pendant la phase de préparation, chaque élément a l'occasion de se préparer ; ce que cela signifie dépend de l'élément : pour un SKETCHPAD, cela signifie dessiner un canevas (mais ne pas le montrer) ; pour un SAMPLER, cela signifie charger un fichier son (mais ne pas le jouer) ; etc.
- Pendant la phase d'exécution, chaque élément est effectivement exécuté ; là encore, ce que cela signifie dépend de l'élément : pour un SKETCHPAD, cela signifie montrer le canevas préparé précédemment ; pour un SAMPLER, cela signifie jouer un fichier son précédemment chargé.

Pour un INLINE_JAVASCRIPT, vous devez décider vous-même quoi mettre dans la phase de préparation et quoi mettre dans la phase d'exécution. La distinction est généralement assez claire : dans notre cas, nous mettons le code pour dessiner le canevas dans la phase de préparation et le code pour montrer le canevas (qui est petit) dans la phase d'exécution.

Voir aussi :

- %link:prepare-run%

__Choisir votre version de JavaScript : ECMA 5.1 ou 6__

Le nom formel de JavaScript est ECMASCRIPT, qui existe en différentes versions. La dernière version, ECMA 6 (ou ECMA 2015), a un certain nombre de fonctionnalités utiles. ECMA 6 est pris en charge par la plupart des navigateurs modernes, ce qui signifie que vous pouvez utiliser ces fonctionnalités lorsque vous exécutez une expérience dans un navigateur. Cependant, en raison d'une limitation de la bibliothèque `js2py`, qui est utilisée par OpenSesame pour exécuter du JavaScript sur le bureau, vous ne pouvez utiliser que ECMA 5.1 lors de l'exécution de l'expérience sur le bureau.

Dans de nombreux cas, vous ne vous souciez pas vraiment de pouvoir exécuter votre expérience en ligne également sur le bureau, auquel cas il est logique d'utiliser ECMA 6. C'est également l'approche que nous adopterons pour ce tutoriel.

En d'autres termes : nous utiliserons la syntaxe ECMA 6, et donc nous ne pourrons exécuter l'expérience que dans un navigateur et non sur le bureau.

__Mettre en œuvre le niveau abstrait__

Nous commençons au niveau le plus abstrait : définir une fonction qui dessine un affichage de recherche visuelle. Nous ne précisons pas *comment* cela est fait ; nous supposons simplement qu'il y a une fonction qui fait cela, et nous nous soucierons des détails plus tard - c'est de la programmation descendante.

Dans l'onglet Préparer, entrez le code suivant :

```js
persistent.c = draw_canvas()
```

Que se passe-t-il ici ? Nous ...

- Appelons `draw_canvas()`, qui renvoie un objet `Canvas` que nous stockons en tant que `c` ; en d'autres termes, `c` est un objet `Canvas` qui correspond à l'affichage de recherche. Cela suppose qu'il y a une fonction `draw_canvas()`, même si nous ne l'avons pas encore définie.

Un objet `Canvas` est un seul affichage ; il est, en un sens, l'équivalent JavaScript d'un SKETCHPAD. Voir aussi :

- %link:manual/javascript/canvas%

Nous attribuons `c` comme propriété de l'objet `persistent`. Cela garantit que nous sommes en mesure d'accéder à `c` également dans la phase *Run*. Cela est nécessaire, car (contrairement aux éléments INLINE_SCRIPT Python) les variables ne sont pas automatiquement partagées entre différents éléments INLINE_JAVASCRIPT, ni entre les phases Run et Prepare du même élément INLINE_JAVASCRIPT. Voir aussi :

Nous passons maintenant à un niveau inférieur en définissant `draw_canvas()` (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine le canevas de recherche.
 * @return Un Canvas
 **/
function draw_canvas() {
    let c = Canvas()
    let xy_list = xy_random(vars.set_size, 500, 500, 75)
    if (vars.target_present === 'present') {
        let [x, y] = xy_list.pop()
        draw_target(c, x, y)
    } else if (vars.target_present !== 'absent') {
        throw 'Valeur invalide pour target_present ' + vars.target_present
    }
    for (let [x, y] of xy_list) {
        draw_distractor(c, x, y)
    }
    return c
}
```

Que se passe-t-il ici ? Nous …

- Créez un canvas vide, `c`, en utilisant la fonction usine `Canvas()`.
- Générez un tableau de coordonnées `x, y` aléatoires, appelé `xy_list`, en utilisant une autre fonction courante, `xy_random()`. Ce tableau détermine où les stimuli sont affichés. Les emplacements sont échantillonnés à partir d'une zone de 500 × 500 px avec un espacement minimum de 75 px.
- Vérifiez si la variable expérimentale `target_present` a la valeur 'present' ; si c'est le cas, `pop()` une paire `x, y` de `xy_list` et dessinez la cible à cet emplacement. Cela suppose qu'il y a une fonction `draw_target()`, même si nous ne l'avons pas encore définie.
- Si `target_present` n'est ni 'present' ni 'absent', nous lançons une erreur ; c'est de la programmation défensive et cela nous protège des erreurs de frappe (par exemple, si nous avions accidentellement entré 'presenr' au lieu de 'present').
- Bouclez toutes les valeurs restantes de `x, y` et dessinez un distracteur à chaque position. Cela suppose qu'il y a une fonction `draw_distractor()`, même si nous ne l'avons pas encore définie.
- Retournez `c`, qui a maintenant l'affichage de recherche dessiné dessus.

Il y a plusieurs fonctions courantes, telles que `Canvas()` et `xy_random()`, qui sont toujours disponibles dans un élément INLINE_JAVASCRIPT. Voir :

- %link:manual/javascript/common%

En JavaScript, les variables expérimentales sont stockées en tant que propriétés de l'objet `vars`. C'est pourquoi vous écrivez `vars.set_size` et non directement `set_size`.

__Mettre en œuvre le niveau intermédiaire__

Nous passons maintenant à une étape supplémentaire en définissant `draw_target` (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine la cible.
 * @param c Un Canvas
 * @param x Une coordonnée x
 * @param y Une coordonnée y
 **/
function draw_target(c, x, y) {
    draw_shape(c, x, y, vars.target_color, vars.target_shape)
}
```

Que se passe-t-il ici ? Nous...

- Appelons une autre fonction, `draw_shape()`, et spécifions la couleur et la forme à dessiner. Cela suppose qu'il y a une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

Nous définissons également `draw_distractor` (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine un seul distracteur.
 * @param c Un Canvas
 * @param x Une coordonnée x
 * @param y Une coordonnée y
 **/
function draw_distractor(c, x, y) {
    if (vars.condition === 'conjunction') {
        draw_conjunction_distractor(c, x, y)
    } else if (vars.condition === 'feature_shape') {
        draw_feature_shape_distractor(c, x, y)
    } else if (vars.condition === 'feature_color') {
        draw_feature_color_distractor(c, x, y)
    } else {
        throw 'Condition non valide : ' + vars.condition
    }
}
```

Que se passe-t-il ici ? Nous...

- Appelons une autre fonction pour dessiner un distracteur plus spécifique en fonction de la condition.
- Vérifions si `vars.condition` a l'une des valeurs attendues. Sinon, nous lançons une erreur. C'est de la programmation défensive ! Sans cette vérification, si nous faisions une erreur de frappe quelque part, le distracteur pourrait simplement ne pas être affiché sans provoquer de message d'erreur.

Maintenant, nous définissons la fonction qui dessine les distracteurs dans la condition Conjonction (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine un seul distracteur dans la condition de conjonction : un objet qui
 * peut avoir n'importe quelle forme et couleur, mais ne peut pas être identique à la cible.
 * @param c Un Canvas.
 * @param x Une coordonnée x.
 * @param y Une coordonnée y.
 **/
function draw_conjunction_distractor(c, x, y) {
    let conjunctions = [
        ['jaune', 'cercle'],
        ['bleu', 'cercle'],
        ['jaune', 'carré'],
        ['bleu', 'carré'],
    ]
    let [couleur, forme] = random.pick(conjunctions)
    while (couleur === vars.target_color && forme === vars.target_shape) {
        [couleur, forme] = random.pick(conjunctions)
    }
    draw_shape(c, x, y, couleur, forme)
}
```

Que se passe-t-il ici ? Nous …

- Définir une liste, `conjonctions`, de toutes les combinaisons possibles de couleurs et de formes.
- Sélectionnez au hasard l'une des combinaisons de couleurs et de formes dans `conjonctions`.
- Vérifiez si la couleur et la forme sélectionnées sont toutes deux égales à la couleur et à la forme de la cible. Si c'est le cas, continuez à sélectionner une nouvelle couleur et une nouvelle forme jusqu'à ce que ce ne soit plus le cas. Après tout, le distracteur ne peut pas être identique à la cible !
- Appelez une autre fonction, `draw_shape()`, et spécifiez la couleur et la forme du distracteur à dessiner. Cela suppose qu'il existe une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

De plus, nous ...

- Utilisons la bibliothèque `random`, qui correspond au paquet `random-ext`. Cette bibliothèque contient des fonctions de randomisation utiles (telles que `random.pick()`) et fait partie des bibliothèques JavaScript non standard incluses avec OSWeb.

Maintenant, nous définissons la fonction qui dessine les distracteurs dans la condition Shape Feature (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine un seul distracteur dans la condition feature-shape : un objet qui
 * a une forme différente de la cible, mais peut avoir n'importe quelle couleur.
 * @param c Un Canvas.
 * @param x Une coordonnée x.
 * @param y Une coordonnée y.
 **/
function draw_feature_shape_distractor(c, x, y) {
    let colors = ['jaune', 'bleu']
    let color = random.pick(colors)
    let shape
    if (vars.target_shape === 'cercle') {
        shape = 'carré'
    } else if (vars.target_shape === 'carré') {
        shape = 'cercle'
    } else {
        throw 'Invalid target_shape: ' + vars.target_shape
    }
    draw_shape(c, x, y, color, shape)
}
```

Que se passe-t-il ici ? Nous ...

- Sélectionnez au hasard une couleur.
- Choisissez une forme carrée si la cible est un cercle, et une forme circulaire si la cible est un carré.
- Si `target_shape` n'est ni 'cercle' ni 'carré', `throw` une erreur - plus de programmation défensive !
- Appelez une autre fonction, `draw_shape()`, et spécifiez la couleur et la forme du distracteur à dessiner. Cela suppose qu'il existe une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

Maintenant, nous définissons la fonction qui dessine les distracteurs dans la condition Color Feature (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine un seul distracteur dans la condition feature-color : un objet qui
 * a une couleur différente de la cible, mais peut avoir n'importe quelle forme.
 * @param c Un Canvas.
 * @param x Une coordonnée x.
 * @param y Une coordonnée y.
 **/
function draw_feature_color_distractor(c, x, y) {
    let shapes = ['cercle', 'carré']
    let shape = random.pick(shapes)
    let color
    if (vars.target_color === 'jaune') {
        color = 'bleu'
    } else if (vars.target_color === 'bleu') {
        color = 'jaune'
    } else {
        throw 'Invalid target_color: ' + vars.target_color
    }
    draw_shape(c, x, y, color, shape)
}
```

Que se passe-t-il ici ? Nous ...

- Sélectionnez au hasard une forme.
- Choisissez une couleur bleue si la cible est jaune, et une couleur jaune si la cible est bleue.
- Si `target_color` n'est ni 'jaune' ni 'bleu', `throw` une erreur - plus de programmation défensive !
- Appelez une autre fonction, `draw_shape()`, et spécifiez la couleur et la forme du distracteur à dessiner. Cela suppose qu'il existe une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

__Implémenter le niveau détaillé__

Maintenant, nous descendons jusqu'aux détails en définissant la fonction qui dessine réellement une forme sur le canevas (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine une forme unique.
 * @param c Un Canvas.
 * @param x Une coordonnée x.
 * @param y Une coordonnée y.
 * @param color Une couleur (jaune ou bleue)
 * @param shape Une forme (carré ou cercle)
 **/
function draw_shape(c, x, y, color, shape) {
    if (shape === 'carré') {
        // Les paramètres sont passés sous forme d'objet !
        c.rect({x:x-25, y:y-25, w:50, h:50, color:color, fill:true})
    } else if (shape === 'cercle') {
        // Les paramètres sont passés sous forme d'objet !
        c.circle({x:x, y:y, r:25, color:color, fill:true})
    } else {
        throw 'Forme invalide: ' + shape
    }
    if (color !== 'jaune' && color !== 'bleue') {
        throw 'Couleur invalide: ' + color
    }
}
```

Que se passe-t-il ici ? Nous …

- Vérifions quelle forme doit être dessinée. Pour les carrés, nous ajoutons un élément `rect()` au canvas. Pour les cercles, nous ajoutons un élément `circle()`.
- Vérifions si la forme est un carré ou un cercle, et sinon, nous "lançons" une erreur. Ceci est un autre exemple de programmation défensive ! Nous nous assurons que nous n'avons pas accidentellement spécifié une forme invalide.
- Vérifions si la couleur n'est ni jaune ni bleue, et si ce n'est pas le cas, nous lançons une erreur.

Important, les fonctions `Canvas` acceptent un seul objet (`{}`) qui spécifie tous les paramètres par nom, comme suit :

```js
// Correct : passez un seul objet qui contient tous les paramètres par nom
c.rect({x:x-25, y:y-25, w:50, h:50, color:color, fill:true})
// Incorrect : ne passez pas les paramètres par ordre
// c.rect(x-25, y-25, 50, 50, color, true)
// Incorrect : les paramètres nommés ne sont pas pris en charge en JavaScript
// c.rect(x=x-25, y=y-25, w=50, h=50, color=color, fill=true)
```

__Implémentez la phase Run__

Comme nous avons fait tout le travail difficile dans la phase Prepare, la phase Run est juste :

```js
persistent.c.show()
```

Notez que nous avons attribué le canvas en tant que propriété de l'objet `persistent` dans la phase Prepare, c'est pourquoi nous pouvons également nous y référer dans la phase Run.

C'est tout ! Maintenant, vous avez dessiné un affichage complet de recherche visuelle. Et, surtout, vous l'avez fait d'une manière facile à comprendre, grâce à la programmation du haut vers le bas et sûre, grâce à la programmation défensive.


## Étape 7 : Définir la bonne réponse

Pour savoir si le participant répond correctement, nous devons connaître la bonne réponse. Vous pouvez la définir explicitement dans *block_loop* (comme indiqué dans le tutoriel pour débutants) ; mais ici, nous allons utiliser un simple JavaScript qui vérifie si la cible est présente ou non et définit la réponse correcte en conséquence.

Pour ce faire, insérez un nouveau INLINE_JAVASCRIPT au début de *trial_sequence* et renommez-le *correct_response_script*. Dans la phase Prepare, entrez le code suivant :

```js
if (vars.target_present === 'présent') {
    vars.correct_response = 'right'
} else if (vars.target_present === 'absent') {
    vars.correct_response = 'left'
} else {
    throw 'target_present doit être absent ou présent, pas ' + vars.target
}
```

Que se passe-t-il ici ? Nous …

- Vérifions si la cible est présente ou non. Si la cible est présente, la réponse correcte est 'right' (la touche fléchée vers la droite) ; si la cible est absente, la réponse correcte est 'left' (la touche fléchée vers la gauche). La variable expérimentale `correct_response` est automatiquement utilisée par OpenSesame ; par conséquent, nous n'avons pas besoin d'indiquer explicitement que cette variable contient la bonne réponse.
- Vérifions si la cible est soit présente, soit absente, et si ce n'est pas le cas, nous lançons une erreur - un autre exemple de programmation défensive.

## Étape 8 : Donner un retour d'information par essai

Un retour d'information après chaque essai peut motiver les participants ; cependant, un retour d'information par essai ne doit pas interférer avec le déroulement de l'expérience. Une bonne manière de donner un retour d'information par essai est de montrer brièvement un point de fixation vert après une réponse correcte et un point de fixation rouge après une réponse incorrecte.

Pour ce faire :

- Insérez deux nouveaux SKETCHPADs dans *trial_sequence*, juste après *keyboard_response*.
- Renommez un SKETCHPAD en *green_dot*, dessinez un point de fixation vert central dessus, et changez sa durée à 500.
- Renommez l'autre SKETCHPAD en *red_dot*, dessinez un point de fixation rouge central dessus, et changez sa durée à 500.

Bien sûr, un seul des deux points doit être affiché à chaque essai. Pour ce faire, nous préciserons les instructions run-if dans *trial_sequence* :

- Changez l'instruction run-if pour *green_dot* en '[correct] = 1', indiquant qu'il ne doit être affiché qu'après une réponse correcte.
- Changez l'instruction run-if pour *red_dot* en '[correct] = 0', indiquant qu'il ne doit être affiché qu'après une réponse incorrecte.

La variable `correct` est automatiquement créée si la variable `correct_response` est disponible ; c'est pourquoi nous avons défini `correct_response` à l'étape 7. Pour plus d'informations sur les variables et les instructions run-if, voir :

- %link:manual/variables%

Le *trial_sequence* devrait maintenant ressembler à %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  Le *trial_sequence* à la fin de l'étape 8.
--%


## Étape 9 : Vérification de la compatibilité

Lorsque vous souhaitez exécuter une expérience dans un navigateur, vous ne pouvez pas utiliser toutes les fonctionnalités d'OpenSesame. Pour vérifier si votre expérience peut fonctionner dans un navigateur, vous pouvez utiliser la vérification de compatibilité OSWeb en allant dans Menu → Outils → OSweb. Si vous avez suivi toutes les étapes de ce didacticiel, la vérification de compatibilité échouera avec l'avertissement suivant (%FigCompatibilityCheck):

%--
figure:
 id: FigCompatibilityCheck
 source: compatibility-check.png
 caption: |
  La vérification de compatibilité peut donner des avertissements ou des erreurs.
--%

Ceci est un avertissement que le *logger* a l'option 'Log all variables' activée. Activer cette option est recommandé lors de l'exécution d'une expérience sur le bureau, auquel cas il ne pose aucun problème de collecter beaucoup d'informations inutiles. Toutefois, cette option n'est *pas* recommandée lors de l'exécution d'une expérience en ligne, car cela entraîne des fichiers de données inutilement volumineux et consomme une quantité inutile de bande passante.

Par conséquent, allez dans le *logger*, désactivez l'option 'Log all variables' et sélectionnez uniquement les variables dont vous avez réellement besoin. Vous pouvez le faire en ouvrant l'inspecteur de variables et en faisant glisser les variables dans le tableau du *logger* (%FigLogger).

%--
figure:
 id: FigLogger
 source: logger.png
 caption: |
  La journalisation des variables pertinentes uniquement est recommandée lors de l'exécution d'une expérience en ligne pour économiser de la bande passante.
--%


Pour une liste des fonctionnalités prises en charge par OSWeb, voir :

- %link:manual/osweb/osweb%

## Terminé !

Félicitations, l'expérience est terminée ! Vous pouvez faire un essai en appuyant sur le bouton de la barre d'outils qui affiche un cercle vert avec un bouton de lecture gris à l'intérieur (raccourci : `Alt+Ctrl+W`).

Si l'expérience ne fonctionne pas du premier coup : Ne vous inquiétez pas et déterminez calmement d'où vient l'erreur. Les plantages font partie du processus de développement normal. Mais vous pouvez vous épargner beaucoup de temps et de maux de tête en travaillant de manière structurée, comme nous l'avons fait dans ce tutoriel.

## Références

<div class='reference' markdown='1'>

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, 12(1), 97–136. doi:10.1016/0010-0285(80)90005-5

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
