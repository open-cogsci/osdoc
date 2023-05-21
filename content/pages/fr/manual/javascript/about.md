title: À propos de JavaScript
hash: 073e796248136726c6b04b838715a867d5ef1958a34beae0785870553faa2e4c
locale: fr
language: French

Dans OpenSesame, vous pouvez créer des expériences complexes en utilisant uniquement l'interface graphique (GUI). Mais il vous arrivera parfois de rencontrer des situations où les fonctionnalités offertes par le GUI sont insuffisantes. Dans ces cas, vous pouvez ajouter du code JavaScript à votre expérience.

JavaScript est pour les expériences qui s'exécutent dans un navigateur avec OSWeb. Si vous avez besoin d'exécuter votre expérience sur le bureau, vous devez utiliser [Python](%url:manual/python/about%) au lieu de JavaScript.

__Note de version :__ Le support du bureau pour JavaScript a été supprimé dans OpeSesame 4.0. Cela est dû au fait que la prise en charge de JavaScript sur le bureau était incomplète et perçue par les utilisateurs comme source de confusion sans apporter beaucoup d'avantages.
{: .page-notification}

[TOC]


## Apprendre JavaScript

Il existe de nombreux tutoriels JavaScript disponibles en ligne. Une bonne ressource est Code Academy :

- <https://www.codecademy.com/learn/introduction-to-javascript>


## JavaScript dans l'interface graphique OpenSesame


### Éléments Inline_javascript

Pour utiliser du code JavaScript, vous devez ajouter un élément INLINE_JAVASCRIPT à votre expérience. Une fois cela fait, vous verrez quelque chose comme %FigInlineJavaScript.

%--
figure:
 id: FigInlineJavaScript
 source: inline-javascript.png
 caption: L'élément INLINE_JAVASCRIPT.
--%

Comme vous pouvez le voir, l'élément INLINE_JAVASCRIPT se compose de deux onglets : un pour la phase de préparation et un pour la phase d'exécution. La phase de préparation est exécutée en premier, pour permettre aux éléments de se préparer pour la phase d'exécution sensible au temps. Il est recommandé de construire les objets `Canvas` pendant la phase de préparation, afin qu'ils puissent être présentés sans délai pendant la phase d'exécution. Mais cela n'est qu'une convention ; vous pouvez exécuter du code JavaScript arbitraire pendant les deux phases.

Pour plus d'informations sur la stratégie de préparation-exécution, voir :

- %link:prepare-run%


### Afficher des informations sur la console

Vous pouvez imprimer sur la console avec la commande `console.log()` :

```js
console.log('Ceci apparaîtra dans la console !')
```

Lors de l'exécution sur le bureau, la sortie apparaîtra dans la console OpenSesame (ou : fenêtre de débogage). Lors de l'exécution dans un navigateur, la sortie apparaîtra dans la console du navigateur.


## Choses à savoir

### Fonctions courantes

De nombreuses fonctions courantes sont directement disponibles dans un élément INLINE_JAVASCRIPT. Par exemple :

```js
// `Canvas()` est une fonction d'usine qui renvoie un objet `Canvas`
let fixdotCanvas = Canvas()
if (sometimes()) {  // Parfois, le fixdot est vert
    fixdotCanvas.fixdot({color: 'green'})
} else {  // Parfois, il est rouge
    fixdotCanvas.fixdot({color: 'red'})
}
fixdotCanvas.show()
```

Pour une liste de fonctions courantes, voir :

- %link:manual/javascript/common%


### L'objet `persistent` : conserver des objets entre les scripts

__Note de version__ À partir d'OSWeb 2.0, tous les codes JavaScript sont exécutés dans le même espace de travail et les objets sont donc conservés entre les scripts. Cela signifie que vous n'avez plus besoin de l'objet `persistent`.
{:.page-notification}

Chaque élément INLINE_JAVASCRIPT est exécuté dans son propre espace de travail. Cela signifie — et cela diffère des éléments Python INLINE_SCRIPT ! — que vous ne pouvez pas utiliser de variables ou de fonctions que vous avez déclarées dans un script dans un autre script. Pour contourner cela, vous pouvez attacher des variables ou des fonctions en tant que propriétés à l'objet `persistent`, qui sert de conteneur pour les choses que vous voulez conserver entre les scripts.

De cette manière, vous pouvez construire un `Canvas` dans un INLINE_JAVASCRIPT ...

```js
persistent.myCanvas = Canvas()
persistent.myCanvas.fixdot()
```

... et l'afficher dans un autre INLINE_JAVASCRIPT :

```js
persistent.myCanvas.show()
```


### L'objet `vars` : Accès aux variables expérimentales

__Note de version__ À partir d'OSWeb 2.0, toutes les variables expérimentales sont disponibles en tant que globales. Cela signifie que vous n'avez plus besoin de l'objet `vars`.
{:.page-notification}

Vous pouvez accéder aux variables expérimentales via l'objet `vars` :

```js
// Obtenir une variable expérimentale
console.log('my_variable est : ' + vars.my_variable)
// Définir une variable expérimentale
vars.my_variable = 'my_value'
```

### L'objet `pool` : Accès à la réserve de fichiers

Vous accédez aux 'fichiers' de la réserve de fichiers via l'objet `pool`. L'utilisation la plus évidente de cela est de lire les fichiers CSV, par exemple avec les conditions expérimentales, à partir de la réserve de fichiers en utilisant la bibliothèque `csv-parse` (décrite plus en détail ci-dessous).

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

Vous pouvez également jouer des fichiers sonores directement à partir de la réserve de fichiers. En supposant qu'il y ait un fichier appelé `bark.ogg` dans la réserve de fichiers, vous pouvez le jouer comme ceci :

```js
pool['bark.ogg'].data.play()
```


### La classe `Canvas` : Présentation de stimuli visuels

La classe `Canvas` est utilisée pour présenter des stimuli visuels. Par exemple, vous pouvez montrer un point de fixation comme suit :

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

Un aperçu complet de la classe `Canvas` se trouve ici :

- %link:manual/javascript/canvas%

## Bibliothèques JavaScript disponibles

Les bibliothèques JavaScript suivantes sont incluses par défaut :

- [Fonctions aléatoires (`random-ext`)](%url:manual/javascript/random%)
- [Fonctions de conversion de couleurs (`color-convert`)](%url:manual/javascript/color-convert%)
- [Fonctions CSV (`csv-parse`)](%url:manual/javascript/csv%)
- [Itérateurs de type Python (`pythonic`)](%url:manual/javascript/pythonic%)

Vous pouvez inclure des bibliothèques JavaScript supplémentaires en ajoutant les URL des bibliothèques dans le champ 'Bibliothèques JavaScript externes' du panneau de configuration d'OSWeb.


## Débogage

La plupart des navigateurs modernes, notamment Chrome et Firefox, disposent d'un débogueur intégré puissant. Vous pouvez activer le débogueur en ajoutant une ligne qui indique simplement `debugger` à votre script (%FigDebuggerInlineJavaScript).

%--
figure:
 id: FigDebuggerInlineJavaScript
 source: debugger-inline-javascript.png
 caption: Activation du débogueur à partir d'un élément INLINE_JAVASCRIPT.
--%


Ensuite, démarrez l'expérience et affichez le débogueur (ou : Dev tools dans Chrome, ou : Outils web de développement dans Firefox) dès que l'écran d'accueil d'OSWeb apparaît. Le débogueur mettra alors en pause l'expérience lorsqu'il rencontrera l'instruction `debugger`. À ce stade, vous pouvez utiliser la Console pour interagir avec l'espace de travail JavaScript, ou vous pouvez inspecter les variables en utilisant l'outil Scope (%FigDebuggerChrome).

%--
figure:
 id: FigDebuggerChrome
 source: debugger-chrome.png
 caption: Inspecter la portée des variables dans Chrome.
--%

Voir aussi :

- %link:manual/osweb/osweb%