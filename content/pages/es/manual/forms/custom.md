title: Creando formularios personalizados
hash: a7ba48cceefdfccdc42df16e4cfeb5980dcbd13a9a5b8516a328456704b5b400
locale: es
language: Spanish


## Acerca de formularios, geometrías y widgets

Un formulario es un conjunto de widgets (botones, etiquetas, campos de texto de entrada, etc.) organizados en una cuadrícula con una geometría particular. En la imagen de abajo puedes ver un ejemplo de un formulario de 2 (columnas) × 3 (filas). La geometría de un formulario es simple y consta de las siguientes propiedades:

- Los *márgenes* aseguran que los widgets no toquen el borde de la pantalla. Puedes tener diferentes márgenes para la parte superior, derecha, inferior e izquierda.
- El *espaciado* asegura que los widgets no se toquen entre sí. El espaciado horizontal y vertical es el mismo.
- Hay una o más *filas*, posiblemente de diferentes tamaños.
- Hay una o más *columnas*, posiblemente de diferentes tamaños.

%--
figure:
 id: FigGeometry
 source: geometry.png
 caption: Un esquemático de las geometrías de FORM.
--%

Por supuesto, un formulario vacío no es divertido. Así que vamos a añadir los siguientes widgets para crear un formulario de pregunta simple:

- Una `label` que abarca las dos columnas de la fila superior. Usamos esta etiqueta para dar un título al formulario.
- Otra `label` que abarca las dos columnas de la fila del medio. Esta etiqueta contiene la pregunta actual.
- Un `button` en el área del widget inferior derecho. Este botón permite al usuario dar la respuesta de $0.05.
- Otro `button` en el área del widget inferior izquierdo. Este botón permite al usuario dar la respuesta de $0.10.

%--
figure:
 id: FigSchematicExample1
 source: schematic-example1.png
 caption: Un ejemplo esquemático de FORM.
--%

Las imágenes de arriba son ejemplos esquemáticos. Cómo se ve este formulario en OpenSesame depende de tus configuraciones (notablemente tu fuente y colores), pero podría verse algo así:

%--
figure:
 id: FigExample1
 source: example1.png
 caption: Un formulario de ejemplo.
--%

## Creando formularios personalizados

Hay dos maneras de crear formularios personalizados. Puedes:

- Usar el ítem FORM_BASE y especificar tu formulario usando el script de OpenSesame.
- Usar Python en un ítem de INLINE_SCRIPT. El método Python es ligeramente más flexible, pero para la mayoría de los propósitos ambos métodos pueden usarse.

### Creando formularios usando el script de OpenSesame

Crearemos el formulario descrito arriba usando el script de OpenSesame. Primero, arrastra el plugin FORM_BASE a tu experimento. Haz clic en el ítem recién creado para abrir su pestaña. A continuación, haz clic en el botón 'Editar script' (con el ícono de terminal), en la parte superior derecha del área de la pestaña. Esto abrirá el editor de script. Introduce el siguiente script para generar el formulario descrito anteriormente (vea los comentarios para explicaciones).

~~~
# Los márgenes se definen como "superior;derecha;inferior;izquierda". Cada valor corresponde a un
# margen en píxeles.
set margins "50;100;50;100"
# El espaciado es simplemente un valor en píxeles.
set spacing "25"
# Los tamaños de las filas son relativos. "1;2;1" significa que hay tres filas,
# donde la del medio es dos veces más grande que las de arriba y abajo. Así que "1;2;1"
# significa exactamente lo mismo que "3;6;3". Tenga en cuenta que "3" no significa
# que haya tres filas del mismo tamaño (pero "1;1;1" sí lo hace).
set rows "1;2;1"
# Las columnas se definen de la misma manera. "1;1" simplemente significa que hay
# dos columnas del mismo tamaño.
set cols "1;1"
# Los widgets se definen de la siguiente manera:
# widget [columna] [fila] [expansión de columna] [expansión de fila] [tipo de widget] [palabras clave]
#
# Las columnas y filas comienzan a contar en 0. Si no deseas que tu widget
# se extienda a través de múltiples columnas y filas, simplemente establece la expansión de columna y fila a 1.
widget 0 0 2 1 label text="Pregunta"
widget 0 1 2 1 label center="no" text="Un bate y una pelota de béisbol juntos cuestan $1.10. El bate cuesta un dólar más que la pelota. ¿Cuánto cuesta la pelota?"
widget 0 2 1 1 button text="$0.10"
widget 1 2 1 1 button text="$0.05"
~~~

Si quieres que un widget específico reciba el enfoque cuando se ejecute el formulario, puedes aplicar la palabra clave `focus=yes` a uno de los widgets:

```
widget 0 0 1 1 text_input text="Texto inicial" frame=yes center=no stub="Escribe aquí …" return_accepts=yes var=response focus=yes
```


### Creando formularios usando Python inline script

La misma forma se puede crear usando un INLINE_SCRIPT y un poco de código Python. Notarás que el código Python se asemeja un poco al script de OpenSesame mostrado arriba. No es de extrañar: El plugin FORM_BASE básicamente traduce el script de OpenSesame a código Python.

Primero, arrastra un INLINE_SCRIPT a tu experimento. Selecciona el elemento recién creado para abrir su pestaña y añade el siguiente script en la fase de ejecución del elemento INLINE_SCRIPT (mira los comentarios para explicaciones).

~~~ .python
# Crear un formulario
formulario = Form(
    cols=[1,1], rows=[1,2,1],
    margins=(50,100,50,100), spacing=25
)
# Crear cuatro widgets
etiquetaTitulo = Label(text='Pregunta')
etiquetaPregunta = Label(
    text='Un bate y una pelota de béisbol cuestan $1.10. El bate cuesta un dólar más que la pelota. ¿Cuánto cuesta la pelota?',
    center=False
)
boton5cts = Button(text='$0.05')
boton10cts = Button(text='$0.10')
# Añadir los widgets al formulario. La posición en el formulario se indica con una
# tupla (columna, fila).
formulario.set_widget(etiquetaTitulo, (0,0), colspan=2)
formulario.set_widget(etiquetaPregunta, (0,1), colspan=2)
formulario.set_widget(boton5cts, (0,2))
formulario.set_widget(boton10cts, (1,2))
# ¡Ejecutar el formulario! En este caso, el formulario devolverá el texto del botón que
# fue clickeado. Esta es una forma de obtener un valor de retorno del formulario. Otra forma
# es usar la palabra clave 'var', admitida en algunos de los widgets.
boton_clickeado = formulario._exec()
~~~

Si quieres que un widget específico reciba el foco cuando se ejecute el formulario, puedes usar la palabra clave `focus_widget`:

~~~ .python
boton_clickeado = formulario._exec(focus_widget=boton5cts)
~~~

### Formularios no interactivos

Normalmente, un formulario tendrá un campo de entrada, un botón u otro elemento interactivo. Sin embargo, también puedes usar formularios sin ningún elemento interactivo. Para hacer esto en un script de OpenSesame, configuras `only_render` a "yes":

```python
set only_render yes
```

Para hacer esto en un Python INLINE_SCRIPT, llamas a `formulario.render()`, en lugar de `formulario._exec()`.

### Temas

Los formularios admiten temas. Actualmente, hay dos temas disponibles: 'gray' y 'plain'. El tema 'gray' es el predeterminado. Aunque el tema 'gray' ya es bastante sencillo, el tema 'plain' es aún más básico. Puedes elegir un tema así en el script de OpenSesame:

```python
set theme plain
```

Y usando la palabra clave `theme` en el script Python inline:

~~~ .python
formulario = Form(theme='plain')
~~~

### Widgets y palabras clave disponibles

Para obtener una lista de los widgets y palabras clave disponibles, consulta:

- %link:manual/forms/widgets%

### Validar entrada

Para ver cómo puedes validar la entrada del formulario, consulta:

- %link:manual/forms/validation%

## Otro ejemplo

El siguiente script de OpenSesame (en un plugin FORM_BASE) producirá un cuestionario de tres escalas de valoración más un botón de siguiente:

```python
set rows "1;1;1;1;1"
set cols "1;1"
widget 0 0 2 1 label text="Indica cuánto estás de acuerdo con las siguientes afirmaciones"
widget 0 1 1 1 label center="no" text="Los formularios son fáciles"
widget 1 1 1 1 rating_scale var="question1" nodes="De acuerdo;No sé;En desacuerdo"
widget 0 2 1 1 label center="no" text="Me gustan los datos"
widget 1 2 1 1 rating_scale var="question2" nodes="De acuerdo;No sé;En desacuerdo"
widget 0 3 1 1 label center="no" text="Me gustan los cuestionarios"
widget 1 3 1 1 rating_scale var="question3" nodes="De acuerdo;No sé;En desacuerdo"
widget 0 4 2 1 button text="Siguiente"
```

El siguiente script Python inline producirá el mismo cuestionario.

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