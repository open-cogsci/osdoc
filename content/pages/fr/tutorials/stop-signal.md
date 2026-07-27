title: Tâche stop-signal (travailler avec coroutines)
hash: a90dc175aa27f6f7bdfc95ae0c91f7aa1f0aacaeeac9a505a63772d5a363d5d5
locale: fr
language: French

[TOC]

## À propos d’OpenSesame

OpenSesame est un programme convivial pour le développement d’expériences comportementales en psychologie, en neurosciences et en économie expérimentale. Pour les débutants, OpenSesame dispose d’une interface graphique complète de type pointer-cliquer. Pour les utilisateurs avancés, OpenSesame prend en charge Python (bureau uniquement) et JavaScript (bureau et navigateur).

OpenSesame est disponible gratuitement sous la [General Public License v3][gpl].

## À propos de ce tutoriel

Ce tutoriel montre comment créer une tâche stop-signal dans OpenSesame à l’aide du plugin `coroutines`. L’expérience est basée sur la version à temps de réaction simple de [Logan, Cowan and Davis (1984)][references]. L’objectif principal de ce tutoriel n’est pas seulement de construire la tâche, mais aussi de comprendre comment les coroutines permettent de placer plusieurs événements sur une seule ligne temporelle d’essai.

## Ressources

- __Télécharger__ — Ce tutoriel suppose que vous utilisez OpenSesame version 4.1 ou ultérieure, et que vous exécutez l’expérience sur le bureau. Vous pouvez télécharger la version la plus récente d’OpenSesame ici :
	- <https://osdoc.cogsci.nl/4.1/download/>
- __Documentation__ — Un site web de documentation dédié est disponible à l’adresse suivante :
	- <http://osdoc.cogsci.nl/>
- __Forum__ — Un forum d’assistance est disponible à l’adresse suivante :
	- <http://forum.cogsci.nl/>
- __Sigmund__ — SigmundAI est un assistant IA ayant une connaissance experte d’OpenSesame et est disponible ici :
	- <https://sigmundai.eu/>

## L’expérience

Dans cette expérience, les participants répondent aussi rapidement que possible aux lettres qui apparaissent à l’écran. Dans la plupart des essais, ils doivent appuyer sur la barre d’espace lorsqu’une lettre apparaît. Dans certains essais, une tonalité est jouée peu après l’apparition de la lettre, et les participants doivent essayer de retenir leur réponse. Le but de la tâche est d’estimer le temps de réaction au signal d’arrêt (SSRT), une mesure latente de la vitesse du processus d’inhibition. Une estimation fiable du SSRT exige que les participants répondent rapidement lors des essais go et qu’ils tentent d’inhiber leur réponse uniquement lorsque le signal d’arrêt est présenté.

L’expérience utilise quatre lettres : `E`, `F`, `H` et `L`. La réponse est toujours la même, quelle que soit la lettre affichée. Cela fait de la tâche une version à temps de réaction simple du paradigme stop-signal.

Chaque essai a la structure suivante :

- Un point de fixation est affiché pendant 500 ms.
- Une lettre est affichée après la fixation.
- Une fenêtre de réponse s’ouvre lorsque la lettre apparaît.
- Lors des essais stop, une tonalité de 900 Hz est jouée après un court délai.
- Un masque suit la lettre.
- La durée totale de l’essai est fixée à 3500 ms.

%--
figure:
 id: Fig_paradigm
 source: stop_paradigm.png
 caption: A schematic overview of the stop-signal paradigm implemented in this tutorial.
--%

Des tâches comme celle-ci montrent généralement que les participants sont moins susceptibles d’inhiber leur réponse lorsque le délai du signal d’arrêt est long que lorsqu’il est court. Les participants peuvent parfois ralentir stratégiquement s’ils s’attendent à un signal d’arrêt. Pour cette raison, les instructions doivent souligner que les participants doivent répondre rapidement et ne doivent pas attendre la tonalité.

## Plan expérimental

Ce plan :

- est intra-sujets, parce que tous les participants effectuent tous les types d’essais
- comprend des essais go et des essais stop
- comprend quatre délais de signal d’arrêt dans les essais stop :
	- `50`
	- `100`
	- `150`
	- `200`
- comprend quatre lettres :
	- `E`
	- `F`
	- `H`
	- `L`

La table de loop contient 80 lignes et est répétée quatre fois, ce qui donne quatre blocs de 80 essais.

Nous allons maintenant construire l’expérience étape par étape.

## Étape 1 : Créer la structure de base de l’expérience

Démarrez OpenSesame et créez une nouvelle expérience. Dans ce tutoriel, la sequence principale s’appelle `experiment` et contient :

- `new_form_consent`
- `instructions`
- `simple_rt`

L’item `simple_rt` est une loop qui contient la structure d’essai de l’expérience.

La zone d’aperçu devrait maintenant ressembler à ceci :

%--
figure:
 id: Fig_overview
 source: stop_overview.png
 caption: The overview area of the stop-signal experiment.
--%

## Étape 2 : Ajouter un formulaire de consentement et un écran d’instructions

L’exemple d’expérience commence par un formulaire de consentement. Cela est facultatif d’un point de vue technique, mais dans de nombreuses expériences réelles, il est utile ou nécessaire de demander le consentement éclairé des participants avant le début de la tâche.

Après le formulaire de consentement, les participants voient un écran d’instructions. Les instructions expliquent que les participants doivent appuyer sur la barre d’espace chaque fois qu’une lettre apparaît, mais essayer de retenir leur réponse lorsqu’ils entendent la tonalité de stop. Les instructions doivent également souligner que les participants ne doivent pas attendre la tonalité avant de répondre.

L’élément d’instruction peut ressembler à ceci :

%--
figure:
 id: Fig_instructions
 source: stop_instructions.png
 caption: The instruction screen shown before the experiment starts.
--%

## Étape 3 : Créer la boucle d’essais

La structure des essais est définie dans une loop appelée `simple_rt`. Cette loop contient 80 lignes et est répétée quatre fois. L’ordre des essais est randomisé à l’intérieur de chaque répétition.

Chaque ligne définit au moins les variables suivantes :

- `letters`
- `is_stop`
- `delay`
- `correct_response`

Pour les essais go :

- `is_stop` est `no`
- `delay` est `0`
- `correct_response` est `space`

Pour les essais stop :

- `is_stop` est `yes`
- `delay` est l’une des valeurs `50`, `100`, `150` ou `200`
- `correct_response` est `None`

C’est une manière pratique d’utiliser le score intégré de l’élément `keyboard_response`. Dans les essais go, appuyer sur la barre d’espace est correct. Dans les essais stop, retenir la réponse est correct parce que la réponse correcte est définie comme `None`.

La table de la loop doit ressembler à ceci :

%--
figure:
 id: Fig_loop
 source: stop_loop.png
 caption: The loop table that defines go trials and stop trials.
--%

## Étape 4 : Créer les éléments d’essai

La coroutine utilise plusieurs éléments qui doivent d’abord être créés séparément.

### 4.1 Fixation

Insérez un nouveau sketchpad et renommez-le en `fixation`. Dessinez-y un point de fixation central. Bien que les sketchpads aient leur propre paramètre de durée, le timing de cet élément sera plus tard contrôlé par la coroutine.

### 4.2 Affichage de la lettre

Insérez un nouveau sketchpad et renommez-le en `letter`. Ajoutez un élément texte qui affiche la valeur de la variable `{letters}`, afin que la lettre affichée change d’un essai à l’autre. Les accolades autour de `{letters}` indiquent qu’il ne s’agit pas de texte littéral, mais de la valeur de la variable expérimentale `letters`, qui est définie dans la table de la loop.

Le sketchpad de la lettre doit ressembler à ceci :

%--
figure:
 id: Fig_letter
 source: stop_letter.png
 caption: The letter sketchpad, which shows the value of the variable `letters`.
--%

### 4.3 Masque

Insérez un nouveau sketchpad et renommez-le en `mask`. Dans l’expérience actuelle, ce sketchpad est vide et fonctionne donc principalement comme un espace réservé dans la chronologie de l’essai. Comme pour les autres sketchpads, son timing effectif sera plus tard déterminé par la coroutine.

### 4.4 Élément de réponse

Insérez un nouvel élément `keyboard_response` et renommez-le en `resp_simple_rt`. Définissez la réponse autorisée sur `space`. Lorsque cet élément est utilisé dans la coroutine, la fenêtre de réponse sera contrôlée par la chronologie de la coroutine plutôt que par le propre paramètre de délai d’expiration de l’élément.

Les paramètres de keyboard response doivent ressembler à ceci :

%--
figure:
 id: Fig_keyboard
 source: stop_keyboard.png
 caption: The keyboard response item configured to collect a spacebar response.
--%

### 4.5 Signal stop

Insérez un nouvel élément `synth` et renommez-le en `stop_signal`. Définissez :

- waveform sur `sine`
- frequency sur `900`
- length sur `500`
- duration sur `0`

Une durée de `0` garantit que le son démarre et que la coroutine continue immédiatement, au lieu d’attendre la fin du son.

%--
figure:
 id: Fig_synth
 source: stop_synth.png
 caption: The synth item configured to produce a 900-Hz tone lasting 500 ms.
--%

### 4.6 Logger

Insérez un nouvel item `logger` et renommez-le en `logger`. Désactivez l’enregistrement automatique et enregistrez manuellement les variables critiques. En particulier, assurez-vous que des variables telles que `letters`, `is_stop`, `delay`, `response`, `response_time` et `correct` sont incluses.

Les paramètres du logger doivent ressembler à ceci :

%--
figure:
 id: Fig_logger
 source: stop_logger.png
 caption: The logger item configured to log the critical stop-signal variables.
--%

## Étape 5 : Ajouter l’item coroutine

Insérez maintenant un item `coroutines` et renommez-le en `coroutines`. Cet item définira le timing de chaque essai sur une timeline partagée.

Définissez la durée totale de la coroutine sur `3500`, et ajoutez les items de l’essai afin qu’ils soient placés sur la même timeline d’essai.

À ce stade, il est important de garder à l’esprit que tous les items OpenSesame ne peuvent pas être utilisés dans une coroutine. Les items pris en charge comprennent au moins :

- `feedback`
- `inline_script`
- `keyboard_response`
- `logger`
- `mouse_response`
- `sampler`
- `synth`
- `sketchpad`

Si un item ne prend pas en charge les coroutines, il ne peut pas être placé sur la timeline partagée de la coroutine.

## Étape 6 : Configurer l’item coroutines

L’item `coroutines` est le cœur temporel de l’expérience. Il permet de coordonner plusieurs événements d’essai sur une seule timeline, de sorte que la présentation, le recueil de réponse et la planification sonore puissent se chevaucher dans le temps.

Ceci est particulièrement utile pour la tâche stop-signal. L’affichage de fixation apparaît d’abord, la lettre apparaît plus tard, le participant peut répondre pendant que l’essai se poursuit, et la tonalité d’arrêt n’est présentée que sur certains essais et seulement après un délai variable. Un item sequence normal n’est pas bien adapté à ce type de chevauchement temporel, alors qu’une coroutine est conçue exactement pour cet usage.

### 6.1 La timeline de la coroutine

Dans cette expérience :

- `fixation` commence à `0`
- `letter` commence à `500`
- `resp_simple_rt` commence à `500`
- `mask` commence à `1000`
- `stop_signal` commence à `{delay + 500}` uniquement lors des essais stop
- `logger` s’exécute à la fin de l’essai

La valeur de `delay` provient de la table de loop. Comme la lettre apparaît à `500` ms, l’expression `{delay + 500}` planifie le signal d’arrêt par rapport au début de la lettre plutôt que par rapport au début de l’essai entier.

### 6.2 Fonctionnement de `start`, `end` et `run_if`

Chaque ligne d’une coroutine spécifie quand un item doit s’exécuter et, dans certains cas, quand il doit s’arrêter.

- `start` indique quand l’item commence, en millisecondes après le début de la coroutine.
- `end` indique quand l’item s’arrête, si l’item reste actif sur un intervalle.
- `run_if` indique si l’item doit s’exécuter ou non.

Cela signifie que la coroutine fait plus que simplement lister des items. Elle définit une timeline et place chaque item sur cette timeline.

Par exemple :

- `letter` commence à `500`, ce qui signifie que la lettre apparaît 500 ms après le début de l’essai.
- `resp_simple_rt` commence également à `500`, ce qui signifie que le recueil de réponse commence lorsque la lettre apparaît.
- `stop_signal` utilise une condition `run_if` de sorte qu’il ne soit joué que lors des essais stop.

Une expression `run_if` typique pour le signal d’arrêt est :

`is_stop == "yes"`

Cette expression est évaluée pour chaque essai. Lors des essais stop, l’item synth est exécuté. Lors des essais go, il est ignoré.

### 6.3 Quand `end` s’applique

Tous les items d’une coroutine n’utilisent pas `end` de la même manière.

Certains items sont en pratique des items à déclenchement unique. Un sketchpad, par exemple, prépare un affichage et l’affiche lorsqu’il est démarré. En pratique, le paramètre important pour un tel item est généralement le moment `start`. Le changement d’affichage se produit à ce moment-là, et le sketchpad lui-même n’a pas besoin de rester actif de la même manière qu’un item de réponse ou un item sonore.

D’autres items restent actifs pendant un certain temps. Un `keyboard_response`, par exemple, peut rester actif pendant une fenêtre de réponse, et un item sonore peut rester actif pendant la lecture de l’audio. Pour ces items, `end` est significatif parce qu’il détermine quand l’item cesse d’être actif sur la chronologie de la coroutine.

Donc, en général :

- `start` est pertinent pour tous les items
- `end` est surtout pertinent pour les items qui restent actifs sur un intervalle
- `run_if` est pertinent chaque fois qu’un item ne doit s’exécuter que dans certaines conditions

### 6.4 Comment cela s’applique à la tâche stop-signal

Dans l’expérience actuelle :

- `fixation`, `letter` et `mask` sont principalement utilisés pour mettre à jour l’affichage à des moments précis
- `resp_simple_rt` reste actif pendant la fenêtre de réponse
- `stop_signal` ne démarre que lorsque `is_stop == "yes"`
- `logger` s’exécute à la fin de l’essai

Cela signifie que les sketchpads reposent principalement sur leurs temps de `start`, tandis que l’item de réponse et l’item stop-signal sont mieux compris comme des items qui sont actifs pendant une partie de la chronologie de l’essai.

### 6.5 Comment la durée des items est liée au timing de la coroutine

Lorsque vous travaillez avec des coroutines, il est important de se rappeler que c’est la coroutine qui contrôle quand les items sont actifs. En d’autres termes, le timing effectif est déterminé par les paramètres `start`, `end` et `run_if` de la coroutine, et non principalement par les paramètres de durée ou de timeout à l’intérieur des items individuels.

C’est pourquoi les sketchpads dans cette expérience n’ont pas besoin de leurs propres durées pour définir la structure de l’essai. Leur rôle dans la chronologie est déterminé par la coroutine. La même logique s’applique au `keyboard_response` : même si l’item possède son propre paramètre de timeout, la fenêtre de réponse est effectivement définie par la chronologie de la coroutine.

Le synth `stop_signal` illustre cela clairement. Ses propriétés sonores, telles que la forme d’onde et la durée, sont définies dans l’item synth lui-même, mais le moment auquel il démarre est défini par la coroutine.

### 6.6 Pourquoi le synth stop-signal utilise `duration = 0`

L’item `stop_signal` a une durée sonore de 500 ms et une durée de `0`. C’est important, car cela signifie que le son démarre et que la coroutine continue immédiatement, au lieu d’attendre que le son se termine.

Par conséquent, le ton peut être joué pendant que le reste de la chronologie de la coroutine continue. C’est exactement ce qui est nécessaire dans une tâche stop-signal : le signal doit survenir à un moment précis, mais il ne doit pas interrompre la collecte des réponses ni le reste de l’essai.

Les paramètres de la coroutine devraient ressembler à ceci :

%--
figure:
 id: Fig_coroutines
 source: stop_coroutines.png
 caption: The coroutine item that controls the shared trial timeline.
--%

### 6.7 Pourquoi le logger est placé à `3400`

Dans l’exemple d’expérience, la durée totale de la coroutine est de `3500` ms, mais `resp_simple_rt` et `logger` sont tous deux réglés sur `3400`. Cela signifie que la fenêtre de réponse se ferme à `3400` ms et que l’essai est enregistré à ce même moment, plutôt qu’à la toute fin de la coroutine.

Ceci est utile, car cela garantit que la collecte des réponses ne se poursuit pas au-delà du moment où l’essai est enregistré. En même temps, les `100` ms finaux de la coroutine restent inutilisés comme une petite marge de sécurité avant que la coroutine elle-même ne se termine.

En pratique, cela signifie que lorsque le logger s’exécute, les variables de réponse pertinentes, telles que `response`, `response_time` et `correct`, ont déjà été définies.

## Étape 7 : Tester l’expérience

Lorsque la structure de l’expérience est terminée, effectuez un essai et vérifiez que :

- le point de fixation apparaît en premier
- la lettre apparaît après 500 ms
- la fenêtre de réponse s’ouvre au début de la lettre
- le ton stop n’est joué que lors des essais stop
- le timing du ton stop dépend de `delay`
- la durée de l’essai est toujours de 3500 ms

Il est également utile d’inspecter le fichier log pour vérifier que `letters`, `is_stop`, `delay`, `response`, `response_time` et `correct` sont correctement enregistrés.

## Terminé

Félicitations, l’expérience est terminée. Vous pouvez maintenant l’essayer en appuyant sur le bouton bleu à double flèche (raccourci : `Ctrl+W`).

Vous trouverez ci-dessous une démonstration d’une version abrégée de l’expérience créée à des fins de tutoriel.

<video controls width ="100%"> 
    <source src="/video/stop_demo.mp4" type="video/mp4">
</video>
<p align="center"><em>Vidéo 1. Démonstration de la tâche stop-signal terminée.</em></p>

## Références

Logan, G. D., Cowan, W. B., & Davis, K. A. (1984). Sur la capacité à inhiber des réponses à temps de réaction simples et de choix : un modèle et une méthode. *Journal of Experimental Psychology: Human Perception and Performance*, *10*(2), 276–291.

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame : un constructeur d’expériences graphique, open source, pour les sciences sociales. *Behavior Research Methods*, *44*(2), 314–324.

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html