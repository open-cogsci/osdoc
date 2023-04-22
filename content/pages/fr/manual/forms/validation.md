title: Validation de l'entrée du formulaire
hash: 8f257c66947b338bded5e3096f9fd8535d30a638ed3dda7124df22044e543a9d
locale: fr
language: French

Pour valider un formulaire, passez une fonction avec le mot-clé `validator` à `Form()`. Dans l'exemple ci-dessous, `my_form_validator()` est utilisé de cette manière. Une fonction de validation ne doit pas attendre d'arguments et doit renvoyer un `bool` pour indiquer si le formulaire est valide ou non. Si le formulaire n'est pas valide, aucun message d'erreur n'est affiché, mais le formulaire reste simplement ouvert.

De plus, vous pouvez valider (ou filtrer) la saisie dans un widget `TextInput` pour exclure certains caractères en entrée. Pour ce faire, passez une fonction avec le mot-clé `key_filter` à `TextInput()`. Dans l'exemple ci-dessous, `filter_digits()` est utilisé de cette manière. Une fonction de filtre de clés doit accepter un seul argument, correspondant à une seule pression de touche, et doit renvoyer un `bool` pour indiquer si la touche est acceptée en entrée.

~~~ .python
def my_form_validator():
    """Vérifie si les champs sexe et âge sont remplis"""
    return gender != 'no' and age != ''


def filter_digits(ch):
    """Accepte uniquement les caractères numériques en entrée"""
    return ch in '0123456789'


# Définition de tous les widgets
button_ok = Button(text='Ok')
label_gender= Label('Votre sexe')
checkbox_male = Checkbox(text='Homme', group='gender', var='gender')
checkbox_female = Checkbox(text='Femme', group='gender', var='gender')
label_age = Label('Votre âge')
# Spécifiez un filtre de clés pour que seuls les chiffres soient acceptés en entrée de texte
input_age = TextInput(stub='Âge ici …', var='age', key_filter=filter_digits)
# Construire le formulaire. Spécifiez une fonction de validation pour vous assurer que le formulaire est
# terminé.
my_form = Form(validator=my_form_validator, rows=[1,1,1], cols=[1,1,1])
my_form.set_widget(label_gender, (0, 0))
my_form.set_widget(checkbox_male, (1, 0))
my_form.set_widget(checkbox_female, (2, 0))
my_form.set_widget(label_age, (0, 1))
my_form.set_widget(input_age, (1, 1), colspan=2)
my_form.set_widget(button_ok, (1, 2))
my_form._exec()
~~~