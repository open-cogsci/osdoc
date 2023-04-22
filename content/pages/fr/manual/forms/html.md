title: Formulaires HTML personnalisés
hash: 7ce4d5848c0a4e0e32e903dbfb423bd42fbcf30dea52cc43cde013192eeab9dd
locale: fr
language: French

L'élément INLINE_HTML vous permet de mettre en place des formulaires en utilisant du HTML personnalisé.

- L'attribut `name` des balises `input` correspond à une variable expérimentale. Par conséquent, le texte saisi dans l'entrée de texte de l'exemple 1 sera stocké en tant que variable expérimentale `text_response`.
- Pour les éléments `checkbox` et `radio`, vous pouvez utiliser l'attribut `id` pour attribuer une valeur spécifique à la variable expérimentale associée.
- Vous pouvez utiliser l'attribut `required` pour indiquer qu'un formulaire ne peut être soumis avant qu'un champ ait été complété.
- Le formulaire est fermé lorsque le participant clique sur une entrée de type submit.
- Pour inclure des images provenant de la réserve de fichiers dans un formulaire HTML personnalisé, commencez par récupérer l'URL du fichier, attribuez-le à une variable expérimentale, puis utilisez cette variable comme source pour la balise `<img>` (voir exemple 3).

Exemple 1 :

Un formulaire de saisie de texte très basique :

```html
<input type='text' name='text_response'>
<input type='submit' value='cliquez ici pour continuer'>
```

Exemple 2 :

Un formulaire avec plusieurs boutons radio :

```html
<p>Veuillez sélectionner votre âge :</p>
<input type="radio" id="age1" name="age" value="30" required>
<label for="age1">0 - 30</label><br>
<input type="radio" id="age2" name="age" value="60">
<label for="age2">31 - 60</label><br>  
<input type="radio" id="age3" name="age" value="100">
<label for="age3">61 - 100</label><br><br>
<input type="submit" value="Envoyer">
```

Exemple 3 :

Vous pouvez inclure des références de variables (excepté dans les balises `<script>`, où les accolades sont simplement interprétées comme faisant partie du code JavaScript) :

```html
<p>Votre tranche d'âge est {age}</p>
<input type='submit' value='ok'>
```

Exemple 4 :

Vous pouvez utiliser JavaScript via les balises `<script>`. Par exemple, vous pouvez obtenir une image de la réserve de fichiers et l'attribuer à une balise `<img>` initialement vide comme ceci :

```html
<img id='capybara'>
<input type='submit' value='ok'>

<script>
document.getElementById('capybara').src = pool['capybara.png'].data.src
</script>
```