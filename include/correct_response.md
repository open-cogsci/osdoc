## Correct response

The *Correct response* field indicates which response is considered correct. After a correct response, the `correct` variable is automatically set to 1; after an incorrect response (i.e. everything else), `correct` is set to 0.

You can indicate the correct response in three main ways:

- *Leave the field empty.* If you leave the *Correct response* field empty, OpenSesame will automatically check if a variable called `correct_response` has been defined, and, if so, use this variable for the correct response.
- *Enter a literal value.* You can explicitly enter a response, such as 'left' in the case of a `keyboard_response` item. This is only useful if the correct response is fixed.
- *Enter a variable name.* You can enter a variable, such as '[cr]'. In this case, this variable will be used for the correct response.
