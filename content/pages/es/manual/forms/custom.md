title: Creando formularios personalizados
hash: a87d6a87fa567e6e8d52bfd533cc60fb77b7e646afa3b49d05009bbe198d852f
locale: es
language: Spanish

[TOC]


## Acerca de formularios, geometrías y widgets

Un formulario es un conjunto de widgets (botones, etiquetas, campos de entrada de texto, etc.) organizados en una cuadrícula con una geometría particular. En la imagen de abajo, ves un ejemplo de un formulario de 2 (columnas) × 3 (filas). La geometría de un formulario es simple y consta de las siguientes propiedades:

- Los *márgenes* aseguran que los widgets no toquen el borde de la pantalla. Puedes tener márgenes diferentes para la parte superior, derecha, inferior e izquierda.
- Los *espacios* aseguran que los widgets no se toquen entre sí. El espacio horizontal y vertical es el mismo.
- Hay una o más *filas*, posiblemente de diferentes tamaños.
- Hay una o más *columnas*, posiblemente de diferentes tamaños.

%--
figure:
 id: FigGeometry
 source: geometry.png
 caption: Un esquema de las geometrías de FORM.
--%

Por supuesto, un formulario vacío no es divertido. Así que agreguemos los siguientes widgets para crear un formulario de pregunta simple:

- Una etiqueta `label` que abarca las dos columnas de la fila superior. Usamos esta etiqueta para darle un título al formulario.
- Otra etiqueta `label` que abarca las dos columnas de la fila central. Esta etiqueta contiene la pregunta real.
- Un botón `button` en el área inferior derecha del widget. Este botón permite al usuario dar la respuesta de $0.05.
- Otro botón `button` en el área inferior izquierda del widget. Este botón permite al usuario dar la respuesta de $0.10.

%--
figure:
 id: FigSchematicExample1
 source: schematic-example1.png
 caption: Un ejemplo esquemático de FORM.
--%

Las imágenes de arriba son ejemplos esquemáticos. Cómo se ve este formulario en OpenSesame depende de tus configuraciones (notablemente tu fuente y colores), pero puede verse algo así:

%--
figure:
 id: FigExample1
 source: example1.png
 caption: Un ejemplo de FORM.
--%

## Creando formularios personalizados

Hay dos formas de crear formularios personalizados. Puedes:

- Usar el ítem FORM_BASE y especificar tu formulario utilizando el script de OpenSesame.
- Usar Python en un ítem INLINE_SCRIPT. La forma en Python es un poco más flexible, pero para la mayoría de los propósitos, ambos métodos pueden ser utilizados.

### Creando formularios utilizando el script de OpenSesame

Crearemos el formulario descrito anteriormente utilizando el script de OpenSesame. Primero, arrastra el complemento FORM_BASE a tu experimento. Haz clic en el ítem recién creado para abrir su pestaña. Luego, haz clic en el botón "Editar script" (con el ícono del terminal), en la parte superior derecha del área de la pestaña. Esto abrirá el editor de scripts. Ingresa el siguiente script para generar el formulario descrito anteriormente (consulta los comentarios para obtener explicaciones).

~~~
# Los márgenes se definen como "arriba;derecha;abajo;izquierda". Cada valor corresponde a un
# margen en píxeles.
set margins "50;100;50;100"
# El espacio es simplemente un valor en píxeles.
set spacing "25"
# Los tamaños de las filas son relativos. "1;2;1" significa que hay tres filas,
# donde la del medio es el doble de grande que las de la parte inferior y superior. Entonces "1;2;1"
# significa exactamente lo mismo que "3;6;3". Ten en cuenta que "3" no significa
# que haya tres filas del mismo tamaño (pero "1;1;1" sí lo hace).
set rows "1;2;1"
# Las columnas se definen de la misma manera. "1;1" simplemente significa que hay
# dos columnas del mismo tamaño.
set cols "1;1"
# Los widgets se definen de la siguiente manera:
# widget [columna] [fila] [expansión de columna] [expansión de fila] [tipo de widget] [palabras clave]
#
# Las columnas y filas comienzan a contar en 0. Si no deseas que tu widget
# abarque varias columnas y filas, simplemente establece la expansión de columna y fila en 1.
widget 0 0 2 1 label text="Pregunta"
widget 0 1 2 1 label center="no" text="Un bate y una pelota de béisbol juntos cuestan $1.10. El bate cuesta un dólar más que la pelota. ¿Cuánto cuesta la pelota?"
widget 0 2 1 1 button text="$0.10"
widget 1 2 1 1 button text="$0.05"
~~~

### Creando formularios utilizando Python en un Inline Script

El mismo formulario se puede crear utilizando un INLINE_SCRIPT y un poco de código Python. Notarás que el código Python se parece un poco al script de OpenSesame mostrado anteriormente. No es de extrañar: El complemento FORM_BASE esencialmente traduce el script de OpenSesame en código Python.

Primero, arrastra un INLINE_SCRIPT a tu experimento. Selecciona el elemento recién creado para abrir su pestaña y agrega el siguiente script en la fase Run del elemento INLINE_SCRIPT (consulta los comentarios para obtener explicaciones).

~~~ .python
# Crear un formulario
form = Form(
    cols=[1,1], rows=[1,2,1],
    margins=(50,100,50,100), spacing=25
)
# Crear cuatro widgets
labelTitle = Label(text='Pregunta')
labelQuestion = Label(
    text='Un bate y una pelota de béisbol juntos cuestan $1.10. El bate cuesta un dólar más que la pelota. ¿Cuánto cuesta la pelota?',
    center=False
)
button5cts = Button(text='$0.05')
button10cts = Button(text='$0.10')
# Añadir los widgets al formulario. La posición en el formulario se indica como un
# Tuple (columna, fila).
form.set_widget(labelTitle, (0,0), colspan=2)
form.set_widget(labelQuestion, (0,1), colspan=2)
form.set_widget(button5cts, (0,2))
form.set_widget(button10cts, (1,2))
# ¡Ejecutar el formulario! En este caso, el formulario devolverá el texto del botón que
# se hizo clic. Esta es una forma de obtener un valor de retorno del formulario. Otra forma
# es usar la palabra clave 'var', admitida en algunos de los widgets.
button_clicked = form._exec()
~~~

Si deseas que un widget específico reciba el enfoque cuando se ejecuta el formulario, puedes usar la palabra clave `focus_widget`:

~~~ .python
button_clicked = form._exec(focus_widget=button5cts)
~~~

### Formularios no interactivos

Por lo general, un formulario tendrá un campo de entrada, un botón u otro elemento interactivo. Sin embargo, también puedes usar formularios sin tener ningún elemento interactivo. Para hacer esto en el script de OpenSesame, establece `only_render` en "yes":

```python
set only_render yes
```

Para hacer esto en un INLINE_SCRIPT de Python, llamas a `form.render()`, en lugar de `form._exec()`.

### Temas

Los formularios admiten la creación de temas. Actualmente, hay dos temas disponibles: 'gray' y 'plain'. El tema 'gray' es el predeterminado. Aunque el tema 'gray' ya es bastante simple, el tema 'plain' es aún más básico. Puedes elegir un tema de esta manera en el script de OpenSesame:

```python
set theme plain
```

Y utilizando la palabra clave `theme` en el script en línea de Python:

~~~ .python
form = Form(theme='plain')
~~~

### Widgets y palabras clave disponibles

Para obtener una lista de widgets y palabras clave disponibles, consulta:

- %link:manual/forms/widgets%

### Validar entrada

Para ver cómo puedes validar la entrada del formulario, consulta:

- %link:manual/forms/validation%

## Otro ejemplo

El siguiente script de OpenSesame (en un complemento FORM_BASE) producirá un cuestionario de tres escalas de calificación más un botón siguiente:

```python
set rows "1;1;1;1;1"
set cols "1;1"
widget 0 0 2 1 label text="Indicar cuánto estás de acuerdo con las siguientes afirmaciones"
widget 0 1 1 1 label center="no" text="Los formularios son fáciles"
widget 1 1 1 1 rating_scale var="question1" nodes="De acuerdo;No sé;En desacuerdo"
widget 0 2 1 1 label center="no" text="Me gustan los datos"
widget 1 2 1 1 rating_scale var="question2" nodes="De acuerdo;No sé;En desacuerdo"
widget 0 3 1 1 label center="no" text="Me gustan los cuestionarios"
widget 1 3 1 1 rating_scale var="question3" nodes="De acuerdo;No sé;En desacuerdo"
widget 0 4 2 1 button text="Siguiente"
```

El siguiente script en línea de Python producirá el mismo cuestionario.

~~~ .python
form = Form(cols=[1,1], rows=[1,1,1,1,1])
title = Label(
    text='Indica cuánto estás de acuerdo con la siguiente afirmación'
)
question1 = Label(text='Los formularios son fáciles', center=False)
question2 = Label(text='Me gustan los datos', center=False)
question3 = Label(text='Me gustan los cuestionarios', center=False)
ratingScale1 = RatingScale(
    var='question1',
    nodes=['De acuerdo', u"No sé", 'En desacuerdo']
)
ratingScale2 = RatingScale(
    var='question2',
    nodes=['De acuerdo', u"No sé", 'En desacuerdo']
)
ratingScale3 = RatingScale(var='question3',
    nodes=['De acuerdo', u"No sé", 'En desacuerdo'])
nextButton = Button(text='Siguiente')
form.set_widget(title, (0, 0), colspan=2)
form.set_widget(question1, (0, 1))
form.set_widget(question2, (0, 2))
form.set_widget(question3, (0, 3))
form.set_widget(ratingScale1, (1, 1))
form.set_widget(ratingScale2, (1, 2))
form.set_widget(ratingScale3, (1, 3))
form.set_widget(nextButton, (0, 4), colspan=2)
form._exec()
~~~

El formulario resultante se ve algo así. (La apariencia exacta depende de tu fuente, colores, etc.)

%--
figura:
 id: FigExample2
 fuente: example2.png
 leyenda: Otro ejemplo de FORMULARIO.
--%