title: Formularios HTML personalizados
hash: 7ce4d5848c0a4e0e32e903dbfb423bd42fbcf30dea52cc43cde013192eeab9dd
locale: es
language: Spanish

El elemento INLINE_HTML te permite implementar formularios utilizando HTML personalizado.

- El atributo `name` de las etiquetas `input` corresponde a una variable experimental. Por lo tanto, el texto que se ingrese en el campo de texto del Ejemplo 1 se almacenará como la variable experimental `text_response`.
- Para los elementos `checkbox` y `radio`, puedes usar el atributo `id` para asignar un valor específico a la variable experimental asociada.
- Puedes usar el atributo `required` para indicar que un formulario no se puede enviar antes de que se haya completado un campo.
- El formulario se cierra cuando el participante hace clic en una entrada de tipo de envío.
- Para incluir imágenes del archivo de contenido en un formulario HTML personalizado, primero obtén la URL del archivo, asígnala a una variable experimental y luego usa esta variable como fuente para la etiqueta `<img>` (ver Ejemplo 3).


Ejemplo 1:

Un formulario de entrada de texto muy básico:

```html
<input type='text' name='text_response'>
<input type='submit' value='haz clic aquí para continuar'>
```

Ejemplo 2:

Un formulario con múltiples botones de radio:

```html
<p>Por favor, selecciona tu edad:</p>
<input type="radio" id="age1" name="age" value="30" required>
<label for="age1">0 - 30</label><br>
<input type="radio" id="age2" name="age" value="60">
<label for="age2">31 - 60</label><br>  
<input type="radio" id="age3" name="age" value="100">
<label for="age3">61 - 100</label><br><br>
<input type="submit" value="Enviar">
```

Ejemplo 3:

Puedes incluir referencias a variables (excepto dentro de las etiquetas `<script>`, donde las llaves simplemente se interpretan como parte del código de JavaScript):

```html
<p>Tu grupo de edad es {age}</p>
<input type='submit' value='ok'>
```

Ejemplo 4:

Puedes usar JavaScript a través de las etiquetas `<script>`. Por ejemplo, puedes obtener una imagen del archivo de contenido y asignarla a una etiqueta `<img>` inicialmente vacía de esta manera:

```html
<img id='capybara'>
<input type='submit' value='ok'>

<script>
document.getElementById('capybara').src = pool['capybara.png'].data.src
</script>
```