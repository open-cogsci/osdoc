title: Custom HTML forms


The INLINE_HTML item allows you to implement forms using custom HTML.

- The `name` attribute of `input` tags corresponds to an experimental variable. Therefore, the text that is entered into the text input of Example 1 will be stored as the experimental variable `text_response`.
- For `checkbox` and `radio` elements, you can use the `id` attribute to assign a specific value to the associated experimental variable.
- You can use the `required` attribute to indicate that a form cannot be submitted before a field has been filled out.
- The form is closed when the participant clicks on an input of type submit.
- To include images from the file pool in a custom HTML form, first retrieve the URL to the file, assign it to an experimental variable, and then use this variable as the source for the `<img>` tag (see Example 3).


Example 1:

A very basic text input form:

```html
<input type='text' name='text_response'>
<input type='submit' value='click here to continue'>
```

Example 2:

A form with multiple radio buttons:

```html
<p>Please select your age:</p>
<input type="radio" id="age1" name="age" value="30" required>
<label for="age1">0 - 30</label><br>
<input type="radio" id="age2" name="age" value="60">
<label for="age2">31 - 60</label><br>  
<input type="radio" id="age3" name="age" value="100">
<label for="age3">61 - 100</label><br><br>
<input type="submit" value="Submit">
```

Example 3:

You can include variable references (except within `<script>` tags, where curly braces are simply interpreted as part of JavaScript code):

```html
<p>You age group is {age}</p>
<input type='submit' value='ok'>
```

Example 4:

You can JavaScript through `<script>` tags. For example, you can get an image from the file pool and assign to an initially empty `<img>` tag like this:

```html
<img id='capybara'>
<input type='submit' value='ok'>

<script>
document.getElementById('capybara').src = pool['capybara.png'].data.src
</script>
```
