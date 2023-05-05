title: Texto
hash: 1958b3f404645f67ec8c328c22b9b876e1507c616fa82878164f23ac0d364e92
locale: es
language: Spanish

[TOC]

## ¿Cómo puedo presentar texto?

La forma más común de mostrar texto es usando un SKETCHPAD o FEEDBACK. Estos te permiten ingresar texto y otros estímulos visuales. Para una forma tipo cuestionario de mostrar texto, puedes usar [formularios](%link:manual/forms/about%).


## Formato HTML

Puedes usar etiquetas HTML, que puedes simplemente insertar en tu texto. Puedes usar estas etiquetas en todas partes: en los elementos SKETCHPAD, en INLINE_SCRIPTs (siempre que uses la clase `Canvas`), en formularios, etc.

Ejemplo:

~~~ .html
OpenSesame admite un subconjunto de etiquetas HTML:
- <b>Texto en negrita</b>
- <i>Cursiva</i>
- <u>Subrayado</u>

Además, puedes pasar 'color', 'size' y 'style' como palabras clave a una etiqueta 'span':
- <span style='color:red;'>Color</span>
- <span style='font-size:32px;'>Tamaño de fuente</span>
- <span style='font-family:serif;'>Estilo de fuente</span>

Finalmente, puedes forzar saltos de línea con la etiqueta 'br':
Linea 1<br>Linea 2
~~~

## Variables y código Python en línea

Puedes insertar variables en texto usando la sintaxis `{...}`. Por ejemplo, lo siguiente:

~~~ .python
El número de participante es {subject_nr}
~~~

... podría evaluarse para (para el participante 1):

~~~ .python
El número de participante es 1
~~~

También puedes incrustar expresiones de Python. Por ejemplo, lo siguiente:

~~~ .python
El número de participante módulo cinco es {subject_nr % 5}
~~~

... podría evaluarse para (para el participante 7)

~~~ .python
El número de participante módulo cinco es 2
~~~

## Fuentes

### Fuentes predeterminadas

Puedes seleccionar una de las fuentes predeterminadas en los cuadros de selección de fuentes (%FigFontSelect). Estas fuentes están incluidas en OpenSesame y, por lo tanto, tu experimento será totalmente portátil cuando las utilices.

%--
figure:
 id: FigFontSelect
 source: font-selection-dialog.png
 caption: "Un número de fuentes predeterminadas, que se incluyen con OpenSesame, se pueden seleccionar a través de los cuadros de selección de fuentes."
--%

Las fuentes se han renombrado por claridad, pero corresponden a las siguientes fuentes de código abierto:

|__Nombre en OpenSesame__		|__Fuente real__		|
|---------------------------|-----------------------|
|`sans`						|Droid Sans				|
|`serif`					|Droid Serif			|
|`mono`						|Droid Sans Mono		|
|`chinese-japanese-korean`	|WenQuanYi Micro Hei	|
|`arabic`					|Droid Arabic Naskh		|
|`hebrew`					|Droid Sans Hebrew		|
|`hindi`					|Lohit Hindi			|

### Seleccionar una fuente personalizada a través del cuadro de selección de fuentes

Si seleccionas 'otra ...' en el cuadro de selección de fuentes, puedes seleccionar cualquier fuente disponible en tu sistema operativo. Si haces esto, tu experimento ya no será completamente portátil y requerirá que la fuente seleccionada esté instalada en el sistema donde se ejecute tu experimento.

### Colocar una fuente personalizada en el archivo de fuentes

Otra forma de usar una fuente personalizada es colocar un archivo de fuente en el archivo de fuentes. Por ejemplo, si colocas el archivo de fuente `inconsolata.ttf` en el archivo de fuentes, puedes usar esta fuente en un elemento SKETCHPAD, así:

	dibuja línea_de_texto 0.0 0.0 "Esto será inconsolata" font_family="inconsolata"

Ten en cuenta que el archivo de fuente debe ser un archivo ".ttf" de truetype.