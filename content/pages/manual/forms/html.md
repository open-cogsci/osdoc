title: Custom HTML forms

Custom HTML forms are only supported in when running in a browser. Make sure to use the latest version of OSWeb, because this functionality improves rapidly.
{:.page-notification}

The INLINE_HTML item allows you to implement forms using custom HTML.

- The `name` attribute of `input` tags corresponds to an experimental variable. Therefore, the text that is entered into the text input of Example 1 will be stored as the experimental variable `text_response`.
- For `checkbox` and `radio` elements, you can use the `id` attribute to assign a specific value to the associated experimental variable.
- You can use the `required` attribute to indicate that a form cannot be submitted before a field has been filled out.
- The form is closed when the participant clicks on an input of type submit.
- To include images from the file pool in a custom HTML form, first retrieve the URL to the file, assign it to an experimental variable, and then use this variable as the source for the `<img>` tag (see Example 3).


Example 1:

```html
<input type='text' name='text_response'>
<input type='submit' value='click here to continue'>
```

Example 2:

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

You can get the URL to an image in the file pool …

```javascript
vars.img_url = pool['capybara.png'].data.src
```

… and then use this URL in a custom HTML form:

```html
<img src="[img_url]">
<input type='submit' value='ok'>
```
