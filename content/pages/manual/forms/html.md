title: Custom HTML forms

Custom HTML forms are only supported in OSWeb 1.4 when running in a browser
{:.page-notification}

The INLINE_HTML item allows you to implement forms using custom HTML.

The `name` attribute of `input` tags corresponds to an experimental variable. Therefore, the text that is entered into the following text input will be stored as the experimental variable `text_response`:

```html
<input type='text' name='text_response'>
```

The form is closed when the participants clicks on an input of type submit:

```html
<input type='submit' value='click here to continue'>
```
