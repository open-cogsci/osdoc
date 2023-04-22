title: Moteurs
hash: 1447d1754e76a00442c1709babb3c8b9ef77f76eb2aeb0c1e6bb57c9a232512c
locale: fr
language: French

Le *backend* est la couche logicielle qui traite les entrées (entrée clavier, entrée souris, etc.) et les sorties (présentation de l'affichage, lecture du son, etc.). Il existe de nombreuses bibliothèques offrant ce type de fonctionnalité et OpenSesame pourrait, en principe, utiliser n'importe laquelle d'entre elles. Pour cette raison, OpenSesame est indépendant du backend, en ce sens que vous pouvez choisir quel backend doit être utilisé. Actuellement, il existe quatre backends : *legacy*, *psycho*, *xpyriment* et *osweb*.

[TOC]

## Différences et quelques conseils

Habituellement, vous ne remarquerez pas quel backend est utilisé. Les différences entre les backends sont en grande partie techniques et, tant que vous utilisez l'interface utilisateur graphique, tous les backends fonctionnent plus ou moins de la même manière. Cependant, il y a quelques raisons de préférer un backend à un autre :

- Si vous souhaitez exécuter l'expérience dans un navigateur, vous devez sélectionner le backend *osweb*.
- Les backends diffèrent en [précision temporelle](%link:timing%).
	- Conseil : Si vous vous souciez de la précision temporelle en millisecondes, utilisez *xpyriment* ou *psycho*.
- Les backends diffèrent dans la durée de préparation des stimuli.
	- Conseil : Si les [formulaires](%link:manual/forms/about%) sont lents, utilisez *legacy*.
	- Conseil : Si l'intervalle inter-essais est long (en raison de la préparation des stimuli), utilisez *legacy*.
- Vous pouvez utiliser des fonctionnalités spécifiques au backend en écrivant du code Python.
	- Conseil : Si vous souhaitez utiliser les fonctionnalités de PsychoPy, utilisez *psycho*.
	- Conseil : Si vous souhaitez utiliser les fonctionnalités d'Expyriment, utilisez *xpyriment*.
	- Conseil : Si vous souhaitez utiliser les fonctionnalités de PyGame, utilisez *legacy*.
- Certains backends ne sont pas disponibles sur toutes les plateformes.

## Sélection d'un backend

Vous pouvez sélectionner un backend dans les propriétés générales de l'expérience (%FigSelect).

%--
figure:
 id: FigSelect
 source: fig-select.png
 caption: "Sélection d'un backend"
--%

Si vous affichez le script général (sélectionnez "Afficher l'éditeur de script"), vous verrez qu'il y a en réalité six backends distincts : canvas, keyboard, mouse, sampler, color et clock. La méthode combobox sélectionne automatiquement une combinaison appropriée et prédéfinie de backends, mais vous pourriez, en théorie, les mélanger et les assortir.

Par exemple, si vous sélectionnez le backend *xpyriment*, le code suivant sera généré :

	set sampler_backend legacy
	set mouse_backend xpyriment
	set keyboard_backend legacy
	set color_backend legacy
	set clock_backend legacy
	set canvas_backend xpyriment

## xpyriment

Le backend *xpyriment* est basé sur [Expyriment][], une bibliothèque conçue pour créer des expériences de psychologie. C'est un backend léger et accéléré par le matériel avec d'excellentes propriétés de synchronisation. Si vous vous souciez de la précision temporelle, mais ne prévoyez pas de générer des stimuli complexes (c'est-à-dire des patchs Gabor, des grilles de points aléatoires, etc.), *xpyriment* est un bon choix.

### Utilisation d'Expyriment directement

Vous pouvez trouver une documentation détaillée sur Expyriment à l'adresse <http://www.expyriment.org/doc>. L'extrait de code suivant montre une ligne de texte :

~~~ .python
from expyriment import stimuli
text = stimuli.TextLine('Ceci est expyriment !')
text.present()
~~~

### Citation

Bien qu'Expyriment soit inclus avec les distributions binaires d'OpenSesame, il s'agit d'un projet distinct. Lorsque cela est approprié, veuillez fournir la citation suivante en plus de citer OpenSesame :

Krause, F., & Lindemann, O. (sous presse). Expyriment: A Python library for cognitive and neuroscientific experiments. *Behavior Research Methods*.
{: .reference}

## psycho

Le backend psycho est construit sur [PsychoPy][], une bibliothèque conçue pour créer des expériences de psychologie. Il est accéléré par le matériel et fournit des routines de haut niveau pour créer des stimuli visuels complexes (gratings en mouvement, etc.). Si vous vous souciez de la synchronisation et prévoyez de créer des stimuli complexes, Psycho est un bon choix.

### Utilisation de PsychoPy directement

Vous pouvez trouver une documentation complète sur PsychoPy à l'adresse <http://www.psychopy.org/>. Lors de l'utilisation de PsychoPy dans OpenSesame, il est important de savoir que la fenêtre principale peut être accessible via `self.experiment.window` ou simplement `win`. Ainsi, le fragment de code suivant dessine un patch de Gabor :

~~~ .python
from psychopy import visual
gabor = visual.PatchStim(win, tex="sin", size=256, mask="gauss", sf=0.05, ori=45)
gabor.draw()
win.flip()
~~~

### Tutoriels

Un tutoriel spécifique pour l'utilisation de PsychoPy depuis OpenSesame :

- <http://www.cogsci.nl/blog/tutorials/211-a-bit-about-patches-textures-and-masks-in-psychopy>

Et un tutoriel PsychoPy plus général :

- <http://gestaltrevision.be/wiki/coding>

### Citation

Bien que PsychoPy soit intégré aux distributions binaires d'OpenSesame, il s'agit d'un projet distinct. Le cas échéant, veuillez citer les articles suivants en plus de citer OpenSesame :

Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017
{: .reference}

Peirce, J. W. (2009). Generating stimuli for neuroscience using PsychoPy. *Frontiers in Neuroinformatics*, *2*(10). doi:10.3389/neuro.11.010.2008
{: .reference}

## legacy

Le backend legacy est construit sur [PyGame][] en mode non-OpenGL. L'inconvénient est qu'il n'y a pas d'accélération matérielle et que les propriétés de synchronisation ne sont pas aussi bonnes que celles des backend psycho ou xpyriment. L'avantage est que PyGame est très facile à utiliser, très fiable et bien pris en charge sur un large éventail de plateformes.

### Visibilité du curseur de souris

Sur certains systèmes, le curseur de la souris n'est pas visible lors de l'utilisation du backend *legacy* en mode plein écran. Vous pouvez contourner ce problème de plusieurs manières :

1. Ouvrez les paramètres du backend *legacy* et réglez "Double buffering" sur "non".
    - *Remarque :* Cela peut désactiver la synchronisation verticale, qui peut être importante pour les expériences critiques en termes de temps, comme discuté [ici](%link:timing%).
2. Ouvrez les paramètres du backend *legacy* et réglez "Custom cursor" sur "oui".
3. Passez à un autre backend.

### Utilisation de PyGame directement

PyGame est bien documenté et vous pouvez trouver tout ce que vous devez savoir sur l'utilisation de PyGame sur <http://www.pygame.org/docs/>. Particulier à OpenSesame, le fait que la surface d'affichage est stockée en tant que `self.experiment.window` ou simplement `win`. Ainsi, le fragment de code suivant, que vous pourriez coller dans un élément INLINE_SCRIPT, dessine un rectangle rouge sur l'affichage :

~~~ .python
import pygame # Import du module PyGame
pygame.draw.rect(self.experiment.window, pygame.Color("red"),
	[20, 20, 100, 100]) # Dessine un rectangle rouge. Pas encore affiché...
pygame.display.flip() # Met à jour l'affichage pour montrer le rectangle rouge.
~~~

## osweb

Le backend *osweb* est construit sur OSWeb et permet d'exécuter des expériences dans un navigateur. Pour plus d'informations, consultez :

- %link:manual/osweb/workflow%