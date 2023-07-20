title: À propos de JavaScript
hash: a7f9ce07f8ba8ef35658430e6e490db256a6c6c1681e7b791f85a4d8f288ae44
locale: fr
language: French

Dans OpenSesame, vous pouvez créer des expériences complexes en utilisant uniquement l'interface graphique utilisateur (GUI). Mais vous rencontrerez parfois des situations où les fonctionnalités fournies par la GUI sont insuffisantes. Dans ces cas, vous pouvez ajouter du code JavaScript à votre expérience.

JavaScript est destiné aux expériences qui s'exécutent dans un navigateur avec OSWeb. Si vous avez besoin d'exécuter votre expérience sur le bureau, vous devez utiliser [Python](%url:manual/python/about%) au lieu de JavaScript.

__Note de version :__ Le support du bureau pour JavaScript a été supprimé dans OpeSesame 4.0. C'est parce que le support de JavaScript sur le bureau était incomplet et a été perçu par les utilisateurs comme déroutant sans apporter beaucoup d'avantages.
{: .page-notification}

[TOC]


## Apprendre JavaScript

Il existe de nombreux tutoriels JavaScript disponibles en ligne. Une bonne ressource est Code Academy :

- <https://www.codecademy.com/learn/introduction-to-javascript>


## JavaScript dans l'interface GUI d'OpenSesame


### Items inline_javascript

Pour utiliser le code JavaScript, vous devez ajouter un élément INLINE_JAVASCRIPT à votre expérience. Après avoir fait cela, vous verrez quelque chose comme %FigInlineJavaScript.

%--
figure:
 id: FigInlineJavaScript
 source: inline-javascript.png
 caption: L'élément INLINE_JAVASCRIPT.
--%

Comme vous pouvez le voir, l'élément INLINE_JAVASCRIPT se compose de deux onglets : l'un pour la phase de préparation et l'autre pour la phase d'exécution. La phase de préparation est exécutée en premier, pour permettre aux éléments de se préparer pour la phase d'exécution qui est critique en termes de temps. Il est recommandé de construire des objets `Canvas` lors de la phase de préparation, afin qu'ils puissent être présentés sans délai lors de la phase d'exécution. Mais cela n'est qu'une convention ; vous pouvez exécuter du code JavaScript arbitraire lors des deux phases.

Pour plus d'informations sur la stratégie de préparation-exécution, voir :

- %link:prepare-run%


### Afficher la sortie à la console

Vous pouvez imprimer à la console avec la commande `console.log()` :

```js
console.log('Ceci apparaîtra dans la console !')
```

Lors de l'exécution sur le bureau, la sortie apparaîtra dans la console OpenSesame (ou : fenêtre de débogage). Lors de l'exécution dans un navigateur, la sortie apparaîtra dans la console du navigateur.


## Choses à savoir

### Fonctions communes

De nombreuses fonctions communes sont directement disponibles dans un élément INLINE_JAVASCRIPT. Par exemple :

```js
// `Canvas()` est une fonction d'usine qui retourne un objet `Canvas`
let fixdotCanvas = Canvas()
if (sometimes()) {  // Parfois le fixdot est vert
    fixdotCanvas.fixdot({color: 'green'})
} else {  // Parfois il est rouge
    fixdotCanvas.fixdot({color: 'red'})
}
fixdotCanvas.show()
```

Pour une liste de fonctions communes, voir :

- %link:manual/javascript/common%


### L'objet `persistent` : conservation des objets entre les scripts

__Note de version__ À partir de OSWeb 2.0, tout le code JavaScript est exécuté dans le même espace de travail et les objets sont donc conservés entre les scripts. Cela signifie que vous n'avez plus besoin de l'objet `persistent`.
{:.page-notification}

Chaque élément INLINE_JAVASCRIPT est exécuté dans son propre espace de travail. Cela signifie - et c'est différent des éléments INLINE_SCRIPT Python ! - que vous ne pouvez pas utiliser de variables ou de fonctions que vous avez déclarées dans un script dans un autre script. Comme solution de contournement, vous pouvez attacher des variables ou des fonctions en tant que propriétés à l'objet `persistent`, qui sert de conteneur pour les choses que vous voulez conserver entre les scripts.

De cette façon, vous pouvez construire un `Canvas` dans un INLINE_JAVASCRIPT ...

```js
persistent.myCanvas = Canvas()
persistent.myCanvas.fixdot()
```

.. et le montrer dans un autre INLINE_JAVASCRIPT :

```js
persistent.myCanvas.show()
```


### L'objet `vars` : Accès aux variables expérimentales

__Note de version__ À partir de OSWeb 2.0, toutes les variables expérimentales sont disponibles en tant que globales. Cela signifie que vous n'avez plus besoin de l'objet `vars`.
{:.page-notification}

Vous pouvez accéder aux variables expérimentales grâce à l'objet `vars` :

```js
// OSWeb <= 1.4 (avec l'objet vars)
// Obtenez une variable expérimentale
console.log('ma_variable est : ' + vars.ma_variable)
// Définir une variable expérimentale
vars.my_variable = 'ma_valeur'

// OSWeb >= 2.0 (sans l'objet vars)
// Obtenez une variable expérimentale
console.log('ma_variable est: ' + ma_variable)
// Définir une variable expérimentale
var ma_variable = 'ma_valeur'
```


### L'objet `pool` : Accéder à la réserve de fichiers

Vous accédez aux 'fichiers' de la réserve de fichiers via l'objet `pool`. L'utilisation la plus évidente de cela est de parser les fichiers CSV, par exemple avec les conditions expérimentales, à partir de la réserve de fichiers en utilisant la bibliothèque `csv-parse` (décrite en détail ci-dessous).

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

Vous pouvez également lire des fichiers sonores directement à partir de la réserve de fichiers. En supposant qu'il y a un fichier appelé `bark.ogg` dans la réserve de fichiers, vous pouvez le lire comme suit :

```js
pool['bark.ogg'].data.play()
```


### La classe `Canvas` : Présenter des stimuli visuels

La classe `Canvas` est utilisée pour présenter des stimuli visuels. Par exemple, vous pouvez montrer un point de fixation comme suit :

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

Une vue d'ensemble complète de la classe `Canvas` peut être trouvé ici :

- %link:manual/javascript/canvas%

## Bibliothèques JavaScript disponibles

Les bibliothèques JavaScript suivantes sont incluses par défaut :

- [Fonctions aléatoires (`random-ext`)](%url:manual/javascript/random%)
- [Fonctions de conversion de couleur (`color-convert`)](%url:manual/javascript/color-convert%)
- [Fonctions CSV (`csv-parse`)](%url:manual/javascript/csv%)
- [Itérateurs semblables à Python (`pythonic`)](%url:manual/javascript/pythonic%)

Vous pouvez inclure des bibliothèques JavaScript supplémentaires par des URLs vers les bibliothèques dans le champ 'Bibliothèques JavaScript externes' du panneau de contrôle OSWeb.


## Débogage

Voir :

- %link:debugging%