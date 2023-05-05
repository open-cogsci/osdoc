title: Widgets de formulario y palabras clave
hash: a4f02ea6550b00af4807cff9e990f6b79be4e00837de3d2ed8f8c3d34f77a19e
locale: es
language: Spanish

[TOC]


## Captura de pantalla

%--
figure:
 id: FigWidgets
 source: widgets.png
 caption: Una lista de widgets de FORM disponibles.
--%


## Widgets y palabras clave

Todas las palabras clave son opcionales, a menos que se indique lo contrario.

### Formulario

Las palabras clave `cols` y `rows` pueden ser valores `int` simples, en cuyo caso especifican el número de columnas y filas de igual tamaño, o listas de `int`, en cuyo caso especifican los tamaños relativos de cada columna y fila. Para obtener más información sobre la geometría de los formularios, consulte:

- %link:manual/forms/custom%

La palabra clave `validator` se puede utilizar para validar la entrada del formulario. Para obtener más información, consulte:

- %link:manual/forms/validation%

(En el guion de OpenSesame, no es necesario crear explícitamente un formulario).

Script de Python:

~~~ .python
form = Form(
    cols=2, rows=2, spacing=10, margins=(100, 100, 100, 100), theme='gray',
    timeout=None, clicks=False, validator=None
)
button = Button(text='¡Ok!')
form.set_widget(button, (0, 0))
form._exec()
~~~


### button / Button

Guion de OpenSesame:

~~~python
widget 0 0 1 1 button text="¡Haga clic aquí!" center=yes frame=yes var=response
~~~

Script de Python:

~~~ .python
form = Form()
button = Button(text='¡Haga clic aquí!', frame=True, center=True, var='response')
form.set_widget(button, (0, 0))
form._exec()
~~~


### checkbox / Checkbox

Si se especifica un grupo, marcar una casilla de verificación de ese grupo desmarcará todas las otras casillas de verificación de ese grupo. Las casillas de verificación que forman parte de un grupo no se pueden desmarcar, excepto haciendo clic en otra casilla de verificación del mismo grupo.

La palabra clave `group` también afecta cómo se almacenan las variables, como se describe aquí:

- %link:manual/forms/variables%

Guion de OpenSesame:

~~~python
widget 0 0 1 1 checkbox group=group text="Opción 1"
widget 0 1 1 1 checkbox group=group text="Opción 2"
~~~

Script de Python:

~~~ .python
form = Form()
checkbox1 = Checkbox(text='Opción 1', group='group')
checkbox2 = Checkbox(text='Opción 2', group='group')
form.set_widget(checkbox1, (0, 0))
form.set_widget(checkbox2, (0, 1))
form._exec()
~~~


### image / ImageWidget

El objeto de Python se llama `ImageWidget` para distinguirlo del elemento `Image` del canvas.

Guion de OpenSesame:

~~~python
# Solo path es una palabra clave requerida
widget 0 0 1 1 image path="mi_imagen.png" adjust=yes frame=no
~~~

Script de Python:

~~~ .python
# Solo path es una palabra clave requerida
form = Form()
image = ImageWidget(path=pool['mi_imagen.png'], adjust=True, frame=False)
form.set_widget(image, (0, 0))
form._exec()
~~~


### image_button / ImageButton

La palabra clave `image_id` se utiliza para identificar el botón de imagen cuando se hace clic en él. Si no se proporciona un `image_id`, la ruta de la imagen se utiliza como id.

Guion de OpenSesame:

~~~python
# Solo path es una palabra clave requerida
widget 0 0 1 1 image_button path="mi_imagen.png" adjust=yes frame=no image_id=mi_imagen var=response
~~~

Script de Python:

~~~ .python
# Solo path es una palabra clave requerida
form = Form()
image_button = ImageButton(
    path=pool['mi_imagen.png'], adjust=True, frame=False,
    image_id='mi_imagen', var='response'
)
form.set_widget(image_button, (0, 0))
form._exec()
~~~


### label / Label

Guion de OpenSesame:

~~~python
widget 0 0 1 1 label text="Mi texto" frame=no center=yes
~~~

Script de Python:

~~~ .python
form = Form()
label = Label(text='Mi texto', frame=False, center=True)
form.set_widget(label, (0,0))
form._exec()
~~~


### rating_scale / RatingScale

La palabra clave `nodes` puede ser un `int` o una lista separada por punto y coma de etiquetas. Si `nodes` es un `int`, especifica el número de nodos (sin etiquetar).

La palabra clave `default` indica qué número de nodo está seleccionado por defecto, donde el primer nodo es 0.

Guion de OpenSesame:

~~~python
widget 0 1 1 1 rating_scale var=response nodes="De acuerdo;No lo sé;En desacuerdo" click_accepts=no orientation=horizontal var=response default=0
~~~

Script de Python:

~~~ .python
form = Form()
rating_scale = RatingScale(
    nodes=['De acuerdo', u"No sé", 'En desacuerdo'], click_accepts=False,
    orientation='horizontal', var='response', default=0
)
form.set_widget(rating_scale, (0, 0))
form._exec()
~~~


### text_input / TextInput

La palabra clave `stub` indica el texto del marcador de posición que se muestra cuando no se ha ingresado texto. La palabra clave `key_filter`, disponible solo en Python, especifica una función para filtrar las pulsaciones de teclas. Esto se describe con más detalle en:

- %link:manual/forms/validation%

OpenSesame script:

~~~python
widget 0 0 1 1 text_input text="Texto inicial" frame=yes center=no stub="Escriba aquí …" return_accepts=yes var=response
~~~

Python script:

~~~ .python
form = Form()
text_input = TextInput(
    text='Texto inicial', frame=True, center=False, stub='Escriba aquí …',
    return_accepts=True, var='response', key_filter=my_filter_function
)
form.set_widget(text_input, (0, 0))
form._exec()
~~~