<div class="ClassDoc YAMLDoc" markdown="1">

# instancia __responses__

El objeto `responses` contiene el historial de las respuestas que se
recopilaron durante el experimento.

Se crea automáticamente un objeto `responses` cuando comienza el experimento.

Además de las funciones enumeradas a continuación, se admiten las siguientes semánticas:

__Ejemplo__

~~~ .python
# Recorrer todas las respuestas, en las que las últimas respuestas dadas vienen primero
# Cada respuesta tiene atributos correctos, respuesta, tiempo_de_respuesta, elemento y retroalimentación.
for response in responses:
    print(response.correct)
# Imprimir las dos últimas respuestas dadas
print('las dos últimas respuestas:')
print(responses[:2])
~~~

[TOC]

## add(response=None, correct=None, response_time=None, item=None, feedback=True)

Añade una respuesta.


__Parámetros__

- **response**: El valor de la respuesta, por ejemplo, 'space' para la barra espaciadora, 0 para el botón 0 del joystick, etc.
- **correct**: La corrección de la respuesta.
- **response_time**: El tiempo de respuesta.
- **item**: El elemento que recopiló la respuesta.
- **feedback**: Indica si la respuesta debe incluirse en la retroalimentación sobre
precisión y tiempo promedio de respuesta.

__Ejemplo__

~~~ .python
responses.add(response_time=500, correct=1, response='left')
~~~



## clear(self)

Borra todas las respuestas.



__Ejemplo__

~~~ .python
responses.clear()
~~~



## reset_feedback(self)

Establece el estado de retroalimentación de todas las respuestas en Falso, de modo que solo
las nuevas respuestas se incluirán en la retroalimentación.



__Ejemplo__

~~~ .python
responses.reset_feedback()
~~~



</div>