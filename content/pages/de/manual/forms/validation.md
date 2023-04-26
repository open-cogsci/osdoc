title: Formulareingabe validieren
hash: 8f257c66947b338bded5e3096f9fd8535d30a638ed3dda7124df22044e543a9d
locale: de
language: German

Um ein Formular zu validieren, übergeben Sie eine Funktion mit dem Schlüsselwort `validator` an `Form()`. Im folgenden Beispiel wird `my_form_validator()` auf diese Weise verwendet. Eine Validator-Funktion sollte keine Argumente erwarten und sollte einen `bool` zurückgeben, um anzuzeigen, ob das Formular validiert wird oder nicht. Wenn das Formular nicht validiert wird, wird keine Fehlermeldung angezeigt, sondern das Formular bleibt einfach offen.

Außerdem können Sie die Eingabe in ein `TextInput`-Widget validieren (oder filtern), um bestimmte Zeichen als Eingabe auszuschließen. Um dies zu tun, übergeben Sie eine Funktion mit dem Schlüsselwort `key_filter` an `TextInput()`. Im folgenden Beispiel wird `filter_digits()` auf diese Weise verwendet. Eine Key-Filter-Funktion sollte ein einzelnes Argument akzeptieren, das einem einzigen Tastendruck entspricht, und sollte einen `bool` zurückgeben, um anzuzeigen, ob der Schlüssel als Eingabe akzeptiert wird oder nicht.

~~~ .python
def my_form_validator():
    """Überprüft, ob sowohl das Geschlecht als auch das Alter ausgefüllt wurden"""
    return gender != 'no' and age != ''


def filter_digits(ch):
    """Erlaubt nur Ziffern als Eingabe"""
    return ch in '0123456789'


# Definieren Sie alle Widgets
button_ok = Button(text='Ok')
label_gender= Label('Ihr Geschlecht')
checkbox_male = Checkbox(text='Männlich', group='gender', var='gender')
checkbox_female = Checkbox(text='Weiblich', group='gender', var='gender')
label_age = Label('Ihr Alter')
# Geben Sie einen Tastenfilter an, damit nur Ziffern als Texteingabe akzeptiert werden
input_age = TextInput(stub='Alter hier eintragen …', var='age', key_filter=filter_digits)
# Erstellen Sie das Formular. Geben Sie eine Validator-Funktion an, um sicherzustellen, dass das Formular
# ausgefüllt ist.
my_form = Form(validator=my_form_validator, rows=[1,1,1], cols=[1,1,1])
my_form.set_widget(label_gender, (0, 0))
my_form.set_widget(checkbox_male, (1, 0))
my_form.set_widget(checkbox_female, (2, 0))
my_form.set_widget(label_age, (0, 1))
my_form.set_widget(input_age, (1, 1), colspan=2)
my_form.set_widget(button_ok, (1, 2))
my_form._exec()
~~~