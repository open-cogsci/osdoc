title: OSWeb
hash: d0eed8ce85e569f15d774ecf9cc4dff90b02dffd12470987bae00484d0c05865
locale: fr
language: French

[TOC]


## À propos d'OSWeb

OSWeb est un environnement d'exécution en ligne pour les expériences OpenSesame. C'est une bibliothèque JavaScript qui exécute les expériences OpenSesame dans un navigateur. Pour utiliser OSWeb, vous avez besoin du package `opensesame-extension-osweb`, qui est préinstallé avec les distributions Windows et macOS d'OpenSesame.


## Exécuter une expérience dans un navigateur Web

Pour exécuter une expérience dans un navigateur web à l'aide d'OSWeb, suivez ces étapes :

1. Ouvrez les propriétés de l'expérience et sélectionnez 'Dans un navigateur avec OSWeb (osweb)' dans la section 'Exécuter l'expérience'.
2. Cliquez sur n'importe quel bouton 'Exécuter' pour démarrer l'expérience.
3. Si l'expérience n'est pas compatible avec OSWeb, un message d'erreur apparaîtra détaillant les problèmes de compatibilité. (Consultez la section 'fonctionnalités prises en charge' pour plus de détails.)
4. S'il n'y a pas de problèmes de compatibilité, l'expérience s'ouvrira dans une nouvelle fenêtre de navigateur. Notez que même si l'expérience se déroule dans un navigateur web, elle est toujours exécutée localement sur votre propre ordinateur. Pour héberger l'expérience en ligne, vous devez la publier sur [JATOS](%url:jatos%). 
5. Lorsque l'expérience est terminée, les données sont téléchargées au format `.json`. Ce fichier de données peut ensuite être [converti au format `.xlsx` ou `.csv`](%url:manual/osweb/data%) pour une analyse ultérieure.


%--
figure:
 id: FigTestRun
 source: testrun.png
 caption: Ouvrir les propriétés de l'expérience et sélectionner 'Dans un navigateur avec OSWeb (osweb)' sous 'Exécuter l'expérience'.
--%

## Panneau de contrôle d'OSWeb

Pour avoir plus de contrôle sur les expériences OSWeb, vous pouvez accéder au panneau de contrôle d'OSWeb et de JATOS depuis le menu Outils. Ce panneau propose une série d'options de configuration :

- **Numéros de sujet possibles :** Lors de l'exécution d'une expérience depuis JATOS, un numéro de sujet est aléatoirement sélectionné dans cette liste. Vous pouvez spécifier des numéros individuels à l'aide de virgules (par exemple, '1,2,3') ou des plages de numéros (par exemple, '1-10'). Lors de l'exécution d'une expérience depuis OpenSesame, cette option ne s'applique pas, car le numéro de sujet est spécifié lorsque l'expérience commence.
- **Passer le navigateur en plein écran :** Cette option détermine si le navigateur doit passer en mode plein écran lorsqu'une expérience commence dans JATOS. Si vous exécutez une expérience directement depuis OpenSesame, cette option est ignorée ; à la place, vous pouvez exécuter l'expérience en plein écran en utilisant le bouton Exécuter normal, tandis que le bouton Exécution rapide n'active pas le plein écran.
- **Afficher l'écran d'accueil d'OSWeb :** Ce bascule contrôle si les participants verront un écran d'accueil avant que l'expérience commence. L'écran d'accueil peut transmettre des informations cruciales aux participants. De plus, il a une fonction technique – en raison des politiques de sécurité des navigateurs, la lecture des médias et certaines fonctionnalités ne sont disponibles que si l'expérience est initiée par une action de l'utilisateur. Par conséquent, il est généralement recommandé de laisser cette option activée.
- **Contourner le contrôle de compatibilité :** Activer cette option vous permet d'exécuter l'expérience même lorsque le contrôle de compatibilité d'OSWeb échoue. Notez que ceci ne résoudra pas automatiquement les problèmes de compatibilité !
- **Texte de bienvenue :** Ce champ vous permet de personnaliser le message de bienvenue affiché aux participants sur l'écran d'accueil.
- **Bibliothèques externes :** Ce champ vous permet de spécifier toute bibliothèque externe qui devrait être chargée avec votre expérience. L'utilisation de bibliothèques externes est expliquée plus en détail dans la section ci-dessous.

%--
figure:
 id: FigOSWebControlPanel
 source: osweb-control-panel.png
 caption: Le panneau de contrôle OSWeb et JATOS propose une série d'options de configuration pour vos expériences OSWeb.
--%

## Fonctionnalités prises en charge

Lorsque vous exécutez l'expérience depuis OpenSesame, une vérification de compatibilité est automatiquement effectuée. Cependant, cette vérification est assez superficielle. Un aperçu plus complet des fonctionnalités prises en charge peut être trouvé ci-dessous.

- `advanced_delay`
- `feedback`
    - Voir `sketchpad`
- `form_consent` (supporté >= v1.4)
- `form_text_display` (supporté >= 1.4)
- `form_text_input` (supporté >= 1.4)
    - Non pris en charge : mode plein écran
- `form_multiple_choice` (supporté >= 1.4)
- `inline_html` (supporté >= 1.4)
- `inline_javascript`
- `keyboard`
    - Non pris en charge : relâchement de la touche
    - Non pris en charge : espaces de couleurs HSV, HSL et CIELab
- `logger`
- `loop`
    - Non pris en charge : reprise après pause
    - Non pris en charge : Désactivation de l'évaluation lors du premier cycle
    - Non pris en charge : contraintes (pseudorandomisation)
    - Supporté >= 1.4: source de fichier
- `mouse`
    - Non pris en charge : relâchement de la souris
    - Non pris en charge : sketchpad lié
- `notepad`
- `repeat_cycle`
- `reset_feedback`
- `sampler`
    - Supporté >= 1.4.12 : balayage, hauteur et estompage
    - Supporté >= 1.4.12 : Lecture de son sur Safari sur Mac OS ou n'importe quel navigateur sur iOS
    - Non pris en charge : stop après
- `sequence`
- `sketchpad`
    - Non pris en charge : éléments nommés
    - Supporté >= 1.4 : rotation de l'image
    - Non pris en charge : espaces de couleurs HSV, HSL et CIELab
- `touch_response`


La vérification de compatibilité peut également indiquer des erreurs du type suivant :

> La phase de préparation pour l'élément new_logger est appelée plusieurs fois de suite

Cette erreur résulte de la façon dont l'expérience est structurée, et en particulier de l'utilisation de copies liées. Il n'est pas toujours facile de comprendre d'où vient cette erreur, mais vous pouvez en savoir plus sur la stratégie de préparation-exécution dans [cet article](%url:prepare-run%). Comme solution de contournement, vous pouvez placer les éléments problématiques dans une boucle factice, c'est-à-dire, une boucle qui appelle simplement l'élément une fois.


## Inclusion de packages JavaScript externes

Vous pouvez inclure des packages JavaScript externes en entrant les URL de ces packages (une URL par ligne) dans le champ d'entrée intitulé 'Bibliothèques JavaScript externes'. Ces packages sont ensuite inclus avec des balises `<script>` dans l'en-tête du HTML.

Par exemple, vous pouvez inclure [WebGazer](%url:webgazer%) pour le navigateur en entrant le lien suivant :

```
https://webgazer.cs.brown.edu/webgazer.js
```


## Débogage

Voir :

- %link:debugging%