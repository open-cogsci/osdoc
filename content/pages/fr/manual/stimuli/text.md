title: Texte
hash: 2c5f78c24fe19088d9f96d120232def3d4ca9bb4bc48409ae868d353c7ebc4ed
locale: fr
language: French

## Comment présenter du texte ?

La façon la plus courante de présenter du texte est d’utiliser un élément SKETCHPAD ou FEEDBACK. Cela vous permet de saisir du texte et d'autres stimuli visuels. Pour une manière similaire à un questionnaire de présenter du texte, vous pouvez utiliser des [formulaires](%link:manual/forms/about%).

## Mise en forme HTML

Vous pouvez utiliser des balises HTML, que vous pouvez simplement insérer dans votre texte. Vous pouvez utiliser ces balises partout : dans les éléments SKETCHPAD, dans les INLINE_SCRIPTs (à condition d'utiliser la classe `Canvas`), dans les formulaires, etc.

Exemple :

~~~ .html
OpenSesame prend en charge un sous-ensemble de balises HTML :
- <b>Gras</b>
- <i>Italique</i>
- <u>Souligné</u>

De plus, vous pouvez passer 'color', 'size' et 'style' en tant que mots-clés à une balise 'span' :
- <span style='color:red;'>Couleur</span>
- <span style='font-size:32px;'>Taille de police</span>
- <span style='font-family:serif;'>Style de police</span>

Enfin, vous pouvez forcer les retours à la ligne avec la balise 'br' :
Ligne 1<br>Ligne 2
~~~

## Variables et Python en ligne

Vous pouvez intégrer des variables dans le texte en utilisant la syntaxe `{...}`. Par exemple, ce qui suit :

~~~ .python
Le numéro du sujet est {subject_nr}
~~~

... pourrait être évalué pour (sujet 1) :

~~~ .python
Le numéro du sujet est 1
~~~

Vous pouvez également intégrer une expression Python. Par exemple, ce qui suit :

~~~ .python
Le numéro du sujet modulo cinq est {subject_nr % 5}
~~~

... pourrait être évalué pour (sujet 7) :

~~~ .python
Le numéro du sujet modulo cinq est 2
~~~

## Polices de caractère

### Polices par défaut

Vous pouvez sélectionner une des polices de caractère par défaut à partir des boîtes de dialogue de sélection de police (%FigFontSelect). Ces polices sont incluses avec OpenSesame et votre expérience sera donc entièrement portable lorsque vous les utilisez.

%--
figure:
 id: FigFontSelect
 source: font-selection-dialog.png
 caption: "Un certain nombre de polices par défaut, qui sont regroupées avec OpenSesame, peuvent être sélectionnées à travers les boîtes de dialogue de sélection de police."
--%

Les polices ont été renommées pour plus de clarté, mais correspondent aux polices open-source suivantes :

|__Nom dans OpenSesame__		|__Police réelle__		|
|---------------------------|-----------------------|
|`sans`						|Droid Sans				|
|`serif`					|Droid Serif			|
|`mono`						|Droid Sans Mono		|
|`chinois-japonais-coréen`	|WenQuanYi Micro Hei	|
|`arabe`					|Droid Arabic Naskh		|
|`hébreu`					|Droid Sans Hebrew		|
|`hindi`					|Lohit Hindi			|

### Sélectionner une police personnalisée via la boîte de dialogue de sélection de police

Si vous sélectionnez 'autre ...' dans la boîte de dialogue de sélection de police, vous pouvez choisir n'importe quelle police disponible sur votre système d'exploitation. Si vous faites cela, votre expérience ne sera plus entièrement portable, et nécessitera que la police sélectionnée soit installée sur le système sur lequel vous exécutez votre expérience.

Cela fonctionne uniquement pour OpenSesame sur le bureau, pas pour les expériences en ligne OSWeb.

### Placer une police personnalisée dans le pool de fichiers (OpenSesame bureau)

Lorsque vous exécutez votre expérience sur le bureau, une autre façon d'utiliser une police personnalisée est de mettre un fichier de police dans le pool de fichiers. Par exemple, si vous placez le fichier de police `inconsolata.ttf` dans le pool de fichiers, vous pouvez utiliser cette police dans un élément SKETCHPAD, comme ceci :

	draw textline 0.0 0.0 "Ceci sera en inconsolata" font_family="inconsolata"

Le fichier de police doit être un fichier truetype `.ttf`. Cela fonctionne uniquement pour OpenSesame sur le bureau, pas pour les expériences en ligne OSWeb.

### Utiliser une police personnalisée de Google Fonts (OSWeb)

Lorsque vous exécutez votre expérience dans un navigateur avec OSWeb, vous pouvez utiliser des polices de Google Fonts. Pour ce faire, modifiez simplement le script d'un élément de texte et spécifiez le nom de la police sous `font_family` :

```
draw textline x=0 y=0 font_family="Jacquard 12 Charted" text="Ceci est affiché dans une police amusante"
```

Ceci fonctionne uniquement pour les expériences en ligne OSWeb, pas pour OpenSesame sur le bureau.