title: Temps
reviewed: false
hash: 220d36e32fac1e6b240a9d60c9d1a9e560276d629ba1cf584425ef078b5c3c85
locale: fr
language: French

Cette page décrit divers problèmes liés au timing et fournit des résultats de tests et des conseils pour tester votre propre système. Si vous rencontrez des problèmes de timing, veuillez prendre le temps de lire cette page. De nombreux problèmes sont résolus en tenant compte de choses telles que la préparation des stimuli et les propriétés de votre écran.

[TOC]

## OpenSesame est-il capable de gérer le temps avec une précision en millisecondes ?

La réponse courte est : oui. La réponse longue est le reste de cette page.

## Considérations importantes pour les expériences sensibles au temps

### Vérifiez votre timing !

OpenSesame vous permet de contrôler très précisément le timing de vos expériences. Mais cela ne garantit pas un timing précis dans chaque expérience spécifique ! Pour diverses raisons, dont beaucoup sont décrites sur cette page, vous pouvez rencontrer des problèmes de timing. Par conséquent, dans les expériences sensibles au temps, vous devez toujours vérifier si le timing de votre expérience est conforme à ce qui est prévu. La façon la plus simple de le faire est de vérifier les horodatages d'affichage rapportés par OpenSesame.

Chaque élément SKETCHPAD possède une variable appelée `time_[sketchpad name]` qui contient l'horodatage de la dernière fois que le SKETCHPAD a été montré. Par conséquent, si vous voulez que le SKETCHPAD *cible* soit montré pendant 100 ms, suivi du SKETCHPAD *masque*, vous devez vérifier que `time_mask` - `time_target` est bien de 100. Lors de l'utilisation de code Python inline, vous pouvez utiliser le fait que `canvas.show()` renvoie l'horodatage d'affichage.

### Comprendre votre écran

Les écrans d'ordinateur se rafraîchissent périodiquement. Par exemple, si le taux de rafraîchissement de votre écran est de 100 Hz, l'écran se rafraîchit toutes les 10 ms (1000 ms / 100 Hz). Cela signifie qu'un stimulus visuel est toujours présenté pendant une durée multiple de 10 ms et que vous ne pourrez pas présenter un stimulus pendant, par exemple, 5 ou 37 ms. Le taux de rafraîchissement le plus courant est de 60 Hz (= cycle de rafraîchissement de 16,67 ms), bien que des écrans avec des taux de rafraîchissement beaucoup plus élevés soient parfois utilisés pour les systèmes expérimentaux.

Dans %VidRefresh, vous pouvez voir à quoi ressemble un rafraîchissement d'écran au ralenti. Sur les écrans CRT (c'est-à-dire non à écran plat, au centre), le rafraîchissement est un seul pixel qui se déplace sur l'écran de gauche à droite et de haut en bas. Par conséquent, un seul pixel est allumé à la fois, c'est pourquoi les écrans CRT scintillent légèrement. Sur les écrans LCD ou TFT (à écran plat, à gauche et à droite), le rafraîchissement est un "remplissage progressif" de haut en bas. Les écrans LCD et TFT ne scintillent donc pas. (À moins que vous ne présentiez un stimulus clignotant, bien sûr.)

%--
video:
 id: VidRefresh
 source: vimeo
 videoid: 24216910
 width: 640
 height: 240
 caption: Une vidéo au ralenti du cycle de rafraîchissement sur les écrans CRT (centre) et LCD/TFT. Vidéo avec l'aimable autorisation de Jarik den Hartog et du personnel de support technique de l'Université VU d'Amsterdam.
--%

Si un nouvel affichage de stimulus est présenté pendant que le cycle de rafraîchissement est à mi-chemin, vous observerez un "déchirement". C'est-à-dire que la moitié supérieure de l'écran affiche l'ancien affichage, tandis que la partie inférieure affiche le nouvel affichage. Ceci est généralement considéré comme indésirable et, par conséquent, un nouvel affichage doit être présenté au moment précis où le cycle de rafraîchissement commence par le haut. Ceci est appelé "synchronisation avec le rafraîchissement vertical" ou simplement "v-sync". Lorsque le v-sync est activé, le déchirement n'est plus visible, car il coïncide avec le bord supérieur de l'écran. Cependant, le v-sync ne change rien au fait qu'un écran ne se rafraîchit pas instantanément et affiche donc toujours, pendant un certain temps, à la fois l'ancien et le nouvel affichage.

Un autre concept important est celui du "blocage sur le rafraîchissement vertical" ou le "basculement bloquant". Habituellement, lorsque vous envoyez une commande pour afficher un nouvel écran, l'ordinateur accepte cette commande immédiatement et place l'écran à afficher dans une file d'attente. Cependant, l'écran peut ne pas apparaître réellement sur le moniteur avant un certain temps, généralement jusqu'au début du prochain cycle de rafraîchissement (en supposant que la synchronisation verticale soit activée). Par conséquent, vous ne savez pas exactement quand l'écran apparaît, car votre horodatage reflète le moment où l'affichage a été mis en file d'attente, plutôt que le moment où il a été présenté. Pour contourner ce problème, vous pouvez utiliser un "basculement bloquant". Cela signifie essentiellement que lorsque vous envoyez une commande pour afficher un nouvel écran, l'ordinateur se bloque jusqu'à ce que l'affichage apparaisse réellement. Cela vous permet d'obtenir des horodatages d'affichage très précis, au prix d'une baisse significative des performances due au fait que l'ordinateur est bloqué pendant une grande partie du temps alors qu'il attend qu'un affichage soit montré. Mais pour les expériences, un basculement bloquant est généralement considéré comme la stratégie optimale.

Enfin, les moniteurs LCD peuvent souffrir de "latence d'entrée". Cela signifie qu'il y a un délai supplémentaire et parfois variable entre le moment où l'ordinateur "pense" qu'un écran apparaît et le moment où l'écran apparaît réellement. Ce délai résulte de diverses formes de traitement numérique effectuées par le moniteur, telles que la correction des couleurs ou le lissage des images. À ma connaissance, la latence d'entrée ne peut pas être résolue de manière programmatique, et vous devez éviter les moniteurs avec une latence d'entrée significative pour des expériences critiques en matière de temps.

Pour une discussion connexe, voir :

- <http://docs.expyriment.org/Timing.html#visual>


### Respecter la limite de rafraîchissement

Imaginez que vous arrivez à une gare à 10h30. Votre train part à 11h00, ce qui vous laisse exactement 30 minutes pour prendre un café. Cependant, si vous prenez un café pendant exactement 30 minutes, vous arriverez de nouveau sur le quai juste à temps pour voir votre train partir, et vous devrez attendre le prochain train. Par conséquent, si vous avez 30 minutes d'attente, vous devriez prendre un café pendant légèrement moins de 30 minutes, comme 25 minutes.

La situation est analogue lors de la spécification des intervalles pour la présentation de stimuli visuels. Disons que vous avez un moniteur 100 Hz (donc 1 rafraîchissement toutes les 10 ms) et que vous voulez présenter un stimulus cible pendant 100 ms, suivi d'un masque. Votre première inclination pourrait être de spécifier un intervalle de 100 ms entre la cible et le masque, car c'est après tout ce que vous voulez. Cependant, spécifier un intervalle de 100 ms exactement fera probablement en sorte que le masque "manque la limite de rafraîchissement", et le masque ne sera présenté que lors du prochain cycle de rafraîchissement, soit 10 ms plus tard (en supposant que la synchronisation verticale soit activée). Donc, si vous spécifiez un intervalle de 100 ms, vous obtiendrez dans la plupart des cas un intervalle de 110 ms !

La solution est simple : vous devez spécifier un intervalle légèrement plus court que ce que vous visez, comme 95 ms. Ne vous inquiétez pas de l'intervalle étant trop court, car sur un moniteur 100 Hz, l'intervalle entre deux affichages de stimulus est nécessairement un multiple de 10 ms. Par conséquent, 95 ms deviendront 100 ms (10 images), 1 ms deviendra 10 ms (1 image), etc. Autrement dit, les intervalles seront arrondis à la hausse (et jamais arrondis à la baisse!) à l'intervalle le plus proche qui est cohérent avec la fréquence de rafraîchissement de votre moniteur.

### Désactiver les effets du bureau

De nombreux systèmes d'exploitation modernes utilisent des effets graphiques de bureau. Ceux-ci fournissent, par exemple, les effets de transparence et les effets de minimisation et de maximisation de fenêtre fluides que vous voyez sur la plupart des systèmes d'exploitation modernes. Bien que le logiciel qui sous-tend ces effets diffère d'un système à l'autre, ils forment généralement une couche supplémentaire entre votre application et l'affichage. Cette couche supplémentaire peut empêcher OpenSesame de se synchroniser avec le rafraîchissement vertical et/ou de mettre en œuvre un basculement bloquant.

Bien que les effets de bureau *puissent* causer des problèmes, ils ne le font généralement pas. Cela semble varier d'un système à l'autre et d'une carte vidéo à l'autre. Néanmoins, lorsque le système d'exploitation le permet, il est préférable de désactiver les effets de bureau sur les systèmes utilisés pour les tests expérimentaux.

Quelques conseils concernant les effets de bureau pour les différents systèmes d'exploitation :

- Sous *Windows XP*, il n'y a pas du tout d'effets de bureau.
- Sous *Windows 7*, les effets de bureau peuvent être désactivés en sélectionnant l'un des thèmes répertoriés sous « Thèmes de base et à contraste élevé » dans la section « Personnalisation ».
- Sous *Windows 10*, il n'y a pas de moyen de désactiver complètement les effets de bureau.
- Sous *Ubuntu et autres distributions Linux utilisant Gnome 3*, il n'y a pas de moyen de désactiver complètement les effets de bureau.
- Sous *les distributions Linux utilisant KDE*, vous pouvez désactiver les effets de bureau dans la section « Effets de bureau » des Paramètres du système.
- Sous *Mac OS*, il n'y a apparemment pas de moyen de désactiver complètement les effets de bureau.

### Prendre en compte le temps de préparation des stimuli / la structure préparer-exécuter

Si vous vous souciez du temps de réponse précis lors de la présentation de stimuli visuels, vous devez préparer vos stimuli à l'avance. De cette façon, vous n'aurez pas de retards imprévisibles dus à la préparation des stimuli pendant les parties critiques de votre expérience.

Prenons d'abord en considération un script (que vous pouvez coller dans un élément INLINE_SCRIPT) qui inclut le temps de préparation des stimuli dans l'intervalle entre `canvas1` et `canvas2` (%LstStimPrepBad). L'intervalle spécifié est de 95 ms, donc - en tenant compte de la règle d'« arrondir à la hausse » décrite dans [Respecter la date limite de rafraîchissement] - vous vous attendriez à un intervalle de 100 ms sur mon moniteur 60 Hz. Cependant, sur mon système de test, le script ci-dessous donne un intervalle de 150 ms, ce qui correspond à 9 images sur un moniteur 60 Hz. Il s'agit d'un retard inattendu de 50 ms, soit 3 images, dû à la préparation de `canvas2`.

%--
code :
 id : LstStimPrepBad
 syntaxe : python
 source : stimulus-preparation-bad.py
 légende : « Dans ce script, la durée entre `canvas1` et `canvas2` est confondue avec le temps de préparation des stimuli. »
--%

Prenons maintenant en considération une simple variation du script ci-dessus (%LstStimPrepGood). Cette fois, nous préparons d'abord les deux `canvas1` et `canvas2`, puis nous les présentons ensuite. Sur mon système de test, cela donne un intervalle constant de 100 ms, comme il se doit!

%--
code :
 id : LstStimPrepGood
 syntaxe : python
 source : stimulus-preparation-good.py
 légende : « Dans ce script, la durée entre `canvas1` et `canvas2` n'est pas confondue avec le temps de préparation des stimuli.»
--%

Lors de l'utilisation de l'interface graphique, les mêmes considérations s'appliquent, mais OpenSesame vous aide en gérant automatiquement la plupart de la préparation des stimuli à l'avance. Cependant, vous devez tenir compte du fait que cette préparation se fait au niveau des éléments SEQUENCE et non pas au niveau des éléments LOOP. En pratique, cela signifie que le temps *à l'intérieur* d'une SEQUENCE n'est pas confondu avec le temps de préparation des stimuli. Mais le temps *entre* les SEQUENCEs l'est.

Pour rendre cela plus concret, prenons en considération la structure présentée ci-dessous (%FigStimPrepBad). Supposons que la durée de l'élément SKETCHPAD soit réglée sur 95 ms, visant ainsi une durée de 100 ms, soit 6 images sur un moniteur 60 Hz. Sur mon système de test, la durée réelle est de 133 ms, soit 8 images, car le temps est confondu par la préparation de l'élément SKETCHPAD, qui a lieu chaque fois que la séquence est exécutée. C'est donc un exemple de la manière dont vous NE devez PAS mettre en œuvre les parties critiques de votre expérience en termes de temps.

%--
figure:
 id: FigStimPrepBad
 source: stimulus-preparation-incorrect.png
 caption: "Un exemple de structure expérimentale dans laquelle le temps entre les présentations successives de SKETCHPAD est confondu par le temps de préparation des stimuli. La séquence d'événements dans ce cas est la suivante : préparer SKETCHPAD (2 images), afficher SKETCHPAD (6 images), préparer SKETCHPAD (2 images), afficher SKETCHPAD (6 images), etc."
--%

Maintenant, considérons la structure montrée ci-dessous (%FigStimPrepGood). Supposons que la durée de `sketchpad1` soit réglée à 95 ms, visant ainsi un intervalle de 100 ms entre `sketchpad1` et `sketchpad2`. Dans ce cas, les deux éléments sont affichés dans la même SEQUENCE et le temps ne sera pas confondu par le temps de préparation des stimuli. Sur mon système de test, l'intervalle réel entre `sketchpad1` et `sketchpad2` est donc bien de 100 ms, soit 6 images sur un écran de 60 Hz.

Notez que cela ne s'applique qu'à l'intervalle entre `sketchpad1` et `sketchpad2`, car ils sont exécutés dans cet ordre dans la même séquence. L'intervalle entre `sketchpad2` lors de la répétition *i* et `sketchpad1` lors de la répétition *i+1* est à nouveau confondu par le temps de préparation des stimuli.

%--
figure:
 id: FigStimPrepGood
 source: stimulus-preparation-correct.png
 caption: "Un exemple de structure expérimentale dans laquelle le temps entre les présentations de `sketchpad1` et `sketchpad2` n'est pas confondu par le temps de préparation des stimuli. La séquence d'événements dans ce cas est la suivante: préparer `sketchpad1` (2 images), préparer `sketchpad2` (2 images), afficher `sketchpad1` (6 images), afficher `sketchpad2` (6 images), préparer `sketchpad1` (2 images), préparer `sketchpad2` (2 images), afficher `sketchpad1` (6 images), afficher `sketchpad2` (6 images), etc."
--%

Pour plus d'informations, voir :

- [usage/prepare-run]

### Différences entre les backends

OpenSesame n'est pas lié à une manière spécifique de contrôler l'affichage, le minuteur système, etc. Par conséquent, OpenSesame *per se* n'a pas de propriétés de minutage spécifiques, car celles-ci dépendent du backend utilisé. Les caractéristiques de performance des différents backends ne sont pas parfaitement corrélées : il est possible que sur un système, le backend [psycho] fonctionne mieux, tandis que sur un autre système, le backend [xpyriment] fonctionne mieux. L'un des grands avantages d'OpenSesame est donc que vous pouvez choisir le backend qui vous convient le mieux !

En général, les backends [xpyriment] et [psycho] sont préférables pour les expériences critiques en termes de temps, car ils utilisent un flip bloquant. D'un autre côté, le backend [legacy] est légèrement plus stable et également considérablement plus rapide lors de l'utilisation de [forms].

Dans des conditions normales, les trois backends actuels d'OpenSesame ont les propriétés présentées dans %TblBackendInfo.

%--
table:
 id: TblBackendInfo
 source: backend-info.csv
 caption: Propriétés des backends.
--%

Voir également :

- [backends]

## Résultats des tests et conseils pour tester votre propre système

### Vérifier si le v-sync est activé

Comme décrit dans [Understanding your monitor], la présentation d'un nouvel affichage devrait idéalement coïncider avec le début d'un nouveau cycle de rafraîchissement (c'est-à-dire le 'v-sync'). Vous pouvez vérifier si c'est le cas en présentant des affichages de différentes couleurs en alternance rapide. Si le v-sync n'est pas activé, vous observerez clairement des lignes horizontales qui traversent l'écran (c'est-à-dire des 'déchirures'). Pour effectuer ce test, exécutez une expérience avec le script suivant dans un élément INLINE_SCRIPT (%LstVSync) :

%--
code:
 id: LstVSync
 syntax: python
 source: v-sync-check.py
 caption: Un script qui présente des affichages jaunes et bleus en alternance rapide. Un manque de synchronisation avec le rafraîchissement vertical peut être observé sous forme de lignes horizontales traversant l'écran.
--%

### Tester la précision et l'exactitude du temps

La synchronisation est précise ou cohérente lorsque vous pouvez présenter des stimuli visuels encore et encore avec la même synchronisation. Les horodatages sont exacts lorsqu'ils reflètent avec précision l'apparition des stimuli visuels sur le moniteur. Le script ci-dessous montre comment vous pouvez vérifier la précision et l'exactitude de la synchronisation. Ce test peut être effectué avec ou sans photodiode externe, bien que l'utilisation d'une photodiode fournisse une vérification supplémentaire.

Pour simplifier, supposons que votre moniteur fonctionne à 100 Hz, ce qui signifie qu'une seule image dure 10 ms. Le script présente ensuite un canevas blanc pendant 1 image (10 ms). Ensuite, le script présente un canevas noir pendant 9 images (90 ms). Notez que nous avons spécifié une durée de 85, qui est arrondie comme expliqué sous [Respecter la date limite de rafraîchissement]. Par conséquent, nous nous attendons à ce que l'intervalle entre les débuts de deux affichages blancs consécutifs soit de 10 images ou 100 ms (= 10 ms + 90 ms).

Nous pouvons utiliser deux méthodes pour vérifier si l'intervalle entre deux affichages blancs est bien de 100 ms :

1. En utilisant les horodatages rapportés par OpenSesame. C'est la méthode la plus simple et généralement précise lorsque le backend utilise un flip bloquant.
2. En utilisant une photodiode qui réagit aux débuts des affichages blancs et enregistre les horodatages de ces débuts sur un ordinateur externe. C'est la meilleure façon de vérifier le timing, car elle ne repose pas sur l'introspection du logiciel. Certains problèmes, tels que le décalage d'entrée TFT, discuté ci-dessus, ne sortiront qu'en utilisant une mesure de photodiode externe.

%--
code :
 id: LstIntervalBenchmark
 syntax: python
 source: interval-benchmark.py
 légende: Un script Python pour tester la cohérence et l'exactitude des horodatages d'affichage. Vous pouvez coller ce code dans un élément INLINE_SCRIPT.
--%

J'ai exécuté %LstIntervalBenchmark sur Windows XP, en utilisant les trois backends. J'ai également enregistré les débuts des affichages blancs en utilisant une photodiode connectée à un deuxième ordinateur. Les résultats sont résumés dans %TblBenchmarkResults.

%--
table :
 id: TblBenchmarkResults
 source: benchmark-results.csv
 légende: Résultats de référence pour %LstIntervalBenchmark. Testé avec Windows XP, HP Compaq dc7900, Intel Core 2 Quad Q9400 @ 2.66Ghz, 3GB, 21" ViewSonic P227f CRT. Chaque test a été effectué deux fois (c'est-à-dire deux sessions). La colonne `Session` correspond à différentes séquences de test. La colonne `Source` indique si les mesures proviennent d'une photiodiode externe ou des horodatages internes d'OpenSesame.
--%

Comme vous pouvez le voir, les backends [xpyriment] et [psycho] montrent constamment un intervalle de 100 ms. C'est bien, et c'est juste comme nous le prévoyions. Cependant, le backend [legacy] montre un intervalle de 90 ms. Cette différence est due au fait que le backend [legacy] n'utilise pas de flip bloquant (voir [Comprendre votre moniteur]), ce qui entraîne une certaine imprévisibilité dans la synchronisation de l'affichage. Notez également qu'il y a un accord étroit entre les horodatages enregistrés par la photodiode externe et les horodatages rapportés par OpenSesame. Cet accord démontre que les horodatages d'OpenSesame sont fiables, bien que, encore une fois, ils le soient légèrement moins pour le backend [legacy] en raison de l'absence de flip bloquant.

## Benchmarks et suite de tests Expyriment

Un ensemble très intéressant de benchmarks est disponible sur le site web d'Expyriment. Ces informations sont applicables aux expériences OpenSesame utilisant le backend [xpyriment].

- <http://docs.expyriment.org/Timing.html>

Expyriment inclut une suite de tests très utile. Vous pouvez lancer cette suite de tests en exécutant l'expérience exemple `test_suite.opensesame` ou en ajoutant un INLINE_SCRIPT simple à votre expérience avec les lignes de code suivantes (%LstExpyrimentTestSuite) :

%--
code :
 id: LstExpyrimentTestSuite
 syntax: python
 source: expyriment-test-suite.py
 légende: Un script pour démarrer la suite de tests Expyriment.
--%

Pour plus d'informations, veuillez visiter :

- <http://docs.expyriment.org/Testsuite.html>

## Benchmarks PsychoPy et informations relatives au timing

Certaines informations sur la synchronisation sont disponibles sur le site de documentation PsychoPy. Ces informations sont applicables aux expériences OpenSesame utilisant le backend [psycho].

- <http://www.psychopy.org/general/timing/timing.html>

[psycho]: /backends/xpyriment/
[xpyriment]: /backends/xpyriment/
[legacy]: /backends/legacy/
[miscellaneous/clock-drift]: /miscellaneous/clock-drift
[usage/prepare-run]: /usage/prepare-run
[backends]: /backends
[forms]: /forms