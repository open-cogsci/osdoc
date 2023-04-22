title: Variables
hash: 87f8069d56f529c53b29b95555f8d096d7d742f9b355ff6689a0d6e7cb2b8654
locale: fr
language: French

[TOC]

## Qu'est-ce qu'une variable expérimentale dans OpenSesame ?

Les variables expérimentales dans OpenSesame sont celles qui :

- Peuvent être mentionnées dans l'interface utilisateur avec la syntaxe '{variable_name}'.
- Sont disponibles en tant que variables globales dans un INLINE_SCRIPT Python.
- Sont disponibles en tant que variables globales dans un INLINE_JAVASCRIPT JavaScript.
- Contiennent des éléments tels que :
	- Les variables que vous avez définies dans un élément LOOP.
	- Les réponses que vous avez collectées.
	- Diverses propriétés de l'expérience.
	- Etc.

## L'inspecteur de variables

L'inspecteur de variables (`Ctrl+I`) fournit un aperçu des variables disponibles (%FigVariableInspector). Lorsque l'expérience n'est pas en cours, cet aperçu est basé sur une meilleure estimation des variables qui deviendront disponibles au cours de l'expérience. Cependant, lorsque l'expérience est en cours, l'inspecteur de variables montre un aperçu en direct des variables et de leurs valeurs. Ceci est utile pour déboguer votre expérience.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: L'inspecteur de variables fournit un aperçu de toutes les variables qu'OpenSesame connaît.
--%

## Définition des variables

La façon la plus simple de définir une variable est via l'élément LOOP. Par exemple, %FigLoop montre comment définir une variable nommée `gaze_cue`. Dans cet exemple, l'élément *trial_sequence* est appelé quatre fois alors que `gaze_cue` est 'left' et quatre autres fois alors que 'gaze_cue' est 'right'.

%--
figure:
 id: FigLoop
 source: defining-variables-in-a-loop.png
 caption: La façon la plus courante de définir des variables indépendantes est en utilisant la table LOOP.
--%

## Variables intégrées

Les variables suivantes sont toujours disponibles :

### Variables d'expérience

|Nom de la variable			|Description|
|-----------------------|-----------|
|`title`				|Le titre de l'expérience|
|`description`			|La description de l'expérience|
|`foreground`			|La couleur d'avant-plan par défaut. Ex. : 'white' ou '#FFFFFF'.|
|`background`			|La couleur d'arrière-plan par défaut. Ex. : 'black' ou '#000000'.|
|`height`				|La hauteur de la résolution d'affichage. Ex. : '768'|
|`width`				|La largeur de la résolution d'affichage. Ex. : '1024'|
|`subject_nr`			|Le numéro du sujet, qui est demandé lors du démarrage de l'expérience.|
|`subject_parity`		|Est 'odd' si `subject_nr` est impair et 'even' si `subject_nr` est pair. Utile pour la contrebalancement.|
|`experiment_path`		|Le dossier de l'expérience en cours, sans le nom de fichier de l'expérience elle-même. Si l'expérience n'a pas été enregistrée, sa valeur est `None`.|
|`pool_folder`			|Le dossier où les éléments du fichier "pool" ont été extraits. Il s'agit généralement d'un dossier temporaire.|
|`logfile`				|Le chemin d'accès au fichier de journal.|

### Variables des éléments

Il existe également des variables qui suivent tous les éléments de l'expérience.

|Nom de la variable			|Description|
|-----------------------|-----------|
|`time_[item_name]`		|Contient un horodatage du dernier moment où l'élément a été exécuté. Pour les éléments SKETCHPAD, cela peut être utilisé pour vérifier le moment de présentation de l'affichage.|
|`count_[item_name]`	|Est égal au nombre de fois moins un (commençant par 0, en d'autres termes) qu'un élément a été appelé. Ceci peut être utilisé, par exemple, comme un compteur d'essais ou de blocs.|

### Variables de réponse

Lorsque vous utilisez les éléments de réponse standard, tels que KEYBOARD_RESPONSE et MOUSE_RESPONSE, un certain nombre de variables sont définies en fonction de la réponse du participant.

|Nom de la variable					|Description|
|-------------------------------|-----------|
|`response`						|Contient la dernière réponse donnée.|
|`response_[item_name]`			|Contient la dernière réponse pour un élément de réponse spécifique. Ceci est utile s'il y a plusieurs éléments de réponse.|
|`response_time`				|Contient l'intervalle en millisecondes entre le début de l'intervalle de réponse et la dernière réponse.|
|`response_time_[item_name]`	|Contient le temps de réponse pour un élément de réponse spécifique.|
|`correct`						|Est défini sur '1' si la dernière `response` correspond à la variable `correct_response`, '0' sinon, et 'undefined' si la variable `correct_response` n'a pas été définie.|
|`correct_[item_name]`			|Comme `correct`, mais pour un élément de réponse spécifique.|

### Variables de feedback

Les variables de feedback maintiennent une moyenne mobile de la précision et des temps de réponse.

|Nom de la variable					|Description|
|-------------------------------|-----------|
|`average_response_time`		|Le temps de réponse moyen. Cette variable est utile pour présenter un feedback au participant.|
|`avg_rt`						|Synonyme de `average_response_time`|
|`accuracy`						|Le pourcentage moyen de réponses correctes. Cette variable est utile pour présenter un feedback au participant.|
|`acc`							|Synonyme de `accuracy`|

## Utilisation des variables dans l'interface utilisateur

Partout où vous voyez une valeur dans l'interface utilisateur, vous pouvez remplacer cette valeur par une variable en utilisant la notation '{variable name}'. Par exemple, si vous avez défini une variable `soa` dans un élément LOOP, vous pouvez utiliser cette variable pour la durée d'un sketchpad comme indiqué dans %FigSketchpad.

%--
figure :
 id: FigSketchpad
 source: variable-duration.png
 légende: La durée '{soa}' indique que la durée du SKETCHPAD dépend de la variable `soa`.
--%

Cela fonctionne dans toute l'interface utilisateur. Par exemple, si vous avez défini une variable `my_freq`, vous pouvez utiliser cette variable comme fréquence dans un élément SYNTH, comme le montre %FigSynth.

%--
figure :
 id: FigSynth
 source: variable-frequency.png
 légende : La fréquence '{my_freq}' indique que la fréquence du SYNTH dépend de la variable `my_freq`.
--%

Parfois, l'interface utilisateur ne vous permet pas de taper du texte arbitraire. Par exemple, les éléments d'un SKETCHPAD sont affichés visuellement et vous ne pouvez pas changer directement une coordonnée X en une variable. Cependant, vous pouvez cliquer sur le bouton *Select view → View script* en haut à droite et modifier directement le script.

Par exemple, vous pouvez changer la position d'un point de fixation du centre :

```text
draw fixdot x=0 y=0
```

... vers une position définie par les variables `xpos` et `ypos` :

```text
draw fixdot x={xpos} y={ypos}
```

## Utilisation des expressions Python dans l'interface utilisateur

Lorsque vous faites référence aux variables en utilisant la notation `{my_var}`, vous utilisez en fait ce qu'on appelle une [f-string](https://peps.python.org/pep-0498/), qui est un moyen d'intégrer du code Python dans des chaînes de texte. Vous pouvez également utiliser des f-strings pour évaluer du code Python arbitraire. Par exemple, vous pouvez multiplier les variables `width` et `height` et inclure le résultat dans un SKETCHPAD, comme suit :

%--
figure :
 id: FigFString
 source: fstrings.png
 légende: Vous pouvez intégrer des expressions Python en utilisant des f-strings.
--%

Les f-strings sont du code Python et ne sont donc pris en charge que sur le bureau, mais voir ci-dessous pour une alternative JavaScript pour les expériences sur navigateur.

## Utilisation des expressions JavaScript dans l'interface utilisateur

Lors de l'utilisation d'OSWeb, les expressions incluses entre accolades sont interprétées comme des [modèles littéraux](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Litt%C3%A9raux_gabarits). Cela ressemble beaucoup aux f-strings en Python, avec la différence importante qu'il utilise JavaScript.

Dans le JavaScript normal, les expressions à l'intérieur des littéraux de modèle sont précédées d'un `$`, comme ceci : `${expression}`. Ceci est autorisé dans OpenSesame, mais pas nécessaire : le préfixe est ajouté automatiquement pour améliorer la compatibilité entre les expériences de bureau et de navigateur. Dans la plupart des cas, comme sur la figure ci-dessous, la même expression exacte est valable sous forme de chaîne f en Python sur le bureau et de littéral de modèle en JavaScript dans le navigateur.

%--
figure:
 id: FigTempalteLiteral
 source: template-literals.png
 caption: Vous pouvez intégrer des expressions JavaScript en utilisant des littéraux de modèle.
--%

## Utilisation de variables en Python

Dans un INLINE_SCRIPT, les variables expérimentales sont disponibles en tant que variables globales. Par exemple, si vous avez défini `exemple_variable` dans une LOOP, alors le code suivant affichera la valeur `exemple_variable` dans la fenêtre de débogage :

~~~ .python
print(example_variable)
~~~

Vous pouvez définir la variable expérimentale `exemple_variable` à la valeur 'some value' comme suit :

~~~ .python
exemple_variable = 'some value'
~~~

## Utilisation de variables en JavaScript

Dans un INLINE_JAVASCRIPT, les variables expérimentales sont disponibles en tant que variables globales. Par exemple, si vous avez défini `exemple_variable` dans une LOOP, alors le code suivant affichera la valeur `exemple_variable` dans la console du navigateur :

```js
console.log(example_variable)
```

Vous pouvez définir la variable expérimentale `exemple_variable` à la valeur 'some value' comme suit :

```js
exemple_variable = 'some value'
```

## Utilisation des instructions conditionnelles ("if")

Les instructions conditionnelles, ou 'instructions if', permettent d'indiquer que quelque chose doit se produire uniquement dans des circonstances spécifiques, par exemple lorsqu'une variable a une valeur spécifique. Les instructions conditionnelles sont des expressions Python régulières.

L'instruction if la plus couramment utilisée dans OpenSesame est l'instruction run-if de la SEQUENCE, qui vous permet de spécifier les conditions dans lesquelles un élément particulier est exécuté. Si vous ouvrez un élément de SEQUENCE, vous pouvez voir que chaque élément de la séquence a une option 'Run if …'. La valeur par défaut est 'always', ce qui signifie que l'élément est toujours exécuté ; mais vous pouvez également entrer une condition ici. Par exemple, si vous voulez montrer un point de fixation vert après une réponse correcte et un point de fixation rouge après une réponse incorrecte, vous pouvez créer une SEQUENCE comme suit (cela suppose qu'un élément KEYBOARD_RESPONSE ajuste automatiquement la variable `correct`, comme discuté précédemment) comme indiqué dans %FigRunIf.

*Important :* Les instructions Run-if ne s'appliquent qu'à la phase Run des éléments. La phase Prepare est toujours exécutée. Voir également [cette page](%link:prepare-run%).

%--
figure:
 id: FigRunIf
 source: run-if.png
 caption: |
  'Run if' peut être utilisé pour indiquer que certains éléments d'une SEQUENCE ne doivent être exécutés que dans des circonstances spécifiques.
--%

Vous pouvez utiliser des conditions plus complexes. Voyons quelques exemples :

```python
correct == 1 and response_time > 2000
correct != 1 or response_time > max_response_time or response_time < min_response_time
```

Le même principe s'applique aux champs 'Show if' dans les items SKETCHPAD. Par exemple, si vous souhaitez dessiner une flèche pointant vers le haut à droite uniquement si la variable `quadrant` a été définie sur "upper right", il suffit de saisir la condition appropriée dans le champ 'Show if ...' et de dessiner la flèche, comme dans %FigShowIf. Assurez-vous de dessiner la flèche après avoir défini la condition.

%--
figure:
 id: FigShowIf
 source: show-if.png
 caption: "'Show if' peut être utilisé pour indiquer que certains éléments d'un item SKETCHPAD ou FEEDBACK ne doivent être montrés que dans des circonstances spécifiques."
--%

Important : Le moment auquel une instruction conditionnelle est évaluée peut affecter le fonctionnement de votre expérience. Ceci est lié à la stratégie prepare-run utilisée par OpenSesame, qui est expliquée ici :

- %link:prepare-run%