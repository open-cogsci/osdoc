title: Texte
hash: 1958b3f404645f67ec8c328c22b9b876e1507c616fa82878164f23ac0d364e92
locale: fr
language: French

[TOC]

## Comment présenter du texte ?

La manière la plus courante de montrer du texte est d'utiliser un élément SKETCHPAD ou FEEDBACK. Ceux-ci vous permettent d'entrer du texte et d'autres stimuli visuels. Pour une manière de type questionnaire de montrer du texte, vous pouvez utiliser [formulaires](%link:manual/forms/about%).


## Formatage HTML

Vous pouvez utiliser des balises HTML, que vous pouvez simplement insérer dans votre texte. Vous pouvez utiliser ces balises partout : dans les éléments SKETCHPAD, INLINE_SCRIPT (à condition d'utiliser la classe "Canvas"), dans les formulaires, etc.

Exemple :

~~~ .html
OpenSesame prend en charge un sous-ensemble de balises HTML :
- <b>Gras</b>
- <i>Italique</i>
- <u>Souligné</u>

De plus, vous pouvez passer "color", "size" et "style" comme mots-clés à une balise "span" :
- <span style='color:red;'>Couleur</span>
- <span style='font-size:32px;'>Taille de la police</span>
- <span style='font-family:serif;'>Style de police</span>

Enfin, vous pouvez forcer les sauts de ligne avec la balise "br" :
Ligne 1<br>Ligne 2
~~~


## Variables et Python en ligne

Vous pouvez intégrer des variables dans du texte en utilisant la syntaxe `{...}`. Par exemple, ce qui suit :

~~~ .python
Le numéro du sujet est {subject_nr}
~~~

... pourrait s'évaluer à (pour le sujet 1) :

~~~ .python
Le numéro du sujet est 1
~~~

Vous pouvez également intégrer des expressions Python. Par exemple, ce qui suit :

~~~ .python
Le numéro du sujet modulo cinq est {subject_nr % 5}
~~~

... pourrait s'évaluer à (pour le sujet 7) :

~~~ .python
Le numéro du sujet modulo cinq est 2
~~~


## Polices de caractères

### Polices par défaut

Vous pouvez sélectionner l'une des polices par défaut dans les boîtes de dialogue de sélection de police (%FigFontSelect). Ces polices sont incluses dans OpenSesame et votre expérience sera donc entièrement portable lorsque vous les utiliserez.

%--
figure:
 id: FigFontSelect
 source: font-selection-dialog.png
 caption: "Un certain nombre de polices par défaut, qui sont livrées avec OpenSesame, peuvent être sélectionnées via les boîtes de dialogue de sélection de police."
--%

Les polices ont été renommées pour plus de clarté, mais correspondent aux polices open-source suivantes :

|__Nom dans OpenSesame__		|__Police réelle__		|
|---------------------------|-----------------------|
|`sans`						|Droid Sans				|
|`serif`					|Droid Serif			|
|`mono`						|Droid Sans Mono		|
|`chinese-japanese-korean`	|WenQuanYi Micro Hei	|
|`arabic`					|Droid Arabic Naskh		|
|`hebrew`					|Droid Sans Hebrew		|
|`hindi`					|Lohit Hindi			|

### Sélectionner une police personnalisée grâce à la boîte de dialogue de sélection de police

Si vous sélectionnez "autre ..." dans la boîte de dialogue de sélection de police, vous pouvez sélectionner n'importe quelle police disponible sur votre système d'exploitation. Si vous faites cela, votre expérience n'est plus entièrement portable et nécessitera que la police sélectionnée soit installée sur le système sur lequel vous exécutez votre expérience.

### Placer une police personnalisée dans la file d'attente des fichiers

Une autre façon d'utiliser une police personnalisée consiste à mettre un fichier de police dans le pool de fichiers. Par exemple, si vous placez le fichier de police `inconsolata.ttf` dans le pool de fichiers, vous pouvez utiliser cette police dans un élément SKETCHPAD, comme ceci :

	draw textline 0.0 0.0 "Ce sera inconsolata" font_family="inconsolata"

Notez que le fichier de police doit être un fichier de type `.ttf`.