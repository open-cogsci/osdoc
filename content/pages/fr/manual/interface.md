title: En utilisant l'interface
hash: 76f98fb7d0797037375f61ab159fef066c3fe407e469e0f97494e76d38e6177e
locale: fr
language: French

OpenSesame possède une interface graphique puissante composée de plusieurs composants (%FigInterface).

%--
figure:
 id: FigInterface
 source: interface.png
 caption: L'interface utilisateur d'OpenSesame.
--%


[TOC]

## Barre d'outils et barre de menu

### La barre de menu

La barre de menu (%FigMenubar) est affichée en haut de la fenêtre ou, sur certains systèmes d'exploitation, est intégrée à la bordure autour de la fenêtre. La barre de menu contient des fonctionnalités générales, telles que l'enregistrement et l'ouverture d'expériences, l'exécution d'expériences, etc.

%--
figure:
 id: FigMenubar
 source: menubar.png
 caption: La barre de menu.
--%

### La barre d'outils principale

La barre d'outils principale (%FigMainToolbar) est (par défaut) affichée en haut de la fenêtre, juste en dessous de la barre de menu. La barre d'outils principale contient une sélection des fonctionnalités les plus pertinentes de la barre de menu.

%--
figure:
 id: FigMainToolbar
 source: main-toolbar.png
 caption: La barre d'outils principale.
--%

### La barre d'outils des éléments

La barre d'outils des éléments (%FigItemToolbar) est (par défaut) affichée à gauche de la fenêtre. La barre d'outils des éléments contient tous les éléments, c'est-à-dire tous les blocs de construction d'une expérience. Vous pouvez ajouter des éléments à votre expérience en les faisant glisser depuis la barre d'outils des éléments dans la zone de présentation générale.

%--
figure:
 id: FigItemToolbar
 source: item-toolbar.png
 caption: La barre d'outils des éléments.
--%

## La zone des onglets

La zone des onglets est la partie centrale de la fenêtre (%FigTabArea). La zone des onglets affiche les contrôles des éléments, la documentation, les messages importants, etc. La zone des onglets peut contenir plusieurs onglets et fonctionne de manière similaire à un navigateur Web à onglets.

%--
figure:
 id: FigTabArea
 source: tab-area.png
 caption: La zone des onglets.
--%

## La zone de présentation générale

La zone de présentation générale (%FigOverviewArea) est (par défaut) affichée à gauche de la fenêtre, à droite de la barre d'outils des éléments. La zone de présentation générale montre la structure de votre expérience sous forme d'arbre. Vous pouvez réorganiser les éléments de votre expérience en les faisant glisser d'une position à une autre dans la zone de présentation générale.

- Raccourci pour masquer/afficher : `Ctrl+\`

%--
figure:
 id: FigOverviewArea
 source: overview-area.png
 caption: La zone de présentation générale.
--%

## La réserve de fichiers

La réserve de fichiers (%FigFilePool) est (par défaut) affichée à droite de la fenêtre. Elle offre un aperçu de tous les fichiers associés à l'expérience.

- Raccourci pour masquer/afficher : `Ctrl+P`

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: La réserve de fichiers.
--%

## La fenêtre de débogage

La fenêtre de débogage (%FigDebugWindow) est (par défaut) affichée en bas de la fenêtre. Elle fournit un [interpréteur IPython](https://ipython.org/) et est utilisée comme sortie standard lorsqu'une expérience est en cours d'exécution. Autrement dit, si vous utilisez la fonction Python `print()`, le résultat sera affiché dans la fenêtre de débogage.

- Raccourci pour masquer/afficher : `Ctrl+D`

%--
figure:
 id: FigDebugWindow
 source: debug-window.png
 caption: La fenêtre de débogage.
--%

## L'inspecteur de variables

L'inspecteur de variables (%FigVariableInspector) est (par défaut) affiché à droite de la fenêtre. Il fournit une liste de toutes les variables détectées dans votre expérience. Lorsque vous exécutez une expérience, l'inspecteur de variables offre également un aperçu en temps réel des variables et de leurs valeurs.

- Raccourci pour masquer/afficher : `Ctrl+I`

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: L'inspecteur de variables.
--%

## Raccourcis clavier

Les raccourcis clavier listés ci-dessous sont des valeurs par défaut. Beaucoup d'entre eux peuvent être modifiés via *Menu → Outils → Préférences*.

### Raccourcis généraux

Les raccourcis clavier suivants sont disponibles partout :

- Sélecteur rapide : `Ctrl+Espace`
- Palette de commandes : `Ctrl+Maj+P`
- Nouvelle expérience : `Ctrl+N`
- Ouvrir une expérience : `Ctrl+O`
- Sauvegarder une expérience : `Ctrl+S`
- Sauvegarder une expérience sous : `Ctrl+Maj+S`
- Annuler : `Ctrl+Alt+Z`
- Rétablir : `Ctrl+Alt+Maj+Z`
- Lancer l'expérience en plein écran : `Ctrl+R`
- Lancer l'expérience dans une fenêtre : `Ctrl+W`
- Lancer l'expérience rapidement : `Ctrl+Maj+W`
- Tester l'expérience dans un navigateur : `Alt+Ctrl+W`
- Afficher/ masquer la zone d'aperçu : `Ctrl+\`
- Afficher/ masquer la fenêtre de débogage : `Ctrl+D`
- Afficher/ masquer la liste de fichiers : `Ctrl+P`
- Afficher/ masquer l'inspecteur de variables : `Ctrl+I`
- Mettre l'accent sur la zone d'aperçu : `Ctrl+1`
- Mettre l'accent sur la zone des onglets : `Ctrl+2`
- Mettre l'accent sur la fenêtre de débogage : `Ctrl+3`
- Mettre l'accent sur la liste de fichiers : `Ctrl+4`
- Mettre l'accent sur l'inspecteur de variables : `Ctrl+5`

### Raccourcis de l'éditeur

Les raccourcis clavier suivants sont disponibles dans les composants de l'éditeur, tels que le INLINE_SCRIPT :

- (Dé)commenter la ou les lignes sélectionnées : `Ctrl+/`
- Rechercher du texte : `Ctrl+F`
- Remplacer du texte : `Ctrl+H`
- Masquer la boîte de dialogue rechercher/remplacer : `Échap`
- Dupliquer la ligne : `Ctrl+Maj+D`
- Annuler : `Ctrl+Z`
- Rétablir : `Ctrl+Maj+Z`
- Copier : `Ctrl+C`
- Couper : `Ctrl+X`
- Coller : `Ctrl+V`

### Raccourcis de la zone des onglets

Les raccourcis clavier suivants sont disponibles dans la zone des onglets :

- Onglet suivant : `Ctrl+Tab`
- Onglet précédent : `Ctrl+Maj+Tab`
- Fermer les autres onglets : `Ctrl+T`
- Fermer tous les onglets : `Ctrl+Alt+T`
- Fermer l'onglet actuel : `Alt+T`

### Raccourcis de la zone d'aperçu et des séquences

Les raccourcis clavier suivants sont disponibles dans la zone d'aperçu et l'élément SEQUENCE :

- Menu contextuel : `+`
- Copier l'élément (non lié) : `Ctrl+C`
- Copier l'élément (lié) : `Ctrl+Maj+C`
- Coller l'élément : `Ctrl+V`
- Supprimer l'élément : `Suppr`
- Supprimer définitivement l'élément : `Maj+Suppr`
- Renommer : `F2`
- Modifier la déclaration run-if (si applicable) : `F3`