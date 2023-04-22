title: OSWeb
hash: 9fc0b6a63aa91000243df7d41fe843fc7eb52f30b3e6ac866728b5e0e8ebde0a
locale: fr
language: French

[TOC]


## À propos d'OSWeb

OSWeb est un environnement d'exécution en ligne pour les expériences OpenSesame. C'est-à-dire, une bibliothèque JavaScript qui interprète et exécute les expériences OpenSesame.


## L'extension OSWeb

L'extension OSWeb pour OpenSesame (%FigOSWebExtension) vous permet de tester les expériences dans un navigateur et d'exporter les expériences dans un format que vous pouvez importer dans [JATOS](%url:jatos%).


%--
figure:
 id: FigOSWebExtension
 source: osweb-extension.png
 caption: L'extension OSWeb pour OpenSesame.
--%


## Tests dans un navigateur

- Dans OpenSesame, ouvrez l'extension OSWeb (Menu → Outils → OSWeb).
- L'extension effectuera une vérification simple (et incomplète) pour voir si votre expérience semble être compatible avec OSWeb.
- Si aucun problème n'est détecté, cliquez sur 'Tester l'expérience dans un navigateur externe' ou cliquez sur le bouton correspondant dans la barre d'outils principale.
- Cela ouvrira l'expérience dans votre navigateur par défaut afin que vous puissiez vérifier si l'expérience fonctionne comme prévu (%FigTestRun).
- Vous pouvez également cliquer sur le bouton 'Exécuter dans un navigateur' dans la barre d'outils principale (Alt+Ctrl+W)

%--
figure:
 id: FigTestRun
 source: testrun.png
 caption: L'écran de bienvenue d'OSWeb lors du test de l'expérience dans un navigateur.
--%


## Débogage

Tout d'abord, assurez-vous que votre expérience n'utilise que les fonctionnalités prises en charge, comme décrit ci-dessous. Ensuite, exécutez l'expérience de manière traditionnelle (hors navigateur) dans OpenSesame. Cela vous donnera les messages d'erreur les plus informatifs que vous pouvez utiliser pour le débogage.

Si votre expérience n'utilise que des fonctionnalités prises en charge et fonctionne normalement dans OpenSesame, vous pouvez utiliser la console du navigateur pour voir les messages d'erreur JavaScript. Ces messages sont beaucoup moins informatifs que les messages d'erreur d'OpenSesame, mais ils peuvent toujours être utiles. Chaque navigateur a une manière différente d'accéder à la console. Dans Chrome, vous pouvez accéder à la console en faisant un clic droit quelque part, en sélectionnant Inspecter (`Ctrl+Shift+I`) puis en passant à l'onglet Console (voir % FigChromeConsole). Dans Firefox, vous pouvez accéder à la console en cliquant sur l'icône du menu en haut à droite, puis en sélectionnant Développeur Web → Console Web (`Ctrl+Shift+I`).

Si vous utilisez des éléments INLINE_JAVASCRIPT dans votre expérience, la console du navigateur est également un moyen puissant de déboguer vos scripts, comme décrit ici :

- %link:manual/javascript/about%

%--
figure:
 id: FigChromeConsole
 source: chrome-console.png
 caption: La console du navigateur Chrome.
--%



## Fonctionnalités prises en charge

Vous pouvez vérifier si votre expérience est compatible avec OSWeb en utilisant la vérification de compatibilité (%FigOSWebExtension). Cette vérification de compatibilité est assez superficielle. Un aperçu plus complet des fonctionnalités prises en charge se trouve ci-dessous.

__Important__: Beaucoup de fonctionnalités prises en charge ont été ajoutées dans OSWeb 1.4. Par conséquent, vérifiez votre version d'OSWeb par rapport aux notes de version dans la liste ci-dessous.

- `advanced_delay`
- `feedback`
    - Voir `sketchpad`
- `form_consent` (supported >= v1.4)
- `form_text_display` (supported >= 1.4)
- `form_text_input` (supported >= 1.4)
    - Non pris en charge : mode plein écran
- `form_multiple_choice` (supported >= 1.4)
- `inline_html` (supported >= 1.4)
- `inline_javascript`
- `keyboard`
    - Non pris en charge : relâchement des touches
    - Non pris en charge : espaces colorimétriques HSV, HSL et CIELab
- `logger`
- `loop`
    - Non pris en charge : reprise après une pause
    - Non pris en charge : désactivation de l'évaluation lors du premier cycle
    - Non pris en charge : contraintes (pseudo-randomisation)
    - Pris en charge >= 1.4 : source de fichier
- `mouse`
    - Non pris en charge : relâchement de la souris
    - Non pris en charge : sketchpad lié
- `notepad`
- `repeat_cycle`
- `reset_feedback`
- `sampler`
    - Pris en charge >= 1.4.12 : panoramique, hauteur et fondu
    - Pris en charge >= 1.4.12 : lecture du son sur Safari sur Mac OS ou sur n'importe quel navigateur sur iOS
    - Non pris en charge : arrêter après
- `sequence`
- `sketchpad`
    - Non pris en charge : éléments nommés
    - Pris en charge >= 1.4 : rotation de l'image
    - Non pris en charge : espaces colorimétriques HSV, HSL et CIELab
- `touch_response`

La vérification de compatibilité peut également indiquer des erreurs du type suivant :

```bash
La phase de préparation pour l'élément new_logger est appelée plusieurs fois de suite
La phase d'exécution pour l'élément new_logger est appelée plusieurs fois de suite
```

Cette erreur provient de la structure de l'expérience, et plus précisément de l'utilisation de copies liées. Il n'est pas toujours facile de comprendre d'où vient cette erreur, mais vous pouvez en savoir plus sur la stratégie de préparation-exécution dans [cet article](%url:prepare-run%). En guise de solution temporaire, vous pouvez mettre les éléments problématiques dans une boucle factice, c'est-à-dire une boucle qui appelle simplement l'élément une fois.

## Navigateurs pris en charge

Les combinaisons de navigateurs et de systèmes d'exploitation suivantes ont été testées avec la dernière version d'OSWeb. Les versions antérieures des navigateurs, des systèmes d'exploitation et des versions d'OSWeb peuvent fonctionner, mais n'ont pas été testées récemment. Certaines extensions, telles que les bloqueurs de publicités ou les bloqueurs de scripts, peuvent empêcher OSWeb de fonctionner.

### Complètement pris en charge

- Chrome >= 101 (Windows 11, Mac OS Monterey, Ubuntu 22.04, Android 12.0)
- Edge >= 101 (Windows 11, Mac OS Monterey)
- Firefox >= 99 (Windows 11, Mac OS Monterey, Ubuntu 22.04, Android 12.0)
- Opera >= 86 (Windows 11)
- Chromium >= 101 (iOS 15.2)
- Firefox >= 99 (iOS 15.2)
- Opera >= 86 (Mac OS Monterey)
- Safari >= 15 (iOS 15.2, Mac OS Monterey)

### Non pris en charge

- Internet Explorer >= 11 (Windows 10)

## Mise à jour d'OSWeb

OSWeb est en développement actif. Si vous souhaitez vous assurer que vous utilisez la dernière version, vous pouvez mettre à jour l'extension OSWeb, appelée `opensesame-extension-osweb`. À partir d'OpenSesame 3.3, vous pouvez le faire en exécutant la commande suivante dans la console :

```bash
conda update opensesame-extension-osweb -c cogsci -c conda-forge -y
```

Ou :

```bash
pip install opensesame-extension-osweb --upgrade
```

Voir aussi :

- <https://rapunzel.cogsci.nl/manual/environment/>

## Inclure des bibliothèques JavaScript externes

Nouveau dans OSWeb v1.4.6.1
{:.page-notification}

Vous pouvez inclure des bibliothèques JavaScript externes en saisissant les URL de ces bibliothèques (une URL par ligne) dans le champ de saisie intitulé 'Bibliothèques JavaScript externes'. Ces bibliothèques sont ensuite incluses avec des balises `<script>` dans l'en-tête du HTML.

Par exemple, vous pouvez inclure [WebGazer](%url:webgazer%) pour un navigateur en entrant le lien suivant :

```
https://webgazer.cs.brown.edu/webgazer.js
```