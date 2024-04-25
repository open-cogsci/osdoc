title: Texto
hash: 2c5f78c24fe19088d9f96d120232def3d4ca9bb4bc48409ae868d353c7ebc4ed
locale: es
language: Spanish

[TOC]

## ¿Cómo puedo presentar texto?

La manera más común de mostrar texto es usando un elemento SKETCHPAD o FEEDBACK. Estos te permiten ingresar texto y otros estímulos visuales. Para mostrar texto de una manera parecida a un cuestionario, puedes usar [formularios](%link:manual/forms/about%).

## Formato HTML

Puedes utilizar etiquetas HTML, las cuales puedes insertar simplemente en tu texto. Estas etiquetas se pueden utilizar en cualquier lugar: en elementos SKETCHPAD, en INLINE_SCRIPTs (siempre que utilices la clase `Canvas`), en formularios, etc.

Ejemplo:

~~~ .html
OpenSesame soporta un subconjunto de etiquetas HTML:
- <b>Negrita</b>
- <i>Cursiva</i>
- <u>Subrayado</u>

Además, puedes pasar 'color', 'size' y 'style' como palabras clave a una etiqueta 'span':
- <span style='color:red;'>Color</span>
- <span style='font-size:32px;'>Tamaño de fuente</span>
- <span style='font-family:serif;'>Estilo de fuente</span>

Finalmente, puedes forzar saltos de línea con la etiqueta 'br':
Línea 1<br>Línea 2
~~~


## Variables y Python en línea

Puedes embeber variables en el texto utilizando la sintaxis `{...}`. Por ejemplo, lo siguiente:

~~~ .python
El número de sujeto es {subject_nr}
~~~

... podría evaluar (para el sujeto 1):

~~~ .python
El número de sujeto es 1
~~~

También puedes embeber expresiones de Python. Por ejemplo, lo siguiente:

~~~ .python
El número de sujeto módulo cinco es {subject_nr % 5}
~~~

... podría evaluar (para el sujeto 7)

~~~ .python
El número de sujeto módulo cinco es 2
~~~


## Fuentes

### Fuentes predeterminadas

Puedes seleccionar una de las fuentes predeterminadas de los diálogos de selección de fuentes (%FigFontSelect). Estas fuentes están incluidas con OpenSesame y, por tanto, tu experimento será completamente portable cuando las utilices.

%--
figure:
 id: FigFontSelect
 source: font-selection-dialog.png
 caption: "Se pueden seleccionar una serie de fuentes predeterminadas, que vienen con OpenSesame, a través de los diálogos de selección de fuentes."
--%

Las fuentes han sido renombradas para mayor claridad, pero corresponden a las siguientes fuentes de código abierto:

|__Nombre en OpenSesame__		|__Fuente real__			|
|---------------------------|---------------------------|
|`sans`						|Droid Sans					|
|`serif`					|Droid Serif				|
|`mono`						|Droid Sans Mono			|
|`chinese-japanese-korean`	|WenQuanYi Micro Hei		|
|`arabic`					|Droid Arabic Naskh			|
|`hebrew`					|Droid Sans Hebrew			|
|`hindi`					|Lohit Hindi				|

### Seleccionar una fuente personalizada a través del diálogo de selección de fuentes

Si seleccionas 'otra ...' en el diálogo de selección de fuentes, puedes seleccionar cualquier fuente disponible en tu sistema operativo. Si haces esto, tu experimento ya no será completamente portable, y requerirás que la fuente seleccionada esté instalada en el sistema en el que ejecutas tu experimento.

Esto solo funciona para OpenSesame en el escritorio, no para experimentos en línea con OSWeb.

### Colocar una fuente personalizada en el pool de archivos (OpenSesame de escritorio)

Cuando ejecutes tu experimento en el escritorio, otra manera de usar una fuente personalizada es poner un archivo de fuente en el pool de archivos. Por ejemplo, si colocas el archivo de fuente `inconsolata.ttf` en el pool, puedes usar esta fuente en un elemento SKETCHPAD, así:

	draw textline 0.0 0.0 "Esto será inconsolata" font_family="inconsolata"

El archivo de fuente debe ser un archivo truetype `.ttf`. Esto solo funciona para OpenSesame en el escritorio, no para experimentos en línea con OSWeb.

### Usar una fuente personalizada de Google Fonts (OSWeb)

Cuando ejecutes tu experimento en un navegador con OSWeb, puedes usar fuentes de Google Fonts. Para hacerlo, simplemente edita el script de un elemento de texto y especifica el nombre de la fuente bajo `font_family`:

```
draw textline x=0 y=0 font_family="Jacquard 12 Charted" text="Esto se muestra en una fuente curiosa"
```

Esto solo funciona para experimentos en línea con OSWeb, no para OpenSesame en el escritorio.