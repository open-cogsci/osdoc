title: Validando la entrada del formulario
hash: 8f257c66947b338bded5e3096f9fd8535d30a638ed3dda7124df22044e543a9d
locale: es
language: Spanish

Para validar un formulario, pasa una función con la palabra clave `validator` a `Form()`. En el ejemplo a continuación, se utiliza `my_form_validator()` de esta manera. Una función de validador no debe esperar ningún argumento y debe devolver un `bool` para indicar si el formulario es válido o no. Si el formulario no se valida, no se muestra ningún mensaje de error, pero el formulario simplemente permanece abierto.

Además, puedes validar (o filtrar) la entrada en un widget `TextInput` para excluir ciertos caracteres como entrada. Para hacerlo, pasa una función con la palabra clave `key_filter` a `TextInput()`. En el siguiente ejemplo, se utiliza `filter_digits()` de esta manera. Una función de filtro de teclas debe aceptar un solo argumento, que corresponde a una sola pulsación de tecla, y debe devolver un `bool` para indicar si la tecla es aceptada como entrada o no.

~~~ .python
def my_form_validator():
    """Verifica si ambos campos de género y edad están completos"""
    return gender != 'no' and age != ''


def filter_digits(ch):
    """Solo permite caracteres de dígito como entrada"""
    return ch in '0123456789'


# Definir todos los widgets
button_ok = Button(text='Ok')
label_gender= Label('Tu género')
checkbox_male = Checkbox(text='Masculino', group='gender', var='gender')
checkbox_female = Checkbox(text='Femenino', group='gender', var='gender')
label_age = Label('Tu edad')
# Especificar un filtro de teclas para que solo se acepten dígitos como entrada de texto
input_age = TextInput(stub='Edad aquí …', var='age', key_filter=filter_digits)
# Construir el formulario. Especificar una función de validador para asegurarse de que el formulario esté
# completo.
my_form = Form(validator=my_form_validator, rows=[1,1,1], cols=[1,1,1])
my_form.set_widget(label_gender, (0, 0))
my_form.set_widget(checkbox_male, (1, 0))
my_form.set_widget(checkbox_female, (2, 0))
my_form.set_widget(label_age, (0, 1))
my_form.set_widget(input_age, (1, 1), colspan=2)
my_form.set_widget(button_ok, (1, 2))
my_form._exec()
~~~