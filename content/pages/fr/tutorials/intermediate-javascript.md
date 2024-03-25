title: Tutoriel intermédiaire (JavaScript) : recherche visuelle
hash: 8a884ef49e4ac79ec8dd0e01bf078980622b9f0365927917c21e42253e76321c
locale: fr
language: French

## À propos d'OpenSesame

OpenSesame est un programme convivial pour le développement d'expériences comportementales en psychologie, neurosciences et économie expérimentale. Pour les débutants, OpenSesame propose une interface graphique complète et intuitive. Pour les utilisateurs avancés, OpenSesame prend en charge Python (uniquement sur ordinateur de bureau) et JavaScript (sur ordinateur de bureau et dans le navigateur).

OpenSesame est librement disponible sous la [General Public License v3][gpl].

## À propos de ce tutoriel

Ce tutoriel montre comment créer une expérience de recherche visuelle de base en utilisant OpenSesame [(Mathôt, Schreij, & Theeuwes, 2012)][references]. Nous utiliserons à la fois l'interface graphique et JavaScript pour développer une expérience que vous pouvez exécuter en ligne dans un navigateur. Une certaine expérience avec OpenSesame et JavaScript est recommandée. Ce tutoriel prend environ une heure.

Une version de ce tutoriel basée sur Python est également disponible. Si vous n'avez pas besoin d'exécuter vos expériences en ligne, alors le tutoriel Python est probablement ce dont vous avez besoin :

- %link:tutorials/intermediate%


## Ressources

- __Téléchargement__ — Ce tutoriel suppose que vous utilisez la version 4.0.0 d'OpenSesame ou ultérieure et OSWeb 2.0 ou ultérieure. Vous pouvez télécharger la version la plus récente d'OpenSesame depuis :
	- %link:download%
- __Documentation__ — Un site web dédié à la documentation peut être trouvé à :
	- <http://osdoc.cogsci.nl/>
- __Forum__ — Un forum de support peut être trouvé à :
	- <http://forum.cogsci.nl/>
- __Sigmund__ -- SigmundAI est un assistant IA avec une connaissance experte d'OpenSesame et peut être trouvé à :
	- <https://sigmundai.eu/>


## L'expérience

Dans ce tutoriel, vous allez créer une expérience de recherche visuelle de base. L'expérience ressemble aux études classiques de recherche visuelle de [Treisman et Gelade (1980)][references], mais elle n'est pas identique.

Avant de commencer à *construire* l'expérience par vous-même, vous pouvez déjà *y participer*. Cela vous donnera une bonne idée de ce vers quoi vous travaillez dans ce tutoriel.

<a role="button" class="btn btn-success btn-align-left" href="https://jatos.mindprobe.eu/publix/1938/start?batchId=2191&generalMultiple">Participez à l'expérience!</a>

Dans cette expérience, les participants recherchent un objet cible, qui peut être un carré jaune, un cercle jaune, un carré bleu ou un cercle bleu; l'identité de la cible varie entre les blocs d'essais. Les participants indiquent si la cible est présente ou non en appuyant sur la flèche droite (présente) ou gauche (absente).

En plus de la cible, zéro ou plusieurs objets distracteurs sont montrés. Il y a trois conditions, et la condition détermine quel type de distracteurs il y a :

- Dans la condition *Conjonction*, les distracteurs peuvent avoir n'importe quelle forme et couleur, avec la seule restriction qu'ils ne peuvent pas être identiques à la cible. Donc, par exemple, si la cible est un carré jaune, alors les distracteurs sont des cercles jaunes, des cercles bleus et des carrés bleus.
- Dans la condition *Caractéristique Forme*, les distracteurs ont une forme différente de la cible, mais peuvent avoir n'importe quelle couleur. Donc, par exemple, si la cible est un carré jaune, alors les distracteurs sont des cercles jaunes et des cercles bleus.
- Dans la condition *Caractéristique Couleur*, les distracteurs peuvent avoir n'importe quelle forme, mais ont une couleur différente de la cible. Donc, par exemple, si la cible est un carré jaune, alors les distracteurs sont des carrés bleus et des cercles bleus.

Un retour immédiat est donné après chaque essai : un point vert après une réponse correcte, et un point rouge après une réponse incorrecte. Un retour détaillé sur les temps de réponse moyens et la précision est montré après chaque bloc d'essais.

figure:
 id: FigVisualSearch
 source: visual-search.svg
 caption: |
  L'expérience de recherche visuelle que vous mettrez en œuvre dans ce tutoriel.

Des expériences comme celle-ci montrent deux résultats typiques :

- Il faut plus de temps pour trouver la cible dans la condition Conjonction que dans les deux conditions Caractéristiques.
- Dans la condition Conjonction, les temps de réponse augmentent à mesure que le nombre de distracteurs augmente. Cela suggère que les personnes recherchent la cible un élément à la fois ; on appelle cela la *recherche sérielle*.
- Dans les conditions Caractéristiques (forme et couleur), les temps de réponse n'augmentent pas, ou presque pas, à mesure que le nombre de distracteurs augmente. Cela suggère que les personnes traitent l'ensemble de l'affichage en même temps ; on appelle cela la *recherche parallèle*.

Selon la théorie de l'intégration des caractéristiques de Treisman et Gelade, ces résultats reflètent le fait que la condition Conjonction exige que vous combiniez, ou *liiez*, la couleur et la forme de chaque objet. Cette liaison nécessite de l'attention, et vous devez donc déplacer votre attention d'un objet à l'autre ; c'est lent, et cela explique pourquoi les temps de réponse dépendent du nombre d'objets présents. En revanche, dans les conditions Caractéristiques, la couleur et la forme n'ont pas besoin d'être liées, et donc l'ensemble de l'affichage peut être traité en un seul balayage sans que l'attention ne soit dirigée vers chaque objet.

## Conception expérimentale

Cette conception :

- Est *intra-sujets*, car tous les participants réalisent toutes les conditions
- Est *entièrement croisée* (ou factorielle complète), car toutes les combinaisons de conditions se produisent
- A trois conditions (ou facteurs) :
	- Varie à l'intérieur des blocs :
		- `set_size` avec trois niveaux (1, 5, 15), ou SS<sub>3</sub>
		- `condition` avec trois niveaux (conjonction, caractéristique_forme, caractéristique_couleur), ou CN<sub>3</sub>
		- `target_present` avec deux niveaux (présent, absent), ou TP<sub>2</sub>
	- Varie entre les blocs :
		- `target_shape` avec deux niveaux (carré, cercle), ou TS<sub>2</sub>
		- `target_color` avec deux niveaux (jaune, bleu), ou TC<sub>2</sub>
- A N sujets, ou <u>S</u><sub>N</sub>

Vous pouvez écrire ce plan comme <u>S</u><sub>N</sub>×SS<sub>3</sub>×CN<sub>3</sub>×TP<sub>2</sub>×TS<sub>2</sub>×TC<sub>2</sub>

Pour plus d'informations sur cette notation pour la conception expérimentale, voir :

- %link:experimentaldesign%

## Étape 1 : Créer la structure de base de l'expérience

Ouvrez OpenSesame et, dans l'onglet "Get started!", sélectionnez le modèle "Extended". Ce modèle fournit la structure de base qui est commune à de nombreuses expériences de psychologie cognitive, comme celle que nous allons créer ici.

Le modèle "Extended" contient quelques éléments dont nous n'avons pas besoin. Supprimez les éléments suivants :

- *about_this_template*
- *practice_loop*
- *end_of_practice*

Lorsque vous avez supprimé ces éléments, ils sont encore visibles dans la corbeille "Unused items". Pour supprimer définitivement ces éléments, cliquez sur la corbeille "Unused items", puis cliquez sur le bouton "Permanently delete unused items".

Enfin, donnez un bon titre à l'expérience, comme "Recherche visuelle". Pour ce faire, ouvrez l'onglet "general-properties" (en cliquant sur "Extended template" dans la zone d'aperçu) et cliquez sur le nom de l'expérience pour le modifier.

Configurez également OpenSesame pour exécuter l'expérience dans un navigateur, plutôt que sur le bureau.

La zone d'aperçu doit maintenant ressembler à %FigStep1:

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  La zone d'aperçu à la fin de l'étape 1.
--%


## Étape 2 : Définir les variables expérimentales qui varient entre les blocs

Comme décrit ci-dessus, deux variables varient entre les blocs dans notre expérience : `target_shape` et `target_color`. Nous devons donc définir ces variables dans la *experimental_loop*. Pour comprendre pourquoi, considérez la structure montrée dans %FigStep1, en commençant par le bas (c'est-à-dire le niveau le plus indenté).

- *trial_sequence* correspond à un essai unique
- *block_loop* correspond à un bloc d'essais
    - Ainsi, les variables définies ici varient pour chaque exécution de *trial_sequence*; en d'autres termes, les variables définies dans *block_loop* varient __au sein des blocs__.
- *block_sequence* correspond à un bloc d'essais, précédé par la réinitialisation des variables de feedback, et suivi par le feedback du participant
- *experimental_loop* correspond à plusieurs blocs d'essais
    - Ainsi, les variables définies ici varient pour chaque exécution de *block_sequence*; en d'autres termes, les variables définies dans *experimental_loop* varient __entre les blocs__.
- *experiment* correspond à l'ensemble de l'expérience, qui est un écran d'instructions, suivi par plusieurs blocs d'essais, puis par un écran de fin d'expérience

Cliquez sur experimental loop et définissez :

- `target_shape`, qui peut être 'carré' ou 'cercle'; et
- `target_color`, qui peut être 'jaune' ou 'bleu'.

Nous avons un plan factoriel complet, ce qui signifie que les 2 × 2 = 4 combinaisons doivent se produire. La table de *experimental_loop* doit maintenant ressembler à %FigStep2:

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  La table de *experimental_loop* à la fin de l'étape 2.
--%

## Étape 3: Donner des instructions au début de chaque bloc

Pour le moment, l'expérience commence par un écran unique *instructions*. Dans notre cas, nous souhaitons donner des instructions avant chaque bloc d'essais, pour dire au participant quelle cible chercher (car l'identité de la cible varie entre les blocs).

__Déplacer les instructions dans block_sequence__

Ainsi, prenez l'élément *instructions* et faites-le glisser sur *block_sequence*. Une fenêtre contextuelle apparaîtra, vous demandant si vous voulez :

- Insérer l'élément dans *block_sequence*, auquel cas *instructions* deviendrait le premier élément de *block_sequence*; ou
- Insérer l'élément après *block_sequence*, auquel cas *instructions* se déplacerait vers une position après *block_sequence*.

Sélectionnez la première option ('Insérer dans'). Maintenant *block_sequence* commence avec un écran d'instructions, ce que nous voulons.

__Ajouter du texte d'instruction__

Cliquez sur *instructions* pour l'ouvrir et ajouter un bon texte d'instruction, tel que :

```text
INSTRUCTIONS

Cherchez le {target_shape} {target_color}

Appuyez sur la touche flèche droite si vous le trouvez
Appuyez sur la touche flèche gauche si vous ne trouvez pas

Appuyez sur une touche pour commencer
```

Les accolades autour de '{target_color}' et '{target_shape}' indiquent que ce ne sont pas du texte littéral, mais font référence aux variables que nous avons définies dans *experimental_loop*. Lorsque l'expérience se déroule, les valeurs de ces variables apparaîtront ici et le participant verra (par exemple) 'Cherchez le cercle jaune'.

__Donner un aperçu visuel de la cible__

Il est également bon de montrer au participant le stimulus réel qu'il doit trouver. Pour ce faire :

- Dessinez un cercle rempli au centre de l'affichage (assurez-vous qu'il ne chevauche pas le texte) ;
- Changez la couleur du cercle en '{target_color}'. Cela signifie que la couleur du cercle dépend de la valeur de la variable `target_color`; et
- Changez l'expression show-if en `target_shape == 'circle'`. Il s'agit d'une expression Python qui vérifie si la variable `target_shape` a la valeur 'cercle'. Notez que même si vous *ne pouvez pas* utiliser des éléments Python `inline_script` complets lors de l'exécution d'expériences dans un navigateur, vous *pouvez* utiliser Python pour ces expressions conditionnelles simples.

En d'autres termes, nous avons dessiné un cercle dont la couleur est déterminée par `target_color`; de plus, ce cercle est montré uniquement lorsque la variable `target_shape` a la valeur 'cercle'. Pour plus d'informations sur les variables et les instructions show-if, voir :

- %link:manual/variables%

Nous utilisons la même astuce pour dessiner un carré :

- Dessinez un carré rempli au centre de l'affichage ;
- Changez la couleur du carré en '{target_color}' ; et
- Changez l'instruction  show-if en `target_shape == 'square'`

L'écran *instructions* doit maintenant ressembler à %FigStep3:

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  L'écran *instructions* à la fin de l'étape 3.
--%


## Étape 4: Définir les variables expérimentales qui varient à l'intérieur des blocs

Trois variables varient à l'intérieur des blocs dans notre expérience : `condition`, `set_size` et `target_present`. Comme décrit dans l'étape 2, nous devons définir ces variables dans la *block_loop* afin qu'elles varient pour chaque exécution de *trial_sequence*.

Les trois variables représentent un total de 3 × 3 × 2 = 18 combinaisons différentes. Nous pouvons les saisir manuellement dans le tableau, mais comme nous avons une conception factorielle complète, nous pouvons également utiliser l'assistant de conception factorielle complète. Pour ce faire, ouvrez d'abord *block_loop* et cliquez sur le bouton 'Full-factorial design'.

Dans le tableau qui apparaît, mettez les noms des variables sur la première rangée et les valeurs sur les rangées ci-dessous, comme le montre %FigFullFactorial.

%--
figure:
 id: FigFullFactorial
 source: fullfactorial.png
 caption: |
  L'écran *instructions* à la fin de l'étape 3.
--%

Cliquez maintenant sur 'Ok' pour générer la conception complète. Le tableau de *block_loop* doit maintenant ressembler à %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  Le tableau de *block_loop* à la fin de l'étape 4.
--%

## Étape 5: Créer la séquence d'essai et ajouter un script d'initialisation

Nous voulons que notre séquence d'essai soit constituée comme suit :

- Un point de fixation, pour lequel nous utiliserons un SKETCHPAD.
- Un écran de recherche, que nous créerons en JavaScript avec un INLINE_JAVASCRIPT personnalisé.
- La collecte des réponses, pour laquelle nous utiliserons un KEYBOARD_RESPONSE.
- L'enregistrement des données, pour lequel nous utiliserons un LOGGER.
- (Nous souhaitons également avoir un retour immédiat après chaque essai, mais nous y reviendrons plus tard.)

La seule chose qui manque dans *trial_sequence* est un INLINE_JAVASCRIPT.

- Insérez un nouveau INLINE_JAVASCRIPT après *sketchpad* et renommez-le *search_display_script*.
- Renommez *sketchpad* en *fixation_dot*, afin que sa fonction soit claire ; et
- Changez la durée de *fixation_dot* à 500, afin que le point de fixation soit affiché pendant 500 ms. (Un point de fixation devrait déjà être dessiné ; sinon, dessinez-en un au centre de *fixation_dot*.)

Nous devons également ajouter un script d'initialisation au début de l'expérience. Nous l'utiliserons uniquement pour définir (`let`) une variable qui contiendra l'objet `Canvas` sur lequel nous dessinerons. En JavaScript, vous devez définir une variable exactement une fois, c'est pourquoi nous ne pouvons pas le faire dans la *trial_sequence*.

- Insérez un nouveau INLINE_JAVASCRIPT en haut de la séquence *experiment* et renommez-le *init*.

La zone d'aperçu doit maintenant ressembler à %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  La zone d'aperçu à la fin de l'étape 5.
--%

## Étape 6: Générer l'écran de recherche

__Programmation descendante et défensive__

Maintenant, les choses vont devenir intéressantes : nous allons commencer à programmer en JavaScript. Nous utiliserons deux principes directeurs : la programmation *descendante* et *défensive*.

- La *programmation descendante* signifie que nous commençons par la logique la plus abstraite, sans se préoccuper de la manière dont cette logique est mise en œuvre. Une fois que la logique la plus abstraite est en place, nous passons à un niveau de logique légèrement moins abstrait, et ainsi de suite, jusqu'à arriver aux détails de l'implémentation. Cette technique aide à garder le code structuré.
- La *programmation défensive* signifie que nous supposons que nous faisons des erreurs. Par conséquent, pour nous protéger de nous-mêmes, nous intégrons des vérifications de bon sens dans le code.

*Remarque :* L'explication ci-dessous suppose que vous êtes un peu familier avec JavaScript. Si des concepts tels que `Array`, boucle `for` et fonctions ne vous disent rien, il est préférable de suivre d'abord un tutoriel d'introduction sur JavaScript. Vous pouvez trouver des liens vers des tutoriels JavaScript ici :

- %link:manual/javascript/about%

La logique du code est présentée dans %FigHierarchy. Les chiffres indiquent l'ordre dans lequel nous mettrons en œuvre la fonctionnalité, en commençant par le niveau abstrait.

%--
figure:
 id: FigHierarchy
 source: hierarchy.svg
 caption: |
  La logique du code pour dessiner un affichage de recherche visuelle.
--%

__Déclarer des variables avec let, var, et const__

En JavaScript, vous devez 'déclarer' une variable avant de pouvoir l'utiliser. (En Python, ce n'est pas nécessaire.) Dans notre cas, nous utiliserons une variable appelée `c`, que nous devons donc déclarer. Pour ce faire, ouvrez l'onglet Préparer du script *init* et utilisez le mot-clé `let` pour déclarer la variable `c`:

```js
let c
```

Il y a trois façons différentes de déclarer des variables:

- En utilisant `let`, comme nous l'avons fait ici. Dans OpenSesame, cela rend la variable disponible en JavaScript mais pas en tant que variable expérimentale dans l'interface utilisateur.
- En utilisant `var`. Dans OpenSesame, cela rend la variable également disponible en tant que variable expérimentale dans l'interface utilisateur. (Nous ferons cela plus tard pour la variable `correct_response`.)
- En utilisant `const`. C'est comme `var` avec la différence importante que la variable ne peut pas être réaffectée plus tard.

__Les phases de préparation et d'exécution__

Ouvrez *search_display_script* et passez à l'onglet Préparer. OpenSesame distingue deux phases d'exécution:

- Pendant la phase de préparation, chaque élément a la possibilité de se préparer; cela dépend de l'élément: Pour un SKETCHPAD, cela signifie dessiner un canevas (mais ne pas l'afficher); pour un SAMPLER, cela signifie charger un fichier sonore (mais ne pas le lire); etc.
- Pendant la phase d'exécution, chaque élément est effectivement exécuté; encore une fois, cela dépend de l'élément: pour un SKETCHPAD, cela signifie afficher le canevas préparé précédemment; pour un SAMPLER, cela signifie lire un fichier sonore chargé précédemment.

Pour un INLINE_JAVASCRIPT, vous devez décider vous-même quoi mettre dans la phase de préparation et quoi mettre dans la phase d'exécution. La distinction est généralement très claire: dans notre cas, nous mettons le code pour dessiner le canevas dans la phase de préparation et le code pour afficher le canevas (qui est petit) dans la phase d'exécution.

Voir aussi :

- %link:prepare-run%

__Implémenter le niveau abstrait__

Nous commençons au niveau le plus abstrait : définir une fonction qui dessine un affichage de recherche visuelle. Nous ne spécifions pas *comment* cela est fait ; nous supposons simplement qu'il y a une fonction qui fait cela, et nous nous préoccuperons des détails plus tard, c'est la programmation descendante.

Dans l'onglet Préparer, saisissez le code suivant :

```js
c = draw_canvas()
```

Qu'est-ce qui se passe ici ? Nous…

- Appelons `draw_canvas()`, qui renvoie un objet `Canvas` que nous stockons en tant que `c`; en d'autres termes, `c` est un objet `Canvas` qui correspond à l'affichage de recherche. Cela suppose qu'il y a une fonction `draw_canvas()`, même si nous ne l'avons pas encore définie.

Un objet `Canvas` est un affichage unique; c'est en quelque sorte l'équivalent JavaScript d'un SKETCHPAD. Voir aussi:

- %link:manual/javascript/canvas%

Nous descendons maintenant d'un cran en définissant `draw_canvas()` (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine le canevas de recherche.
 * @return Un Canvas
 **/
function draw_canvas() {
    let c = Canvas()
    let xy_list = xy_random(set_size, 500, 500, 75)
    if (target_present === 'present') {
        let [x, y] = xy_list.pop()
        draw_target(c, x, y)
    } else if (target_present !== 'absent') {
        throw 'Valeur invalide pour target_present ' + target_present
    }
    for (let [x, y] of xy_list) {
        draw_distractor(c, x, y)
    }
    return c
}
```

Qu'est-ce qui se passe ici ? Nous ...

- Créez un canevas vide, `c`, en utilisant la fonction usine `Canvas()`.
- Générez un tableau de coordonnées `x, y` aléatoires, appelé `xy_list`, en utilisant une autre fonction courante, `xy_random()`. Ce tableau détermine où les stimuli sont affichés. Les emplacements sont échantillonnés à partir d'une zone de 500 × 500 px avec un espacement minimum de 75 px.
- Vérifiez si la variable expérimentale `target_present` a la valeur 'present'; si c'est le cas, `pop()` un tuple `x, y` de `xy_list`, et dessinez la cible à cet emplacement. Cela suppose qu'il y a une fonction `draw_target()`, même si nous ne l'avons pas encore définie.
- Si `target_present` n'est ni 'present' ni 'absent', nous lançons une erreur; c'est de la programmation défensive et nous protège des fautes de frappe (par exemple, si nous avions accidentellement entré 'presenr' au lieu de 'present').
- Parcourez toutes les valeurs `x, y` restantes et dessinez un distracteur à chaque position. Cela suppose qu'il y a une fonction `draw_distractor()`, même si nous ne l'avons pas encore définie.
- Retournez `c`, qui a maintenant l'affichage de recherche dessiné dessus.

Il existe plusieurs fonctions courantes, telles que `Canvas()` et `xy_random()`, qui sont toujours disponibles dans un élément INLINE_JAVASCRIPT. Voir :

- %link:manual/javascript/common%

Les variables expérimentales sont des variables globales. C'est pourquoi vous pouvez vous référer à `set_size`, qui est défini dans *block_loop*, même si la variable `set_size` n'est jamais explicitement définie dans le script. Il en va de même pour `target_shape`, `target_color`, `condition`, etc. Voir :

- %link:var%


__Mettre en place le niveau intermédiaire__

Nous faisons maintenant un pas de plus en définissant `draw_target` (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine la cible.
 * @param c Un canevas
 * @param x Une coordonnée x
 * @param y Une coordonnée y
 **/
function draw_target(c, x, y) {
    draw_shape(c, x, y, target_color, target_shape)
}
```

Que se passe-t-il ici ? Nous…

- Appelons une autre fonction, `draw_shape()`, et spécifions la couleur et la forme à dessiner. Cela suppose qu'il y a une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

Nous définissons également `draw_distractor` (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine un seul distracteur.
 * @param c Un canevas
 * @param x Une coordonnée x
 * @param y Une coordonnée y
 **/
function draw_distractor(c, x, y) {
    if (condition === 'conjonction') {
        draw_conjunction_distractor(c, x, y)
    } else if (condition === 'feature_shape') {
        draw_feature_shape_distractor(c, x, y)
    } else if (condition === 'feature_color') {
        draw_feature_color_distractor(c, x, y)
    } else {
        throw 'Invalid condition: ' + condition
    }
}
```

Que se passe-t-il ici ? Nous…

- Appelons une autre fonction pour dessiner un distracteur plus spécifique en fonction de la condition.
- Vérifiez si `condition` a l'une des valeurs attendues. Sinon, nous lançons une erreur. C'est de la programmation défensive ! Sans cette vérification, si nous faisions une faute de frappe quelque part, le distracteur pourrait simplement ne pas être montré sans causer de message d'erreur.

Maintenant, nous définissons la fonction qui dessine les distracteurs dans la condition Conjonction (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine un seul distracteur dans la condition de conjonction : un objet qui
 * peut avoir n'importe quelle forme et couleur, mais ne peut pas être identique à la cible.
 * @param c Un canevas.
 * @param x Une coordonnée x.
 * @param y Une coordonnée y.
 **/
function draw_conjunction_distractor(c, x, y) {
    let conjunctions = [
        ['jaune', 'cercle'],
        ['bleu', 'cercle'],
        ['jaune', 'carré'],
        ['bleu', 'carré']
    ]
    let [color, shape] = random.pick(conjunctions)
    while (color === target_color && shape === target_shape) {
        [color, shape] = random.pick(conjunctions)
    }
    draw_shape(c, x, y, color, shape)
}
```

Que se passe-t-il ici ? Nous…

- Définir une liste, `conjunctions`, de toutes les combinaisons possibles de couleur et de forme.
- Sélectionnez au hasard l'une des combinaisons de couleur et de forme dans `conjunctions`.
- Vérifier si la couleur et la forme sélectionnées sont toutes deux égales à la couleur et à la forme de la cible. Si c'est le cas, continuez à sélectionner une nouvelle couleur et forme jusqu'à ce que ce ne soit plus le cas. Après tout, le distracteur ne peut pas être identique à la cible !
- Appelez une autre fonction, `draw_shape()`, et précisez la couleur et la forme du distracteur à dessiner. Cela suppose qu'il existe une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

En outre, nous ...

- Utilisez la bibliothèque `random`, qui correspond au package `random-ext`. Cette bibliothèque contient des fonctions de randomisation utiles (telles que `random.pick()`) et fait partie des bibliothèques JavaScript non standard qui sont incluses avec OSWeb.

Maintenant, nous définissons la fonction qui dessine les distracteurs dans la condition de caractéristique forme (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine un seul distracteur dans la condition de caractéristique forme : un objet qui
 * a une forme différente de la cible, mais peut avoir n'importe quelle couleur.
 * @param c Un Canvas.
 * @param x Une coordonnée x.
 * @param y Une coordonnée y.
 **/
function draw_feature_shape_distractor(c, x, y) {
    let colors = ['jaune', 'bleu']
    let color = random.pick(colors)
    let shape
    if (target_shape === 'cercle') {
        shape = 'carré'
    } else if (target_shape === 'carré') {
        shape = 'cercle'
    } else {
        throw 'Forme cible invalide : ' + target_shape
    }
    draw_shape(c, x, y, color, shape)
}
```

Que se passe-t-il ici ? Nous ...

- Sélectionnons au hasard une couleur.
- Choisissons une forme carrée si la cible est un cercle et une forme circulaire si la cible est un carré.
- Si `target_shape` n'est ni 'cercle' ni 'carré', `throw` une erreur - encore plus de programmation défensive !
- Appelez une autre fonction, `draw_shape()`, et précisez la couleur et la forme du distracteur à dessiner. Cela suppose qu'il existe une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

Maintenant, nous définissons la fonction qui dessine les distracteurs dans la condition de caractéristique couleur (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine un seul distracteur dans la condition de caractéristique couleur : un objet qui
 * a une couleur différente de la cible, mais peut avoir n'importe quelle forme.
 * @param c Un Canvas.
 * @param x Une coordonnée x.
 * @param y Une coordonnée y.
 **/
function draw_feature_color_distractor(c, x, y) {
    let shapes = ['cercle', 'carré']
    let shape = random.pick(shapes)
    let color
    if (target_color === 'jaune') {
        color = 'bleu'
    } else if (target_color === 'bleu') {
        color = 'jaune'
    } else {
        throw 'Couleur cible invalide : ' + target_color
    }
    draw_shape(c, x, y, color, shape)
}
```

Que se passe-t-il ici ? Nous ...

- Sélectionnons au hasard une forme.
- Choisissons une couleur bleue si la cible est jaune, et une couleur jaune si la cible est bleue.
- Si `target_color` n'est ni 'jaune' ni 'bleu', `throw` et erreur - encore plus de programmation défensive !
- Appelez une autre fonction, `draw_shape()`, et précisez la couleur et la forme du distracteur à dessiner. Cela suppose qu'il existe une fonction `draw_shape()`, même si nous ne l'avons pas encore définie.

__Mettre en œuvre le niveau détaillé__

Maintenant, nous descendons jusqu'aux détails en définissant la fonction qui dessine réellement une forme sur le canevas (au-dessus du reste du script jusqu'à présent) :

```js
/**
 * Dessine une forme unique.
 * @param c Un Canvas.
 * @param x Une coordonnée x.
 * @param y Une coordonnée y.
 * @param color Une couleur (jaune ou bleu)
 * @param shape Une forme (carré ou cercle)
 **/
function draw_shape(c, x, y, color, shape) {
    if (shape === 'square') {
        // Les paramètres sont passés sous forme d'objet !
        c.rect({x:x-25, y:y-25, w:50, h:50, color:color, fill:true})
    } else if (shape === 'circle') {
        // Les paramètres sont passés sous forme d'objet !
        c.circle({x:x, y:y, r:25, color:color, fill:true})
    } else {
        throw 'Forme invalide: ' + shape
    }
    if (color !== 'yellow' && color !== 'blue') {
        throw 'Couleur invalide: ' + color
    }
}
```

Que se passe-t-il ici ? Nous...

- Vérifions quelle forme doit être dessinée. Pour les carrés, nous ajoutons un élément `rect()` au canevas. Pour les cercles, nous ajoutons un élément `circle()`.
- Vérifions si la forme est soit un carré, soit un cercle, et si ce n'est pas le cas, nous envoyons une erreur. Ceci est un autre exemple de programmation défensive ! Nous nous assurons que nous n'avons pas accidentellement spécifié une forme invalide.
- Vérifions si la couleur n'est ni jaune ni bleue, et si ce n'est pas le cas, nous envoyons une erreur.

De manière importante, les fonctions `Canvas` acceptent un seul objet (`{}`) qui spécifie tous les paramètres par nom, comme ceci :

```js
// Correct : passez un seul objet contenant tous les paramètres par nom
c.rect({x:x-25, y:y-25, w:50, h:50, color:color, fill:true})
// Incorrect : ne passez pas les paramètres par ordre
// c.rect(x-25, y-25, 50, 50, color, true)
// Incorrect : les paramètres nommés ne sont pas pris en charge en JavaScript
// c.rect(x=x-25, y=y-25, w=50, h=50, color=color, fill=true)
```

__Mettre en œuvre la phase Run__

Parce que nous avons fait tout le travail difficile lors de la phase Prepare, la phase Run est simplement :

```js
c.show()
```

C'est tout ! Maintenant, vous avez dessiné un affichage complet de recherche visuelle. Et, surtout, vous l'avez fait de manière facile à comprendre, grâce à la programmation top-down, et sécurisée, grâce à la programmation défensive.


## Étape 7 : Définir la réponse correcte

Pour savoir si le participant répond correctement, nous devons connaître la réponse correcte. Vous pouvez définir cela explicitement dans le *block_loop* (comme cela a été fait dans le tutoriel pour débutants) ; mais ici, nous allons utiliser un simple JavaScript qui vérifie si la cible est présente ou non et définit la réponse correcte en conséquence.

Pour ce faire, nous devons d'abord déclarer la variable dans l'onglet Prepare du script *init*, juste en dessous de `let c`. Cette fois-ci, nous utilisons le mot-clé `var` pour déclarer `correct_response`, car cela rend la variable disponible dans l'interface utilisateur (alors que `let` ne le fait pas) :

```js
var correct_response
```

Ensuite, insérez un nouveau INLINE_JAVASCRIPT au début de *trial_sequence* et renommez-le *correct_response_script*. Dans la phase Prepare, entrez le code suivant :

```js
if (target_present === 'present') {
    correct_response = 'right'
} else if (vars.target_present === 'absent') {
    correct_response = 'left'
} else {
    throw 'target_present doit être absent ou présent, pas ' + target
}
```

Que se passe-t-il ici ? Nous...

- Vérifions si la cible est présente ou non. Si la cible est présente, la réponse correcte est 'right' (touche flèche droite) ; si la cible est absente, la réponse correcte est 'left' (touche flèche gauche). La variable expérimentale `correct_response` est automatiquement utilisée par OpenSesame ; par conséquent, nous n'avons pas besoin d'indiquer explicitement que cette variable contient la réponse correcte.
- Vérifions si la cible est présente ou absente, et si ce n'est pas le cas, nous envoyons une erreur - un autre exemple de programmation défensive.

## Étape 8 : donner un retour d'information par essai

Des commentaires après chaque essai peuvent motiver les participants ; cependant, les commentaires par essai ne doivent pas interférer avec le déroulement de l'expérience. Un bon moyen de donner un retour d'information par essai est de montrer brièvement un point de fixation vert après une réponse correcte et un point de fixation rouge après une réponse incorrecte.

Pour faire cela:

- Insérez deux nouveaux SKETCHPAD dans *trial_sequence*, juste après *keyboard_response*.
- Renommez un SKETCHPAD en *green_dot*, dessinez un point de fixation vert central dessus et changez sa durée à 500.
- Renommez l'autre SKETCHPAD en *red_dot*, dessinez un point de fixation rouge central dessus et changez sa durée à 500.

Naturellement, un seul des deux points devrait être montré à chaque essai. Pour y parvenir, nous allons spécifier des instructions run-if dans *trial_sequence* :

- Changez l'instruction run-if pour *green_dot* en 'correct == 1', indiquant qu'il devrait seulement être montré après une réponse correcte.
- Changez l'instruction run-if pour *red_dot* en 'correct == 0', indiquant qu'il devrait seulement être montré après une réponse incorrecte.

La variable `correct` est automatiquement créée si la variable `correct_response` est disponible ; c'est pourquoi nous avons défini `correct_response` à l'étape 7. Pour plus d'informations sur les variables et les instructions run-if, voir :

- %link:manual/variables%

La *trial_sequence* devrait maintenant ressembler à %FigStep8.

figure:
 id: FigStep8
 source: step8.png
 caption: |
  La *trial_sequence* à la fin de l'étape 8.


## Terminé !

Félicitations, l'expérience est terminée ! Vous pouvez la tester en cliquant sur le bouton de la barre d'outils qui montre un cercle vert avec un bouton de lecture gris à l'intérieur (raccourci : `Alt+Ctrl+W`).

Si l'expérience ne fonctionne pas du premier coup : Ne vous inquiétez pas et déterminez calmement d'où vient l'erreur. Les plantages font partie du processus de développement normal. Mais vous pouvez vous épargner beaucoup de temps et de maux de tête en travaillant de manière structurée, comme nous l'avons fait dans ce tutoriel.

## Références

<div class='reference' markdown='1'>

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame : Un constructeur d'expériences graphique open-source pour les sciences sociales. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Treisman, A. M., & Gelade, G. (1980). Une théorie de l'intégration des caractéristiques de l'attention. *Cognitive Psychology*, 12(1), 97-136. doi:10.1016/0010-0285(80)90005-5

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html