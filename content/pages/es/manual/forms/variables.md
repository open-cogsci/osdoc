title: Variables del formulario
hash: 5699e805a79ad2de0de21343a912e41c96c96935e89844f6af55864fcb4864cc
locale: es
language: Spanish

[TOC]

## Acerca de las variables de formulario

Cuando presentas un formulario con múltiples `checkbox`, generalmente quieres saber qué `checkbox` el usuario ha marcado. De manera similar, cuando presentas un formulario con dos `button`, quieres saber qué `button` el usuario ha hecho clic. Esta información está disponible a través de variables que se establecen automáticamente cuando el usuario interactúa con un formulario. Puedes especificar tú mismo qué variables de respuesta deben usarse. Cómo se hace esto depende de cómo hayas creado tu formulario.

### En los complementos de formulario predefinidos

Cuando usas uno de los complementos de formulario predefinidos, como FORM_TEXT_INPUT, puedes especificar el nombre de la variable de respuesta directamente en los controles del complemento.

### En formularios personalizados

Puedes usar la palabra clave `var` para indicar qué variable debe usarse. Por ejemplo, el siguiente guión de OpenSesame, que puedes ingresar en un complemento FORM_BASE, indica que la respuesta de un widget `text_input` debe almacenarse en una variable llamada `my_response_var`:

```python
widget 0 0 1 1 text_input var=my_response_var
```

El código Python equivalente es:

~~~ .python
my_widget = TextInput(var='my_response_var')
~~~

Ver también:

- %link:manual/forms/widgets%

## Información específica del widget

Cada widget utiliza su variable de respuesta de una manera ligeramente diferente.

### button

El widget `button` establece la variable de respuesta en 'yes' si se ha hecho clic en él y en 'no' si no se ha hecho clic en él.

### checkbox

El widget `checkbox` establece la variable de respuesta en una lista separada por punto y coma del texto en todas las casillas que se hayan marcado (para esa variable) o en 'no' si ninguna `checkbox` ha sido marcada (para esa variable). Esto suena un poco complicado, así que veamos algunos ejemplos.

```python
widget 0 0 1 1 checkbox group="1" text="A" var="my_response_var"
widget 1 0 1 1 checkbox group="1" text="B" var="my_response_var"
widget 1 1 1 1 button text="Next"
```

Aquí hay dos `checkbox` con el texto 'A' y 'B'. Ambos forman parte del mismo grupo, llamado '1'. Ambos tienen la misma variable de respuesta, llamada `my_response_var`. Si se marca 'A', `my_response_var` será 'A'. Si se marca 'B', `my_response_var` será 'B'. Si no se marca ninguno, `my_response_var` será 'no'. Ten en cuenta que solo una `checkbox` en el mismo grupo puede ser marcada, por lo que `my_response_var` *nunca* será 'A;B' en este ejemplo.

Ahora consideremos el mismo guión, con la única diferencia de que las dos `checkbox` no forman parte de un grupo:

```python
widget 0 0 1 1 checkbox text="A" var="my_response_var"
widget 1 0 1 1 checkbox text="B" var="my_response_var"
widget 1 1 1 1 button text="Next"
```

En este caso, la situación es muy parecida a la descrita anteriormente, con la excepción de que ambas `checkbox`es pueden marcarse al mismo tiempo, en cuyo caso se establecerá `my_response_var` en 'A;B'.

No puedes usar la misma variable de respuesta para `checkbox`es en diferentes grupos.

### image

Las variables no son aplicables al widget `image`.

### image_button

El widget `image_button` establece la variable de respuesta en 'yes' si se ha hecho clic en él y en 'no' si no se ha hecho clic en él.

### label

Las variables no son aplicables al widget `label`.

### rating_scale

El widget `rating_scale` establece la variable de respuesta en el número de la opción que se ha hecho clic, donde '0' es la primera opción (indexación basada en cero). Si no se ha seleccionado ninguna opción, la variable de respuesta se establece en 'None'.

### text_input

El widget `text_input` establece la variable de respuesta en el texto ingresado.