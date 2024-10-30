title: À propos de JavaScript
hash: 89b8cd7f6f738823b8fc04558cb7b3e118768d97f5e91a82f90905cbf9bdbe6e
locale: fr
language: French

Dans OpenSesame, vous pouvez créer des expériences complexes en utilisant uniquement l'interface graphique (GUI). Mais vous rencontrerez parfois des situations où les fonctionnalités fournies par la GUI sont insuffisantes. Dans ces cas, vous pouvez ajouter du code JavaScript à votre expérience.

JavaScript est utilisé pour les expériences qui s'exécutent dans un navigateur avec OSWeb. Si vous avez besoin d'exécuter votre expérience sur le bureau, vous devez utiliser [Python](%url:manual/python/about%) au lieu de JavaScript.

__Remarque sur la version :__ Le support de JavaScript sur le bureau a été supprimé dans OpenSesame 4.0. Cela est dû au fait que le support de JavaScript sur le bureau était incomplet et était perçu par les utilisateurs comme déroutant sans apporter beaucoup d'avantages.
{: .page-notification}

[TOC]


## Apprendre JavaScript

Il existe de nombreux didacticiels JavaScript en ligne. Une bonne ressource est Code Academy :

- <https://www.codecademy.com/learn/introduction-to-javascript>


## JavaScript dans l'interface graphique d'OpenSesame


### Éléments Inline_javascript

Pour utiliser du code JavaScript, vous devez ajouter un élément INLINE_JAVASCRIPT à votre expérience. Après cela, vous verrez quelque chose comme %FigInlineJavaScript.

figure:
 id: FigInlineJavaScript
 source: inline-javascript.png
 caption: L'élément INLINE_JAVASCRIPT.

Comme vous pouvez le voir, l'élément INLINE_JAVASCRIPT consiste en deux onglets : un pour la phase de Préparation et l'autre pour la phase de Lancement. La phase de Préparation est exécutée en premier, pour permettre aux items de se préparer pour la phase de Lancement sensible au temps. Il est de bonne pratique de construire des objets `Canvas` pendant la phase de Préparation, afin qu'ils puissent être présentés sans délai pendant la phase de Lancement. Mais c'est seulement une convention ; vous pouvez exécuter du code JavaScript arbitraire pendant les deux phases.

Pour plus d'informations sur la stratégie de préparation-lancement, voir :

- %link:prepare-run%


### Imprimer la sortie dans la console

Vous pouvez imprimer dans la console avec la commande `console.log()` :

```js
console.log('Ceci apparaîtra dans la console !')
```

Lors de l'exécution sur le bureau, la sortie apparaîtra dans la console d'OpenSesame (ou : fenêtre de débogage). Lors de l'exécution dans un navigateur, la sortie apparaîtra dans la console du navigateur.


## Choses à savoir

### Fonctions communes

De nombreuses fonctions communes sont directement disponibles dans un élément INLINE_JAVASCRIPT. Par exemple :

```js
// `Canvas()` est une fonction usine qui renvoie un objet `Canvas`
let fixdotCanvas = Canvas()
if (sometimes()) {  // Parfois le fixdot est vert
    fixdotCanvas.fixdot({color: 'green'})
} else {  // Parfois il est rouge
    fixdotCanvas.fixdot({color: 'red'})
}
fixdotCanvas.show()
```

Pour une liste des fonctions communes, voir :

- %link:manual/javascript/common%


### Déclarer des variables (let et var)

Les éléments INLINE_JAVASCRIPT sont exécutés en mode non-strict (ou : sloppy). Cela signifie que vous pouvez assigner une valeur à une variable qui n'a pas été explicitement déclarée. Lorsque vous faites cela, la variable est implicitement déclarée en utilisant `var` si elle ne l'a pas déjà été.

```js
my_variable = 'ma valeur'  // implicitement déclarée en utilisant var
```

Les variables qui sont déclarées implicitement ou explicitement en utilisant `var` sont globales, ce qui signifie principalement qu'elles peuvent être enregistrées par un LOGGER. Les variables qui sont déclarées en utilisant `let` ne sont pas globales, ce qui signifie principalement qu'elles ne sont pas enregistrées par un LOGGER.

```js
this_is_a_global_variable = 'ma valeur'
var this_is_also_a_global_variable = 'ma valeur'
let this_is_not_a_global_variable = 'ma valeur'
```


### L'objet `persistent` : préserver les objets à travers les scripts

__Remarque de version__ À partir d'OSWeb 2.0, tout le code JavaScript est exécuté dans le même espace de travail et les objets sont donc préservés à travers les scripts. Cela signifie que vous n'avez plus besoin de l'objet `persistent`.
{:.page-notification}

Chaque élément INLINE_JAVASCRIPT est exécuté dans son propre espace de travail. Cela signifie — et c'est différent des éléments INLINE_SCRIPT Python ! — que vous ne pouvez pas utiliser les variables ou les fonctions que vous avez déclarées dans un script dans un autre script. Pour contourner ce problème, vous pouvez attacher des variables ou des fonctions comme propriétés à l'objet `persistent`, qui sert de conteneur pour les éléments que vous souhaitez conserver entre les scripts.

De cette façon, vous pouvez construire un `Canvas` dans un INLINE_JAVASCRIPT ...

```js
persistent.myCanvas = Canvas()
persistent.myCanvas.fixdot()
```

... et l'afficher dans un autre INLINE_JAVASCRIPT :

```js
persistent.myCanvas.show()
```


### L'objet `vars` : Accès aux variables expérimentales

__Note de version__ À partir de OSWeb 2.0, toutes les variables expérimentales sont disponibles en tant que globales. Cela signifie que vous n'avez plus besoin de l'objet `vars`.
{:.page-notification}

Vous pouvez accéder aux variables expérimentales via l'objet `vars` :

```js
// OSWeb <= 1.4 (avec l'objet vars)
// Obtenir une variable expérimentale
console.log('my_variable est : ' + vars.my_variable)
// Définir une variable expérimentale
vars.my_variable = 'my_value'

// OSWeb >= 2.0 (sans l'objet vars)
// Obtenir une variable expérimentale
console.log('my_variable est : ' + my_variable)
// Définir une variable expérimentale
my_variable = 'my_value'
```


### L'objet `pool` : Accès au pool de fichiers

Vous accédez aux 'fichiers' du pool de fichiers via l'objet `pool`. L'utilisation la plus évidente de cela est de parser des fichiers CSV, par exemple avec des conditions expérimentales, depuis le pool de fichiers en utilisant la bibliothèque `csv-parse` (décrite plus en détail ci-dessous).

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

Vous pouvez également jouer des fichiers sonores directement depuis le pool de fichiers. En supposant qu'il y ait un fichier appelé `bark.ogg` dans le pool de fichiers, vous pouvez le jouer ainsi :

```js
audioContext = new (window.AudioContext || window.webkitAudioContext)()
source = audioContext.createBufferSource()
source.buffer = pool['bark.ogg'].data
source.connect(audioContext.destination)
source.start(0)
```

Notez que dans les anciennes versions de OSWeb, vous pourriez simplement utiliser `pool['bark.ogg'].data.play()`. Cependant, cela ne fonctionne plus depuis qu'OSWeb a migré vers l'API Web Audio, qui est une manière plus moderne et largement soutenue de jouer de l'audio.


### La classe `Canvas` : Présentation de stimuli visuels

La classe `Canvas` est utilisée pour présenter des stimuli visuels. Par exemple, vous pouvez montrer un point de fixation comme suit :

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

Un aperçu complet de la classe `Canvas` peut être trouvé ici :

- %link:manual/javascript/canvas%

## Bibliothèques JavaScript disponibles

Les bibliothèques JavaScript suivantes sont incluses par défaut :

- [fonctions aléatoires (`random-ext`)](%url:manual/javascript/random%)
- [fonctions de conversion de couleurs (`color-convert`)](%url:manual/javascript/color-convert%)
- [fonctions CSV (`csv-parse`)](%url:manual/javascript/csv%)
- [itérateurs de style Python (`pythonic`)](%url:manual/javascript/pythonic%)

Vous pouvez inclure des bibliothèques JavaScript supplémentaires en ajoutant les URL des bibliothèques dans le champ 'Bibliothèques JavaScript externes' du panneau de contrôle OSWeb.


## Débogage

Voir :

- %link:debugging%
