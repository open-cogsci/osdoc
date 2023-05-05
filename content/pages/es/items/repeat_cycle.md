title: Repetir_ciclo
hash: 8b04755715703af99fbd951772e0c47a5a1abbf7dcaac1e5ab6f9665cd07cb2c
locale: es
language: Spanish

Este complemento te permite repetir ciclos de un `loop`. Lo más común es que se repita un ensayo cuando un participante cometió un error o fue demasiado lento.

Por ejemplo, para repetir todos los ensayos en los que una respuesta fue más lenta de 3000 ms, puedes agregar un elemento `repeat_cycle` después (generalmente) del `keyboard_response` y agregar la siguiente declaración de repetición si:

```bash
[response_time] > 3000
```

También puedes forzar la repetición de un ciclo estableciendo la variable `repeat_cycle` en 1 en un `inline_script`, de la siguiente manera:

```python
var.repeat_cycle = 1
```