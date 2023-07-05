title: Débogage
hash: 183510524112a0f1a17d60669acd2273f06aa15f0b358eb9d3fdaac1002810c0
locale: fr
language: French

Lors de la conception d'une nouvelle expérience, vous rencontrerez inévitablement des bugs. Les bugs peuvent se manifester sous forme de crashs accompagnés de messages d'erreur, ou sous forme de comportements inattendus sans aucun message d'erreur explicite.

Le débogage, l'art et la compétence de diagnostiquer et de rectifier ces erreurs et comportements imprévus, est une partie essentielle du processus de conception expérimentale.


[TOC]


## Débogage dans l'interface utilisateur

### Utilisation de l'inspecteur de variables

L'Inspecteur de Variables dans OpenSesame fournit un aperçu de toutes les variables actuellement actives dans votre expérience. Cela comprend :

- Les variables explicitement définies dans l'interface utilisateur, généralement dans un élément LOOP.
- Les variables de réponse, qui sont définies par divers éléments de réponse tels qu'un élément KEYBOARD_RESPONSE.
- Les variables qui sont définies en utilisant des éléments INLINE_SCRIPT Python.

Lorsqu'une expérience est en cours, l'Inspecteur de Variables se met à jour dynamiquement, fournissant un aperçu en direct des variables et de leurs valeurs. Cette fonction vous permet de surveiller le comportement de votre expérience en temps réel, vous aidant à identifier d'éventuels problèmes ou bugs.

Par exemple, considérez une situation où vous avez défini une variable `left_letter` pour définir quelle lettre doit apparaître sur le côté gauche d'un SKETCHPAD. Cependant, pendant l'exécution, vous remarquez un décalage dans l'Inspecteur de Variables : `left_letter` est en fait affiché sur le côté droit de votre écran. Cela indique un bug tel que vous avez mal placé les lettres droite et gauche sur le SKETCHPAD.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: Vous pouvez utiliser l'inspecteur de variables pour vérifier si votre expérience se comporte comme il se doit. Dans cet exemple, il y a un bug tel que la lettre qui est définie par la variable `left_letter` apparaît en réalité à droite et vice versa.
--%

Utiliser régulièrement l'Inspecteur de Variables pour surveiller les variables aide à assurer que votre expérience se comporte comme prévu et aide à identifier les problèmes dès le début.


### Imprimer des messages de débogage sur la console IPython/ Jupyter

La fonction `print()` de Python est un outil de débogage simple mais puissant lorsqu'il est utilisé à l'intérieur des éléments INLINE_SCRIPT, et sert un but similaire à l'Inspecteur de Variables. Par exemple, vous pouvez imprimer les valeurs des variables `left_letter` et `right_letter` pendant la phase de Préparation d'un INLINE_SCRIPT au début de chaque essai.

Pour voir ces messages de débogage, ouvrez la console Jupyter/ IPython et surveillez la sortie pendant l'exécution de l'expérience. En faisant cela, vous pouvez vérifier si la sortie affichée dans la console correspond au comportement réel de l'expérience.

%--
figure:
 id: FigPrintingOutput
 source: printing-output.png
 caption: La fonction `print()` de Python peut être utilisée pour afficher des messages de débogage sur la console.
--%

Dans l'exemple ci-dessus, il devient évident que la lettre attribuée à la variable `left_letter` (donc censée apparaître à gauche) apparaît en fait à droite, et vice versa.


### Interprétation des messages d'erreur de l'interface utilisateur

Lorsqu'un bug dans votre expérience provoque un crash, OpenSesame affiche un message d'erreur, également appelé 'Exception'. Un message d'erreur se compose généralement des éléments suivants :

- **Type d'erreur :** Indique la classe générale d'erreur. Dans l'exemple ci-dessous, il s'agit d'une `FStringError`.
- **Description :** Fournit une explication plus spécifique de ce qui a déclenché l'erreur. Dans ce cas, 'Échec de l'évaluation...'.
- **Source :** Spécifie l'élément qui a déclenché l'erreur et si elle s'est produite pendant la phase de Run ou de Prepare.
- **Traceback :** Un message d'erreur Python détaillé. Cette information n'est montrée que si l'erreur s'est produite lors de l'évaluation de code Python personnalisé, ce qui inclut les éléments INLINE_SCRIPT, mais aussi les expressions conditionnelles (par exemple, les expressions run-if), et le texte avec des références de variable intégrées.
- **En savoir plus sur cette erreur :** Un bouton interactif sur lequel vous pouvez cliquer pour obtenir des informations plus détaillées sur le message d'erreur.

Examinons un exemple pour mieux comprendre ces composants et apprendre à corriger une erreur courante :

%--
figure:
 id: FigFStringError
 source: fstring-error.png
 caption: Un `FStringError` indique un problème lors de l'évaluation d'une chaîne de texte contenant une expression Python.
--%

Il s'agit d'une `FStringError`, ce qui signifie qu'il y a eu un problème lors de l'interprétation d'une chaîne de texte qui inclut une expression Python. Dans cet exemple, le texte problématique est `{right_leter}`. Tout ce qui est encadré par des accolades est interprété comme une expression Python, et donc dans ce cas l'expression Python est `right_leter`—qui n'est tout simplement qu'un nom de variable. Essayer d'évaluer l'expression Python `right_leter` a déclenché une `NameError` parce que `right_leter` n'est pas défini.

C'est assez technique, mais qu'est-ce qui s'est exactement mal passé ici en termes simples ? Le problème provient de la référence à une variable non existante : `right_leter`. En regardant le nom de la variable, il semble probable qu'il y ait une faute de frappe : la variable prévue est probablement `right_letter`, avec un double 't'.

Où devrions-nous corriger cette erreur ? Le message d'erreur indique que la source de l'erreur est un élément appelé *target*, qui est un SKETCHPAD. Pour résoudre l'erreur, nous devons ouvrir *target* et changer le texte de '{right_leter}' à '{right_letter}'.


### Interprétation des messages d'erreur Python

En Python, les erreurs se répartissent en deux catégories : les erreurs de syntaxe et les exceptions (ou erreurs d'exécution).


#### Erreurs de syntaxe en Python

Une erreur de syntaxe se produit lorsque l'interpréteur Python ne peut pas analyser le code parce qu'il viole les règles de syntaxe de Python. Cela pourrait être dû à des parenthèses incompatibles, des virgules manquantes, une indentation incorrecte, etc. Dans OpenSesame, cela se traduit par une `PythonSyntaxError`.

%--
figure:
 id: FigPythonSyntaxError
 source: python-syntax-error.png
 caption: une `PythonSyntaxError` est déclenchée lorsque le code viole les règles de syntaxe de Python et ne peut pas être analysé.
--%

Le message d'erreur ci-dessus indique qu'une erreur de syntaxe est survenue à la ligne 16 de la phase Prepare d'un élément nommé *constants*. Voici la ligne problématique :

```python
target_orientations = [('z', 0), ('/', 90]
```

Le message laisse également entendre que des parenthèses incompatibles pourraient être à l'origine de l'erreur. En prenant cela en compte, nous pouvons résoudre le problème en ajoutant une parenthèse manquante `)` avant la parenthèse fermante `]` :

```python
target_orientations = [('z', 0), ('/', 90)]
```


#### Exceptions en Python

Lorsque le code Python est syntaxiquement correct mais rencontre un problème lors de l'exécution, une exception est levée. Dans OpenSesame, de telles exceptions se traduisent par une `PythonError`.

%--
figure:
 id: FigPythonError
 source: python-error.png
 caption: une `PythonError` est déclenchée lorsqu'une exception est levée lors de l'exécution de code Python syntaxiquement correct.
--%

Le message d'erreur ci-dessus indique qu'une `NameError` a été levée à la ligne 2 de la phase Run d'un élément nommé *trial_script*. Plus précisément, l'identifiant 'clock_sleep' n'est pas reconnu. En regardant la ligne qui cause l'erreur, il est évident que nous avons utilisé un guillemet bas (`_`) au lieu d'un point (`.`), ce qui implique incorrectement que `clock_sleep()` est une fonction.

```python
clock_sleep(495)
```

Pour corriger cela, nous devrions correctement référencer la fonction `sleep()` en tant que partie de l'objet `clock` :

```python
clock.sleep(495)
```

## Débogage dans un navigateur web (OSWeb)


### Affichage de la sortie dans la console du navigateur

La fonction JavaScript `console.log()` est un outil de débogage simple mais puissant lorsqu'il est utilisé à l'intérieur d'éléments INLINE_JAVASCRIPT. Il sert un objectif similaire à la fonction Python `print()` et le Variable Inspector, qui ne sont pas disponibles dans OSWeb. Par exemple, vous pouvez imprimer les valeurs des variables `left_letter` et `right_letter` lors de la phase de préparation d'un INLINE_SCRIPT au début de chaque essai.

Pour voir ces messages de débogage, vous devez ouvrir la console du navigateur. Voici comment le faire dans Chrome, Firefox et Edge :

- **Google Chrome:** Appuyez sur Ctrl + Shift + J (Windows / Linux) ouCmd + Option + J (Mac).
- **Mozilla Firefox:** Appuyez sur Ctrl + Shift + K (Windows / Linux) ou Cmd + Option + K (Mac).
- **Microsoft Edge:** Appuyez sur F12 pour ouvrir les outils pour développeurs, puis sélectionnez l'onglet "Console".

Une fois la console ouverte, vous pouvez surveiller la sortie tout en exécutant l'expérience, ce qui vous permet de vérifier si la sortie affichée dans la console correspond au comportement réel de l'expérience.

%--
figure:
 id: FigPrintingOutputOSWeb
 source: printing-output-osweb.png
 caption: The JavaScript `console.log()` function can be used to output debug messages to the browser console.
--%

Dans l'exemple ci-dessus, il devient évident que la lettre attribuée à la variable `left_letter` (qui devrait apparaître à gauche) apparaît en fait à droite, et vice-versa.


### Comprendre les messages d'erreur

Lorsque votre expérience basée sur un navigateur se bloque, OSWeb affichera un message d'erreur dans le navigateur. Un message d'erreur se compose généralement des éléments suivants :

- **Type d'erreur :** Indique la classe générale d'erreurs. Dans cet exemple ci-dessous, il s'agit d'une `ReferenceError`.
- **Description :** Fournit une explication plus précise de ce qui a déclenché l'erreur. Dans ce cas, 'right_leter n'est pas défini'.
- **Source :** Spécifie l'élément qui a déclenché l'erreur et s'il s'est produit pendant la phase Exécution ou Préparation. 
- **Script source :** Le code JavaScript qui a causé l'erreur. Cette information n'est affichée que si l'erreur s'est produite lors de l'évaluation de JavaScript personnalisé, qui comprend les éléments INLINE_JAVASCRIPT, mais aussi les expressions conditionnelles (par exemple, les expressions de type run-if), et le texte avec des références de variables intégrées.

Prenons un exemple pour mieux comprendre ces composants et apprendre à corriger une erreur courante :

%--
figure:
 id: FigOSWebError
 source: osweb-error.png
 caption: A `ReferenceError` indicates a reference to a non-existent variable or other non-existent object.
--%

Il s'agit d'une `ReferenceError`, qui indique que l'expérience fait référence à une variable ou un autre objet non existant. Dans cet exemple, l'erreur provient du texte `${right_leter}`. Tout ce qui est entre accolades et précédé d'un `$` est interprété comme une expression JavaScript, et dans ce cas, l'expression JavaScript est `right_leter` -- qui est simplement un nom de variable. Le fait d'essayer d'évaluer l'expression JavaScript `right_leter` a déclenché une `ReferenceError` car `right_leter` n'est pas défini.

C'est assez technique, mais en termes simples, qu'est-ce qui a mal tourné ici ? Le problème vient de la référence à une variable inexistante : `right_leter`. En regardant le nom de la variable, il semble probable qu'il y ait une erreur de frappe : la variable voulue est probablement `right_letter`, avec un double 't'.

Où devrions-nous corriger cette erreur ? Le message d'erreur indique que la source de l'erreur est un élément appelé *target*, qui est un SKETCHPAD. Pour résoudre l'erreur, nous devons ouvrir *target* et changer le texte de '{right_leter}' en '{right_letter}'.


### Utilisation de l'instruction `debugger` dans les éléments INLINE_JAVASCRIPT

La déclaration JavaScript `debugger` est un outil puissant pour déboguer des éléments `INLINE_JAVASCRIPT` dans les expériences OpenSesame/OSWeb. Il vous permet d'insérer des points d'arrêt dans votre code, provoquant une pause de l'exécution du JavaScript du navigateur à ce point. Ceci vous permet d'inspecter l'état actuel de l'espace de travail JavaScript.

L'utilisation de la déclaration `debugger` est simple. Insérez simplement la déclaration `debugger` à la ligne où vous souhaitez interrompre l'exécution. Par exemple:

```javascript
console.log(`left_letter = ${left_letter}`)
console.log(`right_letter = ${right_letter}`)
debugger // L'exécution s'arrêtera ici
```

Une fois que vous avez inséré la déclaration `debugger` dans votre code, vous devez ouvrir la console du navigateur comme expliqué ci-dessus. Après avoir ouvert la console du navigateur, exécutez votre expérience. Lorsque l'interpréteur JavaScript atteint la déclaration `debugger`, il interrompra l'exécution, et les outils de développement passeront à l'onglet "Sources" (Chrome/Edge) ou "Débogueur" (Firefox), en surlignant la ligne de point d'arrêt.

%--
figure:
 id: FigJavaScriptDebugger
 source: javascript-debugger.png
 caption: Lorsque l'interpréteur JavaScript atteint la déclaration `debugger`, il interrompt l'exécution et vous permet d'inspecter l'espace de travail JavaScript. La déclaration `debugger` ne fonctionne que lorsque la console du navigateur est ouverte.
--%

Pendant que l'exécution est interrompue, vous pouvez inspecter les valeurs des variables, parcourir le code ligne par ligne, et étudier la pile d'appels pour mieux comprendre l'état de votre programme au point d'arrêt.

N'oubliez pas de supprimer ou de commenter les déclarations `debugger` lorsque vous avez terminé le débogage, car les laisser peut interférer avec le fonctionnement normal de votre expérience.

## Gestion des erreurs ExperimentProcessDied

Il peut arriver que vous rencontriez une erreur `ExperimentProcessDied` lors d'une expérience.

%--
figure:
 id: FigExperimentProcessDied
 source: experiment-process-died.png
 caption: L'erreur `ExperimentProcessDied` indique généralement un problème avec le processus Python sous-jacent ou les bibliothèques associées, et non votre code expérimental.
--%

Cette erreur implique que le processus Python dans lequel l'expérience était en cours d'exécution s'est terminé de manière inattendue. Cela n'indique généralement pas un bug dans votre expérience, mais suggère plutôt un problème dans l'une des bibliothèques de bas niveau utilisées par OpenSesame, voire un bug dans Python lui-même.

Déterminer la cause exacte de cette erreur peut être difficile, et la résoudre peut l'être encore plus. Cependant, il existe quelques solutions que vous pouvez essayer pour atténuer le problème:

- **Changer le backend :** Sélectionnez un backend différent sous 'Exécuter l'expérience' dans les propriétés de l'expérience. Cela peut résoudre le problème car différents backends utilisent différents ensembles de bibliothèques de bas niveau.
- **Mettre à jour OpenSesame et les packages pertinents :** Mettre régulièrement à jour OpenSesame et tous les packages associés peut potentiellement résoudre ce problème, car les bugs sont régulièrement corrigés dans les nouvelles versions.